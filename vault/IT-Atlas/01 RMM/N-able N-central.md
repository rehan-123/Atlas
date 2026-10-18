---
type: "tool"
level: "Junior"
category: "[[RMM]]"
vendor: "[[N-able]]"
deployment: "On-prem or N-able hosted"
status: "current"
agent_service: "Windows Agent, Windows Agent Maintenance Service"
aliases: []
tags:
  - "tool"
  - "rmm"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# N-able N-central

> [!abstract] In plain words
> N-able's bigger RMM for MSPs with many clients. A 'probe' at each site can also check devices that have no agent.
>
> **What kind of tool is this?** An RMM is the main remote-control console of an MSP. A small program (the agent) runs on every client computer and reports back, so you can see problems, run fixes and install updates without visiting anyone.

**Made by:** [[N-able]] · **Runs:** On-prem or N-able hosted · **Category:** [[RMM]]

> [!info]+ Words on this page
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **MSP**: Managed service provider: a company that runs IT for other companies.
> **SNMP**: A protocol monitoring tools use to read status from network devices.
> **WMI**: Windows Management Instrumentation: lets tools query Windows for information.
> **TCP**: A connection-based network protocol that confirms delivery.
> **CPU**: The processor, the part of a computer that does the calculations.
> **probe**: A small collector at a client site that monitors devices on the monitoring server's behalf.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> *More in the [[Glossary]].*

## In more detail

N-able's enterprise RMM: service templates, rules, Automation Manager, probes for agentless monitoring, and Windows, macOS and Linux agents.

## Main parts

- Windows Agent and Windows Agent Maintenance Service
- Probe: agentless discovery, SNMP and WMI monitoring for a site
- Service templates and rules
- Automation Manager (drag-and-drop automation policies)
- Patch Manager
- Take Control remote access
- Cove Data Protection integration

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`Windows Agent, Windows Agent Maintenance Service`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 443/TCP agent and probe to the N-central server

## Alerts you'll see

- Device or probe down
- Service thresholds (disk, CPU, services, AV)
- Patch status
- Backup status via Cove

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Device not reporting | Check the Windows Agent services; confirm the server address and 443 reachability |
| Probe down | Check the probe service on the probe host and its credentials |
| Stale appliance ID after imaging | Reinstall the agent so the device registers with a fresh ID |

## Where to find its logs

- `C:\Program Files (x86)\N-able Technologies\Windows Agent\log`

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-Service 'Windows Agent*'
```

## See also

[[N-able N-sight RMM]] · [[Cove Data Protection]] · [[N-able Take Control]] · [[N-able Passportal]] · [[Agent offline]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
