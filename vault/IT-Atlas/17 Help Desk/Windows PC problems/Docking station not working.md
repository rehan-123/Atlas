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

# Docking station not working

> [!abstract] What's going on
> Monitors, keyboard or network through the dock stop working.

> [!tip] Think of it like
> A power strip with a loose plug: everything plugged into it goes dark together.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Windows PC problems]]

> [!info]+ Words on this page
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **firmware**: The software built into hardware such as firewalls, disks and servers.
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Unplug the dock's power for 30 seconds, then reconnect it and the laptop.
2. Check the laptop is connected to the right port (Thunderbolt or USB-C with the lightning or display icon).
3. Restart the laptop with the dock connected.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Update the dock firmware and the laptop's Thunderbolt/USB-C and graphics drivers.
- Check the dock is supported for that laptop model.
- Test with another dock to isolate the problem.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Dock needs a power cycle | Unplug it and reconnect. |
| Old firmware | Update the dock firmware. |
| Wrong port | Use the Thunderbolt/USB-C port that supports docks. |

## Escalate when

- Several docks of one model fail after an update

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

> [!question]- Why update the dock firmware as well as Windows drivers?
> Docks run their own firmware; many display and network bugs are fixed there.

## See also

[[Screen or second monitor not working]] · [[Dell Command Update]]

## Field notes

Add your own tips and client quirks here.
