---
name: help-desk-articles
description: Turn a workflow PDF into a finished, publish-ready user guide or help article for a retailcloud product, for the Document360 help desk - detailed, friendly, in the fixed house voice, with screenshots from the PDF embedded. Works for any product (FanVista, OrderUp, the Retail Console, POS apps and others); it asks which product the writer is documenting and researches it from Brain, Jira, Confluence, Drive and other connected sources. Use this skill whenever someone shares a PDF (or screenshots, a playbook section, a Jira ticket or a release) and wants a user guide, help article, how-to, setup guide, FAQ or troubleshooting page for customers, or asks to check or rewrite an existing help article so it matches the house tone - even if they only say "write a doc for customers on X" or "create the article from this PDF". Every writer on the team uses this skill so that all articles sound the same. Not for internal PRDs, Jira tickets, sales decks or team release notes.
argument-hint: "<path to the workflow PDF> [product, who it is for, anything to know]"
---

# Help desk articles

A writer gives you a PDF showing a workflow in a retailcloud product. You deliver a finished customer guide with the PDF's screenshots in it. Readers are the people who set the product up, the staff who use it, and sometimes the business's own customers; they will do exactly what the article says.

A good result is **publish-ready** (nothing for the writer to fill in), **explanatory** (what each setting is for and what it changes, not a click list), and **in the one house voice** shared by every writer and product.

Arguments, if given: $ARGUMENTS

## Work lean

Quality comes from the fact sheet (step 4), not from reading more. Spend tokens there and save them everywhere else:

- Load only what a step names. Read long files by section (Grep the heading, then Read with offset and limit), never whole.
- Send independent tool calls together in one turn.
- Look at each image once, at the reduced `view/` size.
- Ask sources for the fields you need and a handful of results; fetch full text only for the two or three items that matter.
- Never re-read a file you wrote or a result you already have. Do not narrate between steps.
- Stop researching when the fact sheet is full.

## Steps

### 1. Product, sources, PDF (one turn)

- **Product.** If the writer named it, use it. Otherwise ask once (AskUserQuestion where available): "Which product is this guide for?" Options are the folders in `products/` (not `_template`), plus their own answer. This is the only question you ask; never ask the writer for facts.
- **Pack.** Read `products/<product>/product.md`. No pack: read `products/README.md` and follow "A product with no pack".
- **Sources.** Load the Brain, Jira/Confluence and Drive tools (`references/research.md` section 1) and say in one line which are connected.
- **PDF.** `python <skill>/scripts/pdf_images.py extract "<pdf>" "<scratch>/pdf"`. It prints one line per image. Repeats of a screen get a view copy of the top strip only. No PDF: continue without images and say so.

### 2. Read the flow

Read each image in `<scratch>/pdf/view/` once. Note, in order: each screen and how to reach it; every control with its label **exactly as shown**, including sections, helper text, printed limits, example values, and fields visible on screen that the recorder did not click; and what is missing (top or bottom of a page, a save button, prerequisites, results, errors).

The PDF is the authority on labels, paths and order. Work out the task, the reader and the page type from it.

### 3. Research

Follow `references/research.md` sections 2 to 4, with the pack's search terms and sources. Read from the pack's `knowledge.md` only the sections for this topic, plus its conflicts and not-released sections. Unreleased features do not exist for the reader.

### 4. Fact sheet

Before drafting, write the fact sheet in your reasoning, one row per setting or step:

`label | what it is for | what it changes for the customer or staff | default, limits, required | depends on / affects | what goes wrong | source`

Every row needs a source: PDF, code, a released ticket, the playbook or the pack. A cell with no source is a gap. Close a gap with one targeted lookup; if that fails, mark it "general" (word it without the unknown detail) or "omit". Draft only from this sheet. It is what makes the article accurate and detailed at once.

### 5. Images

Pick an image where the reader must find something, recognise a state or check a result: about one per page section, or one per two to four steps. For each, trim the full-size picture to the relevant part of the screen:

`python <skill>/scripts/pdf_images.py trim "<scratch>/pdf/page-NN-img-K.png" <left> <top> <right> <bottom> "<article folder>/images/<slug>/NN-description.png"`

Coordinates are fractions of the image (0 to 1), read off the view copy. Trimming removes recorder banners and whatever else must not be published: real customer, team or venue names and logos, people's names and contact details, sales figures, test values, unreleased features. View a trimmed image only if you are unsure the crop is clean; if it cannot be made clean, drop it and tell the writer which screen needs a fresh capture.

### 6. Draft

Read `references/voice-and-tone.md` and `references/article-template.md`, and one example from the pack that matches the reader. Write the article once, to `<kebab-case-title>.md` in the folder the writer names, else `./help-articles/<product>/`.

- Never invent a path, label, field, limit or cause. Bold only labels you have seen.
- "General" rows: write at the level you are sure of ("Save your changes."). "Omit" rows: leave out.
- No `[VERIFY]`, `[SCREENSHOT]`, `[TODO]`, questions or notes to the writer in the article.
- Nothing internal: ticket keys, codenames and version labels, other customers, table/class/API names, IDs, steps only retailcloud staff can do (say who does it and what the reader has afterwards), credentials and addresses, vendor internals, roadmap and defects, metrics and pricing, anything the pack tags `[INTERNAL]`.

### 7. Check and build

`python <skill>/scripts/build_article.py "<article.md>"`

It checks the article against the voice and safety rules, lists problems by line, and writes `<slug>.docx` (images embedded, for Document360 import) and `<slug>.html` (preview). Fix what it lists with Edit and run it again until clean. Then ask yourself once: would someone new to the product understand why each setting matters?

### 8. Reply

Paths, then at most ten lines: sources used and what each gave (one line each), sources not reached, rows written as "general" or omitted, images dropped. Nothing else.

### 9. Update the pack

If the PDF or a source confirmed or corrected something, edit the pack's `knowledge.md` (a few lines, correct tag, snapshot date). For a product with no pack, save the new pack. Tell the writer in one line that their copy changed and should be shared.

## Other requests

- **Check or rewrite an existing article:** run `scripts/check_article.py` on it, fix what it lists, then read it once against `voice-and-tone.md`.
- **Batch with no PDFs:** work through the pack's `catalog.md` in order.
- **Add a product:** `products/README.md`.
