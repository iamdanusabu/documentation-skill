---
name: help-desk-articles
description: Turn a workflow PDF into a finished, publish-ready user guide or help article for a retailcloud product, for the Document360 help desk - detailed, friendly, in the fixed house voice, with screenshots from the PDF embedded. Works for any product (FanVista, OrderUp, the Retail Console, POS apps and others); it asks which product the writer is documenting and researches it from Brain, Jira, Confluence, Drive and other connected sources. Use this skill whenever someone shares a PDF (or screenshots, a playbook section, a Jira ticket or a release) and wants a user guide, help article, how-to, setup guide, FAQ or troubleshooting page for customers, or asks to check or rewrite an existing help article so it matches the house tone - even if they only say "write a doc for customers on X" or "create the article from this PDF". Every writer on the team uses this skill so that all articles sound the same. Not for internal PRDs, Jira tickets, sales decks or team release notes.
argument-hint: "<path to the workflow PDF> [product, who it is for, anything to know]"
---

# Help desk articles

You are writing for retailcloud's public help desk. The readers are the people who set a product up, the staff who use it every day, and sometimes the business's own customers. They do not know the internals, and they will do exactly what the article says.

The usual job: a writer gives you **a PDF that shows a workflow** (screens, steps, sometimes notes). You find out which product it is, work out the flow, research everything the screens do not show, and deliver a finished guide with the PDF's screenshots in it.

Three things define a good result:

1. **Ready to publish.** No placeholders, no questions, no notes to the writer in the article. Anything you could not settle is handled by research or by careful wording, and reported in chat.
2. **Detailed and friendly.** A click list is not a guide. Explain what each setting is for, what it changes for the people affected, which choice suits whom, and what to do when it goes wrong.
3. **One voice.** Many writers use this skill across many products. Nobody should be able to tell who wrote an article.

## Files in this skill

| File | Read it when |
| --- | --- |
| `products/README.md` | Step 1. The list of product packs and how to work when a product has none. |
| `products/<product>/product.md` | Once the product is known. Its terms, readers, traps, sources and document sections. |
| `products/<product>/knowledge.md` | Once the product is known. What the product does and how it is set up. Read the sections for your topic plus its conflicts, known-gaps and not-released sections. |
| `products/<product>/catalog.md` | For the canonical title, neighbouring articles and scope. |
| `products/<product>/examples/` | To hear the voice and see the level of detail. |
| `references/voice-and-tone.md` | Always, before drafting. The house voice for every product. |
| `references/article-template.md` | Always, before drafting. Page structures, how much detail, images, a worked example. |
| `references/document360.md` | Always, before saving. Metadata header, callouts, how images reach Document360. |
| `references/research.md` | Steps 1 and 3. Connecting to the sources, the searches to run, what to trust. |
| `scripts/pdf_images.py` | Steps 2 and 5: pull images out of the PDF and trim them. |
| `scripts/build_article.py` | Step 8: build the Word file and preview page with images embedded. |

## Workflow

### 1. Start: the PDF, the product, the sources

The writer's whole input is a PDF path and, sometimes, a line of context. If the skill was invoked with arguments, they are: $ARGUMENTS

**Which product.** Each writer covers different products, so settle this first.

- If the writer named the product, use it.
- Otherwise ask once, with the AskUserQuestion tool where available: "Which product is this guide for?" Offer the packs listed in `products/README.md` and let them type another. Ask this before anything else; it is the one question you ask.
- Do not guess the product from the PDF alone when it was not named. Several products share the same console, and the wrong pack means the wrong terms. You may use what the PDF shows to put the likeliest product first in the question.

Then load the pack: `products/<product>/product.md` and the relevant parts of its `knowledge.md`. If the product has no pack, follow "A product with no pack" in `products/README.md`: you research it from scratch and build the pack as you go.

**The sources.** Straight away, connect them as set out in `references/research.md` section 1: load the Brain, Jira, Confluence and Drive tools, confirm each answers, and tell the writer in one line what is connected.

Beyond the product, do not interview the writer and do not ask them for facts; you fetch those yourself. Ask for the PDF only if no path was given. If there is no PDF, carry on from the pack and the connectors; the article will have no images, and you say so in chat.

Work out the task, the reader and the page type from the PDF and whatever the writer said. The pack names the product's readers.

### 2. Read the PDF and understand the flow

Pull the pages and images out first:

```
python <skill>/scripts/pdf_images.py extract "<pdf>" "<scratch folder>/pdf"
```

This renders every page (`page-NN.png`) and saves each embedded picture (`page-NN-img-K.png`), with a `manifest.json`. It needs PyMuPDF; if it reports that it is missing, run `python -m pip install pymupdf` and try again.

Then look at every picture with the Read tool. Many workflow PDFs (step recorders such as Onvoke or Scribe) are pictures only, with the step text inside the image; the images are the content.

Set out the flow for yourself before writing:

- the screens in order, and how the reader gets from one to the next,
- every control, with its label **exactly as the screenshot shows it**, including section headings, helper text under fields, limits printed on screen, and what the rest of the screen shows (previews, fields the recorder did not click),
- what each field expects, and any example value shown,
- what the PDF does not show: the top or bottom of a page, a save button, prerequisites, what happens afterwards, error cases.

Read the whole of each screenshot, not just the highlighted control.

**The PDF is the authority on what the screens look like.** When it disagrees with the pack on a path or label, the PDF wins, and you record the confirmed label in the pack's `knowledge.md`.

### 3. Research the topic yourself

