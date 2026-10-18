---
type: "guide"
level: "Mid"
area: "[[Email & Outlook problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Recover a deleted email

> [!abstract] What's going on
> Someone deleted an email or folder and needs it back.

> [!tip] Think of it like
> The recycling bin outside the house: emptied bins still go to the depot for a while.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Email & Outlook problems]]

> [!info]+ Words on this page
> **retention**: How long backups or logs are kept.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Check Deleted Items.
2. In Deleted Items, use Recover items recently removed from this folder.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Recoverable Items keeps deleted mail for 14 days by default in Exchange Online (up to 30 if configured).
- Admins can search and restore with Purview content search or Restore-RecoverableItems.
- Older mail needs the backup product (Spanning, Veeam for Microsoft 365, etc.).

## Common causes and fixes

| Cause | Fix |
|---|---|
| Recently deleted | Deleted Items or Recover deleted items. |
| Older than retention | Restore from backup. |

## Escalate when

- Large amounts deleted (possible compromise)
- Legal hold or compliance request

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

> [!question]- How long does Exchange Online keep deleted items recoverable by default?
> 14 days (adjustable up to 30).

## See also

[[Exchange Online]] · [[Recover a deleted file]] · [[Spanning Backup]] · [[Veeam Backup for Microsoft 365]]

## Field notes

Add your own tips and client quirks here.
