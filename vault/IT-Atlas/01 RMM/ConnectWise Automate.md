---
type: "tool"
level: "Junior"
category: "[[RMM]]"
vendor: "[[ConnectWise]]"
deployment: "On-prem or ConnectWise-hosted"
status: "current"
agent_service: "LTService, LTSvcMon"
aliases:
  - "LabTech"
  - "CW Automate"
tags:
  - "tool"
  - "rmm"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# ConnectWise Automate

> [!abstract] In plain words
> ConnectWise's older, very scriptable RMM, formerly called LabTech. Powerful, but its console takes time to learn.
>
> **What kind of tool is this?** An RMM is the main remote-control console of an MSP. A small program (the agent) runs on every client computer and reports back, so you can see problems, run fixes and install updates without visiting anyone.

**Made by:** [[ConnectWise]] · **Runs:** On-prem or ConnectWise-hosted · **Category:** [[RMM]]

> [!info]+ Words on this page
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **MSP**: Managed service provider: a company that runs IT for other companies.
> **SQL**: Structured Query Language; also short for Microsoft SQL Server.
> **TCP**: A connection-based network protocol that confirms delivery.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> *More in the [[Glossary]].*

## In more detail

Formerly LabTech. Script-heavy RMM on a MySQL backend with remote and internal monitors, a deep scripting engine and a plugin ecosystem.

## Main parts

- Agent (LTService and LTSvcMon watchdog)
- Control Center thick client and web console
- Scripts and script scheduling
- Remote monitors (run on agents) and internal monitors (SQL queries on the server)
- Patch Manager
- MySQL database
- Solution Center plugins

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`LTService, LTSvcMon`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 80/443/TCP agent to Automate server

## Alerts you'll see

- Agent offline / not checked in
- Monitor tickets and alerts
- Script failures
- Patch install failures

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Agent offline | Check both LTService and LTSvcMon; read LTErrors.txt for server address or certificate errors |
| Script fails | Open the script log on the computer; check credentials and that the agent is not in maintenance mode |
| Server slow | Check MySQL health and table sizes; heavy internal monitors are a common cause |

## Where to find its logs

- `C:\Windows\LTSvc\LTErrors.txt`

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-Service LTService, LTSvcMon
Restart-Service LTService, LTSvcMon
```

## See also

[[ConnectWise PSA]] · [[ScreenConnect]] · [[ConnectWise RMM]] · [[Agent offline]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
