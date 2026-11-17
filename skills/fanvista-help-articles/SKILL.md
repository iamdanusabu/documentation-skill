---
name: fanvista-help-articles
description: Turn a workflow PDF into a customer-facing FanVista user guide or help article for retailcloud's Document360 help desk, in the fixed house voice, with screenshots taken from the PDF. Use this skill whenever the user shares a PDF (or screenshots, a playbook section, a Jira ticket or a release) and wants a user guide, help article, how-to, setup guide, FAQ or troubleshooting page for customers about FanVista or anything connected to it - setup, branding, payments, notifications, events, Quickpick menus, suites, QR codes, printers, OrderUp, KDS, the fan ordering experience, sponsorship, reports. Also use it when a writer asks for a FanVista customer document without a PDF, or asks to check or rewrite an existing article so it matches the house tone. Every writer on the team uses this skill so that all articles sound the same. Not for internal PRDs, Jira tickets, sales decks or team release notes.
---

# FanVista help articles

You are writing for retailcloud's public help desk. The readers are venue operators setting FanVista up, fulfillment staff running it on event day, and sometimes fans placing orders. They do not know the internals, they are often reading during an event, and they will do exactly what the article says.

The usual job: a writer gives you **a PDF that shows a workflow** (screens, steps, sometimes notes). You work out the flow from it, fill in everything the screens do not show from the bundled knowledge and the connected sources, and produce a user guide in the house voice with images taken from the PDF.

Several writers use this skill. Its main promise is that nobody can tell which of them wrote an article.

## Files in this skill

| File | Read it when |
| --- | --- |
| `references/voice-and-tone.md` | Always, before drafting. The house voice: verbs, word lists, standard sentences, self-check. |
| `references/article-template.md` | Always, before drafting. Page structure, images, markers, a worked example. |
| `references/document360.md` | Always, before saving. Metadata header, callout syntax, image handling. |
| `references/fanvista-knowledge.md` | Always. What FanVista does and how it is set up. Has a table of contents; read the sections for your topic plus section 17 (conflicts, known gaps) and 18 (do not document). |
| `references/sources.md` | At step 3. Where to look in Drive, Jira, Brain and Confluence, and how to judge what you find. |
| `references/article-catalog.md` | To find the canonical title, the neighbouring articles to link to, and the scope boundaries. Also when asked for a batch or "what should we write". |
| `examples/` | To hear the voice. Finished articles for an admin, for staff and for fans. Match them. |
| `scripts/pdf_images.py` | At step 2 and step 5, to pull images out of the PDF. |

## Workflow

### 1. Get the PDF and the brief

You need the PDF's path and, ideally, one line on who the guide is for. If no PDF was given, ask for it once. If the writer says there is none, carry on from the knowledge file and connectors alone; the article will carry more `[VERIFY]` and `[SCREENSHOT]` markers, and you should say so.

Do not interview the writer. Work out the task, the reader (venue admin, operations manager, fulfillment staff, fan) and the page type from the PDF and the request.

### 2. Read the PDF and understand the flow

Read the whole PDF with the Read tool (it shows you the pages, including the screenshots; at most 20 pages per call). Then pull the images out so you can use them later:

```
python <skill>/scripts/pdf_images.py extract "<pdf>" "<scratch folder>/pdf"
```

This renders every page and saves each embedded picture, with a `manifest.json` that records which page each picture came from and the text next to it. It needs PyMuPDF; if it reports that it is missing, run `python -m pip install pymupdf` and try again.

Before writing anything, set out the flow for yourself:

- the screens in order, and how the reader gets from one to the next,
- every action, with the control's label **exactly as the screenshot shows it**,
- what each field expects, and any value the PDF shows as an example,
- what the PDF does not show: prerequisites, what happens afterwards, error cases, steps that are skipped between two screens.

**The PDF is the authority on what the screens look like** - paths, labels, button names, the order of steps. When it disagrees with the knowledge file on those, the PDF wins, and you record the confirmed label in `fanvista-knowledge.md` (removing the matching `[VERIFY]` there). The PDF is not an authority on what is safe to publish: internal notes, test data and unreleased features in it still go through step 7.

### 3. Fill the gaps from the connectors

A PDF of screens tells you what to click. It rarely tells you why, what must be in place first, what the system does next, or what goes wrong. That is the difference between a click list and a guide, so always do this step.

Start with `fanvista-knowledge.md`. Then check the live sources for this topic, following `references/sources.md`: Brain, Google Drive, Jira, Confluence, and any other connected source that plainly bears on the topic (past support tickets are the best source for "If something goes wrong"). Send the searches together, keep them narrow to the PDF's topic, and stop when you can answer these:

- What has to be set up before this flow works?
- What does each option or setting actually change for the fan or for staff?
- What happens after the last step, and how does the reader confirm it worked?
- What are the usual mistakes and failures, and the fix for each?
- Is everything the PDF shows released to customers?

