---
type: "tool"
level: "Mid"
category: "[[Backup & DR]]"
subcategory: "[[Image & server backup]]"
vendor: "[[Arcserve]]"
deployment: "Agent plus local or cloud storage"
status: "current"
aliases:
  - "ShadowProtect"
  - "SPX"
  - "StorageCraft"
  - "ImageManager"
tags:
  - "tool"
  - "backup"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# StorageCraft ShadowProtect SPX

> [!abstract] In plain words
> Takes image backups of servers. A companion tool, ImageManager, combines and checks the backup files and copies them offsite.
>
> **What kind of tool is this?** Image backup copies a whole machine (operating system, apps and data) so it can be rebuilt exactly as it was.

**Made by:** [[Arcserve]] · **Runs:** Agent plus local or cloud storage · **Category:** [[Backup & DR]] › [[Image & server backup]]

> [!info]+ Words on this page
> **DR**: Disaster recovery: getting systems back after a major failure.
> **VSS**: Volume Shadow Copy Service: takes consistent snapshots of in-use files for backups.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **replication**: Copying data or changes to another place, continuously or on a schedule.
> **incremental**: A backup of only what changed since the last backup.
> **bandwidth**: How much data a link can carry per second.
> *More in the [[Glossary]].*

## In more detail

Image-based backup for Windows and Linux servers, paired with ImageManager to consolidate, verify and replicate image chains. StorageCraft merged into Arcserve in 2021.

## Main parts

- ShadowProtect SPX agent
- ImageManager: consolidation, verification, replication and HeadStart Restore
- Image files: .spf (full) and .spi (incremental)
- StorageCraft or Arcserve cloud replication

## Alerts you'll see

- Backup job failed
- ImageManager consolidation or verification failed
- Replication behind
- Chain broken

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Backup fails | Check VSS writers and the SPX service; read the job log |
| Consolidation fails | Check free space at the destination and ImageManager logs; a damaged file may require a new base image |
| Replication behind | Check bandwidth and the replication queue in ImageManager |

## See also

[[Arcserve UDP]] · [[VSS]] · [[Full, incremental & differential]] · [[Backup job failed]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
