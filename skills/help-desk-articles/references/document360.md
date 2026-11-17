# Publishing format: Document360

retailcloud's help desk runs on Document360. Articles are written so they paste straight into its **Markdown editor**.

## File layout

Each file has a metadata header, then the body. The header is for the person publishing; they copy its values into Document360's article settings and do not paste it into the editor.

```markdown
---
title: Set up customer notifications for FanVista
slug: set-up-customer-notifications-for-fanvista
category: FanVista > One-time setup
description: Turn on the emails and texts fans receive when they order, and when their order is ready.
tags: fanvista, notifications, setup
---

<One or two sentence opening.>

## When you would do this
...
```

- **title** - the catalog title. Document360 shows it as the page heading, so the body has **no `#` heading**; body sections start at `##`.
- **slug** - kebab-case of the title. Keep it stable once published.
- **category** - `<Product> > <section>`, using the section names in the product pack's catalog. With no catalog, use a plain section name such as Getting started, Setup, Daily use, Reports or Troubleshooting. The publisher can remap these to the real category tree.
- **description** - one sentence, under about 160 characters, for search results and SEO.
- **tags** - three to six lowercase terms a customer would search.

## Callouts

Use Document360's callout blocks, not blockquotes:

```markdown
:::(Info) (Note)
Helpful context that is not required to finish the task.
:::

:::(Info) (Tip)
A faster or safer way to do it.
:::

:::(Warning) (Warning)
Something that breaks, cannot be undone, or silently fails if ignored.
:::
```

The first bracket is the callout type (`Info`, `Warning`, `Error`); the second is the heading shown to the reader. Put a blank line before and after the block. Inside a numbered list, a callout usually ends the list in Document360, so place it directly after the list item and let the next step continue the numbering explicitly (`3.`, `4.`).

This syntax is from memory of Document360's editor and was not confirmed against a live project. The first time an article is pasted, ask the user whether callouts rendered; if not, record the correct syntax here.

## Getting the images into Document360

Document360 hosts its own images, so a Markdown file that points at local image files shows broken pictures when pasted. Every article is therefore delivered in three forms, built by `scripts/build_article.py`:

| File | Use |
| --- | --- |
| `<slug>.docx` | **The one to publish from.** Word file with all images embedded. In Document360, create the article by importing the Word file; the text, tables and images arrive together. Callouts arrive as shaded boxes; convert them to Document360 callouts if wanted. |
| `<slug>.html` | Self-contained preview with all images embedded. Open it in a browser to review, or send it for sign-off. Selecting all and pasting into the Advanced WYSIWYG editor also carries the formatting. |
| `<slug>.md` + `images/<slug>/` | The source. For the Markdown editor: upload the images folder to Document360 Drive, paste the Markdown, and re-point each image. Also what you edit when the article changes; rebuild the other two afterwards. |

Tell the writer to publish from the `.docx` unless they say they prefer another route. The Word import route was not confirmed against a live Document360 project; the first time, ask the writer whether the images arrived, and record the answer here.

## Other rules

- **Tables**: standard pipe tables work in the Markdown editor. They do **not** render in the Advanced WYSIWYG editor.
- **Links between articles**: write the other article's catalog title in italics with no URL. The publisher links it in Document360, where the URL depends on their category structure.
- **Images**: save them beside the article in `images/<article-slug>/`, named `NN-short-description.png` in order of appearance, and reference them with a relative path: `![Alt text](images/<article-slug>/01-branding-screen.png)`. The publisher uploads the folder to Document360's Drive and re-points each image; the relative paths make it obvious which file goes where. PNG only. Where no usable image exists, write the step so it stands without one.
- **Editor choice**: a Document360 article can be converted from Markdown to the Advanced WYSIWYG editor but not back. If the user says their project uses the Advanced WYSIWYG editor, deliver clean HTML instead (headings from `<h2>`, lists, `<table>`, no inline styles), tell them tables and callouts may need rebuilding with the toolbar, and say so in the reviewer notes.
