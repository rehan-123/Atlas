---
type: "concept"
level: "Mid"
category: "[[Windows & identity concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# RAID levels

> [!abstract] In one line
> How disks are combined for redundancy and performance.

> [!tip] Think of it like
> RAID spreads data across disks so that losing one disk doesn't lose the data, but RAID is not a backup.

> [!info]+ Words on this page
> **RAID**: Combining several disks so one failed disk doesn't lose data. Not a backup.
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> *More in the [[Glossary]].*

## How it works

| Level | Survives | Notes |
|---|---|---|
| RAID 1 | 1 disk | Mirror |
| RAID 5 | 1 disk | Parity; long, risky rebuilds on large disks |
| RAID 6 | 2 disks | Double parity |
| RAID 10 | 1 per mirror pair | Fast; common for databases and VMs |

RAID is not backup. A degraded array is one more failure from data loss, so replace disks the same day.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- A RAID 5 array has one failed disk. Why is it urgent?
> One more failure means the data is lost, and a long rebuild puts extra strain on the remaining disks.

## See also

[[RAID degraded]] · [[Hardware RAID controllers]] · [[SMART]]
