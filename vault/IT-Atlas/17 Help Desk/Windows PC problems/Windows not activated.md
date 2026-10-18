---
type: "guide"
level: "Mid"
area: "[[Windows PC problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Windows not activated

> [!abstract] What's going on
> Windows shows 'Activate Windows' or a licensing warning.

> [!tip] Think of it like
> A shop that hasn't confirmed your receipt yet: everything works, but you get nagging until it's confirmed.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Windows PC problems]]

> [!info]+ Words on this page
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Connect to the internet and restart; activation usually completes on its own.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Settings > System > Activation shows the error.
- `slmgr /dlv` shows licence details.
- Business devices often activate by upgrading Windows Pro to Enterprise through a subscription licence assigned to the user; check the licence is assigned.
- KMS clients need to reach the KMS host (DNS _vlmcs record).

## Common causes and fixes

| Cause | Fix |
|---|---|
| Offline or blocked | Connect and retry. |
| Missing subscription licence | Assign the licence. |
| KMS unreachable | Fix DNS or network to the KMS host. |

## Escalate when

- Volume licensing problems across many devices

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

> [!question]- Which command shows detailed Windows licensing information?
> `slmgr /dlv`.

## See also

[[Windows client]] · [[Office activation error]]

## Field notes

Add your own tips and client quirks here.
