# FanVista product knowledge

**Snapshot date: 17 November 2026.** Setup page labels confirmed from a workflow PDF the same day. Built from the FanVista Playbook v2 (Drive, last edited 29 Oct 2026), the Generic Fan Events quick-start guides, the Setup Wizard spec, and Jira items in RELEASED status as of the snapshot date. See `sources.md` to refresh.

Tags: no tag = confirmed, write as fact. `[VERIFY]` = sources disagree or the exact UI path/label is unconfirmed; flag it in the article. `[INTERNAL]` = true but never published.

## Contents

1. What FanVista is
2. Who uses it and how they sign in
3. Activation
4. One-time venue setup (FanVista Setup)
5. Per-event setup
6. Quickpick menus
7. Items and how they display
8. Food and beverage: KDS and kitchen printing
9. Payments, deposits, tips and discounts
10. URLs and QR codes
11. Order dockets and where sales are recorded
12. Event day: fulfilling orders in OrderUp
13. The fan ordering experience
14. Dashboard, sponsorship and reports
15. Go-live checklist and test orders
16. Common problems and fixes
17. Conflicts between sources - check before stating
18. Not released or not for publication

---

## 1. What FanVista is

FanVista is a web-based ordering app for live events. Fans (and suite holders) browse a venue's menu on their phone, order merchandise or food and drink, pay, and either collect at a pickup point or have the order brought to their seat. There is nothing to download; fans open a link or scan a QR code. Each venue gets its own branded address on the `fanvista.app` domain (for example `yourvenue.fanvista.app`).

It supports **pre-orders** (before the event) and **event-day orders**.

The pieces a venue works with:

| Component | What it is | Who uses it |
| --- | --- | --- |
| FanVista | The fan-facing ordering web app | Fans, suite owners |
| Retail Console | Back office where everything is configured: events, menus, branding, payments, notifications, printers | Venue admins, operations managers |
| OrderUp | Fulfillment app for picking, packing and handing over retail orders | Fulfillment staff |
| KDS (Kitchen Display System) | Screens that show food and beverage orders to the kitchen | Kitchen staff |
| Cloud printer | Prints an order docket at the fulfillment location the moment a retail order is placed | Fulfillment staff |
| Local receipt printer | Paired to the OrderUp device; prints the customer and delivery receipts at packing | Fulfillment staff |

