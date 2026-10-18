---
type: "tool"
level: "Mid"
category: "[[Backup & DR]]"
subcategory: "[[Image & server backup]]"
vendor: "[[N-able]]"
deployment: "Cloud-first with optional local copy"
status: "current"
agent_service: "Backup Service Controller"
aliases:
  - "SolarWinds Backup"
  - "N-able Backup"
tags:
  - "tool"
  - "backup"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Cove Data Protection

> [!abstract] In plain words
> N-able's cloud backup: data goes straight to N-able's cloud, with an optional local copy for faster restores.
>
> **What kind of tool is this?** Image backup copies a whole machine (operating system, apps and data) so it can be rebuilt exactly as it was.

**Made by:** [[N-able]] · **Runs:** Cloud-first with optional local copy · **Category:** [[Backup & DR]] › [[Image & server backup]]

> [!info]+ Words on this page
> **DR**: Disaster recovery: getting systems back after a major failure.
> **deduplication**: Storing identical chunks of data only once to save space.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> *More in the [[Glossary]].*

## In more detail

N-able's cloud-first backup (formerly SolarWinds Backup) for servers, workstations and Microsoft 365. TrueDelta deduplication, optional LocalSpeedVault, and Standby Image for recovery.

## Main parts

- Backup Manager agent
- Cloud storage in N-able data centers
- LocalSpeedVault (optional local copy)
- Standby Image and Recovery Testing
- Microsoft 365 backup

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`Backup Service Controller`

## Alerts you'll see

- Backup failed or not run
- LocalSpeedVault synchronization issues
- Recovery testing failed

## See also

[[N-able N-central]] · [[N-able N-sight RMM]] · [[Backup job failed]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
