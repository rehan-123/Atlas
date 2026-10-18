---
type: "guide"
level: "Junior"
area: "[[Printer & scanner problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Add a network printer

> [!abstract] What's going on
> A user needs a printer added to their PC.

> [!tip] Think of it like
> Adding a contact to your phone: you need the right name or number.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Printer & scanner problems]]

> [!info]+ Words on this page
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **TCP**: A connection-based network protocol that confirms delivery.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Settings > Bluetooth & devices > Printers & scanners > Add device.
2. Pick the printer by name; if it's not listed, ask IT for its name or address.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Shared printers: \\PRINTSERVER\PRINTERNAME.
- Direct IP: add a TCP/IP port and the model's driver.
- Prefer deployment by Group Policy, Intune or Universal Print so users get printers automatically.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Printer not listed | Add by server path or IP. |
| Driver install blocked | Point and Print restrictions require admin approval or pre-installed drivers. |

## Escalate when

- Driver installs blocked by policy for many users

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

> [!question]- Why might Windows ask for admin rights when adding a shared printer?
> Point and Print security restrictions require admin approval to install new printer drivers.

## See also

[[Printer offline]] · [[Print Server]] · [[Group Policy]]

## Field notes

Add your own tips and client quirks here.
