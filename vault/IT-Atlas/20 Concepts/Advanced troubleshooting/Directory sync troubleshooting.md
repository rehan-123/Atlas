---
type: "concept"
level: "Senior"
category: "[[Advanced troubleshooting]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Directory sync troubleshooting

> [!abstract] In one line
> Fixing objects that won't sync between Active Directory and Entra ID.

> [!tip] Think of it like
> Two address books that must stay in step; two contacts with the same phone number and the sync gives up.

> [!info]+ Words on this page
> **UPN**: User principal name: the sign-in name that looks like an email address.
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **immutable**: Can't be changed or deleted until a set date, even by an admin.
> *More in the [[Glossary]].*

## How it works

- Check the sync health and the export/import errors in Entra Connect (Synchronization Service Manager) or the Entra admin center.
- Common errors: duplicate attribute (two objects with the same UPN or proxyAddress), invalid characters, object outside the synced OUs.
- `Start-ADSyncSyncCycle -PolicyType Delta` runs a sync; `Get-ADSyncScheduler` shows the schedule.
- Soft match (by UPN/SMTP) and hard match (by immutable ID) decide which cloud object an AD object links to.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Which cmdlet triggers an immediate delta sync?
> Start-ADSyncSyncCycle -PolicyType Delta

## See also

[[Microsoft Entra Connect]] · [[Entra Connect sync errors]] · [[Hybrid identity models]]
