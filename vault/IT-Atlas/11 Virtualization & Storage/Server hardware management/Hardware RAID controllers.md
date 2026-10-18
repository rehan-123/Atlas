---
type: "tool"
level: "Mid"
category: "[[Virtualization & Storage]]"
subcategory: "[[Server hardware management]]"
vendor:
deployment: "In-server"
status: "current"
aliases:
  - "PERC"
  - "Smart Array"
  - "MegaRAID"
  - "storcli"
tags:
  - "tool"
  - "virtualization"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Hardware RAID controllers

> [!abstract] In plain words
> The card inside a server that combines several disks so one failed disk doesn't lose data.
>
> **What kind of tool is this?** Out-of-band controllers are tiny computers inside a server that let you see its health and console even when Windows is down.

**Runs:** In-server · **Category:** [[Virtualization & Storage]] › [[Server hardware management]]

> [!info]+ Words on this page
> **RAID**: Combining several disks so one failed disk doesn't lose data. Not a backup.
> **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
> *More in the [[Glossary]].*

## In more detail

Dell PERC, HPE Smart Array and Broadcom MegaRAID controllers. Watch virtual disk state, physical disk state and cache battery health.

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
storcli /c0 show
storcli /c0/vall show
storcli /c0/eall/sall show
```

## See also

[[RAID levels]] · [[RAID degraded]] · [[Dell iDRAC]] · [[HPE iLO]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
