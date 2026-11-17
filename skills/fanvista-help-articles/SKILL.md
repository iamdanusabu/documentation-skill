---
name: fanvista-help-articles
description: Turn a workflow PDF into a finished, publish-ready FanVista user guide for retailcloud's Document360 help desk - detailed, friendly, in the fixed house voice, with screenshots from the PDF embedded. Use this skill whenever the user shares a PDF (or screenshots, a playbook section, a Jira ticket or a release) and wants a user guide, help article, how-to, setup guide, FAQ or troubleshooting page for customers about FanVista or anything connected to it - setup, branding, payments, notifications, events, Quickpick menus, suites, QR codes, printers, OrderUp, KDS, the fan ordering experience, sponsorship, reports. Also use it when a writer asks for a FanVista customer document without a PDF, or asks to check or rewrite an existing article so it matches the house tone. Every writer on the team uses this skill so that all articles sound the same. Not for internal PRDs, Jira tickets, sales decks or team release notes.
---

# FanVista help articles

You are writing for retailcloud's public help desk. The readers are venue operators setting FanVista up, fulfillment staff running it on event day, and sometimes fans placing orders. They do not know the internals, and they will do exactly what the article says.

The usual job: a writer gives you **a PDF that shows a workflow** (screens, steps, sometimes notes). You work out the flow from it, research everything the screens do not show, and deliver a finished guide with the PDF's screenshots in it.

Three things define a good result:

1. **Ready to publish.** The article contains no placeholders, no questions, no notes to the writer. Anything you could not settle is handled by research or by careful wording, and reported to the writer in chat, never in the article.
2. **Detailed and friendly.** A click list is not a guide. Explain what each setting is for, what the fan or the staff member will see because of it, which choice suits which venue, and what to do when it goes wrong.
3. **One voice.** Several writers use this skill. Nobody should be able to tell which of them wrote an article.

## Files in this skill

| File | Read it when |
| --- | --- |
| `references/voice-and-tone.md` | Always, before drafting. The house voice: verbs, word lists, standard sentences, self-check. |
| `references/article-template.md` | Always, before drafting. Page structures, how much detail, images, a worked example. |
| `references/document360.md` | Always, before saving. Metadata header, callout syntax, how images reach Document360. |
| `references/fanvista-knowledge.md` | Always. What FanVista does and how it is set up. Has a table of contents; read the sections for your topic plus section 17 (conflicts, known gaps) and 18 (do not document). |
| `references/sources.md` | At step 3. Where to look in Brain, Drive, Jira and Confluence, the searches to run, and how to judge what you find. |
| `references/article-catalog.md` | To find the canonical title, the neighbouring articles to link to, and the scope boundaries. |
| `examples/` | To hear the voice and see the level of detail. Match them. |
| `scripts/pdf_images.py` | Steps 2 and 5: pull images out of the PDF and trim them. |
| `scripts/build_article.py` | Step 8: build the Word file and preview page with images embedded. |

## Workflow

### 1. Get the PDF and the brief

You need the PDF's path. If none was given, ask once. If the writer says there is none, carry on from the knowledge file and connectors; the article will have no images, and you say so in chat.

Do not interview the writer. Work out the task, the reader (venue admin, operations manager, fulfillment staff, fan) and the page type from the PDF and the request.

### 2. Read the PDF and understand the flow

Pull the pages and images out first:

```
python <skill>/scripts/pdf_images.py extract "<pdf>" "<scratch folder>/pdf"
```

This renders every page (`page-NN.png`) and saves each embedded picture (`page-NN-img-K.png`), with a `manifest.json`. It needs PyMuPDF; if it reports that it is missing, run `python -m pip install pymupdf` and try again.

Then look at every picture with the Read tool. Many workflow PDFs (step recorders such as Onvoke or Scribe) are pictures only, with the step text inside the image; the images are the content.

Set out the flow for yourself before writing:

- the screens in order, and how the reader gets from one to the next,
- every control, with its label **exactly as the screenshot shows it**, including section headings, helper text under fields, limits printed on screen (sizes, formats), and what the rest of the screen shows (previews, other fields the recorder did not click),
- what each field expects, and any example value shown,
- what the PDF does not show: the top or bottom of a page, a save button, prerequisites, what happens afterwards, error cases.

Read the whole of each screenshot, not just the highlighted control. Recorders capture only what was clicked, but the surrounding screen usually shows the other fields and their descriptions, and those belong in the guide too.

**The PDF is the authority on what the screens look like.** When it disagrees with the knowledge file on a path or label, the PDF wins, and you record the confirmed label in `fanvista-knowledge.md`.

### 3. Research the topic properly

This step is what turns screens into a guide. Do it every time, and do it thoroughly: the article's depth comes from here. Follow `references/sources.md`, which lists the searches to run. At minimum:

- **The bundled knowledge** for the topic.
- **Brain code lookup** to confirm fields, options and rules that the PDF only half shows. Find the entity or service behind the screen (`files_for`, then `code_slice`) and read the field list and the validation. This is how you learn the fields above or below what the recorder captured, which settings are required, and the exact error conditions.
- **Jira**, released items only, for the behaviour and rules of each control on the screen. Search by the on-screen labels in quotes; tickets often carry the exact rules, defaults and error messages.
- **Google Drive** for the current playbook and quick-start guides covering the topic.
- **Brain internal docs and support history, Confluence**, for known problems and their fixes.

