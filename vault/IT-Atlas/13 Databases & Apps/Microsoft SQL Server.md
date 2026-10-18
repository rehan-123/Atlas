---
type: "tool"
level: "Mid"
category: "[[Databases & Applications]]"
vendor: "[[Microsoft]]"
deployment: "On-prem or cloud VMs"
status: "current"
agent_service: "MSSQLSERVER or MSSQL$INSTANCE, SQLAgent, SQLBrowser"
aliases:
  - "SQL Server"
  - "MSSQL"
tags:
  - "tool"
  - "databases"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Microsoft SQL Server

> [!abstract] In plain words
> Microsoft's database server. Many business apps, and many IT tools, store their data in it.
>
> **What kind of tool is this?** Databases store an application's data in an organized way. Many line-of-business apps depend on one.

**Made by:** [[Microsoft]] · **Runs:** On-prem or cloud VMs · **Category:** [[Databases & Applications]]

> [!info]+ Words on this page
> **SQL**: Structured Query Language; also short for Microsoft SQL Server.
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **TCP**: A connection-based network protocol that confirms delivery.
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **browser**: The app you use to open websites: Edge, Chrome, Safari or Firefox.
> *More in the [[Glossary]].*

## In more detail

Microsoft's relational database, under countless line-of-business apps, RMMs and backup tools.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`MSSQLSERVER or MSSQL$INSTANCE, SQLAgent, SQLBrowser`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 1433/TCP default instance
- 1434/UDP SQL Browser (named instances)

## Alerts you'll see

- SQL service stopped
- Transaction log full (error 9002)
- Database or log disk filling
- Failed SQL Agent jobs (including backups)
- Blocking and long-running queries

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Log file huge or full | Check the recovery model: FULL needs regular log backups; check log_reuse_wait_desc in sys.databases |
| Instance unreachable | Check the service, the TCP/IP protocol in Configuration Manager, port 1433 and SQL Browser for named instances |
| Slow app | Look for blocking in sys.dm_exec_requests and check disk latency |

## Where to find its logs

- `C:\Program Files\Microsoft SQL Server\MSSQLnn.INSTANCE\MSSQL\Log\ERRORLOG`

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
SELECT name, recovery_model_desc, log_reuse_wait_desc FROM sys.databases;
EXEC sp_who2;
SELECT session_id, blocking_session_id, wait_type, command FROM sys.dm_exec_requests WHERE blocking_session_id <> 0;
DBCC SQLPERF(LOGSPACE);
DBCC CHECKDB('DBNAME') WITH NO_INFOMSGS;
```

## See also

[[SQL Server problems]] · [[Low disk space]] · [[VSS]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
