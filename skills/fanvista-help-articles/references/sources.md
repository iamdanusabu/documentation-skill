# Where FanVista knowledge comes from

Use this to refresh `fanvista-knowledge.md` or to check a single fact. Ranked by how much to trust each source for *customer-facing* statements.

## 1. Google Drive (primary)

Search with the Drive connector: `fullText contains 'FanVista'`, ordered by modified time. Document IDs at the snapshot date:

| Document | ID | Use it for |
| --- | --- | --- |
| Fanvista Playbook v2 (three tabs: playbook, FanGuest quick start, SuiteUsers) | `1LiXEBJVt3HSG0kHdFGhwmu2xnvbySUo-R-qBs2HvSGk` | The main reference for setup and operations. Check its modified date first; if it changed since the snapshot, reread it. |
| FanGuest (quick start, 7-step Part A) | `1eqZOJ5IgQSU92Pcmpldcvt169QFAHUQXHpcvC8Zydqs` | Shortest correct setup path for fan events |
| FanVista_Setup_Wizard_PRD | `1fohnXDSeGfYjN2m0g7m3a_BxJ6g5UjyK3CaAWt7DVTY` | Step dependencies, field-level detail, test checklists. It is a spec - the released wizard may differ. |
| Fanvista (feature documentation, 2025) | `1x4yRPohPEs_ab5lP97YtUFvngjUaNEhWeYzGTS7Lm30` | Fan-side behaviour: variants, order history, QR and barcode |
| Print Job Setup for Fanvista | `1RcVhtURcSjmsNLCDv5TwPY1ktrZTEwI79DU0i1Kw2cA` | Internal printer connection procedure. Contains credentials and server addresses - never publish. |
| Open Items for FanVista - August 2026 | `1iRwpA8I0Ay--WBChcbXuIz4NRfHYjvjFbd7GfMtWYqE` | What is *not* built. Use only to keep unreleased features out of articles. |

A newer playbook version, or a document titled like a quick start or release guide, outranks everything below.

## 2. Jira (what has shipped)

Atlassian connector, site `retailcloud.atlassian.net`.

- Planning items: `project = CP AND summary ~ "fanvista" ORDER BY updated DESC`
- Recent work across projects: `text ~ "fanvista" AND updated >= -60d ORDER BY updated DESC`

Only **RELEASED** items describe the product. Treat Open, Discovery, Dev, Awaiting QA/UAT, On Hold, Partially Released and Discarded as not available. A ticket describes intent; where a ticket and the playbook disagree and the ticket is newer and released, the ticket is probably right but mark the detail `[VERIFY]`.

Tickets are internal. Take the behaviour, never the key, the customer name, or the investigation notes.

## 3. Brain (code and internal docs)

- `custom_docs_search` / `custom_docs_article` (the `fanvista` doc) - older internal setup notes. Useful for history and troubleshooting; mostly internal procedure.
- `ask_brain`, `files_for`, `resolve_symbol` - confirm a field name, an enum's values (notification triggers, accessibility levels, event types) or a rule in the backend. Ask one narrow question per call. Good for "does this option exist and what are its values"; it cannot tell you what a console screen looks like.
- `support_search` - past support tickets on a topic. Good for finding what customers actually get stuck on, which is what the "If something goes wrong" section should cover. History, not current behaviour.

## 4. Confluence

`Fanvista Payment Flow` (Engg: Architecture space) - payment internals. Background only.

## 5. The live console and the user

The only authority for exact screen paths and labels. When the user confirms a label or path, or supplies a screenshot, record it in `fanvista-knowledge.md` and remove the matching `[VERIFY]` tag and the entry in its section 17.

## Updating the knowledge file

1. Change the fact in the relevant section; keep it short and customer-oriented.
2. Tag it correctly (none / `[VERIFY]` / `[INTERNAL]`).
3. If a feature moved from unreleased to released, remove it from section 18.
4. Update the snapshot date at the top.
