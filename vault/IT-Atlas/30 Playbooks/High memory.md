---
type: "playbook"
level: "Junior"
severity: "P3"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# High memory

> [!abstract] What this alert means
> The machine is using most of its RAM.
>
> **Why it matters:** When RAM runs out, Windows uses the disk instead and everything slows to a crawl.

**How urgent:** P3. See [[Severity levels]].

> [!info]+ Words on this page
> **SQL**: Structured Query Language; also short for Microsoft SQL Server.
> **RAM**: Memory: the computer's short-term workspace for open apps. Cleared when you restart.
> **threshold**: The value that triggers an alert.
> **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> **domain controller**: A server running Active Directory that checks logins.
> *More in the [[Glossary]].*

## You'll see this when

- Memory above threshold or paging heavily

## First 5 minutes

1. Identify the top processes by working set
2. Check whether the service is designed to use memory (SQL Server, Exchange, sync services)

## Find the cause

- SQL Server takes memory by design; check max server memory is set, leaving room for the OS
- A steady climb over days suggests a leak; RAMMap shows non-process usage such as file cache and paged pool

## Fix it

- Set application memory limits where supported
- Restart a leaking service in a window and report the leak to the vendor
- Add RAM if the workload needs it

## Ask for help (escalate) when

- Paging is causing user impact
- Memory exhaustion on a domain controller or identity sync server

## Write it up

Copy this into the ticket and fill it in:

```
Host: 
Top processes: 
Trend: 
Action:
```

## See also

[[Microsoft SQL Server]] · [[Microsoft Entra Connect]] · [[Sysinternals Suite]] · [[High CPU]]