This step is what turns screens into a guide, and it is your job, not the writer's. Follow `references/research.md` from section 2 onward, every time, using the product name and the sources listed in the pack:

1. Turn the PDF's page names, control labels and messages into search terms.
2. **Brain**: find the code behind the screen and read its fields and validation. This fills in what the recorder did not capture.
3. **Jira**: search the on-screen labels and the feature; take rules, defaults and error messages from released items.
4. **Drive**: the product's playbook and guides.
5. **Support history, internal notes, Confluence**: what customers actually get stuck on.
6. **Any other connected source** that plainly holds material on the topic.

Send searches in parallel and keep going until, for every setting and step, you can say what it is for, what it changes, its default and limits, what depends on it, what goes wrong, and that it is released. If a source cannot be reached, carry on with the others and say so in your notes.

Anything not released does not exist for the reader.

### 4. Plan the guide

One article covers one task or one screen. A PDF that walks through a whole settings page becomes one guide to that page, organised by its sections. A PDF that covers several separate tasks becomes an overview plus one article per task, unless the writer asked for a single document. Use the catalog title when the task matches a catalog article.

### 5. Choose and prepare the images

Use an image where the reader has to find something on a screen, recognise a state, or check a result: usually one per section of a settings page, or one every two to four steps.

For each image:

1. Start from the extracted picture, then trim it to the part of the screen the step is about:
   `python <skill>/scripts/pdf_images.py trim "<image.png>" <left> <top> <right> <bottom> "<out.png>"` (pixels).
   Trimming is almost always needed. Step-recorder PDFs put a banner above each screenshot, and the screen itself often shows the recorder's name, test data, real sales figures or a customer's branding.
   If a screenshot is flattened into the page, cut it from the page instead: `pdf_images.py crop "<pdf>" <page> <left> <top> <right> <bottom> "<out.png>"` (fractions of the page).
2. **Look at the result with the Read tool.** Confirm it shows what the step says and that the labels match your text.
3. Check it is safe to publish. It must not show a real customer, team or venue name or logo, a person's name, email, phone number or card details, sales or revenue figures, internal addresses, test or staging values, or an unreleased feature. If trimming cannot remove the problem, leave the image out and tell the writer which screen needs a clean capture.
4. Save it to `images/<article-slug>/NN-short-description.png` beside the article, numbered in order of appearance.

You cannot draw on images. A recorder's highlight box around the relevant control is fine to keep.

### 6. Draft, then check the voice

Follow `references/article-template.md` for structure and depth, `references/voice-and-tone.md` for wording, and the pack's `product.md` for the product's own terms. Apply the voice as written, whatever the phrasing of the PDF or the request. If a writer asks for a different tone, say that the house voice is fixed in `voice-and-tone.md` and that changing it there changes it for everyone.

**How to handle what you do not know.** The article must be publishable as it stands, so `[VERIFY]`, `[SCREENSHOT]`, `[TODO]`, "confirm with" and similar never appear in it. In order of preference:

1. **Find out.** Most gaps close with one more lookup in the code or Jira.
2. **Write at the level you are sure of.** If you know there is a save action but not its label, write "Save your changes." Bold only labels you have seen.
3. **Leave it out.**

Never invent a click path, button label, field name, limit or cause. Never write from general knowledge about topics the pack lists as known gaps. Everything you settled by method 2 or 3 goes in your chat notes.

Then run the self-check at the end of `voice-and-tone.md`.

### 7. Scrub for internal content

Reread the draft and the images as a customer and remove:

- Jira keys and project names, sprint or release codenames, version labels, "new in".
- Other customers' names, or anything identifying a business, venue or team.
- Database tables, column or class names, SQL, API payloads, internal IDs, repo or service names.
- Steps only retailcloud staff can perform (activation switches, Partner Portal, back-end setup). Say who does it and what the reader has afterwards.
- Credentials, service addresses, environment names.
- Payment vendor internals.
- Roadmap, open tickets, known defects, "coming soon".
- Internal metrics, adoption commentary, pricing or commercial terms.
- Anything the pack marks `[INTERNAL]` or lists as not for publication.

### 8. Build and deliver

Save the article as `<kebab-case-title>.md` in the folder the writer names, or `./help-articles/<product>/` otherwise, with images in `images/<article-slug>/`. Format per `references/document360.md`. Then build the versions that carry their images with them:

```
python <skill>/scripts/build_article.py "<article.md>"
```

This writes `<slug>.docx` (import into Document360 and the images come with it) and `<slug>.html` (a self-contained preview). It needs python-docx; if it reports that it is missing, run `python -m pip install python-docx`.

In your reply, give the paths and short **notes for the writer**:

- each source you used and what it contributed, one line each, and any you could not reach,
- images used and any screen that needs a clean capture,
- anything you worded generally or left out because it could not be confirmed,
- where the PDF and other sources disagreed and which you followed.

Keep these notes out of the article files.

### 9. Keep the pack current

When the PDF, the code or the writer confirms a label, path or behaviour, update the pack's `knowledge.md` per the last section of `research.md`. For a product that had no pack, save what you learned as a new pack. Tell the writer you did, and that the change is only in their copy of the skill until it is shared with the team.

## Other requests

- **Check or rewrite an existing article**: run the `voice-and-tone.md` self-check and the step 7 scrub against it, fix what fails, and list what you changed.
- **A batch with no PDFs**: work through the pack's `catalog.md` in order, one file per article, one combined set of notes.
- **"Add a product"**: follow "Adding a pack" in `products/README.md`.
