---
type: "tool"
level: "Mid"
category: "[[Backup & DR]]"
subcategory: "[[Image & server backup]]"
vendor: "[[Acronis]]"
deployment: "Cloud console with agents"
status: "current"
agent_service: "Acronis Managed Machine Service"
aliases:
  - "Acronis Cyber Protect Cloud"
  - "Acronis Backup"
tags:
  - "tool"
  - "backup"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Acronis Cyber Protect

> [!abstract] In plain words
> Backup and antivirus in one agent, managed from Acronis' cloud console.
>
> **What kind of tool is this?** Image backup copies a whole machine (operating system, apps and data) so it can be rebuilt exactly as it was.

**Made by:** [[Acronis]] · **Runs:** Cloud console with agents · **Category:** [[Backup & DR]] › [[Image & server backup]]

> [!info]+ Words on this page
> **DR**: Disaster recovery: getting systems back after a major failure.
> **TCP**: A connection-based network protocol that confirms delivery.
> **VSS**: Volume Shadow Copy Service: takes consistent snapshots of in-use files for backups.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **token**: A temporary digital key used to prove you're allowed in.
> *More in the [[Glossary]].*

## In more detail

Backup plus security in one agent: image and file backup to local or cloud storage, anti-malware and patching, managed from the Acronis cloud console (Cyber Protect Cloud for service providers).

## Main parts

- Agent for Windows, Linux and macOS (Managed Machine Service)
- Protection plans
- Cloud and local backup storage
- Anti-malware, URL filtering and patch management
- register_agent tool for (re)registration

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`Acronis Managed Machine Service`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 443/TCP outbound to the Acronis data center

## Alerts you'll see

- Backup failed or missed
- Agent offline
- Storage quota exceeded

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Agent offline in the console | Restart the Acronis services, then re-register the agent with a fresh token if it stays offline |
| Backup fails on VSS | Check vssadmin list writers and System and Application event logs |
| Backup missed | Check the machine was powered on and the plan schedule and conditions |

## Where to find its logs

- `C:\ProgramData\Acronis\BackupAndRecovery\MMS (Managed Machine Service logs)`

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
"C:\Program Files\BackupClient\RegisterAgentTool\register_agent.exe" -o register -t cloud -a https://DATACENTER --token TOKEN
Get-Service | Where-Object DisplayName -like 'Acronis*'
```

## See also

[[Datto Endpoint Backup]] · [[VSS]] · [[Agent offline]] · [[Backup job failed]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
