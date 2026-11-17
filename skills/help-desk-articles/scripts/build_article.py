#!/usr/bin/env python3
"""Turn a finished article (.md) into files that carry their images with them.

  python build_article.py <article.md> [--out-dir <folder>]

Writes, next to the article (or into --out-dir):
  <slug>.docx   Word file with every image embedded. Import this into
                Document360 (Create article > Import from Word) and the
                images are uploaded with the text.
  <slug>.html   One self-contained page with every image embedded, for
                reviewing the article in a browser or sharing it for sign-off.

Requires python-docx:  python -m pip install python-docx

Understands the article format this skill writes: a metadata header between
--- lines, ## and ### headings, numbered steps, bullets, pipe tables, images
as ![alt](path), **bold**, *italic*, and Document360 callouts
(:::(Type) (Title) ... :::).
"""
import argparse
import base64
import html
import os
import re
import struct
import sys

INLINE = re.compile(r"(\*\*.+?\*\*|\*.+?\*)")
IMAGE = re.compile(r"^!\[(.*?)\]\((.+?)\)$")
CALLOUT = re.compile(r"^:::\((\w+)\)\s*\((.*?)\)\s*$")
NUMBERED = re.compile(r"^(\d+)\.\s+(.*)$")


def parse(text):
    """Return (metadata dict, list of blocks)."""
    meta = {}
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        end = lines.index("---", 1)
        for line in lines[1:end]:
            if ":" in line:
                key, value = line.split(":", 1)
                meta[key.strip()] = value.strip()
        lines = lines[end + 1:]

    blocks, i = [], 0
    while i < len(lines):
        raw = lines[i]
        line = raw.strip()
        indent = len(raw) - len(raw.lstrip())
        if not line:
            i += 1
            continue
        callout = CALLOUT.match(line)
        if callout:
            body = []
            i += 1
            while i < len(lines) and lines[i].strip() != ":::":
                if lines[i].strip():
                    body.append(lines[i].strip())
                i += 1
            blocks.append(("callout", callout.group(1), callout.group(2), " ".join(body)))
            i += 1
            continue
        if line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            blocks.append(("table", rows))
            continue
        if line.startswith("### "):
            blocks.append(("heading", 3, line[4:]))
        elif line.startswith("## "):
            blocks.append(("heading", 2, line[3:]))
        elif IMAGE.match(line):
            m = IMAGE.match(line)
            blocks.append(("image", m.group(1), m.group(2), indent > 0))
        elif NUMBERED.match(line):
            m = NUMBERED.match(line)
            blocks.append(("step", m.group(1), m.group(2)))
        elif line.startswith("- "):
            blocks.append(("bullet", line[2:], indent > 0))
        else:
            blocks.append(("para", line, indent > 0))
        i += 1
    return meta, blocks


def runs(text):
    """Split inline markdown into (text, bold, italic) pieces."""
    out = []
    for piece in INLINE.split(text):
        if not piece:
            continue
        if piece.startswith("**") and piece.endswith("**"):
            out.append((piece[2:-2], True, False))
        elif piece.startswith("*") and piece.endswith("*"):
            out.append((piece[1:-1], False, True))
        else:
            out.append((piece, False, False))
    return out


def png_size(path):
    with open(path, "rb") as handle:
        head = handle.read(24)
    if head[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", head[16:24])
    return (800, 600)


# ---------------------------------------------------------------- Word

def build_docx(meta, blocks, base, out_path):
    try:
        from docx import Document
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        from docx.oxml import OxmlElement
        from docx.oxml.ns import qn
        from docx.shared import Inches, Pt, RGBColor
    except ImportError:
        sys.exit("python-docx is not installed. Run:  python -m pip install python-docx")

    doc = Document()
    doc.styles["Normal"].font.name = "Calibri"
    doc.styles["Normal"].font.size = Pt(11)

    def add_runs(paragraph, text):
        for piece, bold, italic in runs(text):
            run = paragraph.add_run(piece)
            run.bold = bold
            run.italic = italic

    def shade(cell, color):
        props = cell._tc.get_or_add_tcPr()
        fill = OxmlElement("w:shd")
        fill.set(qn("w:val"), "clear")
        fill.set(qn("w:color"), "auto")
        fill.set(qn("w:fill"), color)
        props.append(fill)

    doc.add_heading(meta.get("title", "Article"), level=1)
    missing = []
    for block in blocks:
        kind = block[0]
        if kind == "heading":
            doc.add_heading(block[2], level=block[1])
        elif kind == "para":
            p = doc.add_paragraph()
            if block[2]:
                p.paragraph_format.left_indent = Inches(0.3)
            add_runs(p, block[1])
        elif kind == "step":
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.3)
            p.paragraph_format.first_line_indent = Inches(-0.3)
            add_runs(p, f"{block[1]}.  {block[2]}")
        elif kind == "bullet":
            p = doc.add_paragraph(style="List Bullet")
            if block[2]:
                p.paragraph_format.left_indent = Inches(0.6)
            add_runs(p, block[1])
        elif kind == "image":
            path = os.path.join(base, block[2])
            if not os.path.exists(path):
                missing.append(block[2])
                continue
            width_px, _ = png_size(path)
            width = min(6.0, max(1.8, width_px / 150))
            doc.add_picture(path, width=Inches(width))
            picture = doc.paragraphs[-1]
            picture.alignment = WD_ALIGN_PARAGRAPH.LEFT
            if block[3]:
                picture.paragraph_format.left_indent = Inches(0.3)
            inline = picture.runs[0]._r.xpath(".//wp:docPr")
            if inline:
                inline[0].set("descr", block[1])  # alt text
        elif kind == "callout":
            table = doc.add_table(rows=1, cols=1)
            table.style = "Table Grid"
            cell = table.rows[0].cells[0]
            shade(cell, "FDF3D8" if block[1].lower() in ("warning", "error") else "E8F1FB")
            p = cell.paragraphs[0]
            title = p.add_run(block[2] + ": ")
            title.bold = True
            add_runs(p, block[3])
            doc.add_paragraph()
        elif kind == "table":
            rows = block[1]
            table = doc.add_table(rows=len(rows), cols=max(len(r) for r in rows))
            table.style = "Table Grid"
            for r, row in enumerate(rows):
                for c, value in enumerate(row):
                    cell = table.rows[r].cells[c]
                    p = cell.paragraphs[0]
                    add_runs(p, value)
                    if r == 0:
                        shade(cell, "EDEDED")
                        for run in p.runs:
                            run.bold = True
            doc.add_paragraph()
    doc.save(out_path)
    return missing