All FanVista configuration lives in the **Retail Console**. KDS register configuration and category-to-screen mapping may still be reached from the Restaurant Console `[VERIFY]` (the playbook's two versions disagree on how much remains there).

## 2. Who uses it and how they sign in

Three ordering experiences, decided by the link or QR code the person opens:

- **Suite Owner** - a customer with a suite booking for the event. Signs in and sees only their own suite and its menu.
- **Fan Guest, event view** - anyone without a booking. Signs in, sees the events open for ordering, picks one, orders from its menu.
- **Fan Guest, suite view** - an unbooked guest sent to a suite-selection view, where each suite can show a different menu.

Sign-in methods: the venue chooses which are offered - **Mobile Number**, **Email**, or both (both on by default; at least one must stay on). The choice applies everywhere a FanVista sign-in appears, including Suite Owner sign-in. Older material also describes email-and-password registration and Google Sign-In `[VERIFY]` whether Google Sign-In is still offered.

**Suite Management** is a single on/off setting. When it is off, everything suite-related disappears: Suite Owner sign-in, suite bookings, suite QR codes, suite assignment on orders, and the Suite Assignment Report. Venues that only serve general fans can leave it off.

## 3. Activation

FanVista is switched on for a venue by retailcloud (or the venue's reseller). One activation turns on the whole feature set - the venue does not enable features one by one. `[INTERNAL]` The switch is the "Click & Collect" permission in the Partner Portal; older notes also mention "FanVista" and "Config Branding Fanvista" permissions. Customer-facing wording: "FanVista is activated on your account by retailcloud. If you do not see the FanVista module in the Retail Console, contact your retailcloud representative or Support."

`[INTERNAL]` New FanVista addresses need a one-time domain authorization (Firebase) by retailcloud before fans can sign in. Symptom if missing: fans see "Authentication Failed. Please Try Again" on a brand-new venue address. Customer-facing fix: contact Support.

## 4. One-time venue setup (FanVista Setup)

Done once per venue; applies to every event afterwards. The Retail Console has a **FanVista module** with a **Setup** area that gathers the one-time settings: **Branding, Login, QR Code Generator, Email Receipt, Suite Management, Notifications, Payments**. A guided **FanVista Setup Wizard** walks through them in order: **Branding -> Payment -> Notification -> Email Receipt -> Cloud Printer -> Complete Setup**. (The local receipt printer is paired later, from OrderUp.) After setup the console confirms "Setup Complete - You're all set! You can now start creating your events." Exact menu labels and wizard entry point `[VERIFY]` against the live console.

Do the steps in this order - several depend on the one before.

### 4.0 The Setup page as it appears in the console (confirmed)

Confirmed from a workflow PDF of the live console, 17 November 2026. These labels are settled; use them without `[VERIFY]`.

- Menu: **FanVista** expands to **Onboarding**, **Dashboard**, **Event**, **Bookings**, **Reports**, **Sponsorships**, **Setup**.
- **FanVista** > **Setup** is one scrolling page with these sections, in order:
  - **Title 1**, **Title 2**, **Title 3** (Title 3 seen on screen; Title 1 and Title 2 confirmed from the branding data model, where the stored fields are three titles, a background image, primary and secondary color, a favicon and the subdomain), **Primary Color**, **Secondary Color** (hex codes), **Login Screen Background Image** with an **Upload Image** button (1080 x 1080, max 5 MB). A phone preview on the right shows the sign-in screen.
  - **Login Options**: toggles **Enable Mobile Number Login** (sign in with a mobile number and an SMS code) and **Enable Email Login** (sign in with an email address and a code sent to the inbox). Sign-in is by one-time code, not password.
  - **Fulfillment Location**: a required **Store** dropdown.
  - **Delivery Method**: checkboxes **In-Seat** and **Pickup**. With **Pickup** selected, **Configure Pickup Time** shows **From** and **To** fields, a plus icon to add a window and a trash icon to remove one. Saving with Pickup selected and no window gives "Please configure the pickup time before saving."
  - **Customized URL**: a name field followed by `.fanvista.app`.
  - **Suite Management**: toggles **Enable Suite Management** (shows or hides Bookings in the menu, the suite tab in Setup, and suite options in the QR Code Generator) and **Enable Fan Guest Login** (lets users sign in as a Fan Guest without a Suite Owner account).
- Not captured: the top of the page, the save button, any tabs within Setup, and where seat sections are set when **In-Seat** is selected `[VERIFY]`.

### 4.1 Branding

- **Fulfillment Location** (section) with a **Store** dropdown: the store where orders are physically picked and packed. This one setting drives three things for fan orders: the stock level fans see, where the sale is recorded and inventory reduced, and where the order docket prints. If it is not set, stock is not tracked and no docket prints. It is also the fallback for any suite that has no store of its own.
- **Look and feel**: venue logo, colours, title and branding text, background image, social media links. A preview shows how the fan app will look. The splash screen shows the text and description entered here.
- **FanVista URL**: the venue's unique ordering address. It is fixed once created and cannot be changed later, so choose it carefully.
- **Delivery Method**: **Pickup**, **In-Seat Delivery**, or both. Fans are offered only what is enabled.
  - Pickup: set the default **pickup time windows** here (for example 12:00-12:15, 12:15-12:30). These apply to every event unless an event overrides them.
  - In-Seat Delivery: set up the **seat sections** fans can choose from.

### 4.2 Login and Suite Management

See section 2. Both live in FanVista Setup.

### 4.3 Payments

- **Payment Gateway**: select **Connect** and link the venue's gateway. No gateway means no checkout, so this comes first. If the gateway cannot be connected from the screen, Support completes it. `[INTERNAL]` Historically this was a manual database configuration.
- **Payment Tenders**: switch on what fans can pay with - **Credit Card**, and **House Accounts** if the venue uses stored credit (common for suite holders). At least one must be on.
- **Deposit Setup** (pre-order deposit percentage, up to 100%): see section 9. Set **100% for fan guests**; set **below 100% for suites**.
- **Tip Setup** (optional): turn on the tipping prompt, choose **Tip Percentage** or **Tip Amount**, set up to three preset options (Option 1 is the default), and optionally allow a custom amount. The tip is added to the payment total.

### 4.4 Customer notifications

Notification rules control every automatic email and SMS a customer receives - order confirmation, ready-for-pickup, delivered. **With no rule, customers receive nothing at all.** This is the most common go-live failure. One rule per venue covers all events.

Where: FanVista Setup -> Notifications (source fixed to FanVista). The playbook gives the older path Settings -> Customer Notifications with **Type: Order** and **Source: FanVista** `[VERIFY]` which path the live console uses; a released change moved FanVista notifications into FanVista Setup.

Fields:

- **Triggers**
  - **Order Checkout** - fires when an order is paid in full. The main order confirmation for fan guests. **Must be on before the email receipt template can be created or edited.**
  - **Cart Checkout** - fires when an order is saved without full payment (a suite owner keeping an order open). Needed for suites.
  - **Ready** - fires when staff mark the order Ready in OrderUp. This is the pickup alert.
  - **Delivered** - fires when staff mark the order Delivered. Optional, recommended.
  - Additional order-status triggers may be listed: Initiated, Sent for Processing, Processing, Cancelled, Returned `[VERIFY]`.
- **Customer type**: rules can be set per audience - Fan Guest and Suite Owner `[VERIFY]` that this is in the live UI.
- **Channel**: **Email** and/or **SMS**. SMS only works if SMS sending has been set up for the venue; that is arranged with retailcloud. `[INTERNAL]` Twilio.
- **Add QR Code in Email**: turn this on. The fan shows this QR code at the counter to collect.

Recommended: fan-guest venues enable Order Checkout + Ready (+ Delivered). Venues with suites also enable Cart Checkout. All triggers can sit on one rule.

### 4.5 Email receipt template

In Branding -> **Email Receipt Template Configurator** (also listed as **Email Receipt** in FanVista Setup). Sets the receipt email fans get at checkout - logo, layout, messaging. **Only works once the Order Checkout trigger is on** (4.4). Doing this first is a known cause of receipts silently not sending.

The **receipt designer** offers logo placement, colour, fields that can be switched on or off, configurable totals, a footer QR code or promotional image, and a live preview.

### 4.6 Cloud printer (order dockets)

Prints a docket the instant a retail order is placed - the counter's order alert. Set up in the Retail Console printer settings (Settings -> Printer Settings `[VERIFY]`; the playbook calls it "Printer Configuration"):

0. Add a new printer `[VERIFY]` the button label, and whether the setup wizard's Cloud Printer step is this same form.
1. Select the **Printer Model** matching the device.
2. Set the **Printer Location** to the Fulfillment Location from 4.1.
3. Enter the printer's **MAC Address**.
4. Set the order source to **FanVista** (label is "Source" in one playbook version and "Auto Print by Order Type" in another `[VERIFY]`). **Printer Category** can be left blank for retail dockets.
5. Save and confirm the printer is online `[VERIFY]` where the status shows. The dependable confirmation is a test order: a docket should print.

Not known from the sources, so do not state: which printer models are supported, where the customer finds the MAC address, and how the printer is chosen when a location has several. Field labels above come from the playbook; the screen they sit on is unconfirmed, so one `[VERIFY]` on the navigation step covers them.

Rules: cloud docket printing is for **retail items only** (in a mixed order the retail part still prints). Several printers can be assigned to one location; each docket prints on one of them, not all. For suites, a printer is needed at each suite's store (section 11). `[INTERNAL]` The printer itself must be pointed at retailcloud's CloudPRNT service; server URLs and printer admin credentials are never published - say retailcloud connects the printer during onboarding or Support supplies the details.

### 4.7 Local receipt printer (OrderUp)

Paired inside the OrderUp app on the fulfillment device, not in the console: OrderUp -> Settings -> Printer -> Scan, then pair `[VERIFY]` exact labels. The OrderUp device and printer must be on the same Wi-Fi network, or connected by Bluetooth. This printer produces two receipts when an order is packed: a **customer receipt** (goes inside the bag) and a **delivery receipt** with a QR code (goes on the outside).

## 5. Per-event setup

Repeated for each event; takes minutes once section 4 is done. An **Event Setup Wizard** guides it: **Event Type -> Delivery Method -> Event Form -> Quick Pick -> QR Code -> Test Order**.

### 5.1 Event types

- **Generic** (also shown as "Normal" in the wizard `[VERIFY]` label) - a standard event.
- **OnTour** - touring or travelling events. The Quickpick menu can be set up directly in the event form. Suite booking is also available on OnTour events from the booking tab. Older setup notes describe OnTour events as built around an **artist** with products entitled to that artist `[VERIFY]` whether this still applies.
- **Suitespot** - venue events with suite bookings; each customer is tied to a suite.

Switching event type part-way through the wizard resets the form.

### 5.2 Event fields that matter for FanVista

| Field | What it does |
| --- | --- |
| **Order Number Prefix** (required) | Short prefix on every order number from the event - "WWE" gives WWE#1, WWE#2. Pick something fans recognise. The same prefix can be reused across events; numbering continues in one sequence. Max length about 5 characters `[VERIFY]`. |
| **Event Location** (required) | The location grouping that holds pickup locations. After choosing it, tick the pickup locations to offer for this event; only ticked ones appear at checkout. Pickup locations are created under an Event Location in Retail Console Settings. Required for pickup to work. |
| **Pickup time windows** | Optional per-event override of the Branding defaults. Fans only see windows that have not passed. |
| **Pre-Order Starts On / Ends On** | The pre-order window. Optional. Available on all event types. |
| **Event Day Order Start Time / End Time** | Daily ordering window, for example 1:00 PM-4:00 PM. On multi-day events the same window applies every day. |

Events can be imported in bulk; the import includes the Order Prefix.

### 5.3 When fans can see an event

A fan sees an event only when they can act on it:

| Event state | In the fan's list? | Can order? |
| --- | --- | --- |
| Created, setup not finished | No | No |
| Set up, pre-order window not yet open | No | No |
| Pre-order window open | Yes | Yes, pre-order |
| On today, ordering open | Yes | Yes |
| On today, ordering closed | Yes, shown as "Ordering closed" | No |
| Finished, cancelled or postponed | No | No |

Staff still see every event in the console. This is the first thing to check when a venue says "fans can't see our event".

### 5.4 Suites

With Suite Management on: create suites (name, number, and an attached **store** - the store drives stock, sales and docket printing for that suite), then for each event **book** suites to customers. Unbooked suites are invisible to everyone. Suite owners sign in and see only their suite's menu.

## 6. Quickpick menus

A Quickpick is the menu fans see. It is a named menu made of one or more **pages** (tabs), each aimed at an audience and an ordering period. Spelling in the UI is "Quickpick" or "Quick Pick" `[VERIFY]`; be consistent with the screen.

Steps:

1. Create a **Menu** and name it. Assign it to an event, to selected events, or to all events; or define it at the **venue level** so every event at the venue inherits it.
2. Add **Menu Pages**.
3. On each page set **Tab Type**, **Accessibility Level** and **Order Period**.
4. Add items and prices.
5. Assign the Quickpick to the event (and to specific suites where relevant).

**Tab Type**

| Value | Effect |
| --- | --- |
| **Retail** | Items go to OrderUp. Negative selling can be enabled. |
| **Food & Beverage** | Items go to the KDS. Negative selling cannot be enabled. |

**Accessibility Level** (checkboxes; combine freely)

| Value | Who sees the page |
| --- | --- |
| **POS** | Point-of-sale terminals only. Not shown in FanVista. |
| **Suite** | Suite-booked customers only. |
| **Fan Guest** | Unbooked fans only. |

POS honours this setting, so a Fan Guest-only menu does not appear on the tills. Ticking Suite + Fan Guest shows the page to everyone in FanVista and still hides it from POS.

**Order Period**

| Value | When the page shows |
| --- | --- |
| **Pre-Order** | Only during the pre-order window |
| **Event Day** (also "Game Day") | Only during the event-day ordering window |
| **All** | Both. Items can carry a separate **Pre-Order Price** and **Event Day Price**. |

Common combinations:

| Goal | Accessibility | Order Period |
| --- | --- | --- |
| Pre-order menu for fans | Fan Guest | Pre-Order |
| VIP suite pre-order menu | Suite | Pre-Order |
| Event-day food and drink for everyone | Suite + Fan Guest | Event Day |
| Retail page for the tills only | POS | Event Day |
| All-day suite retail menu, two price points | Suite | All |

**Different menu per suite**: create one Quickpick per suite, assign each to the event, and select the matching suite(s) in the assignment.

**Inventory Floor Value**: a per-Quickpick-item minimum that reserves stock for the tills. When the store's stock on hand falls to the floor, FanVista shows the item as **Sold Out** while the remaining units stay sellable at POS. Example: stock 100, floor 80 - FanVista sells 20, then shows Sold Out; 80 remain for the counter.

## 7. Items and how they display

- **Merchandise Type** on every item decides routing: **Retail** -> OrderUp + cloud docket; **Food & Beverage** -> KDS, no docket. **Items default to Retail.** An F&B item left as Retail shows up in OrderUp with the merchandise. One order can mix both types; each part routes on its own.
- **Variants**: fans choose from Size and Colour only. Sizes show in the order set by each size's sequence number. To set it: Retail Console -> **Attributes** -> open **Size** -> three-dot menu next to a value -> **Sort by Size** -> give each size a number (S = 1, M = 2, L = 3, XL = 4). Unnumbered sizes appear after numbered ones in no fixed order.
- **Product name**: FanVista shows the item's **e-commerce name**; if that is blank it shows the POS name. POS, receipts and fulfillment screens always use the POS name.
- **Images**: items without an image show a neutral retail-style placeholder.
- **Promotions**: see section 9.

## 8. Food and beverage: KDS and kitchen printing

For F&B items to reach a kitchen screen:

1. Create a **Category** and put the F&B items in it.
2. Map the category to a **KDS register** (which screen shows it). This is how a grill station sees only grill items.
3. Make sure that KDS register belongs to the right store - the venue store, or the suite's store.
4. Orders containing those items then appear on that screen automatically, with modifiers and comments.

For suites, give each suite its own store; the KDS linked to that store shows only that suite's items. KDS also needs to be switched on at account level for the venue, store or register `[VERIFY]` exact setting name.

**Kitchen ticket printing**: instead of (or alongside) a screen, items can print to a kitchen cloud printer by **Printer Category** - give the printer a category in printer settings and give the item the same category. The ticket shows order number and time, suite/seat/location and event, guest name, each item with quantity, modifiers under each item (including removals such as "No onions"), notes, and an "ADDED ITEMS" label when items are added to an open order.

If no store is configured for an order's context, the system records the sale against an automatically created virtual store. That is a safety net only: nothing shows on a KDS and no docket prints from a virtual store.

## 9. Payments, deposits, tips and discounts

- **Ways to pay**: card (entered at checkout or a saved card), **Apple Pay** (iPhone, Safari on Mac) and **Google Pay** (Android, Chrome). Wallets appear automatically with no per-event setup. House Accounts if the venue enabled that tender. Fans can save multiple cards.
- **Pre-Order Deposit %** (set once in Payments):
  - **100%** - the order is paid and closed when placed; nothing can be added to it. Use for fan guests.
  - **Below 100%** - the card is charged the deposit and the order stays open; the customer can keep adding items and settles the balance at the end. Use for suites.
- **Event-day behaviour**: a **fan guest's** order always checks out immediately, whatever the deposit setting. A **suite owner's** order stays open until they pay and close it.
- **Tips**: section 4.3.
- **Card surcharge**: if a surcharge is configured for card payments, it is added to the order total at checkout `[VERIFY]` still current.
- **Promotions**: promotions set up for the retail store - buy-one-get-one, percentage off, fixed amount off - apply automatically in FanVista with the original and discounted price shown. There is nothing separate to configure in FanVista.

## 10. URLs and QR codes

Generated in the Retail Console: **FanVista** module -> **Branding** -> **QR Code Generator** (also listed directly under FanVista Setup `[VERIFY]`). Each can be downloaded as an image or copied as a link.

| QR / link type | What the customer gets | Typical use |
| --- | --- | --- |
| Suite-specific | Signs in and lands on one suite's menu | On the table inside each suite |
| Generic Fan Guest (suite view) | Signs in and sees all suites, each with its menu | General venue signage where suites are browsable |
| Fan Guest Event | Signs in and sees events open for ordering, picks one | Event-wide signage, concourse posters, big screen |
| Generic FanVista URL | The venue's base address; choose Fan Guest or Suite Owner sign-in | Marketing, website, anywhere the event is not yet known |

Suite QR options appear only when Suite Management is on.

## 11. Order dockets and where sales are recorded

**Fan guest orders** always use the Fulfillment Location from Branding: stock is checked there, the sale is recorded there, and the docket prints on a cloud printer assigned to it. No Fulfillment Location or no printer = no docket.

**Suite orders** follow this order of precedence:

| # | Situation | Result |
| --- | --- | --- |
| 1 | The suite has its own store | Sale and stock use the suite's store. Docket prints there if that store has a printer; otherwise no docket. |
| 2 | No store on the suite, Fulfillment Location set in Branding | Sale and stock use the Fulfillment Location; docket prints there if it has a printer. |
| 3 | Neither is set | Sale recorded against an automatically created virtual store for the venue. No docket. |

Practical advice: if a venue wants dockets for suite orders, the suite's store should be the place where those orders are actually prepared. Venues whose accounting needs all FanVista sales in one store should confirm suites are not attached to other stores.

## 12. Event day: fulfilling orders in OrderUp

1. Fan places and pays. They get the order confirmation (email and/or SMS) with their seat or pickup details.
2. A **docket** prints on the cloud printer at the fulfillment location: items, quantities, delivery details and a QR code. OrderUp also shows a notification for the new order.
3. Staff pick from the docket, or build a **Batch Picklist** in OrderUp to pick several orders at once.
4. Staff **scan the docket's QR code** in OrderUp to open the order.
5. Staff pack. OrderUp prints two receipts on the local printer: the **Customer Receipt** (inside the bag) and the **Delivery Receipt** with QR code (outside the bag).
6. The bag goes to the staging area with the delivery receipt visible.
7. Staff mark the order **Ready**. The fan gets the ready notification with their collection QR code (if the rule has Ready and Add QR Code in Email on).
8. At the counter the fan shows their QR code. Staff scan it to bring up the order, then scan the delivery receipt on the bag to confirm the match.
9. Staff mark the order **Delivered**.

For in-seat delivery, steps 1-7 are the same and staff take the bag to the seat section on the docket.

Things staff should know:

- **Changed orders**: if a customer adds to an order after placing it (suites), OrderUp shows an **Updated** badge and the new docket is headed **ORDER UPDATED**. When scanned, newly added items are flagged unpicked and labelled **NEW**.
- **Mark All Ready** is limited to admin roles. Other staff mark orders ready one at a time, which prevents clearing the whole queue by accident.
- OrderUp handles retail items. Food and beverage goes to the KDS or kitchen printer.

## 13. The fan ordering experience

1. Open the venue's link or scan a QR code. No app download.
2. Sign in or register with mobile number or email (whichever the venue offers).
3. Choose a language if offered: **English, German, Spanish or French**.
4. See the venue's branded splash screen, then the list of events open for ordering. The list can be sorted **Date - nearest first** (default), **Date - farthest first**, or **A-Z** by event name. Events not open for ordering are hidden (section 5.3).
5. Pick an event and browse the menu tabs. For items with options, choose size and colour. Promotions show the original and discounted price. Out-of-stock items show Sold Out.
6. Add to cart, open the cart, continue to confirmation.
7. Choose how to receive the order: **Pickup** (choose a pickup location and time window) or **In-Seat Delivery** (enter seat section), depending on what the venue offers.
8. Add a tip if the venue has tipping on. Pay by card, saved card, Apple Pay or Google Pay.
9. Get the confirmation by email and/or text.
10. Get a "ready" message with a QR code. Show it at the pickup point.
11. **Order history** lists past orders, each with its QR code and a transaction barcode that staff can scan.

Carts are not kept if the fan closes the page or loses connection before paying (section 18).

## 14. Dashboard, sponsorship and reports

**FanVista dashboard** (Retail Console): revenue split pre-order vs event day, average order value by customer type, conversion rate, abandoned carts, top sellers, pickup-window utilisation, stockouts. When no event is active it does not show stale event data.

**Sponsorship** (its own section in the console, separate from Branding): create a sponsorship with an internal name, sponsor name and sponsor logo, scope it to **one event or all events**, and switch on any of three **ad types**, each placed on one or more **surfaces** (Event Home, Product Listing, Cart, Checkout):

| Ad type | What fans see | Setup |
| --- | --- | --- |
| **Sponsored Banner** | A header line ("[Event] Ordering - presented by [Sponsor]", editable) and a banner message | Header text, banner text |
| **Featured Product** | A badge on an existing catalog item | Pick one item, set badge label (for example "ABC Credit Union's Pick"). No effect on price or stock. |
| **Featured Promotion** | A popup image, optionally tied to an item that is added to the cart | Upload image, choose surface(s), optional item action |

With no active sponsorship the app looks exactly as normal.

**Sponsorship Performance Report**: filter by date range, sponsor, event and ad type. Columns: Internal Name, Sponsor Name, Event, Surface, Ad Type, Impressions, Unique Fans Reached, Engagements, Engagement Rate % (engagements / impressions x 100), Sponsored Item Views, Add to Cart, Units Sold, Sponsored Item Sales. Exports to CSV. A sale counts toward a sponsorship when the sold item is the sponsored item. Banner engagement counting `[VERIFY]` (one spec says banners are display-only, another counts taps).

Suite venues also have a **Suite Assignment Report**.

## 15. Go-live checklist and test orders

Before an event:

- FanVista active for the venue
- Branding done; Fulfillment Location set
- Delivery method(s) chosen; seat sections and/or pickup windows set
- Payment gateway connected; tenders on; deposit % right for the audience
- Notification rule on: Order Checkout, Ready (and Cart Checkout for suites, Delivered recommended); Email/SMS; QR code in email
- Email receipt template configured (after Order Checkout is on)
- Cloud printer added for the fulfillment location (and each suite store); online
- Local printer paired in OrderUp
- Event created: type, prefix, Event Location and pickup locations, ordering windows
- Quickpick created and assigned; Tab Type, Accessibility Level and Order Period right on each page
- Merchandise Type correct on every item; size sequence set
- Inventory Floor Value set where stock is shared with the tills
- KDS category mapping done (if selling food and drink); store on each suite
- Promotions checked in FanVista
- QR codes generated, printed, placed
- Mark All Ready permission reviewed
- Test order run

**Fan test order (7 checks)**: scan the QR and order -> confirmation email arrives -> docket prints -> order appears in OrderUp -> packing prints both receipts -> marking Ready sends the pickup email with QR -> scanning the fan QR completes as Delivered.

**Suite test order (10 checks)**: scan a suite QR and sign in as the suite owner -> place a pre-order -> confirmation arrives -> add an item on event day and confirm the order stays open -> docket prints at the suite's store -> scan docket in OrderUp -> packing prints receipts -> Ready email arrives -> pay and close, Order Checkout email arrives -> mark Delivered.

## 16. Common problems and fixes

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Fans get no confirmation or ready messages | No notification rule for FanVista, or trigger off | Create the rule; turn on Order Checkout and Ready; turn on Email/SMS |
| Receipt email not sending / template cannot be saved | Template set up before Order Checkout trigger was on | Turn on Order Checkout, then open and save the template again |
| No SMS, email works | SMS not set up for the venue | Contact retailcloud to enable SMS sending |
| Fan has no QR code at pickup | Add QR Code in Email is off | Turn it on in the notification rule; meanwhile use the QR or barcode in the fan's Order History |
| No docket prints | No Fulfillment Location; printer assigned to a different location; printer offline; order source not set to FanVista; items are F&B | Check each in that order |
| Suite order did not print | Suite's store has no printer | Add a printer for that store, or attach the suite to the store where orders are prepared |
| Food item appears in OrderUp | Merchandise Type left as Retail | Set it to Food & Beverage |
| Food order never reaches the kitchen | Category not mapped to a KDS register, or register on the wrong store; for kitchen printers, item and printer categories do not match | Fix the mapping / categories |
| Fans cannot see the event | Outside pre-order and event-day windows; event setup incomplete | Check the windows on the event |
| Fans cannot see the menu | Page Accessibility Level does not include Fan Guest; Order Period does not match the current window; Quickpick not assigned to the event | Correct the page settings / assignment |
| Menu shows on the tills but should not (or the reverse) | Accessibility Level includes/excludes POS | Adjust the checkboxes |
| No pickup locations at checkout | No Event Location on the event, or no pickup locations ticked | Set the Event Location and tick locations |
| Pickup times missing | All windows have passed; none configured | Add windows in Branding or on the event |
| Item shows Sold Out while stock remains | Inventory Floor Value reached | Expected; lower the floor to release more |
| Fan order stays open / fan cannot check out fully | Deposit below 100% | Set deposit to 100% for fan-guest ordering |
| Suite owner cannot add to their order | Deposit at 100% | Set below 100% for suites |
| Sizes in odd order | No size sequence | Set Sort by Size numbers |
| Sales landing in an unexpected store | Suite attached to another store, or virtual-store fallback | Review suite stores and Fulfillment Location (section 11) |
| No Suite Owner option at sign-in, no suite QR codes | Suite Management is off | Turn it on in FanVista Setup |
| "Authentication Failed. Please Try Again" on a new venue address | Address not yet authorized | Contact Support |
| Apple Pay / Google Pay not offered | Unsupported device or browser; fan not on the venue's fanvista.app address | Use a supported device, or pay by card |
| Staff cannot use Mark All Ready | Admin-only permission | Ask an admin, or mark orders ready individually |

## 17. Conflicts between sources - check before stating

Each of these needs a `[VERIFY]` in an article that depends on it, until confirmed against the live console:

1. **Where notification rules live**: FanVista Setup -> Notifications (newer, released) vs Settings -> Customer Notifications with Type/Source selectors (playbook).
2. **Printer settings**: screen name (Printer Configuration vs Settings -> Printer Settings) and the field that ties a printer to FanVista (Source vs Auto Print by Order Type).
3. (Settled: the section is **Fulfillment Location**, the field is **Store**.)
4. **Event type label**: Generic vs Normal.
5. **Quickpick / Quick Pick / QuickPicks** spelling.
6. (Settled: mobile number and email toggles, each verified by a one-time code.) Whether sign-in codes by SMS need the venue's SMS setup is not confirmed.
7. **Delivery method label**: the console shows **In-Seat** and **Pickup**. The labels in the fan app are not confirmed.
8. **Wizard entry points and step names** - the released wizard may differ in detail from the specs.
9. **OnTour artist/product entitlement** - described only in older notes.
10. **How much KDS setup remains in the Restaurant Console.**
11. **Card surcharge** - described only in older notes.
12. **Spelling**: sources mix US and UK English. Default to US English ("fulfillment", "color") and match the UI labels exactly.

### Known gaps - the sources do not say

Do not fill these from general knowledge. Write around them, or add a `[VERIFY]` and list it in the reviewer notes so the user can supply the answer (then record it here).

- **OrderUp screens**: sign-in, the name of the scan control, whether an order can be opened from a list without the docket, whether receipts print automatically at packing. Describe OrderUp actions in plain words; only **Ready**, **Delivered**, **Updated**, **NEW**, **Mark All Ready** and **Batch Picklist** are confirmed labels.
- **Fan app labels**: button names (add to cart, checkout, order history) and whether sign-in uses a one-time code or a password. Only the delivery options, **Sold Out** and "Ordering closed" are confirmed.
- **In-seat delivery handover**: whether Ready is marked, what message the fan gets, and whether a QR scan happens at the seat.
- **Pre-orders on event day**: when dockets print for pre-orders and how staff work through them.
- **Mixed retail and food orders**: whether the fan gets one ready message or two, and one pickup or two.
- **Cancellations, refunds, wrong or missing items, uncollected orders**: no policy or procedure in any source. Do not write about them; tell the user it is a gap.

## 18. Not released or not for publication

Do not describe these as available. If a user asks for an article on one, say it is not released and leave it out.

- Carts that persist after closing the page or losing connection
- Discount banner in FanVista
- Duplicating / cloning an event
- Alcohol quantity limits, alcohol cut-offs, age verification
- Venue-wide pause / kill switch; pausing a location or zone; pickup-window capacity limits
- Choosing a venue before choosing an event (multi-venue accounts); more than one fulfillment location per FanVista address
- FanVista inside team apps / single sign-on with ticketing
- An Orders section inside the FanVista module
- Custom-to-order (personalised product) flows - a separate product area
- Fan analytics tooling
- Self-service SMS setup
- Language selection outside FanVista's own screens

Never publish: anything tagged `[INTERNAL]`, Jira keys, customer names, defects under investigation, adoption or commercial commentary.
