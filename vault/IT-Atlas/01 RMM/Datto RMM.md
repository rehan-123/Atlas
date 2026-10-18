---
type: "tool"
level: "Junior"
category: "[[RMM]]"
vendor: "[[Kaseya]]"
deployment: "SaaS"
status: "current"
agent_service: "CagService"
aliases:
  - "CentraStage"
  - "Autotask Endpoint Management"
  - "AEM"
tags:
  - "tool"
  - "rmm"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Datto RMM

> [!abstract] In plain words
> A cloud RMM now owned by Kaseya. You'll use it to see device health, run ready-made scripts (components) and remote in with Web Remote.
>
> **What kind of tool is this?** An RMM is the main remote-control console of an MSP. A small program (the agent) runs on every client computer and reports back, so you can see problems, run fixes and install updates without visiting anyone.

**Made by:** [[Kaseya]] · **Runs:** SaaS · **Category:** [[RMM]]

> [!info]+ Words on this page
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **MSP**: Managed service provider: a company that runs IT for other companies.
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **SNMP**: A protocol monitoring tools use to read status from network devices.
> **TCP**: A connection-based network protocol that confirms delivery.
> **TLS**: The encryption behind HTTPS and many other secure connections.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> *More in the [[Glossary]].*

## In more detail

Cloud RMM, formerly CentraStage and Autotask Endpoint Management. Components from the ComStore, monitoring and patch policies, jobs and Web Remote.

## Main parts

- Agent (CagService)
- Components and the ComStore (script library)
- Monitoring policies and alert responses
- Patch management policies
- Jobs (scheduled or quick component runs)
- Web Remote and Agent Browser
- Network Nodes: SNMP devices monitored through an agent

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`CagService`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 443/TCP outbound from the agent to the Datto RMM platform

## Alerts you'll see

- Device offline
- Monitor alerts (disk, service, event log, performance)
- Patch policy failures
- Component job failures

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Device offline | Check CagService is running; look for proxy or TLS inspection blocking outbound 443 |
| Component fails | Open the job result and read stdout and stderr; most failures are script exit codes |
| Patches not installing | Check the patch policy schedule, reboot settings and Windows Update health on the device |

## Where to find its logs

- `C:\ProgramData\CentraStage (agent data and logs)`
- Job results and audit trail in the web portal

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-Service CagService
Restart-Service CagService
```

## See also

[[Kaseya VSA]] · [[Autotask PSA]] · [[IT Glue]] · [[Datto BCDR]] · [[Agent offline]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
