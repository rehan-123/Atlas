---
type: "playbook"
level: "Mid"
severity: "P3"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# SMART predictive failure

> [!abstract] What this alert means
> A disk is warning that it's likely to fail soon.
>
> **Why it matters:** Replacing it now is much cheaper than recovering data later.

**How urgent:** P3. See [[Severity levels]].

> [!info]+ Words on this page
> **RAID**: Combining several disks so one failed disk doesn't lose data. Not a backup.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Drive reports predictive failure or rising reallocated or pending sectors

## First 5 minutes

1. Identify the drive and whether it is in a RAID set or a single disk
2. Confirm backups

## Find the cause

- Single disk in a workstation or server: data loss risk is immediate
- In RAID: replace before it fails outright

## Fix it

- Replace the drive proactively
- For single disks, image or migrate data first

## Ask for help (escalate) when

- Single-disk servers
- Several drives in the same array

## Write it up

Copy this into the ticket and fill it in:

```
Device: 
Drive: 
SMART attributes: 
Action:
```

## See also

[[SMART]] · [[RAID degraded]]
