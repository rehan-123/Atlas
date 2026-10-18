---
type: "playbook"
level: "Junior"
severity: "P3 (P2 for critical services)"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Windows service stopped

> [!abstract] What this alert means
> A Windows service that should be running has stopped.
>
> **Why it matters:** The app or feature that depends on that service stops working.

**How urgent:** P3 (P2 for critical services). See [[Severity levels]].

> [!info]+ Words on this page
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Monitored service not running

## First 5 minutes

1. Check the System log for 7031, 7034 (crashed) or 7000, 7009 (failed to start)
2. Try starting it once and see if it stays up

## Find the cause

- Dependency services stopped
- Service account password expired or changed (event 7000 logon failure)
- Application crash in the Application log (event 1000)

## Fix it

- Start the service; set recovery actions to restart on failure
- Update the service account password
- Repair or update the application

## Ask for help (escalate) when

- Service keeps crashing
- Business application down

## Write it up

Copy this into the ticket and fill it in:

```
Service: 
Host: 
Why it stopped: 
Action:
```

## See also

[[Windows Event ID reference]] · [[Windows Server]]
