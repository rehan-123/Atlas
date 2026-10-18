---
type: "tool"
level: "Junior"
category: "[[RMM]]"
vendor: "[[NinjaOne]]"
deployment: "SaaS"
status: "current"
agent_service: "NinjaRMMAgent"
aliases:
  - "NinjaRMM"
  - "Ninja"
tags:
  - "tool"
  - "rmm"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# NinjaOne

> [!abstract] In plain words
> A popular, easy-to-use cloud RMM known for fast patching, with backup and documentation built in.
>
> **What kind of tool is this?** An RMM is the main remote-control console of an MSP. A small program (the agent) runs on every client computer and reports back, so you can see problems, run fixes and install updates without visiting anyone.

**Made by:** [[NinjaOne]] · **Runs:** SaaS · **Category:** [[RMM]]

> [!info]+ Words on this page
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **MSP**: Managed service provider: a company that runs IT for other companies.
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **TCP**: A connection-based network protocol that confirms delivery.
> **CPU**: The processor, the part of a computer that does the calculations.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> *More in the [[Glossary]].*

## In more detail

Cloud RMM known for a fast UI and patching, with policies, scripting, Ninja Remote, backup and documentation in one console.

## Main parts

- Agent (NinjaRMMAgent, plus a patcher service)
- Policies and conditions
- Script library and automations
- OS and third-party patching
- Ninja Remote
- NinjaOne Backup
- Documentation module

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`NinjaRMMAgent`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 443/TCP outbound to the NinjaOne region endpoints

## Alerts you'll see

- Device offline
- Condition alerts (disk, CPU, memory, services, event IDs)
- Patch failures
- Backup failures

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Device offline | Check the NinjaRMMAgent service and outbound 443 |
| Patch fails | Read the patch activity on the device and Windows Update errors |

## Where to find its logs

- `C:\ProgramData\NinjaRMMAgent\logs`

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-Service NinjaRMMAgent*
```

## Good to know

- NinjaOne bought Dropsuite (Microsoft 365 backup) in 2025 (verify).

## See also

[[Dropsuite]] · [[Patch management]] · [[Agent offline]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
