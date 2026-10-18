---
type: "tool"
level: "Junior"
category: "[[RMM]]"
vendor: "[[Atera]]"
deployment: "SaaS"
status: "current"
agent_service: "AteraAgent"
aliases: []
tags:
  - "tool"
  - "rmm"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Atera

> [!abstract] In plain words
> An all-in-one RMM and ticketing tool for small MSPs, charged per technician rather than per device.
>
> **What kind of tool is this?** An RMM is the main remote-control console of an MSP. A small program (the agent) runs on every client computer and reports back, so you can see problems, run fixes and install updates without visiting anyone.

**Made by:** [[Atera]] · **Runs:** SaaS · **Category:** [[RMM]]

> [!info]+ Words on this page
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **MSP**: Managed service provider: a company that runs IT for other companies.
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **PSA**: Professional services automation: the MSP's ticketing, time and billing system.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **threshold**: The value that triggers an alert.
> *More in the [[Glossary]].*

## In more detail

RMM plus PSA priced per technician rather than per device, with built-in ticketing, scripting, patching and integrations with third-party remote access tools.

## Main parts

- AteraAgent
- Alerts and thresholds profiles
- Script library
- Patch management
- Built-in ticketing and billing
- Remote access integrations

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`AteraAgent`

## Alerts you'll see

- Agent offline
- Threshold alerts
- Patch failures

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Agent offline | Check the AteraAgent service and outbound 443 |

## Where to find its logs

- `C:\Program Files\ATERA Networks\AteraAgent (agent folder)`

## See also

[[Splashtop]] · [[AnyDesk]] · [[Agent offline]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
