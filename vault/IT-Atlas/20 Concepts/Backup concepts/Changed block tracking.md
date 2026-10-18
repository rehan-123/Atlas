---
type: "concept"
level: "Mid"
category: "[[Backup concepts]]"
aliases:
  - "CBT"
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Changed block tracking

> [!abstract] In one line
> CBT: the hypervisor or agent tracks which disk blocks changed so incrementals read only those.

> [!tip] Think of it like
> Instead of re-reading the whole book, CBT keeps a list of which pages changed.

> [!info]+ Words on this page
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> **incremental**: A backup of only what changed since the last backup.
> **hypervisor**: Software that runs virtual machines on a physical server.
> *More in the [[Glossary]].*

## How it works

- VMware CBT, Hyper-V Resilient Change Tracking (RCT) and agent drivers all do this.
- Corrupt CBT data can produce silently bad incrementals; reset CBT if a vendor advisory or restore test points at it.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why does CBT make incremental backups fast?
> The backup only reads the changed blocks instead of scanning the whole disk.

## See also

[[Veeam Backup & Replication]] · [[VMware vSphere]] · [[Hyper-V]]
