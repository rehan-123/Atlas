---
type: "concept"
level: "Junior"
category: "[[Operations & process]]"
aliases:
  - "Priority levels"
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Severity levels

> [!abstract] In one line
> How urgent an incident is, usually P1 to P4.

> [!tip] Think of it like
> Hospital triage: P1 is the emergency room, P4 can wait for an appointment.

> [!info]+ Words on this page
> **RAID**: Combining several disks so one failed disk doesn't lose data. Not a backup.
> **ransomware**: Malware that encrypts files and demands payment to unlock them.
> **cluster**: Several servers working together so one can take over if another fails.
> **threshold**: The value that triggers an alert.
> *More in the [[Glossary]].*

## How it works

| Level | Meaning | Example |
|---|---|---|
| P1 | Business down or security incident in progress | Site offline, ransomware |
| P2 | Major degradation or key system at risk | Host down in a cluster, RAID degraded |
| P3 | Limited impact | One server's backup failed |
| P4 | No impact yet | Warning thresholds, housekeeping |

Severity drives response time, escalation and who gets woken up. Agree definitions with each client.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- A client's whole site is offline. What priority?
> P1: business down.

## See also

[[Escalation tiers]] · [[SLA & SLO]]
