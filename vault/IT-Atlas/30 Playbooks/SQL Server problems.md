---
type: "playbook"
level: "Mid"
severity: "P2"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# SQL Server problems

> [!abstract] What this alert means
> The SQL database server is down, full or very slow.
>
> **Why it matters:** The apps that use that database stop working or crawl.

**How urgent:** P2. See [[Severity levels]].

> [!info]+ Words on this page
> **SQL**: Structured Query Language; also short for Microsoft SQL Server.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **replication**: Copying data or changes to another place, continuously or on a schedule.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- SQL service down
- Transaction log full (9002)
- Blocking
- Failed agent or backup jobs

## First 5 minutes

1. Check the service and the SQL ERRORLOG
2. Check data and log disk space

## Find the cause

- Log full: `log_reuse_wait_desc` shows why (LOG_BACKUP, ACTIVE_TRANSACTION, REPLICATION)
- Blocking: `sys.dm_exec_requests` with blocking_session_id
- Service will not start: ERRORLOG often shows a missing file, permissions or a full disk

## Fix it

- Take a log backup or fix the recovery model, then shrink only if required
- Free disk space
- Kill a blocking session only with the app owner's agreement

## Ask for help (escalate) when

- Database corruption (DBCC CHECKDB errors)
- Production app down

## Write it up

Copy this into the ticket and fill it in:

```
Instance / database: 
Error: 
Cause: 
Action:
```

## See also

[[Microsoft SQL Server]] · [[Low disk space]]
