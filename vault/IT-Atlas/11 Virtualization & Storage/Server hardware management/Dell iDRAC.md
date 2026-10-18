---
type: "tool"
level: "Mid"
category: "[[Virtualization & Storage]]"
subcategory: "[[Server hardware management]]"
vendor: "[[Dell Technologies]]"
deployment: "Out-of-band controller"
status: "current"
aliases:
  - "iDRAC"
  - "OpenManage"
tags:
  - "tool"
  - "virtualization"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Dell iDRAC

> [!abstract] In plain words
> The management chip in Dell servers: shows hardware health and gives remote console even if Windows is down.
>
> **What kind of tool is this?** Out-of-band controllers are tiny computers inside a server that let you see its health and console even when Windows is down.

**Made by:** [[Dell Technologies]] · **Runs:** Out-of-band controller · **Category:** [[Virtualization & Storage]] › [[Server hardware management]]

> [!info]+ Words on this page
> **PSU**: Power supply unit.
> **RAID**: Combining several disks so one failed disk doesn't lose data. Not a backup.
> *More in the [[Glossary]].*

## In more detail

Dell's integrated Remote Access Controller: remote console, hardware health, System Event Log and Lifecycle Controller logs. OpenManage Enterprise manages many at once.

## Alerts you'll see

- Drive, PSU, fan or memory faults
- RAID controller (PERC) battery or virtual disk degraded
- Temperature warnings

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
racadm getsysinfo
racadm getsel
racadm lclog view
racadm storage get pdisks -o
```

## See also

[[Hardware RAID controllers]] · [[RAID degraded]] · [[SMART]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
