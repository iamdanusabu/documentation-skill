#!/usr/bin/env python3
"""Pull images out of a workflow PDF for use in a help article.

Requires PyMuPDF:  python -m pip install pymupdf

  python pdf_images.py extract <pdf> <out_dir> [--view-width 1200] [--pages auto|all|none]
      Saves each embedded picture at full size (page-NN-img-K.png, for trimming)
      and a reduced copy in view/ (for reading; much cheaper to look at).
      Pages with no embedded picture are rendered instead (page-NN.png).
      Prints one line per image. A repeat of an earlier screen gets a view copy of
      its top strip only (where step recorders put the step text).

  python pdf_images.py trim <image.png> <left> <top> <right> <bottom> <out.png>
      Cuts a rectangle out of an extracted image. Give fractions of the image
      (0-1) from the top-left corner, or pixels. Use it to keep only the part
      of a screenshot a step is about and to cut away anything that must not
      be published.

  python pdf_images.py crop <pdf> <page> <left> <top> <right> <bottom> <out.png> [--dpi 200]
      Cuts a rectangle (fractions of the page) out of a page, for screenshots
      that are flattened into the page rather than embedded.
"""
import argparse
import json
import os
import sys

try:
    import pymupdf as fitz
except ImportError:
    sys.exit("PyMuPDF is not installed. Run:  python -m pip install pymupdf")


def rgb(pix):
    if pix.colorspace is None or pix.n - pix.alpha >= 4 or pix.alpha:
        return fitz.Pixmap(fitz.csRGB, pix)
    return pix


def signature(pix):
    """Coarse grayscale thumbnail of the lower 85%, to spot near-identical screenshots."""
    data, n, stride = pix.samples, pix.n, pix.stride
    top = int(pix.height * 0.15)
    out = []
    for row in range(24):
        y = top + (pix.height - top - 1) * row // 23
        for col in range(24):
            i = y * stride + ((pix.width - 1) * col // 23) * n
            out.append(sum(data[i:i + 3]) // 3)
    return out


def distance(a, b):
    return sum(abs(x - y) for x, y in zip(a, b)) / len(a)


def save_view(pix, path, view_width):
    if pix.width > view_width:
        pix = fitz.Pixmap(pix, view_width, int(pix.height * view_width / pix.width))
    pix.save(path)


def extract(args):
    doc = fitz.open(args.pdf)
    view_dir = os.path.join(args.out_dir, "view")
    os.makedirs(view_dir, exist_ok=True)
    manifest, seen_sigs = [], []

    for index, page in enumerate(doc, start=1):
        found, seen = [], set()
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
                pix = rgb(fitz.Pixmap(doc, xref))
            except Exception:
                continue
            if pix.width < args.min_width or pix.height < args.min_height:
                continue
            number += 1
            name = f"page-{index:02d}-img-{number}.png"
            pix.save(os.path.join(args.out_dir, name))
            sig = signature(pix)
            twin = next((n for n, s in seen_sigs if distance(sig, s) < 0.3), None)
            seen_sigs.append((name, sig))
            view = pix
            if twin:  # same screen again: keep only the top strip, where recorders put the step text
                strip = fitz.IRect(0, 0, pix.width, int(pix.height * 0.15))
                view = fitz.Pixmap(pix.colorspace, strip, pix.alpha)
                view.copy(pix, strip)
            save_view(view, os.path.join(view_dir, name), args.view_width)
            manifest.append({"file": name, "page": index, "pixels": [pix.width, pix.height], "near_duplicate_of": twin})

        text = " ".join(page.get_text("text").split())
        if args.pages == "all" or (args.pages == "auto" and number == 0):
            name = f"page-{index:02d}.png"
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            pix.save(os.path.join(args.out_dir, name))
            save_view(pix, os.path.join(view_dir, name), args.view_width)
            manifest.append({"file": name, "page": index, "pixels": [pix.width, pix.height], "page_render": True, "near_duplicate_of": None})
        if text:
            manifest.append({"page": index, "text": text[:800]})

    with open(os.path.join(args.out_dir, "manifest.json"), "w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=1, ensure_ascii=False)

    print(f"{len(doc)} pages. Read the copies in {view_dir}; trim from the full-size files in {args.out_dir}.")
    for item in manifest:
        if "file" in item:
            note = f"  same screen as {item['near_duplicate_of']}; view copy is the top strip only" if item["near_duplicate_of"] else ""
            print(f"  {item['file']}  {item['pixels'][0]}x{item['pixels'][1]}{note}")
        else:
            print(f"  page {item['page']} text: {item['text'][:200]}")


def trim(args):
    source = fitz.Pixmap(args.image)
    box = [args.left, args.top, args.right, args.bottom]
    if all(0 <= v <= 1 for v in box):
        box = [box[0] * source.width, box[1] * source.height, box[2] * source.width, box[3] * source.height]
    rect = fitz.IRect(*[int(v) for v in box]) & source.irect
    if rect.is_empty:
        sys.exit(f"That rectangle is outside the image ({source.width}x{source.height}).")
    out = fitz.Pixmap(source.colorspace, rect, source.alpha)
    out.copy(source, rect)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    out.save(args.out)
    print(f"Saved {args.out} ({out.width}x{out.height})")


def crop(args):
    doc = fitz.open(args.pdf)
    if not 1 <= args.page <= len(doc):
        sys.exit(f"Page {args.page} is out of range (1-{len(doc)}).")
    page = doc[args.page - 1]
    w, h = page.rect.width, page.rect.height
    clip = fitz.Rect(args.left * w, args.top * h, args.right * w, args.bottom * h)
    zoom = args.dpi / 72
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
    pix.save(args.out)
    print(f"Saved {args.out} ({pix.width}x{pix.height})")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    e = sub.add_parser("extract")
    e.add_argument("pdf")
    e.add_argument("out_dir")
    e.add_argument("--view-width", type=int, default=1200)
    e.add_argument("--pages", choices=["auto", "all", "none"], default="auto")
    e.add_argument("--min-width", type=int, default=200)
    e.add_argument("--min-height", type=int, default=120)
    e.set_defaults(run=extract)

    t = sub.add_parser("trim")
    t.add_argument("image")
    for name in ("left", "top", "right", "bottom"):
        t.add_argument(name, type=float)
    t.add_argument("out")
    t.set_defaults(run=trim)

    c = sub.add_parser("crop")
    c.add_argument("pdf")
    c.add_argument("page", type=int)
    for name in ("left", "top", "right", "bottom"):
        c.add_argument(name, type=float)
    c.add_argument("out")
    c.add_argument("--dpi", type=int, default=200)
    c.set_defaults(run=crop)

    args = parser.parse_args()
    args.run(args)


if __name__ == "__main__":
    main()
