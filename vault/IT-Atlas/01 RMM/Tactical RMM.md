---
type: "tool"
level: "Junior"
category: "[[RMM]]"
vendor:
deployment: "Self-hosted (open source)"
status: "current"
agent_service: "tacticalrmm, Mesh Agent"
aliases: []
tags:
  - "tool"
  - "rmm"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Tactical RMM

> [!abstract] In plain words
> A free, open-source RMM you host yourself. Popular for labs and practice.
>
> **What kind of tool is this?** An RMM is the main remote-control console of an MSP. A small program (the agent) runs on every client computer and reports back, so you can see problems, run fixes and install updates without visiting anyone.

**Runs:** Self-hosted (open source) · **Category:** [[RMM]]

> [!info]+ Words on this page
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **MSP**: Managed service provider: a company that runs IT for other companies.
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> *More in the [[Glossary]].*

## In more detail

Open-source RMM (Django and Vue server, Go agent) that uses MeshCentral for remote control. Popular in homelabs and with MSPs who want to self-host.

## Main parts

- Tactical RMM agent (Go)
- MeshCentral for remote desktop and terminal
- Checks, tasks and scripts
- Windows patch management
- Alert templates

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`tacticalrmm, Mesh Agent`

## Alerts you'll see

- Agent offline
- Check failures
- Pending patches

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Agent offline | Check the tacticalrmm service and the NATS connection to the server; confirm DNS and certificates on the server |

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-Service tacticalrmm, 'Mesh Agent'
```

## See also

[[MeshCentral]] · [[Agent offline]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
