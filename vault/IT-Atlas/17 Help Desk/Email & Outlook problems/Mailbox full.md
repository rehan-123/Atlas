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

# Mailbox full

> [!abstract] What's going on
> Warnings that the mailbox is almost full, or email bouncing because it's full.

> [!tip] Think of it like
> A full filing cabinet: archive old folders to the basement (online archive) so the drawers open again.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Email & Outlook problems]]

> [!info]+ Words on this page
> **retention**: How long backups or logs are kept.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Empty Deleted Items and Junk Email.
2. Sort by size and delete or save large old attachments.
3. Ask IT about turning on an online archive.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Check size and quota: `Get-EXOMailboxStatistics USER | Select TotalItemSize` and `Get-Mailbox USER | Select ProhibitSendQuota`.
- Enable the online archive: `Enable-Mailbox USER -Archive`, then apply a retention or archive policy.
- Check the Recoverable Items folder size if Deleted Items is already empty.
- Check the license includes enough mailbox space.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Years of attachments | Delete or save to OneDrive. |
| No archive | Enable the online archive and an archive policy. |
| Recoverable Items full due to a hold | Review holds with the compliance admin. |
| Wrong license | Upgrade the license. |

## Escalate when

- The mailbox is on a legal hold
- Quota changes need a license purchase

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

> [!question]- Which PowerShell command turns on a user's online archive?
> `Enable-Mailbox USER -Archive` (Exchange Online PowerShell).

## See also

[[Exchange Online]] · [[Microsoft 365 PowerShell cheat sheet]]

## Field notes

Add your own tips and client quirks here.
