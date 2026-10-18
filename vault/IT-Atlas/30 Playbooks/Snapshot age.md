---
type: "playbook"
level: "Mid"
severity: "P3"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Snapshot age

> [!abstract] What this alert means
> A virtual machine has an old snapshot (checkpoint) that was never cleaned up.
>
> **Why it matters:** Snapshots keep growing, fill storage and slow the VM down.

**How urgent:** P3. See [[Severity levels]].

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **snapshot**: A saved point in time of a VM or disk. Not a backup, and it grows the longer you keep it.
> **checkpoint**: Hyper-V's name for a snapshot: a saved point in time of a VM.
> **threshold**: The value that triggers an alert.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> **datastore**: In VMware, the storage where virtual machines' disk files live.
> *More in the [[Glossary]].*

## You'll see this when

- VM snapshot or checkpoint older than the threshold (often 3 days)

## First 5 minutes

1. Check who or what created it (backup tool, admin, patching)
2. Check whether a backup job is still running

## Find the cause

- Backup tool failed to remove its snapshot
- Admin forgot a pre-change snapshot

## Fix it

- Confirm with the owner, then delete or consolidate it
- Fix the backup integration if it keeps leaving snapshots

## Ask for help (escalate) when

- Snapshot very large or the datastore is filling
- Consolidation fails

## Write it up

Copy this into the ticket and fill it in:

```
VM: 
Snapshot created / by: 
Size: 
Action:
```

## See also

[[VMware vSphere]] · [[Hyper-V]] · [[Veeam Backup & Replication]] · [[Datastore or CSV low space]]
