#!/usr/bin/env python3
"""
Convert a PDF to per-page PNG images for feeding to Claude Code's multimodal reader.

Use when:
  - The PDF >100MB (Claude's Read tool can't open it)
  - Claude Code lacks pdftoppm/poppler-utils
  - You need Claude to see charts/diagrams in the PDF

Usage:
  python3 scripts/pdf_to_pngs.py /path/to/large.pdf [--pages 0-30] [--dpi 150] [--output /tmp/pages]

Dependencies: pymupdf (pip install pymupdf)
"""
import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(description="Convert PDF pages to PNG images for Claude Code")
    parser.add_argument("pdf", help="Path to the PDF file")
    parser.add_argument("--pages", default=None, help="Page range (e.g. '0-30' for first 30 pages, or omit for all)")
    parser.add_argument("--dpi", type=int, default=150, help="Output DPI (default: 150)")
    parser.add_argument("--output", default="/tmp/pdf_pages", help="Output directory (default: /tmp/pdf_pages)")
    parser.add_argument("--sheets", type=int, default=0,
                        help="Contact-sheet mode: combine N pages per image (e.g. 6 = 6 pages per PNG). "
                             "Reduces Claude Read calls by Nx. Recommended: 4-6 for slide decks.")
    args = parser.parse_args()

    if not os.path.exists(args.pdf):
        print(f"Error: PDF not found: {args.pdf}", file=sys.stderr)
        sys.exit(1)

    try:
        import pymupdf
        from PIL import Image
    except ImportError:
        print("Error: pymupdf and/or Pillow not installed. Run: pip install pymupdf Pillow", file=sys.stderr)
        sys.exit(1)

    doc = pymupdf.open(args.pdf)
    total = doc.page_count

    if args.pages:
        parts = args.pages.split("-")
        start = int(parts[0])
        end = int(parts[1]) if len(parts) > 1 else total
    else:
        start, end = 0, total

    end = min(end, total)
    pages = end - start
    os.makedirs(args.output, exist_ok=True)

    # Use 4-digit padding when PDF has 100+ pages
    padding = 4 if total >= 100 else 3

    if args.sheets > 1:
        # Contact-sheet mode: combine N pages per image
        cols = min(3, args.sheets)
        rows = (args.sheets + cols - 1) // cols
        sheet_num = 0
        for batch_start in range(start, end, args.sheets):
            batch_end = min(batch_start + args.sheets, end)
            images = []
            for i in range(batch_start, batch_end):
                pix = doc[i].get_pixmap(dpi=args.dpi)
                img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
                images.append(img)
            if not images:
                continue
            w, h = images[0].size
            rows_needed = (len(images) + cols - 1) // cols
            sheet = Image.new("RGB", (w * cols, h * rows_needed), "white")
            for idx, img in enumerate(images):
                r, c = idx // cols, idx % cols
                sheet.paste(img, (c * w, r * h))
            sheet.save(os.path.join(args.output, f"sheet_{sheet_num:03d}.png"), quality=80)
            sheet_num += 1
        doc.close()
        print(f"\nDone. {pages} pages → {sheet_num} contact sheets in {args.output}/")
        mt = int(sheet_num * 1.3) + 5
        print(f"Feed to Claude (est. {mt} turns):")
        print(f"  claude --dangerously-skip-permissions -p 'Look at all PNGs in {args.output}/ and analyze...' --model sonnet --allowedTools 'Read' --max-turns {mt}")
    else:
        # Normal mode: one PNG per page
        for i in range(start, end):
            pix = doc[i].get_pixmap(dpi=args.dpi)
            path = os.path.join(args.output, f"page_{i+1:0{padding}d}.png")
            pix.save(path)
            print(f"  Page {i+1}/{end}: {path}")
        doc.close()
        print(f"\nDone. {pages} pages saved to {args.output}/")
        mt = int(pages * 1.3) + 5
        print(f"Feed to Claude: claude --dangerously-skip-permissions -p 'Look at all PNGs in {args.output}/ and analyze...' --model sonnet --allowedTools 'Read' --max-turns {mt}")

if __name__ == "__main__":
    main()
