# Help desk articles - a Claude skill

Give Claude a PDF that shows a workflow in a retailcloud product. It asks which product you are documenting, reads the flow, researches the detail from Brain, Jira, Confluence and Drive, and writes a finished, publish-ready user guide for the Document360 help desk, in one fixed house voice, with screenshots taken from the PDF.

Every writer uses the same skill, whatever product they cover, so every article sounds the same.

> **Internal to retailcloud.** The skill bundles internal product knowledge and pointers to internal documents. Keep this repository private.

## What you get

- a finished article with no placeholders, delivered three ways: a Word file with the images embedded (import this into Document360), a self-contained preview page for review, and the Markdown source with a metadata header;
- an `images/<article-slug>/` folder of screenshots cut from the PDF;
- notes in the chat, never in the article: which sources were used, anything worded generally because it could not be confirmed, and any screen that needs a clean capture.

## Products

Product knowledge lives in packs under `skills/help-desk-articles/products/`.

| Product | Pack |
| --- | --- |
| FanVista | Full pack: knowledge, 48-article catalog, four example articles |
| Any other product | No pack yet. The skill researches it from the connected sources, writes the article, and saves what it learned as a new pack for you to commit |

## Install

### Claude Code, as a plugin

```
/plugin marketplace add iamdanusabu/documentation-skill
/plugin install help-desk-articles@retailcloud-docs
```

To update later: `/plugin marketplace update retailcloud-docs`.

### Claude Code, by copying the folder

Clone the repository, then run the installer from inside it:

- Windows (PowerShell): `.\install.ps1`
- macOS, Linux, Git Bash: `bash install.sh`

This copies the skill to `~/.claude/skills/help-desk-articles` and installs the Python packages it needs. Restart Claude Code afterwards. To update, pull and run the installer again.

### Claude desktop app or claude.ai

1. Download `dist/help-desk-articles.skill` from this repository.
2. In Claude, open **Settings** and go to the skills section.
3. Upload the `.skill` file and turn the skill on.

Code execution must be turned on for the image steps to run.

## What you need

| Requirement | Why | Without it |
| --- | --- | --- |
| Brain, Atlassian and Google Drive connectors turned on for your Claude account | The skill researches every article itself from these | It falls back to the product pack, and articles are thinner. For a product with no pack there is little to fall back on |
| Python 3.9 or later with PyMuPDF and python-docx (`pip install -r requirements.txt`) | Cuts screenshots out of the PDF and builds the Word file with images embedded | Articles are delivered as Markdown without images |

You turn the connectors on once, in **Settings > Connectors**. After that the skill loads them by itself each time and tells you in one line which are connected. See [docs/CONNECTORS.md](docs/CONNECTORS.md).

## Use it

Give it the PDF.

```
/help-desk-articles C:/docs/pickup-setup.pdf
```

It asks one question: which product the guide is for. To skip the question, say it up front, with any context that helps:

```
/help-desk-articles C:/docs/pickup-setup.pdf  FanVista, for venue admins
```

What happens next, without further input from you:

1. It loads the product's pack and connects to Brain, Jira, Confluence and Drive.
2. It reads every screen in the PDF.
3. It researches the topic: the code behind the screen, released tickets, the product's playbook, past support questions.
4. It writes the guide in the house voice, cuts the screenshots from the PDF, and builds the Word, preview and Markdown files.
5. It tells you which sources it used and anything it could not confirm.

Other things it does:

- **No PDF**: "Write the help article for creating a Quickpick menu in FanVista."
- **Tone check**: "Check this article against the house voice."
- **Add a product**: "Add a product pack for OrderUp."

### Publishing

In Document360, create the article by importing the `.docx` file, so the text, tables and images arrive together, and copy the title, slug, category, description and tags from the top of the `.md` file into the article settings. To use the Markdown editor instead, upload the images folder to Drive, paste the Markdown body, and re-point each image.

## What is inside

```
skills/help-desk-articles/
  SKILL.md                      the workflow Claude follows
  references/                   shared by every product
    voice-and-tone.md           the house voice
    article-template.md         page structures, level of detail, images
    document360.md              publishing format
    research.md                 connecting to sources, the searches, what to trust
  products/
    README.md                   list of packs; how to work without one; how to add one
    _template/                  empty pack to copy
    fanvista/                   product.md, knowledge.md, catalog.md, examples/
  scripts/
    pdf_images.py               extracts, crops and trims images from a PDF
    build_article.py            builds the Word file and preview page
dist/help-desk-articles.skill   packaged skill for upload
.claude-plugin/                 plugin and marketplace manifests
docs/CONNECTORS.md              turning on Brain, Atlassian and Drive
install.ps1, install.sh, build.sh
```

## Known limits

- **Only FanVista has a pack.** The first article for any other product takes longer and depends entirely on the connectors.
- **Screen labels come from the PDF.** Without a PDF, labels are only as good as the pack.
- **Document360 callout syntax and Word import** have not been confirmed in a live project. If either misbehaves, correct `references/document360.md`.
- **The skill cannot draw on images.**

## Keeping it current

See [CONTRIBUTING.md](CONTRIBUTING.md). This repository is the master copy. When Claude tells you it updated or created a pack, bring that change back here so the other writers get it.
