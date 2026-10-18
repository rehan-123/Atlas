---
type: "tool"
level: "Junior"
category: "[[RMM]]"
vendor: "[[Kaseya]]"
deployment: "On-prem or Kaseya-hosted SaaS"
status: "current"
agent_service: "Kaseya Agent (AgentMon.exe)"
aliases: []
tags:
  - "tool"
  - "rmm"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Kaseya VSA

> [!abstract] In plain words
> Kaseya's RMM. Every managed computer runs the VSA agent, and from the console you can run scripts (called agent procedures), patch, monitor and remote in.
>
> **What kind of tool is this?** An RMM is the main remote-control console of an MSP. A small program (the agent) runs on every client computer and reports back, so you can see problems, run fixes and install updates without visiting anyone.

**Made by:** [[Kaseya]] · **Runs:** On-prem or Kaseya-hosted SaaS · **Category:** [[RMM]]

> [!info]+ Words on this page
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **MSP**: Managed service provider: a company that runs IT for other companies.
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **TCP**: A connection-based network protocol that confirms delivery.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> **ransomware**: Malware that encrypts files and demands payment to unlock them.
> *More in the [[Glossary]].*

## In more detail

Kaseya's long-running RMM: agents, agent procedures, monitor sets, patch management and Live Connect remote control in one console.

## Main parts

- Agent service (AgentMon.exe) on every managed machine
- Agent procedures: the scripting engine
- Monitor sets, event log sets and alert profiles
- Patch management and Software Management
- Live Connect and Kaseya Remote Control
- Organizations and machine groups for multi-tenancy

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`Kaseya Agent (AgentMon.exe)`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 5721/TCP agent check-in to the VSA server
- 443/TCP web console

## Alerts you'll see

- Agent not checked in / offline
- Agent procedure failures
- Patch scan or install failures
- Monitor set and event log alerts

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Agent offline | Check the Kaseya agent service is running, then test 5721/TCP to the VSA server |
| Procedure stuck pending | Confirm the agent is online and no earlier step is waiting on a reboot; read Procedure History |
| Patch scan fails | Check the Windows Update service and update errors on the endpoint, then rescan |

## Where to find its logs

- Agent Logs and Procedure History in the VSA console

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Test-NetConnection VSA-SERVER -Port 5721
Get-Service | Where-Object DisplayName -like 'Kaseya*'
```

## Good to know

- July 2021: the REvil group exploited on-prem VSA servers in a supply-chain ransomware attack on MSPs and their clients. Keep VSA patched and the console off the open internet.

## See also

[[Datto RMM]] · [[Autotask PSA]] · [[IT Glue]] · [[Kaseya BMS]] · [[Windows Update]] · [[Agent offline]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
