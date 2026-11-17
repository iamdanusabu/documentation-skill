# Article standard

Numbered steps are the backbone. Short sections around them tell the reader when to do the task, what to have ready, what happens afterwards, the rules that apply, and what to do if it goes wrong. Bare steps let someone follow clicks without understanding the task; the surrounding sections are what prevent the support ticket.

Wording follows `voice-and-tone.md`. File format (metadata header, callout syntax, images) follows `document360.md`. The skeletons below already use both.

## Page types

### How-to (most articles)

```markdown
---
title: <Task, starting with a verb>
slug: <kebab-case-title>
category: FanVista > <section>
description: <One sentence.>
tags: <three to six terms>
---

<One or two sentences: what this does and the result.>

## When you would do this
<One to three lines. The situation that sends someone here. Say whether it is one-time or per event.>

## Before you start
- <What must already be set up, naming the article that covers it>
- <What to have in hand>

## Steps
1. <One action. Bold the exact on-screen label.>

   ![<What the image shows>](images/<slug>/01-<description>.png)

2. ...

## What happens next
<How the reader confirms it worked, what the system now does, and the next task.>

## Rules to know
- <Behaviours and limits that are not obvious from the screen>

## If something goes wrong
| What you see | Why | What to do |
| --- | --- | --- |

## Related articles
- *<Catalog title>*
```

### Overview

Explains what something is and how the parts fit. Sections: opening summary, "How it works" (a short numbered flow or a table), "What you need", "Where to go next". No Steps section.

### Reference

A lookup page: field lists, option tables, a checklist. Opening sentence, then tables.

### FAQ and troubleshooting

Questions as `###` headings, phrased the way a customer would ask, each answered in 2 to 5 sentences. Lead with the answer. Group by theme.

### By reader

| Reader | Sections |
| --- | --- |
| Venue admin, operations manager | All of them. |
| Fulfillment and kitchen staff | Opening, Before you start, Steps, If something goes wrong, Related articles. Add Rules to know only if there is one staff must not miss. |
| Fan | Opening, Steps, then "If something goes wrong" as plain bullets. No callouts. Fold anything else into the steps. |

Drop a section when it would be empty. Do not pad one to fill the template.

## Images

- Take images from the workflow PDF (see SKILL.md step 5). Place each directly after the step it illustrates, indented 3 spaces so it stays inside the step.
- Alt text says what the image shows and what to look at: `![Branding screen with Fulfillment Location selected](...)`. No "Screenshot of".
- Use an image where the reader must find something, recognise a state, or check a result. Not for every step.
- Where an image is needed and the PDF has none, or the PDF's image cannot be published, write `[SCREENSHOT: what it should show and what to highlight]` on its own line in the same position.

## Markers the writer must clear before publishing

- `[SCREENSHOT: ...]` as above.
- `[VERIFY: ...]` inline, right where the uncertain label or path appears. State exactly what to check.

Both are deliberately loud so they cannot slip into a published page.

## Callouts

One or two per page, placed at the step where they apply, never collected at the top. Reserve Warning for real traps. In FanVista these are mainly: the FanVista URL cannot be changed once created; the email receipt needs the Order Checkout trigger on first; no notification rule means no customer messages; no Fulfillment Location means no stock tracking and no dockets; items default to Retail; the deposit percentage must match the audience.

A callout ends a numbered list in Document360. Put it directly after its step and number the next step explicitly.

## Details that are easy to get wrong

- **Illustrative values** (a sample prefix, a sample time) are fine. Anything factual that is not in the PDF, the knowledge file or a source you checked is a guess: leave it out or mark it `[VERIFY]`, and list it in the reviewer notes.
- **Cross-links**: the other article's catalog title in italics, no URL. The publisher adds links in Document360.
- **Titles and file names**: use the catalog title when the task matches a catalog article.
- **Troubleshooting in a how-to**: keep "If something goes wrong" to the 3 to 5 failures specific to this task, then point to the matching troubleshooting article. This is the first section to trim when a page runs long.
- **Length**: most how-tos land between 250 and 600 words. Past 900 it is probably two articles.

## Worked example

```markdown
---
title: Set up customer notifications for FanVista
slug: set-up-customer-notifications-for-fanvista
category: FanVista > One-time setup
description: Turn on the emails and texts fans receive when they order and when their order is ready.
tags: fanvista, notifications, email, sms, setup
---

Notifications send your fans their order confirmation, the ready for pickup message and the delivery confirmation. You do this once for your venue. It applies to every event.

## When you would do this
During your first FanVista setup, before your first event. Return to it to add text messages or to change which messages fans receive.

## Before you start
- Your branding is saved. If you have not done this yet, see *Set up FanVista branding*.
- To send text messages, SMS must be turned on for your venue. retailcloud sets this up for you. Contact retailcloud Support to request it.

## Steps
1. Go to **FanVista** > **Setup** > **Notifications**.

   ![Notifications screen in FanVista Setup with the trigger list](images/set-up-customer-notifications-for-fanvista/01-notifications-screen.png)

2. Turn on **Order Checkout**. Fans receive the order confirmation as soon as they pay.

:::(Warning) (Warning)
Turn on **Order Checkout** before you design the email receipt. The receipt template cannot be saved until it is on.
:::

3. Turn on **Ready**. Fans receive the pickup message when your staff mark the order **Ready** in OrderUp.
4. Optional: Turn on **Delivered** to send a final confirmation when the order is handed over.
5. If you take suite orders, turn on **Cart Checkout**. Suite owners receive a confirmation while their order is still open.
6. Under **Channel**, turn on **Email**. Turn on **SMS** if your venue sends text messages.
7. Turn on **Add QR Code in Email**. Fans show this code at the counter to collect their order. [VERIFY: confirm whether this control is a toggle or a checkbox]
8. Select **Save**.

   ![Notifications screen with Order Checkout, Ready, Email and Add QR Code in Email turned on](images/set-up-customer-notifications-for-fanvista/02-notifications-complete.png)

## What happens next
To confirm it worked, place a test order. You receive one email when you pay and another, with a QR code, when the order is marked **Ready**. Next, see *Design the FanVista email receipt*.

## Rules to know
- One set of notifications covers every event at your venue.
- With no triggers turned on, fans receive no messages.

## If something goes wrong
| What you see | Why | What to do |
| --- | --- | --- |
| Fans receive no messages | The triggers are turned off | Follow the steps above, then place a test order |
| Email arrives but no text message | SMS is not turned on for your venue | Contact retailcloud Support |
| A fan has no QR code at the counter | **Add QR Code in Email** is turned off | Turn it on. Until then, scan the QR code in the fan's order history |

## Related articles
- *Design the FanVista email receipt*
- *Run a test order before your event*
- *Fulfill FanVista orders with OrderUp*
```
