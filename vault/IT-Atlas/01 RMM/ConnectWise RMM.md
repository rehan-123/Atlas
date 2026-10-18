---
type: "tool"
level: "Junior"
category: "[[RMM]]"
vendor: "[[ConnectWise]]"
deployment: "SaaS"
status: "current"
agent_service: "ITSPlatform (legacy Continuum agents use SAAZ* services)"
aliases:
  - "Continuum Command"
  - "CW RMM"
tags:
  - "tool"
  - "rmm"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# ConnectWise RMM

> [!abstract] In plain words
> ConnectWise's newer cloud RMM, built from the Continuum product.
>
> **What kind of tool is this?** An RMM is the main remote-control console of an MSP. A small program (the agent) runs on every client computer and reports back, so you can see problems, run fixes and install updates without visiting anyone.

**Made by:** [[ConnectWise]] · **Runs:** SaaS · **Category:** [[RMM]]

> [!info]+ Words on this page
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **MSP**: Managed service provider: a company that runs IT for other companies.
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **NOC**: Network operations center: the team that monitors and fixes infrastructure.
> **PSA**: Professional services automation: the MSP's ticketing, time and billing system.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> *More in the [[Glossary]].*

## In more detail

ConnectWise's SaaS RMM built from Continuum Command, with optional ConnectWise NOC services behind it.

## Main parts

- Agent
- Policies and monitoring
- Automation and scripts
- Patch management
- Integration with ConnectWise PSA and ScreenConnect

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`ITSPlatform (legacy Continuum agents use SAAZ* services)`

## Alerts you'll see

- Device offline
- Monitoring alerts and auto-created tickets
- Patch failures

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Device offline | Check the agent services are running and outbound 443 is allowed |

## See also

[[ConnectWise Automate]] · [[ConnectWise PSA]] · [[ScreenConnect]] · [[Agent offline]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
