# FanVista help articles - a Claude skill

Give Claude a PDF that shows a FanVista workflow. It reads the flow, gathers the missing detail from retailcloud's connected sources, and writes a customer-facing user guide for the Document360 help desk, in one fixed house voice, with screenshots taken from the PDF.

Every writer on the team uses the same skill, so every article sounds the same.

> **Internal to retailcloud.** The skill bundles internal product knowledge and pointers to internal documents. Keep this repository private.

## What you get

For each workflow PDF, Claude produces:

- a finished, publish-ready article with no placeholders, delivered three ways: a Word file with the images embedded (import this into Document360), a self-contained preview page for review, and the Markdown source with a metadata header (title, slug, category, description, tags);
- an `images/<article-slug>/` folder of screenshots cut from the PDF;
- notes in the chat, never in the article: which sources were used, anything worded generally because it could not be confirmed, and any screen that needs a clean capture.

## Install

Pick the one that matches how you use Claude.

### Claude Code, as a plugin (updates with one command)

```
/plugin marketplace add iamdanusabu/documentation-skill
/plugin install fanvista-help-articles@retailcloud-docs
```

To update later: `/plugin marketplace update retailcloud-docs`.

### Claude Code, by copying the folder

Clone the repository, then run the installer from inside it:

- Windows (PowerShell): `.\install.ps1`
- macOS, Linux, Git Bash: `bash install.sh`

This copies the skill to `~/.claude/skills/fanvista-help-articles` and installs the one Python package it needs. Restart Claude Code afterwards. To update, pull and run the installer again.

### Claude desktop app or claude.ai

1. Download `dist/fanvista-help-articles.skill` from this repository.
2. In Claude, open **Settings** and go to the skills section (under **Capabilities** on most plans).
3. Upload the `.skill` file and turn the skill on.

Code execution must be turned on for the image extraction to run. Your workspace admin may need to allow custom skills.

## What you need

| Requirement | Why | Without it |
| --- | --- | --- |
| Brain, Atlassian and Google Drive connectors turned on for your Claude account | The skill researches every article itself from these | It falls back to the knowledge snapshot bundled with it, and articles are thinner |
| Python 3.9 or later with PyMuPDF and python-docx (`pip install -r requirements.txt`) | Cuts screenshots out of the PDF and builds the Word file with images embedded | Articles are delivered as Markdown without images |

You turn the connectors on once, in **Settings > Connectors**. After that the skill finds and loads them by itself each time it starts, and tells you in one line which are connected. See [docs/CONNECTORS.md](docs/CONNECTORS.md).

## Use it

Give it the PDF. That is the whole input.

```
/fanvista-help-articles C:\docs\pickup-setup.pdf
```

Add a line of context if it helps: who the guide is for, or something to emphasise.

```
/fanvista-help-articles C:\docs\pickup-setup.pdf  for venue admins, mention that times can differ per event
```

You can also just say it in a sentence: "Write the user guide from C:\docs\pickup-setup.pdf".

What happens next, without further input from you:

1. It connects to Brain, Jira, Confluence and Drive and reports which are available.
2. It reads every screen in the PDF.
3. It researches the topic: the code behind the screen, released tickets, the playbook, past support questions.
4. It writes the guide in the house voice, cuts the screenshots from the PDF, and builds the Word, preview and Markdown files.
5. It tells you which sources it used and anything it could not confirm.

Other things it does:

- **No PDF**: "Write the help article for creating a Quickpick menu." It writes from the bundled knowledge and the connectors, without images.
- **Tone check**: "Check this article against the house voice" with the text or file.
- **Planning**: "What FanVista articles should we write?" It answers from the 48-article catalog.

### Before you publish

The article itself is complete. Read Claude's notes in the chat: they list anything it worded generally because no source confirmed the detail, so you can sharpen it if you know the answer.

Then in Document360: create the article by importing the `.docx` file, so the text, tables and images arrive together, and copy the title, slug, category, description and tags from the top of the `.md` file into the article settings. To use the Markdown editor instead, upload the images folder to Drive, paste the Markdown body, and re-point each image.

## What is inside

```
skills/fanvista-help-articles/
  SKILL.md                      the workflow Claude follows
  references/
    voice-and-tone.md           the house voice - the single authority on wording
    article-template.md         page structure, images, markers, worked example
    document360.md              publishing format
    fanvista-knowledge.md       product knowledge snapshot (dated at the top)
    article-catalog.md          the planned help set and canonical titles
    research.md                 how it connects to the sources, the searches it runs, what to trust
  examples/                     three finished articles: admin, staff, fan
  scripts/pdf_images.py         extracts, crops and trims images from a PDF
  scripts/build_article.py      builds the Word file and preview page with images embedded
dist/fanvista-help-articles.skill   packaged skill for upload
.claude-plugin/                 plugin and marketplace manifests
docs/CONNECTORS.md              turning on Brain, Atlassian and Drive
install.ps1, install.sh         copy-install for Claude Code
build.sh                        rebuilds the package in dist/
```

## Known limits

- **Screen labels in the bundled knowledge are not all confirmed.** It was built from documents, not from the live console. A workflow PDF settles the labels for its own topic; section 17 of `fanvista-knowledge.md` lists what is still open.
- **Document360 callout syntax** (`:::(Warning) (Warning)`) has not been confirmed in a live project. If callouts do not render when pasted, correct `references/document360.md`.
- **The skill cannot draw on images.** It tells you where a highlight or arrow would help.
- **Some topics have no source**: cancellations and refunds, in-seat handover, pre-order handling on event day. The skill flags these instead of guessing.

## Keeping it current

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: this repository is the master copy. When Claude tells you it updated its knowledge file after a PDF confirmed something, bring that change back here so the other writers get it.
