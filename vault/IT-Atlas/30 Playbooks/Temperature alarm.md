---
type: "playbook"
level: "Junior"
severity: "P2"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Temperature alarm

> [!abstract] What this alert means
> The server room or a server is getting too hot.
>
> **Why it matters:** Hardware will throttle, fail or shut itself down.

**How urgent:** P2. See [[Severity levels]].

> [!info]+ Words on this page
> **threshold**: The value that triggers an alert.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Server room, rack or hardware temperature above threshold

## First 5 minutes

1. Check the trend: rising fast means cooling has failed
2. Check multiple sensors and hardware inlet temperatures (iDRAC, iLO)

## Find the cause

- Air conditioning failure
- Blocked airflow or a door left open
- Failed fans in hardware

## Fix it

- Contact the site to check cooling
- Shut down non-critical equipment to reduce heat if needed

## Ask for help (escalate) when

- Temperature still climbing
- Hardware starting thermal shutdowns

## Write it up

Copy this into the ticket and fill it in:

```
Site: 
Readings: 
Cause: 
Action:
```

## See also

[[Environmental monitoring]] · [[APC Smart-UPS]] · [[Dell iDRAC]] · [[HPE iLO]]
