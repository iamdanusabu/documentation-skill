# Changelog

## 2.1.1 - 2026-11-17

- FanVista pack: Sponsorships screen confirmed from a workflow PDF (scope options, multiple featured products, field limits).

## 2.1.0 - 2026-11-17

- Leaner: the guides the skill loads for every article are about 60% shorter, and long files are read by section.
- Images are read at reduced size; repeats of the same screen are reduced to their step text.
- New fact-sheet step: every statement in an article traces to a source before drafting.
- New `check_article.py`: voice and publishing rules checked by script, run automatically by the build.
- Research capped at one round plus one follow-up, with result limits.
- Publishing notes moved to `docs/PUBLISHING.md`.

## 2.0.0 - 2026-11-17

- Renamed to `help-desk-articles` and made product-neutral. The skill asks which product the writer is documenting.
- Product packs under `products/`: FanVista is the first; `_template/` for new ones.
- A product with no pack is researched from the connected sources and saved as a new pack.
- Shared voice, template, research and publishing guides no longer assume FanVista.

## 1.3.0 - 2026-11-17

- The only input is a PDF path, plus an optional line of context.
- The skill connects to Brain, Jira, Confluence and Drive by itself at the start and reports what is available.
- New research protocol (`references/research.md`): search terms from the PDF, code lookup, released tickets, playbook, support history, other connected sources.
- `docs/CONNECTORS.md`: how each writer turns the connectors on.

## 1.2.0 - 2026-11-17

- Articles are delivered publish-ready: no placeholders or notes to the writer in the article.
- More detailed, friendlier articles: each setting explained, option tables, common questions.
- Deeper research step, including code lookup through Brain.
- New `build_article.py`: Word file and preview page with images embedded.
- New model example: Set up FanVista branding.

## 1.1.0 - 2026-11-17

- Setup page labels confirmed from a workflow PDF of the live console.
- Image script: new `trim` command to cut a section out of a screenshot.
- Workflow: handles picture-only PDFs from step recorders; no longer depends on reading the PDF file directly.

## 1.0.0 - 2026-11-17

- First version: PDF-driven workflow, house voice guide, Document360 format, image extraction from PDFs.
- Product knowledge snapshot dated 17 November 2026.
- Three example articles (admin, staff, fan) and a 48-article catalog.
