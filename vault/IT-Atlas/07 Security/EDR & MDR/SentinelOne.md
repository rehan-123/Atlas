---
type: "tool"
level: "Mid"
category: "[[Security]]"
subcategory: "[[EDR & MDR]]"
vendor: "[[SentinelOne]]"
deployment: "SaaS"
status: "current"
agent_service: "SentinelAgent"
aliases:
  - "SentinelOne Singularity"
  - "S1"
tags:
  - "tool"
  - "security"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# SentinelOne

> [!abstract] In plain words
> A modern security agent that detects attacks and can roll back damage such as encrypted files.
>
> **What kind of tool is this?** EDR is modern antivirus: it records what happens on each computer and can stop and undo attacks. MDR adds a team of security people who watch it 24x7.

**Made by:** [[SentinelOne]] · **Runs:** SaaS · **Category:** [[Security]] › [[EDR & MDR]]

> [!info]+ Words on this page
> **EDR**: Endpoint detection and response: modern antivirus that records activity and can stop and undo attacks.
> **MDR**: Managed detection and response: a security team watching your EDR 24x7.
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **XDR**: Extended detection and response: EDR that also watches email, identity and cloud.
> **VSS**: Volume Shadow Copy Service: takes consistent snapshots of in-use files for backups.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **snapshot**: A saved point in time of a VM or disk. Not a backup, and it grows the longer you keep it.
> *More in the [[Glossary]].*

## In more detail

Autonomous EDR/XDR agent (Singularity) with behavioural detection, one-click remediation and Windows rollback using VSS snapshots. Vigilance is its MDR service.

## Main parts

- Singularity agent
- Management console (sites and groups)
- Storyline (attack chain view)
- Remediate and rollback
- Deep Visibility hunting

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`SentinelAgent`

## Alerts you'll see

- Threats (mitigated or not mitigated)
- Agents offline or out of date
- Agent in disabled or monitor mode

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Agent unhealthy | Run SentinelCtl.exe status from the agent install folder |
| Application blocked | Review the threat, then add a targeted exclusion if it is a confirmed false positive |

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
SentinelCtl.exe status
```

## See also

[[CrowdStrike Falcon]] · [[EDR threat detected]] · [[EDR vs MDR vs XDR]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
