---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Windows Server roles]]"
vendor: "[[Microsoft]]"
deployment:
status: "current"
aliases: []
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Storage Replica

> [!abstract] In plain words
> A Windows Server feature that copies a volume block by block to another server for disaster recovery.
>
> **What kind of tool is this?** Roles are the jobs a Windows server can do: hand out IP addresses, host files, run remote desktops and so on.

**Made by:** [[Microsoft]] · **Category:** [[Servers & Operating Systems]] › [[Windows Server roles]]

> [!info]+ Words on this page
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **replication**: Copying data or changes to another place, continuously or on a schedule.
> **cluster**: Several servers working together so one can take over if another fails.
> *More in the [[Glossary]].*

## In more detail

Block-level synchronous or asynchronous volume replication between servers or clusters (stretch clusters).

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-SRGroup
Get-SRPartnership
(Get-SRGroup).Replicas | Select DataVolume, ReplicationStatus
```

## See also

[[Failover Clustering]] · [[Replication vs backup]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
