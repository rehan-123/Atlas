---
type: "guide"
level: "Junior"
area: "[[Windows PC problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Laptop battery drains fast

> [!abstract] What's going on
> The battery runs out much faster than it used to.

> [!tip] Think of it like
> A bucket with a small leak: check what's draining it before buying a bigger bucket.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Windows PC problems]]

> [!info]+ Words on this page
> **BIOS**: The low-level setup program that starts a PC before Windows loads (UEFI on modern PCs).
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Lower screen brightness and close apps you aren't using.
2. Turn on battery saver (Settings > System > Power & battery).
3. Unplug USB devices you don't need.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Run `powercfg /batteryreport` and compare Design capacity with Full charge capacity.
- Check Settings > Power & battery > Battery usage for apps draining power.
- Update BIOS and chipset drivers from the manufacturer.
- Check the battery's warranty if capacity is under about 60-70% of design.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Battery worn out | Replace the battery. |
| Busy background apps | Close or remove them. |
| Old BIOS or drivers | Update them. |

## Escalate when

- Battery is swollen (case bulging): stop using it immediately
- Battery replacement needs a warranty claim

## Write it up

Copy this into the ticket and fill it in:

```
User and contact: 
Device: 
Problem (in their words): 
Exact error message: 
Started when / what changed: 
What I checked: 
What fixed it: 
User confirmed it's fixed (yes/no): 
```

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Which command creates a battery health report on Windows?
> `powercfg /batteryreport`.

## See also

[[PC is slow]] · [[Dell Command Update]] · [[How a computer works]]

## Field notes

Add your own tips and client quirks here.
