---
type: "playbook"
level: "Junior"
severity: "P3 (P2 for system or database volumes)"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Low disk space

> [!abstract] What this alert means
> A drive is nearly full.
>
> **Why it matters:** Full drives crash services, stop databases and break backups and updates.

**How urgent:** P3 (P2 for system or database volumes). See [[Severity levels]].

> [!info]+ Words on this page
> **SQL**: Structured Query Language; also short for Microsoft SQL Server.
> **VSS**: Volume Shadow Copy Service: takes consistent snapshots of in-use files for backups.
> **threshold**: The value that triggers an alert.
> **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Free space under the warning or critical threshold

## First 5 minutes

1. Check which volume and how fast it is filling (sudden growth vs slow trend)
2. Find the largest folders
3. Check whether it is a system, database, log or backup volume (each has different safe actions)

## Find the cause

- TreeSize, WizTree or `Get-ChildItem -Recurse | Sort Length` to find large folders
- Usual suspects: Windows Update cache, WinSxS, temp, IIS logs, SQL transaction logs, old user profiles, VSS shadow storage, backup staging, crash dumps

## Fix it

- Disk Cleanup or DISM component cleanup
- Rotate or compress logs (IIS, app logs)
- SQL: back up and shrink transaction logs only after fixing the cause (recovery model or missing log backups)
- Expand the volume if growth is legitimate

## Ask for help (escalate) when

- System or database volume under 5% and still growing
- Unknown files growing fast (possible attack or runaway process)

## Write it up

Copy this into the ticket and fill it in:

```
Volume: 
Free before / after: 
What was using the space: 
Action: 
Prevention:
```

## See also

[[Monitoring thresholds and baselines]] · [[Windows Update]] · [[IIS]] · [[Microsoft SQL Server]] · [[Datastore or CSV low space]]
