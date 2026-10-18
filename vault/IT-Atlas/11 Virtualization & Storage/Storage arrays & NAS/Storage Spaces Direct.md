---
type: "tool"
level: "Mid"
category: "[[Virtualization & Storage]]"
subcategory: "[[Storage arrays & NAS]]"
vendor: "[[Microsoft]]"
deployment: "Windows Server feature"
status: "current"
aliases:
  - "S2D"
  - "Storage Spaces"
tags:
  - "tool"
  - "virtualization"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Storage Spaces Direct

> [!abstract] In plain words
> Windows' way to pool the disks of several clustered servers into shared storage.
>
> **What kind of tool is this?** Storage arrays and NAS boxes are dedicated machines full of disks that store data for servers and users.

**Made by:** [[Microsoft]] · **Runs:** Windows Server feature · **Category:** [[Virtualization & Storage]] › [[Storage arrays & NAS]]

> [!info]+ Words on this page
> **NAS**: Network-attached storage: a box full of disks that shares files over the network.
> **cluster**: Several servers working together so one can take over if another fails.
> *More in the [[Glossary]].*

## In more detail

Software-defined storage pooling local disks across Windows Server cluster nodes; the storage layer of Azure Local.

## Alerts you'll see

- Virtual disk degraded
- Physical disk lost communication
- Storage jobs running (repair)

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-StoragePool
Get-VirtualDisk
Get-PhysicalDisk | Sort-Object HealthStatus
Get-StorageJob
Get-HealthFault
```

## See also

[[Failover Clustering]] · [[Azure Local]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