# ---------------------------------------------------------------- HTML

CSS = """
body{font:16px/1.6 -apple-system,Segoe UI,Roboto,Arial,sans-serif;color:#1f2933;max-width:820px;margin:40px auto;padding:0 20px}
h1{font-size:30px;margin-bottom:4px} h2{font-size:22px;margin-top:36px;border-bottom:1px solid #e3e7eb;padding-bottom:6px} h3{font-size:17px;margin-top:24px}
.meta{color:#66727f;font-size:14px;margin-bottom:24px}
img{max-width:100%;border:1px solid #d8dde3;border-radius:6px;margin:8px 0 14px}
table{border-collapse:collapse;width:100%;margin:12px 0 20px} th,td{border:1px solid #d8dde3;padding:8px 10px;text-align:left;vertical-align:top} th{background:#f3f5f7}
.step{margin:8px 0 8px 28px;text-indent:-28px} .in{margin-left:28px} ul{margin:6px 0 10px}
.callout{border-left:4px solid #2f6fbd;background:#eef4fb;padding:10px 14px;margin:14px 0;border-radius:4px}
.callout.warning,.callout.error{border-color:#c98a00;background:#fdf5df}
"""


def inline_html(text):
    out = []
    for piece, bold, italic in runs(text):
        safe = html.escape(piece)
        out.append(f"<strong>{safe}</strong>" if bold else f"<em>{safe}</em>" if italic else safe)
    return "".join(out)


def build_html(meta, blocks, base, out_path):
    parts = [f"<h1>{html.escape(meta.get('title', 'Article'))}</h1>"]
    if meta.get("description"):
        parts.append(f"<p class='meta'>{html.escape(meta['description'])}</p>")
    open_list = False

    def close_list():
        nonlocal open_list
        if open_list:
            parts.append("</ul>")
            open_list = False

    for block in blocks:
        kind = block[0]
        if kind != "bullet":
            close_list()
        if kind == "heading":
            parts.append(f"<h{block[1]}>{inline_html(block[2])}</h{block[1]}>")
        elif kind == "para":
            parts.append(f"<p class='{'in' if block[2] else ''}'>{inline_html(block[1])}</p>")
        elif kind == "step":
            parts.append(f"<p class='step'><strong>{block[1]}.</strong>&nbsp; {inline_html(block[2])}</p>")
        elif kind == "bullet":
            if not open_list:
                parts.append(f"<ul class='{'in' if block[2] else ''}'>")
                open_list = True
            parts.append(f"<li>{inline_html(block[1])}</li>")
        elif kind == "image":
            path = os.path.join(base, block[2])
            if os.path.exists(path):
                with open(path, "rb") as handle:
                    data = base64.b64encode(handle.read()).decode()
                parts.append(f"<p class='{'in' if block[3] else ''}'><img alt=\"{html.escape(block[1])}\" src=\"data:image/png;base64,{data}\"></p>")
        elif kind == "callout":
            parts.append(f"<div class='callout {block[1].lower()}'><strong>{html.escape(block[2])}:</strong> {inline_html(block[3])}</div>")
        elif kind == "table":
            rows = block[1]
            cells = "".join(f"<th>{inline_html(c)}</th>" for c in rows[0])
            body = "".join("<tr>" + "".join(f"<td>{inline_html(c)}</td>" for c in row) + "</tr>" for row in rows[1:])
            parts.append(f"<table><tr>{cells}</tr>{body}</table>")
    close_list()
    page = f"<!doctype html><html lang='en'><head><meta charset='utf-8'><title>{html.escape(meta.get('title', 'Article'))}</title><style>{CSS}</style></head><body>{''.join(parts)}</body></html>"
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(page)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("article")
    parser.add_argument("--out-dir")
    args = parser.parse_args()

    with open(args.article, encoding="utf-8") as handle:
        meta, blocks = parse(handle.read())
    base = os.path.dirname(os.path.abspath(args.article))
    out_dir = args.out_dir or base
    os.makedirs(out_dir, exist_ok=True)
    slug = meta.get("slug") or os.path.splitext(os.path.basename(args.article))[0]

    leftovers = [m for m in ("[VERIFY", "[SCREENSHOT") if any(m in str(b) for b in blocks)]
    if leftovers:
        print("Warning: the article still contains", " and ".join(leftovers), "markers.")

    docx_path = os.path.join(out_dir, slug + ".docx")
    html_path = os.path.join(out_dir, slug + ".html")
    missing = build_docx(meta, blocks, base, docx_path)
    build_html(meta, blocks, base, html_path)
    images = sum(1 for b in blocks if b[0] == "image")
    print(f"Wrote {docx_path}")
    print(f"Wrote {html_path}")
    print(f"{images - len(missing)} of {images} images embedded.")
    for path in missing:
        print("  missing image:", path)


if __name__ == "__main__":
    main()
