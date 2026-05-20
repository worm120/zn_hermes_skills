---
name: ocr-and-documents
description: "Extract text from PDFs/scans (pymupdf, marker-pdf). Also covers multimodal/chart-heavy PDFs via Claude Code vision."
version: 2.4.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [PDF, Documents, Research, Arxiv, Text-Extraction, OCR]
    related_skills: [powerpoint]
---

# PDF & Document Extraction

For DOCX: use `python-docx` (parses actual document structure, far better than OCR).
For PPTX: see the `powerpoint` skill (uses `python-pptx` with full slide/notes support).
This skill covers **PDFs and scanned documents**.

## Step 1: Remote URL Available?

If the document has a URL, **always try `web_extract` first**:

```
web_extract(urls=["https://arxiv.org/pdf/2402.03300"])
web_extract(urls=["https://example.com/report.pdf"])
```

This handles PDF-to-markdown conversion via Firecrawl with no local dependencies.

Only use local extraction when: the file is local, web_extract fails, or you need batch processing.

## Step 2: Choose Local Extractor

| Feature | pymupdf (~25MB) | marker-pdf (~3-5GB) |
|---------|-----------------|---------------------|
| **Text-based PDF** | ✅ | ✅ |
| **Scanned PDF (OCR)** | ❌ | ✅ (90+ languages) |
| **Tables** | ✅ (basic) | ✅ (high accuracy) |
| **Equations / LaTeX** | ❌ | ✅ |
| **Code blocks** | ❌ | ✅ |
| **Forms** | ❌ | ✅ |
| **Headers/footers removal** | ❌ | ✅ |
| **Reading order detection** | ❌ | ✅ |
| **Images extraction** | ✅ (embedded) | ✅ (with context) |
| **Images → text (OCR)** | ❌ | ✅ |
| **EPUB** | ✅ | ✅ |
| **Markdown output** | ✅ (via pymupdf4llm) | ✅ (native, higher quality) |
| **Install size** | ~25MB | ~3-5GB (PyTorch + models) |
| **Speed** | Instant | ~1-14s/page (CPU), ~0.2s/page (GPU) |

**Decision**: Use pymupdf unless you need OCR, equations, forms, or complex layout analysis.

If the user needs marker capabilities but the system lacks ~5GB free disk:
> "This document needs OCR/advanced extraction (marker-pdf), which requires ~5GB for PyTorch and models. Your system has [X]GB free. Options: free up space, provide a URL so I can use web_extract, or I can try pymupdf which works for text-based PDFs but not scanned documents or equations."

---

## pymupdf (lightweight)

```bash
pip install pymupdf pymupdf4llm
```

**Via helper script**:
```bash
python scripts/extract_pymupdf.py document.pdf              # Plain text
python scripts/extract_pymupdf.py document.pdf --markdown    # Markdown
python scripts/extract_pymupdf.py document.pdf --tables      # Tables
python scripts/extract_pymupdf.py document.pdf --images out/ # Extract images
python scripts/extract_pymupdf.py document.pdf --metadata    # Title, author, pages
python scripts/extract_pymupdf.py document.pdf --pages 0-4   # Specific pages
```

**Inline**:
```bash
python3 -c "
import pymupdf
doc = pymupdf.open('document.pdf')
for page in doc:
    print(page.get_text())
"
```

---

## marker-pdf (high-quality OCR)

```bash
# Check disk space first
python scripts/extract_marker.py --check

pip install marker-pdf
```

**Via helper script**:
```bash
python scripts/extract_marker.py document.pdf                # Markdown
python scripts/extract_marker.py document.pdf --json         # JSON with metadata
python scripts/extract_marker.py document.pdf --output_dir out/  # Save images
python scripts/extract_marker.py scanned.pdf                 # Scanned PDF (OCR)
python scripts/extract_marker.py document.pdf --use_llm      # LLM-boosted accuracy
```

**CLI** (installed with marker-pdf):
```bash
marker_single document.pdf --output_dir ./output
marker /path/to/folder --workers 4    # Batch
```

---

## Multimodal PDF — Chart/Image-Heavy Documents (Claude Code)

When a PDF is **chart/scan/image-heavy** (e.g. trading course slides, hand-drawn diagrams, annotated charts), neither pymupdf nor marker-pdf extracts useful content. Use Claude Code's vision capability instead.

### Workflow

