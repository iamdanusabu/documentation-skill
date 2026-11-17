# Product packs

Everything specific to one product lives in its pack. The voice, the page structure, the research method and the publishing format are shared.

## Packs available

| Product | Folder | Covers |
| --- | --- | --- |
| FanVista | `fanvista/` | Event-day ordering for fans and suites: setup, events, Quickpick menus, payments, notifications, printers, OrderUp and KDS fulfillment, sponsorship |

When asking the writer which product they are documenting, offer these and let them name another. Other retailcloud products writers may name include the Retail Console (catalog, inventory, purchasing, CRM, financial, reports, settings), OrderUp, OnePOS and the other POS apps, i360, OnTour, and custom-to-order. None of these has a pack yet.

## What a pack contains

| File | Purpose |
| --- | --- |
| `product.md` | Names and search terms, readers, the product's own word list and standard sentences, Warning-worthy traps, sources (Drive documents, Jira queries, Brain hints), Document360 sections |
| `knowledge.md` | What the product does and how it is set up, with a snapshot date, a section of conflicts and known gaps, and a section of unreleased or unpublishable items |
| `catalog.md` | The planned articles with canonical titles, so cross-links stay consistent |
| `examples/` | One or more finished articles that show the level of detail |

## A product with no pack

The article is still written the same way; you just start with nothing bundled.

1. Tell the writer in one line: "There is no pack for <product> yet, so I am researching it from the connected sources and will save what I learn."
2. Copy `_template/` to `products/<product-slug>/`.
3. Do the research in `references/research.md` more widely than usual. Before the topic searches, find the product's standing material: Drive documents with the product name in the title (playbook, guide, PRD), the Jira projects and planning items that mention it, Brain internal docs, and the services or apps that implement it (`files_for`, `brain_status`).
4. Fill `product.md` as you go: the names people use for the product, who the readers are, the terms on its screens, the documents you found. Start `knowledge.md` with what you confirmed for this article's topic. Leave the rest for later articles; a pack grows one article at a time.
5. Write the article. With no pack to fall back on, be stricter about wording only what the PDF and the sources support.
6. Add the article as the pack's first example and its title to `catalog.md`. Add the product to the table above.
7. In your notes, tell the writer a new pack was created and should be shared with the team.

## Adding a pack on request

When a writer asks to add a product without writing an article yet, do steps 2 to 4 above for the whole product rather than one topic, and draft a catalog: the articles a new customer needs, in the order they need them.

## Rules for every pack

- Record what is **released** to customers.
- Tag statements in `knowledge.md`: no tag (confirmed), `[VERIFY]` (unconfirmed), `[INTERNAL]` (true, never published). These tags are for the pack only and never appear in an article.
- No credentials, no customer names, no Jira keys.
- Keep product-specific wording in `product.md`. If a rule should apply to every product, it belongs in `references/voice-and-tone.md`, which the documentation owner changes.
