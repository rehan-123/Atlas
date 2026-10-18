---
type: "playbook"
level: "Senior"
severity: "P2"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# High disk latency

> [!abstract] What this alert means
> Storage is taking too long to answer read and write requests.
>
> **Why it matters:** Everything on top of slow storage is slow: VMs, databases, file shares. It can also be the first sign of a failing disk or array.

**How urgent:** P2. See [[Severity levels]].

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **RAID**: Combining several disks so one failed disk doesn't lose data. Not a backup.
> **IOPS**: Input/output operations per second: how many reads and writes storage can handle.
> **latency**: Delay: how long data takes to get from A to B.
> **hypervisor**: Software that runs virtual machines on a physical server.
> **datastore**: In VMware, the storage where virtual machines' disk files live.
> **snapshot**: A saved point in time of a VM or disk. Not a backup, and it grows the longer you keep it.
> **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
> *More in the [[Glossary]].*

## You'll see this when

- Average disk read or write latency above ~20-25 ms sustained
- Hypervisor datastore latency alerts
- Users report slowness in several apps at once

## First 5 minutes

1. Check whether one VM/process or everything is affected
2. Look at the array or host for failed disks, rebuilds or controller alerts
3. Check whether backups, snapshots consolidation or antivirus scans are running

## Find the cause

- RAID rebuild or degraded array
- Snapshot chains growing on VMs
- A noisy VM saturating IOPS
- Cache battery failed (write cache disabled)
- Thin-provisioned datastore near full

## Fix it

- Reschedule heavy jobs
- Consolidate old snapshots
- Replace failed hardware (cache battery, disks)
- Move busy VMs or add faster storage

## Ask for help (escalate) when

- Latency above 100 ms with production impact
- Array controller faults
- Any sign of data corruption

## Write it up

Copy this into the ticket and fill it in:

```
Storage: 
Latency observed: 
Top consumers: 
Cause: 
Action:
```

## See also

[[Performance analysis]] · [[RAID degraded]] · [[Snapshot age]] · [[Datastore or CSV low space]]
