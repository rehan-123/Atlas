---
type: "playbook"
level: "Junior"
severity: "P3 (P2 after repeated failures)"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Backup job failed

> [!abstract] What this alert means
> A backup didn't complete, or completed with errors.
>
> **Why it matters:** Until the next good backup, data is at risk: the last restore point gets older every hour.

**How urgent:** P3 (P2 after repeated failures). See [[Severity levels]].

> [!info]+ Words on this page
> **RPO**: Recovery point objective: the most data, measured in time, you can afford to lose.
> **VSS**: Volume Shadow Copy Service: takes consistent snapshots of in-use files for backups.
> **NAS**: Network-attached storage: a box full of disks that shares files over the network.
> **BCDR**: Business continuity and disaster recovery: keeping a business running, and getting it back after a disaster.
> **token**: A temporary digital key used to prove you're allowed in.
> **snapshot**: A saved point in time of a VM or disk. Not a backup, and it grows the longer you keep it.
> **hypervisor**: Software that runs virtual machines on a physical server.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> *More in the [[Glossary]].*

## You'll see this when

- Backup job failed, missed or finished with warnings

## First 5 minutes

1. Read the actual error in the job log, not just the status
2. Check how long since the last good backup (the real RPO exposure)
3. Check whether it is one machine or many (product or storage issue)

## Find the cause

- VSS errors: see VSS writer failure
- Destination full or unreachable
- Credentials changed (guest processing, NAS share, cloud token)
- Machine off or asleep during the schedule
- Snapshot creation failed at the hypervisor
- Agent outdated or service stopped

## Where to look, by tool

| Tool | Where to look |
|---|---|
| [[Datto BCDR]] | Device and agent logs in the Datto partner portal and appliance web UI |
| [[Unitrends]] | Jobs and system reports in the appliance UI |
| [[Acronis Cyber Protect]] | C:\ProgramData\Acronis\BackupAndRecovery\MMS (Managed Machine Service logs) |
| [[Windows Server Backup]] | Event Viewer: Applications and Services Logs > Microsoft > Windows > Backup |
| [[Veeam Backup & Replication]] | C:\ProgramData\Veeam\Backup (server and job logs) |

## Fix it

- Run the job again after fixing the cause and confirm success
- Free space or extend retention storage
- Update credentials
- Consolidate stuck snapshots

## Ask for help (escalate) when

- No good backup for more than 48 hours on a server
- Several clients failing at once (vendor or platform issue)
- Backups deleted unexpectedly (possible attack)

## Write it up

Copy this into the ticket and fill it in:

```
Job / machine: 
Error: 
Last good backup: 
Cause: 
Action: 
Re-run result:
```

## See also

[[VSS writer failure]] · [[Backup verification]] · [[RPO & RTO]] · [[Veeam Backup & Replication]] · [[Datto BCDR]] · [[Unitrends]]
