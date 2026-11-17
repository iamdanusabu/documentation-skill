# FanVista

**Search terms:** FanVista, Fanvista, fanvista.app, Click & Collect (internal), SuiteSpot (the suite flow's older name).
**What it is:** a web ordering page for live events. Fans and suite owners order merchandise, food and drinks on their phones, pay, and collect or have the order brought to their seat.
**Where it is set up:** the Retail Console, under **FanVista**. Orders are fulfilled in OrderUp (merchandise) and on the Kitchen Display System (food and beverage).

## Readers

| Reader | Who they are |
| --- | --- |
| Venue admin | Sets FanVista up once. Full Retail Console access. |
| Operations manager | Creates events and menus. |
| Fulfillment and kitchen staff | Pick, pack and hand over orders on event day. |
| Fan, suite owner | The end customers placing orders. Send them to venue staff when stuck. |

## Words we use for this product

| Write | Not |
| --- | --- |
| FanVista | Fanvista, Fan Vista, FV, the app (on first mention) |
| OrderUp | Orderup, Order Up |
| Kitchen Display System (KDS) on first use, then KDS | kitchen screen system |
| Quickpick menu | QP, quick pick, menu system |
| fan | customer, user, guest, patron (for someone ordering without a suite) |
| suite owner | suite holder, suite customer, VIP |
| you, your venue | merchant, operator, client |
| event | game, match, show, concert (unless quoting an example) |
| event day | game day, match day |
| docket | ticket, chit, slip, print job (the printout at the counter) |
| customer receipt, delivery receipt | bag slip, label |
| pickup | pick-up, collection, click and collect |
| in-seat delivery (bold, as on screen, when naming the option) | seat delivery, delivery (alone) |
| food and beverage (food and drinks in fan articles) | F&B, concessions |
| merchandise | merch, retail goods |
| sold out | out of stock, unavailable |
| mark the order **Ready** | set, flag, change to |

## Standard sentences for this product

| Situation | Sentence |
| --- | --- |
| One-time task | "You do this once for your venue. It applies to every event." |
| Activation | "FanVista is activated on your account by retailcloud. If you do not see **FanVista** in the Retail Console, contact retailcloud Support." |
| Escalation for fulfillment staff | "Tell your manager." |
| Escalation for fans | "Ask a member of venue staff." |
| Repeated for every order | "The steps are the same for every order." |

## Traps that deserve a Warning

- The FanVista web address cannot be changed once created.
- The email receipt needs the Order Checkout trigger turned on first.
- No notification rule means fans receive no messages at all.
- No fulfillment location means no stock tracking and no dockets.
- Items default to Retail; food left as Retail goes to OrderUp instead of the kitchen.
- The deposit percentage must match the audience: 100% for fans, below 100% for suites.

## Sources

**Jira:** search `fanvista`. Planning items: `project = CP AND summary ~ "fanvista"`. Delivery work also sits in CON, P20, SA and OC.

**Brain:** the console service holds setup and branding; the order service holds orders and customers; the catalog service holds menu pages. Internal doc id `fanvista`.

**Google Drive standing documents:**

| Document | ID | Use it for |
| --- | --- | --- |
| Fanvista Playbook v2 | `1LiXEBJVt3HSG0kHdFGhwmu2xnvbySUo-R-qBs2HvSGk` | Main reference for setup and operations |
| FanGuest quick start | `1eqZOJ5IgQSU92Pcmpldcvt169QFAHUQXHpcvC8Zydqs` | Shortest correct setup path for fan events |
| Suite retail quick start | `1Q-qG0qV0ZrLt57J4cV78Zxj7xIdSm-Xhdyy3ijdmGzY` | Suite setup, per-suite stores, suite order flow |
| FanVista_Setup_Wizard_PRD | `1fohnXDSeGfYjN2m0g7m3a_BxJ6g5UjyK3CaAWt7DVTY` | Step dependencies, field detail, test checklists. A spec; the released product may differ |
| Fanvista feature documentation (2025) | `1x4yRPohPEs_ab5lP97YtUFvngjUaNEhWeYzGTS7Lm30` | Fan-side behaviour |
| Open Items for FanVista | `1iRwpA8I0Ay--WBChcbXuIz4NRfHYjvjFbd7GfMtWYqE` | What is not built. Use only to keep unreleased features out |
| Print Job Setup for Fanvista | `1RcVhtURcSjmsNLCDv5TwPY1ktrZTEwI79DU0i1Kw2cA` | Internal printer procedure. Contains credentials. Never publish |

## Document360 sections

Getting started, One-time setup, Events and menus, Suites, Food and beverage, Event day, For fans, Insights and sponsorship, Troubleshooting.
