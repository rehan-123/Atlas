---
type: "playbook"
level: "Mid"
severity: "P2"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Datastore or CSV low space

> [!abstract] What this alert means
> The storage holding virtual machines is nearly full.
>
> **Why it matters:** When it fills, VMs pause or crash.

**How urgent:** P2. See [[Severity levels]].

> [!info]+ Words on this page
> **CSV**: In Hyper-V, a Cluster Shared Volume: storage that all servers in a cluster use at once. Elsewhere, a comma-separated spreadsheet file.
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **datastore**: In VMware, the storage where virtual machines' disk files live.
> **threshold**: The value that triggers an alert.
> **snapshot**: A saved point in time of a VM or disk. Not a backup, and it grows the longer you keep it.
> **checkpoint**: Hyper-V's name for a snapshot: a saved point in time of a VM.
> **hypervisor**: Software that runs virtual machines on a physical server.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Datastore, CSV or VM volume above threshold

## First 5 minutes

1. Check for snapshots or checkpoints, which grow fast
2. Check thin-provisioned overcommit

## Find the cause

- Stale snapshots from failed backups
- VM swap files
- Logs or data inside a thin VM growing

## Fix it

- Consolidate or delete stale snapshots (through the hypervisor, never by deleting files)
- Storage vMotion or live migrate VMs
- Expand the LUN or volume

## Ask for help (escalate) when

- Below 5% free (VMs will pause when the datastore fills)

## Write it up

Copy this into the ticket and fill it in:

```
Datastore / CSV: 
Free: 
Cause: 
Action:
```

## See also

[[Snapshot age]] · [[VMware vSphere]] · [[Hyper-V]] · [[Low disk space]]