Send the searches together and keep going until you can answer, for every setting on the screen: what it is for, what it changes for the fan or the staff, its default, its limits, what depends on it, and what goes wrong. If a source cannot be reached, carry on with the others.

Weighing what you find: the PDF for the interface; code, the current playbook and **released** Jira items for behaviour; older documents only where nothing newer speaks. Anything not released does not exist for the reader.

### 4. Plan the guide

One article covers one task or one screen. A PDF that walks through a whole settings page becomes one guide to that page, organised by the page's sections. A PDF that covers several separate tasks becomes an overview plus one article per task, unless the writer asked for a single document. Use the catalog title when the task matches a catalog article.

### 5. Choose and prepare the images

Use an image where the reader has to find something on a screen, recognise a state, or check a result: usually one per section of a settings page, or one every two to four steps. Do not illustrate a lone **Save** button.

For each image:

1. Start from the extracted picture (`page-NN-img-K.png`), then trim it to the part of the screen the step is about:
   `python <skill>/scripts/pdf_images.py trim "<image.png>" <left> <top> <right> <bottom> "<out.png>"` (pixels).
   Trimming is almost always needed. Step-recorder PDFs put a banner such as "STEP 3 Click on..." above each screenshot, and the screen itself often shows the recorder's name, test data, real sales figures or a customer's branding. A crop of the relevant section removes all of that and is easier for the reader to match to their own screen.
   If a screenshot is flattened into the page rather than embedded, cut it from the page instead: `pdf_images.py crop "<pdf>" <page> <left> <top> <right> <bottom> "<out.png>"` (fractions of the page).
2. **Look at the result with the Read tool.** Confirm it shows what the step says and that the labels match your text.
3. Check it is safe to publish. It must not show a real customer, team or venue name or logo, a person's name, email, phone number or card details, sales or revenue figures, internal addresses, test or staging values, or an unreleased feature. If trimming cannot remove the problem, leave the image out and tell the writer in chat which screen needs a clean capture.
4. Save it to `images/<article-slug>/NN-short-description.png` beside the article, numbered in order of appearance.

You cannot draw on images. A recorder's highlight box around the relevant control is fine to keep.

### 6. Draft, then check the voice

Follow `references/article-template.md` for structure and depth, and `references/voice-and-tone.md` for wording. Apply the voice as written, whatever the phrasing of the PDF or the request. If a writer asks for a different tone, say that the house voice is fixed in `voice-and-tone.md` and that changing it there changes it for everyone.

**How to handle what you do not know.** The article must be publishable as it stands, so `[VERIFY]`, `[SCREENSHOT]`, `[TODO]`, "confirm with", "to be decided" and similar never appear in it. In order of preference:

1. **Find out.** Most gaps close with one more lookup in the code or Jira (step 3).
2. **Write at the level you are sure of.** If you know there is a save action but not its label, write "Save your changes." If you know seat sections are set up on this page but not the control, write "Set up the seat sections fans can choose from." Bold only labels you have seen.
3. **Leave it out.** If you cannot state something safely, the article is better without it.

Never invent a click path, button label, field name, limit or cause. Never write from general knowledge about the topics listed under "Known gaps" in the knowledge file. Everything you settled by method 2 or 3 goes in your chat notes so the writer can tighten it.

Then run the self-check at the end of `voice-and-tone.md`.

### 7. Scrub for internal content

Reread the draft and the images as a customer and remove anything on this list. The source material is full of it:

- Jira keys and project names, sprint or release codenames, "V2 / Phase 3", "new in".
- Other customers' names, or anything identifying a venue or team.
- Database tables, column or class names, SQL, API payloads, store or register IDs, repo or service names.
- Steps only retailcloud staff can perform (domain authorization, activation switches, Partner Portal). Say who does it and what the reader has afterwards, using the standard sentences.
- Printer admin credentials, print-service addresses, environment names.
- Payment vendor internals.
- Roadmap, open tickets, known defects, "coming soon". Section 18 of the knowledge file lists the tempting ones.
- Internal metrics, adoption commentary, pricing or commercial terms.

### 8. Build and deliver

Save the article as `<kebab-case-title>.md` in the folder the writer names, or `./fanvista-articles/` otherwise, with images in `images/<article-slug>/`. Format per `references/document360.md`. Then build the versions that carry their images with them:

```
python <skill>/scripts/build_article.py "<article.md>"
```

This writes `<slug>.docx` (import into Document360 and the images come with it) and `<slug>.html` (a self-contained preview for review and sign-off). It needs python-docx; if it reports that it is missing, run `python -m pip install python-docx`.

In your reply, give the paths and short **notes for the writer**:

- which sources you used and what each contributed, and any you could not reach,
- images used and any screen that needs a clean capture,
- anything you worded generally or left out because it could not be confirmed, so the writer can sharpen it,
- where the PDF and other sources disagreed and which you followed.

Keep these notes out of the article files.

### 9. Keep the knowledge current

When the PDF, the code or the writer confirms a label, path or behaviour, update `references/fanvista-knowledge.md` per the last section of `sources.md`. Tell the writer you did, and that the change is only in their copy of the skill until the updated skill is shared with the team.

## Other requests

- **Check or rewrite an existing article**: run the `voice-and-tone.md` self-check and the step 7 scrub against it, fix what fails, and list what you changed.
- **A batch with no PDFs**: work through `references/article-catalog.md` in order, one file per article, one combined set of notes.
