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

# Time or date is wrong

> [!abstract] What's going on
> The PC's clock is wrong, which can break sign-ins and secure websites.

> [!tip] Think of it like
> A watch that's slow: you miss trains, and the guard doesn't believe your ticket.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Windows PC problems]]

> [!info]+ Words on this page
> **DC**: Domain controller: a server running Active Directory.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Settings > Time & language > Date & time: turn on Set time automatically and Set time zone automatically, then click Sync now.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Domain PCs: check w32tm /query /status and the source (should be a DC).
- Resync: w32tm /resync.
- If the clock resets after every restart on an old desktop, the motherboard battery may be flat.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Wrong time zone | Set the right zone. |
| Not syncing | w32tm /resync. |
| Flat CMOS battery | Replace it. |

## Escalate when

- Several PCs or servers have the wrong time (domain time problem)

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

> [!question]- Why can a wrong clock stop a user signing in?
> Kerberos sign-ins fail when the clock is more than 5 minutes off the domain.

## See also

[[NTP]] · [[Time drift]] · [[Kerberos]]

## Field notes

Add your own tips and client quirks here.
