---
type: "concept"
level: "Mid"
category: "[[Backup concepts]]"
aliases:
  - "Volume Shadow Copy Service"
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# VSS

> [!abstract] In one line
> Volume Shadow Copy Service: Windows' framework for consistent point-in-time snapshots, used by nearly every Windows backup tool.

> [!tip] Think of it like
> VSS freezes the frame for a split second so the backup gets a consistent photo of files that are in use, even open databases.

> [!info]+ Words on this page
> **SQL**: Structured Query Language; also short for Microsoft SQL Server.
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **snapshot**: A saved point in time of a VM or disk. Not a backup, and it grows the longer you keep it.
> *More in the [[Glossary]].*

## How it works

- **Requestor**: the backup tool. **Writers**: apps such as SQL, Exchange, AD and Hyper-V that flush data. **Providers**: create the snapshot (Microsoft software provider or a hardware or third-party one).
- A failed writer means application-inconsistent backups or job failures.
- Left-over third-party providers from an old backup product cause failures in the new one.
- Shadow storage too small causes snapshots to be deleted mid-backup.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Which command shows the state of VSS writers?
> vssadmin list writers (run as administrator).

> [!question]- Name a common cause of VSS failures after changing backup products.
> The old product's VSS provider was left behind and conflicts with the new one.

## See also

[[VSS writer failure]] · [[Backup job failed]] · [[Windows Server Backup]]