**Step 1: Render pages to PNG with pymupdf**
```bash
pip install pymupdf
python3 -c "
import pymupdf, os
doc = pymupdf.open('/path/to/doc.pdf')
os.makedirs('/tmp/pdf_pages', exist_ok=True)
for i in range(doc.page_count):
    page = doc[i]
    pix = page.get_pixmap(dpi=100)   # 100-150 DPI balances quality vs size
    pix.save(f'/tmp/pdf_pages/page_{i+1:04d}.png')
doc.close()
print(f'Done: {len(os.listdir(\"/tmp/pdf_pages\"))} images')
"
```

**Step 2: Read batches with Claude Code**
```bash
claude --dangerously-skip-permissions -p '
请用 Read 工具逐一查看 /tmp/pdf_pages/ 下 page_XXXX.png 到 page_YYYY.png 的所有图片。
这是[文档名称]，每页都有图表和文字标注。
看完后告诉我：
1. 核心内容
2. 所有量化规则
3. 入场、止损、目标位的具体规则
4. 实战注意事项
用中文简洁列出关键规则。
' --model sonnet --max-turns 35 --allowedTools "Read"
```

### Critical Rules (from hard-won experience)

| Rule | Why |
|------|-----|
| **Batch 10–25 pages per call** | Larger batches cause SIGINT (exit 130). Claude seems to time out on >30 images. |
| **Use `--dangerously-skip-permissions`** | Without it, Claude prompts for directory access interactively and blocks. |
| **Set max-turns = pages/1.5 + buffer** | ~1.5 turns per image for reading + 5-10 for output. 25 pages → 35 turns; 40 pages → 50 turns. |
| **`--allowedTools "Read"` is required** | Claude needs explicit Read tool permission to access local images. |
| **Use sonnet (not opus/haiku)** | Sonnet has the best vision quality/speed/cost balance for chart reading. |
| **DPI 100-150 is sufficient** | Higher DPI creates huge files (50+ MB per image) for no real gain. |
| **Chinese-language prompts work well** | Claude reads Chinese text in charts natively. |
| **Iterate in multiple calls, not one giant call** | One giant 100-page batch always fails. 10 smaller calls each succeed. |
| **Check if text extraction works first** | Some PDFs have extractable text — run `pymupdf` get_text() on a sample page first. If it returns meaningful text (>500 chars/page), skip the vision approach entirely. |

### Batch Planning (for large docs)

For a 1000+ page PDF, plan batches per chapter/section:
```
Chapter 40: p.167-256 → 3-4 batches of 25 pages each
Chapter 41: p.257-345 → 3-4 batches of 25 pages each
...
```

Track progress with `todo` tool to avoid losing your place over multiple turns.

---

## Arxiv Papers

```
# Abstract only (fast)
web_extract(urls=["https://arxiv.org/abs/2402.03300"])

# Full paper
web_extract(urls=["https://arxiv.org/pdf/2402.03300"])

# Search
web_search(query="arxiv GRPO reinforcement learning 2026")
```

## Split, Merge & Search

pymupdf handles these natively — use `execute_code` or inline Python:

```python
# Split: extract pages 1-5 to a new PDF
import pymupdf
doc = pymupdf.open("report.pdf")
new = pymupdf.open()
for i in range(5):
    new.insert_pdf(doc, from_page=i, to_page=i)
new.save("pages_1-5.pdf")
```

```python
# Merge multiple PDFs
import pymupdf
result = pymupdf.open()
for path in ["a.pdf", "b.pdf", "c.pdf"]:
    result.insert_pdf(pymupdf.open(path))
result.save("merged.pdf")
```

```python
# Search for text across all pages
import pymupdf
doc = pymupdf.open("report.pdf")
for i, page in enumerate(doc):
    results = page.search_for("revenue")
    if results:
        print(f"Page {i+1}: {len(results)} match(es)")
        print(page.get_text("text"))
```

No extra dependencies needed — pymupdf covers split, merge, search, and text extraction in one package.

---

## Notes

- `web_extract` is always first choice for URLs
- pymupdf is the safe default — instant, no models, works everywhere
- marker-pdf is for OCR, scanned docs, equations, complex layouts — install only when needed
- Both helper scripts accept `--help` for full usage
- marker-pdf downloads ~2.5GB of models to `~/.cache/huggingface/` on first use
- For Word docs: `pip install python-docx` (better than OCR — parses actual structure)
- For PowerPoint: see the `powerpoint` skill (uses python-pptx)
