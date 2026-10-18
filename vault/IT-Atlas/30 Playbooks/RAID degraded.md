---
type: "playbook"
level: "Mid"
severity: "P2"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# RAID degraded

> [!abstract] What this alert means
> A disk in a server's RAID set has failed; the server is running without its safety net.
>
> **Why it matters:** One more disk failure could lose everything on that array.

**How urgent:** P2. See [[Severity levels]].

> [!info]+ Words on this page
> **NAS**: Network-attached storage: a box full of disks that shares files over the network.
> **RAID**: Combining several disks so one failed disk doesn't lose data. Not a backup.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
> **firmware**: The software built into hardware such as firewalls, disks and servers.
> *More in the [[Glossary]].*

## You'll see this when

- Controller, iDRAC, iLO, NAS or array reports a degraded virtual disk or failed drive

## First 5 minutes

1. Confirm which drive, which slot and which array
2. Confirm the last backup is good before anything else
3. Check whether a hot spare has started rebuilding

## Find the cause

- Single drive failure: replace it
- Several drives reporting errors: risk of losing the array; check backups and escalate
- Controller cache battery failed: performance drops (write-through mode)

## Fix it

- Order the exact replacement part (part number and firmware compatibility)
- Replace the drive and monitor the rebuild to completion

## Ask for help (escalate) when

- Always tell the client the same day
- A second drive fails or shows errors during rebuild
- RAID 5 on large disks during a long rebuild

## Write it up

Copy this into the ticket and fill it in:

```
Server / array: 
Slot / drive: 
RAID level: 
Last good backup: 
Part ordered: 
Rebuild status:
```

## See also

[[RAID levels]] · [[Hardware RAID controllers]] · [[Dell iDRAC]] · [[HPE iLO]] · [[SMART predictive failure]]
