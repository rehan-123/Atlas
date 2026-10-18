---
type: "tool"
level: "Junior"
category: "[[RMM]]"
vendor: "[[N-able]]"
deployment: "SaaS"
status: "current"
agent_service: "Advanced Monitoring Agent"
aliases:
  - "SolarWinds RMM"
  - "GFI MAX RemoteManagement"
  - "N-sight"
tags:
  - "tool"
  - "rmm"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# N-able N-sight RMM

> [!abstract] In plain words
> N-able's simpler RMM for small businesses. It runs regular health checks on each device and flags failures.
>
> **What kind of tool is this?** An RMM is the main remote-control console of an MSP. A small program (the agent) runs on every client computer and reports back, so you can see problems, run fixes and install updates without visiting anyone.

**Made by:** [[N-able]] · **Runs:** SaaS · **Category:** [[RMM]]

> [!info]+ Words on this page
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **MSP**: Managed service provider: a company that runs IT for other companies.
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> *More in the [[Glossary]].*

## In more detail

SMB-focused cloud RMM, formerly SolarWinds RMM and GFI MAX. 24x7 checks and Daily Safety Checks, automated tasks and patch management.

## Main parts

- Advanced Monitoring Agent
- 24x7 checks and Daily Safety Checks
- Automated tasks (scripts)
- Patch Management
- Take Control

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`Advanced Monitoring Agent`

## Alerts you'll see

- Failed 24x7 checks
- Overdue devices
- Failed Daily Safety Checks
- Patch failures

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Device overdue | Check the Advanced Monitoring Agent service and outbound connectivity |

## Where to find its logs

- `C:\Program Files (x86)\Advanced Monitoring Agent (agent folder and logs)`

## See also

[[N-able N-central]] · [[Cove Data Protection]] · [[N-able Take Control]] · [[Agent offline]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
