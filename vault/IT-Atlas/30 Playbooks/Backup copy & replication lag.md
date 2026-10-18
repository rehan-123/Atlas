---
type: "playbook"
level: "Mid"
severity: "P3"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Backup copy & replication lag

> [!abstract] What this alert means
> The offsite copy of the backups is falling behind.
>
> **Why it matters:** If the site is lost (fire, theft, ransomware), the offsite copy is older than you think.

**How urgent:** P3. See [[Severity levels]].

> [!info]+ Words on this page
> **ISP**: Internet service provider.
> **WAN**: Wide area network: links between sites, or to the internet.
> **replication**: Copying data or changes to another place, continuously or on a schedule.
> **bandwidth**: How much data a link can carry per second.
> **throttling**: Deliberately slowing something down, for example limiting backup bandwidth during the day.
> **uplink**: The connection from a switch or site up to the next level of the network.
> **retention**: How long backups or logs are kept.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Offsite copy, cloud sync or replication behind schedule

## First 5 minutes

1. Check how far behind it is and whether the gap is growing
2. Check bandwidth limits, throttling windows and the uplink

## Find the cause

- A new large server or a big data change (seed) saturating the link
- ISP problems or a failed WAN link
- Retention or space limits at the target

## Fix it

- Adjust throttling to allow more bandwidth after hours
- Seed large new datasets by physical drive if the vendor supports it
- Fix WAN issues

## Ask for help (escalate) when

- Offsite copy more than 72 hours behind
- Gap keeps growing for a week

## Write it up

Copy this into the ticket and fill it in:

```
Device / job: 
Lag: 
Cause: 
Action: 
Expected catch-up:
```

## See also

[[RPO & RTO]] · [[Datto BCDR]] · [[Unitrends]] · [[Firewall WAN down]]
