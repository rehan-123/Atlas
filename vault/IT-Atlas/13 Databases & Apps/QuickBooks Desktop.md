---
type: "tool"
level: "Mid"
category: "[[Databases & Applications]]"
vendor: "[[Intuit]]"
deployment:
status: "current"
agent_service: "QuickBooksDBXX (XX = version)"
aliases: []
tags:
  - "tool"
  - "databases"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# QuickBooks Desktop

> [!abstract] In plain words
> Accounting software many small businesses run on a shared server; a common source of help desk tickets.
>
> **What kind of tool is this?** Databases store an application's data in an organized way. Many line-of-business apps depend on one.

**Made by:** [[Intuit]] · **Category:** [[Databases & Applications]]

> [!info]+ Words on this page
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Desktop accounting with company files (.QBW) hosted on a file server running the QuickBooks Database Server Manager.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`QuickBooksDBXX (XX = version)`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- Dynamic ports set by Database Server Manager (see its Port Monitor tab)

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| H202/H505 errors (can't open company file in multi-user mode) | Check the Database Server Manager service on the host, the firewall ports it lists, and that the file share is reachable |
| Company file slow | Run Verify/Rebuild data; keep the file on local fast storage on the host |

## See also

[[File Server & DFS]] · [[Windows Defender Firewall]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
