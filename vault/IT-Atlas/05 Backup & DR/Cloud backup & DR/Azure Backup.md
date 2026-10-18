---
type: "tool"
level: "Mid"
category: "[[Backup & DR]]"
subcategory: "[[Cloud backup & DR]]"
vendor: "[[Microsoft]]"
deployment: "Azure"
status: "current"
aliases:
  - "MARS agent"
  - "Recovery Services vault"
tags:
  - "tool"
  - "backup"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Azure Backup

> [!abstract] In plain words
> Azure's built-in backup for Azure VMs, and for on-site servers through a small agent.
>
> **What kind of tool is this?** These are the backup and disaster-recovery services built into Azure and AWS, plus tools that keep a live copy of servers in another location.

**Made by:** [[Microsoft]] · **Runs:** Azure · **Category:** [[Backup & DR]] › [[Cloud backup & DR]]

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **DR**: Disaster recovery: getting systems back after a major failure.
> **SQL**: Structured Query Language; also short for Microsoft SQL Server.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **immutable**: Can't be changed or deleted until a set date, even by an admin.
> *More in the [[Glossary]].*

## In more detail

Azure's native backup: Azure VMs, SQL in VMs, Azure Files and on-prem servers through the MARS agent, stored in Recovery Services or Backup vaults.

## Main parts

- Recovery Services vault
- Backup vault
- MARS agent for on-prem files and folders
- Azure VM backup
- Soft delete and immutable vaults

## Alerts you'll see

- Backup job failed
- Vault soft-delete events
- MARS agent offline

## See also

[[Microsoft Azure]] · [[Azure Site Recovery]] · [[Immutability & air gap]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