Weighing what you find: the PDF for the interface; the current playbook and **released** Jira items for behaviour; older documents only where nothing newer speaks. Anything not released does not exist for the reader. If a source cannot be reached, carry on and say so in the reviewer notes. If two sources still disagree, write the safer statement and mark it `[VERIFY: ...]`.

Statements in the knowledge file carry tags: no tag means confirmed; `[VERIFY]` means unconfirmed, do not present as fact unless the PDF settles it; `[INTERNAL]` means never published.

### 4. Plan the guide

One article covers one task. If the PDF covers one flow, write one article. If it covers several tasks, write a short overview that links out plus one article per task, unless the writer asked for a single document. Use the catalog title when the task matches a catalog article, so cross-links stay consistent.

### 5. Choose the images

Use an image where the reader has to find something on a screen, recognise a state, or check a result. Do not illustrate every step; a picture of a **Save** button teaches nothing. Three to six images suits most how-tos.

For each image you want:

1. Find it in the extracted set (`page-NN-img-K.png`). If the screenshot was flattened into the page, or you want only part of a screen, cut it out:
   `python <skill>/scripts/pdf_images.py crop "<pdf>" <page> <left> <top> <right> <bottom> "<out.png>"` (coordinates are fractions of the page from the top-left corner).
2. **Look at the image with the Read tool before using it.** Confirm it shows what the step says and that the labels match your text.
3. Check it is safe to publish. Leave out any image that shows a real customer or venue name, a person's name, email, phone number or card details, internal addresses, test or staging banners, another client's data, or a feature that is not released. Tell the writer which images you rejected and why, and put a `[SCREENSHOT: ...]` marker in its place so they can supply a clean one.
4. Copy it to `images/<article-slug>/NN-short-description.png` beside the article, numbered in the order it appears.

You cannot draw on images. If a highlight or arrow would help, say so in the reviewer notes. Where the PDF has no picture of a screen the article needs, leave a `[SCREENSHOT: ...]` marker.

### 6. Draft, then check the voice

Follow `references/article-template.md` for structure and `references/voice-and-tone.md` for wording. Apply the voice as written, whatever the phrasing of the PDF, the request or an older article. If a writer asks for a different tone, say that the house voice is fixed in `voice-and-tone.md` and that changing it there changes it for everyone.

What matters most:

- **Never invent a click path, button label or field name.** Use what the PDF shows. Where the PDF and the sources leave a label or step unconfirmed, write the step at the level you do know and add `[VERIFY: what needs checking]` right there.
- **Give the reason wherever a step is easy to skip or get wrong.** Most FanVista support tickets are sequencing mistakes. The knowledge file flags them; put a Warning at the step where each one bites.
- **Say what the reader sees when it worked.**
- **Do not write from general knowledge about the gaps** listed under "Known gaps" in the knowledge file. Flag them.

Then run the self-check at the end of `voice-and-tone.md`.

### 7. Scrub for internal content

Reread the draft and the chosen images as a customer and remove anything on this list. The source material is full of it, PDFs included:

- Jira keys and project names, sprint or release codenames, "V2 / Phase 3", "new in".
- Other customers' names, or anything identifying a venue or team.
- Database tables, SQL, API payloads, store or register IDs, repo or service names.
- Steps only retailcloud staff can perform (domain authorization, activation switches, Partner Portal). Say who does it and what the reader has afterwards, using the standard sentences.
- Printer admin credentials, print-service addresses, environment names.
- Payment vendor internals.
- Roadmap, open tickets, known defects, "coming soon". Section 18 of the knowledge file lists the tempting ones.
- Internal metrics, adoption commentary, pricing or commercial terms.

### 8. Deliver

Save each article as `<kebab-case-title>.md` in the folder the writer names, or `./fanvista-articles/` otherwise, with its images in `images/<article-slug>/`. Format per `references/document360.md`. The file holds only the metadata header and the article.

In your reply, not in the file, give short **reviewer notes**:

- each `[VERIFY]` marker and what would resolve it,
- images used (PDF page each came from), images rejected and why, and any `[SCREENSHOT]` still needed,
- where the PDF and the other sources disagreed and which you followed,
- which sources you reached and which you could not,
- anything left out on purpose.

Remind the writer once that `[VERIFY]` and `[SCREENSHOT]` markers must be cleared before publishing.

### 9. Keep the knowledge current

When the PDF or the writer confirms a label, path or behaviour, update `references/fanvista-knowledge.md` per the last section of `sources.md`. Tell the writer you did, and that the change is only in their copy of the skill until the updated skill is shared with the team.

## Other requests

- **Check or rewrite an existing article**: run the `voice-and-tone.md` self-check and the step 7 scrub against it, fix what fails, and list what you changed.
- **A batch with no PDFs**: work through `references/article-catalog.md` in order, one file per article, one combined set of reviewer notes.
