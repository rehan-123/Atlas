---
type: "tool"
level: "Mid"
category: "[[Backup & DR]]"
subcategory: "[[BCDR appliances]]"
vendor: "[[Axcient]]"
deployment: "Appliance, virtual appliance or direct-to-cloud"
status: "current"
aliases: []
tags:
  - "tool"
  - "backup"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Axcient x360Recover

> [!abstract] In plain words
> Axcient's backup appliance or cloud service. Its backups don't depend on a chain of earlier backups, so one bad file can't break them.
>
> **What kind of tool is this?** A BCDR appliance is a box at the client's office that backs up their servers, sends copies to the cloud, and can even run a failed server as a virtual machine until it's fixed.

**Made by:** [[Axcient]] · **Runs:** Appliance, virtual appliance or direct-to-cloud · **Category:** [[Backup & DR]] › [[BCDR appliances]]

> [!info]+ Words on this page
> **BCDR**: Business continuity and disaster recovery: keeping a business running, and getting it back after a disaster.
> **DR**: Disaster recovery: getting systems back after a major failure.
> **BDR**: Backup and disaster recovery appliance.
> **appliance**: A dedicated box (or virtual machine) built to do one job, such as backup or firewall.
> **incremental**: A backup of only what changed since the last backup.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **failover**: Automatically switching to a backup system when the main one fails.
> *More in the [[Glossary]].*

## In more detail

Axcient's BDR with Chain-Free backup (no incremental chains to break), AirGap protection of cloud copies and Virtual Office for cloud DR.

## Main parts

- Physical or virtual appliance, or direct-to-cloud agent
- Chain-Free backup
- AirGap (protects cloud copies from deletion)
- AutoVerify
- Virtual Office cloud failover

## See also

[[Datto BCDR]] · [[Immutability & air gap]] · [[Backup job failed]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
