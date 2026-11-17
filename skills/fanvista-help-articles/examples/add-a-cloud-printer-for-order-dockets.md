---
title: Add a cloud printer for order dockets
slug: add-a-cloud-printer-for-order-dockets
category: FanVista > One-time setup
description: Add a cloud printer in the Retail Console so a docket prints at your counter each time a fan orders merchandise.
tags: fanvista, cloud printer, docket, printing, setup
---

A cloud printer prints a docket at your counter as soon as a fan places an order with merchandise items. The docket tells your staff that an order has arrived and what to pick.

## When you would do this

You do this once for your venue. It applies to every event. Repeat the steps when you add another printer, or when a suite has its own store.

## Before you start

- Your **Fulfillment Location** is saved in your branding. [VERIFY: the label may be Fulfillment Store] If you have not done this yet, see *Set up FanVista branding*.
- The printer is turned on and connected for cloud printing. retailcloud sets this up for you. Contact retailcloud Support to request it.
- You have the printer's model name and its MAC address. [VERIFY: say where the reader finds the MAC address, and list the supported printer models]

## Steps

1. Open the Retail Console and go to **Settings** > **Printer Settings**. [VERIFY: confirm the path; the screen may be named Printer Configuration]
2. Select the option to add a printer. [VERIFY: the button label, and whether the Cloud Printer step of the setup wizard opens this same form]
3. Select your printer's model from **Printer Model**.
4. Select your **Fulfillment Location** from **Printer Location**.

:::(Warning) (Warning)
The **Printer Location** must match the **Fulfillment Location** in your branding. If the 2 are different, no docket prints.
:::

5. Enter the printer's MAC address in **MAC Address**, for example 00:11:62:1A:2B:3C.
6. Select **FanVista** from **Source**. This sends FanVista orders to this printer. [VERIFY: the field may be labeled Auto Print by Order Type]
7. Select **Save**.

   [SCREENSHOT: the printer form with Printer Model, Printer Location, MAC Address and Source filled in, and Source set to FanVista highlighted]

## What happens next

A docket prints on this printer each time a fan places an order with merchandise items. [VERIFY: whether the printer list shows an online status, and where]

To confirm it worked, place a test order that includes a merchandise item. A docket prints at your **Fulfillment Location**. For the full test, see *Run a test order before your event*.

Next, set up the printer for bag receipts: see *Pair a receipt printer in OrderUp*.

## Rules to know

- Dockets print for merchandise items only. Food and beverage items go to the Kitchen Display System (KDS). In an order with both, the merchandise items still print.
- You can add several printers for 1 location. Each docket prints on 1 of them, not on all of them.
- Fan orders always print at your **Fulfillment Location**.
- A suite order prints at the suite's own store when the suite has one. Add a printer for each suite store. See *Where FanVista sales and dockets go*.
- **Printer Category** can stay blank for dockets. It is used for kitchen printing. See *Print kitchen tickets*.

## If something goes wrong

| What you see | Why | What to do |
| --- | --- | --- |
| No docket prints | No **Fulfillment Location** is set in your branding | Select one. See *Set up FanVista branding* |
| No docket prints | The printer is assigned to a different location | Select your **Fulfillment Location** from **Printer Location** |
| No docket prints | The printer is offline | Check that the printer is turned on and connected |
| No docket prints | The order source is not set to FanVista | Select **FanVista** from **Source** |
| A suite order does not print | The suite's store has no printer | Add a printer for that store |

For other causes, see *Order dockets or receipts are not printing*. If the problem continues, contact retailcloud Support.

## Related articles

- *Set up FanVista branding*
- *Pair a receipt printer in OrderUp*
- *Run a test order before your event*
- *Where FanVista sales and dockets go*
- *Order dockets or receipts are not printing*
