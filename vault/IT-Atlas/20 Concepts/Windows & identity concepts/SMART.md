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

# SMART

> [!abstract] In one line
> Self-Monitoring, Analysis and Reporting Technology: drive health data that predicts failure.

> [!tip] Think of it like
> A disk's own health report, warning that it's about to fail.

> [!info]+ Words on this page
> **SSD**: Solid-state drive: fast storage with no moving parts. Much quicker than an old hard disk.
> **RAID**: Combining several disks so one failed disk doesn't lose data. Not a backup.
> *More in the [[Glossary]].*

## How it works

- Watch reallocated sectors, pending sectors, uncorrectable errors and wear level (SSDs).
- Behind a hardware RAID controller, read health from the controller or iDRAC/iLO, not the OS.
- `Get-PhysicalDisk | Get-StorageReliabilityCounter` on Windows, `smartctl -a /dev/sda` on Linux.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Behind a hardware RAID card, where do you read disk health?
> From the RAID controller or the server's management chip (iDRAC or iLO), not from Windows.

## See also

[[SMART predictive failure]] · [[RAID levels]] · [[Dell iDRAC]]
