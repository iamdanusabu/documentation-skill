#!/usr/bin/env python3
"""Pull images out of a workflow PDF for use in a help article.

Requires PyMuPDF:  python -m pip install pymupdf

  python pdf_images.py extract <pdf> <out_dir> [--dpi 150] [--min-width 200] [--min-height 120]
      Saves, per page:
        page-03.png          the whole page rendered (always)
        page-03-img-1.png    each embedded picture on that page, in reading order
      and manifest.json describing every file (page, size, position on the
      page, and the page text nearest to it) so you can match pictures to steps.

  python pdf_images.py crop <pdf> <page> <left> <top> <right> <bottom> <out.png> [--dpi 200]
      Cuts a rectangle out of a page. Coordinates are fractions of the page
      (0-1) from the top-left corner. Use this when a screenshot is not a
      separate embedded picture (flattened or vector PDFs), or to trim an
      embedded screenshot down to the part a step is about.
      Example: the top half of page 4 ->  crop guide.pdf 4 0 0 1 0.5 out.png

  python pdf_images.py trim <image.png> <left> <top> <right> <bottom> <out.png>
      Cuts a rectangle out of an already extracted image, in pixels. Use this
      to keep only the part of a screenshot a step is about, or to leave out
      a part that must not be published (a name, a customer logo, test data).
"""
import argparse
import json
import os
import sys

try:
    import pymupdf as fitz
except ImportError:
    sys.exit("PyMuPDF is not installed. Run:  python -m pip install pymupdf")


def nearby_text(page, rect, limit=240):
    """Text just above and below an image: usually its caption or its step."""
    band = fitz.Rect(0, max(0, rect.y0 - 90), page.rect.width, min(page.rect.height, rect.y1 + 60))
    words = " ".join(page.get_text("text", clip=band).split())
    return words[:limit]


def extract(args):
    doc = fitz.open(args.pdf)
    os.makedirs(args.out_dir, exist_ok=True)
    manifest = {"pdf": os.path.abspath(args.pdf), "pages": []}
    zoom = args.dpi / 72

    for index, page in enumerate(doc, start=1):
        page_file = f"page-{index:02d}.png"
        page.get_pixmap(matrix=fitz.Matrix(zoom, zoom)).save(os.path.join(args.out_dir, page_file))
        entry = {
            "page": index,
            "render": page_file,
            "text": " ".join(page.get_text("text").split())[:600],
            "images": [],
        }

        seen = set()
        found = []
        for info in page.get_images(full=True):
            xref = info[0]
            if xref in seen:
                continue
            seen.add(xref)
            for rect in page.get_image_rects(xref):
                found.append((rect, xref))
        found.sort(key=lambda item: (round(item[0].y0), round(item[0].x0)))

        number = 0
        for rect, xref in found:
            try:
                pix = fitz.Pixmap(doc, xref)
                if pix.colorspace is None or pix.n - pix.alpha >= 4 or pix.alpha:
                    pix = fitz.Pixmap(fitz.csRGB, pix)  # CMYK / masks / alpha -> plain RGB
            except Exception as error:  # damaged or unsupported image stream
                entry.setdefault("skipped", []).append(f"xref {xref}: {error}")
                continue
            if pix.width < args.min_width or pix.height < args.min_height:
                continue  # icons, bullets, logos
            number += 1
            name = f"page-{index:02d}-img-{number}.png"
            pix.save(os.path.join(args.out_dir, name))
            width, height = page.rect.width, page.rect.height
            entry["images"].append({
                "file": name,
                "pixels": [pix.width, pix.height],
                "position": [round(rect.x0 / width, 3), round(rect.y0 / height, 3),
                             round(rect.x1 / width, 3), round(rect.y1 / height, 3)],
                "nearby_text": nearby_text(page, rect),
            })
        manifest["pages"].append(entry)

    with open(os.path.join(args.out_dir, "manifest.json"), "w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2, ensure_ascii=False)

    total = sum(len(p["images"]) for p in manifest["pages"])
    print(f"{len(manifest['pages'])} pages rendered, {total} embedded images saved to {args.out_dir}")
    for p in manifest["pages"]:
        print(f"  page {p['page']}: {len(p['images'])} image(s)")
    if total == 0:
        print("No embedded images found. The screenshots are probably flattened into the page;"
              " view the page renders and use the 'crop' command.")


def crop(args):
    doc = fitz.open(args.pdf)
    if not 1 <= args.page <= len(doc):
        sys.exit(f"Page {args.page} is out of range (1-{len(doc)}).")
    box = [args.left, args.top, args.right, args.bottom]
    if not all(0 <= v <= 1 for v in box) or args.left >= args.right or args.top >= args.bottom:
        sys.exit("Coordinates must be fractions between 0 and 1, with left < right and top < bottom.")
    page = doc[args.page - 1]
    w, h = page.rect.width, page.rect.height
    clip = fitz.Rect(args.left * w, args.top * h, args.right * w, args.bottom * h)
    zoom = args.dpi / 72
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
    pix.save(args.out)
    print(f"Saved {args.out} ({pix.width}x{pix.height})")


def trim(args):
    source = fitz.Pixmap(args.image)
    box = fitz.IRect(args.left, args.top, args.right, args.bottom) & source.irect
    if box.is_empty:
        sys.exit(f"That rectangle is outside the image ({source.width}x{source.height}).")
    out = fitz.Pixmap(source.colorspace, box, source.alpha)
    out.copy(source, box)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    out.save(args.out)
    print(f"Saved {args.out} ({out.width}x{out.height})")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    e = sub.add_parser("extract")
    e.add_argument("pdf")
    e.add_argument("out_dir")
    e.add_argument("--dpi", type=int, default=150)
    e.add_argument("--min-width", type=int, default=200)
    e.add_argument("--min-height", type=int, default=120)
    e.set_defaults(run=extract)

    c = sub.add_parser("crop")
    c.add_argument("pdf")
    c.add_argument("page", type=int)
    for name in ("left", "top", "right", "bottom"):
        c.add_argument(name, type=float)
    c.add_argument("out")
    c.add_argument("--dpi", type=int, default=200)
    c.set_defaults(run=crop)

    t = sub.add_parser("trim")
    t.add_argument("image")
    for name in ("left", "top", "right", "bottom"):
        t.add_argument(name, type=int)
    t.add_argument("out")
    t.set_defaults(run=trim)

    args = parser.parse_args()
    args.run(args)


if __name__ == "__main__":
    main()
