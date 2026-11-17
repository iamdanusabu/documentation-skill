# Article format

## File

```markdown
---
title: <catalog title, or a new one>
slug: <kebab-case-title>
category: <Product> > <section from the pack>
description: <one sentence, under 160 characters>
tags: <3 to 6 lowercase search terms>
---

<Opening. No # heading: the help desk adds the title. Sections start at ##.>
```

## Structures

**Guide to a settings page** (a PDF that walks through one page):

```
Opening: what the page is for, how long it takes, one-time or repeated
## What you will set up      table: section | what you decide | what it means for your customers
## Before you start
## Step 1: Open the <page> page
## Step 2: <first section, as a task>    1-2 sentences of purpose, numbered actions from 1, image, option table or tip
...
## Step N: Save and check your work
## What happens next
## Good to know
## Common questions          ### question, answered in 2-5 sentences, answer first
## If something goes wrong   table: What you see | Why | What to do
## Related articles          - *Title*
```

**How-to** (one task): Opening, `## When you would do this`, `## Before you start`, `## Steps`, `## What happens next`, `## Rules to know`, `## If something goes wrong`, `## Related articles`.

**Overview:** Opening, How it works, What you need, Where to go next. **Reference:** opening sentence, then tables. **FAQ / troubleshooting:** questions as `###`, grouped by theme.

Staff articles drop Rules to know unless one cannot be missed. End-customer articles keep only the opening, the steps, and problems as plain bullets, with no callouts. Drop any section that would be empty.

## Depth

For every setting or step that is not self-evident, give: what it is, what it changes for the customer or staff, how to choose (option table or example), an example value, and what depends on it. All of it comes from the fact sheet. A single-action how-to may be 300 words; a settings-page guide is often 1,200 to 2,000. Cut repetition, never explanation.

## Images

`![What it shows and what to look at](images/<slug>/01-description.png)` directly after its step, indented 3 spaces. No image available: write the step so it stands alone.

## Callouts

```
:::(Info) (Note)
Context that is not required.
:::
:::(Info) (Tip)
A faster or safer way.
:::
:::(Warning) (Warning)
Breaks, cannot be undone, or fails silently.
:::
```

At most two per section, at the step they apply to, with a blank line before and after. Warnings are for real traps; the pack lists the known ones. A callout ends a numbered list, so number the next step explicitly.

## Links

Other articles by catalog title in italics, no URL.
