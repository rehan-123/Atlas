---
type: "tool"
level: "Mid"
category: "[[Security]]"
subcategory: "[[EDR & MDR]]"
vendor: "[[Huntress]]"
deployment: "SaaS"
status: "current"
agent_service: "HuntressAgent, HuntressUpdater"
aliases: []
tags:
  - "tool"
  - "security"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Huntress

> [!abstract] In plain words
> Security built for MSPs: a human security team watches Defender, Microsoft 365 sign-ins and logs, and tells you what to fix.
>
> **What kind of tool is this?** EDR is modern antivirus: it records what happens on each computer and can stop and undo attacks. MDR adds a team of security people who watch it 24x7.

**Made by:** [[Huntress]] · **Runs:** SaaS · **Category:** [[Security]] › [[EDR & MDR]]

> [!info]+ Words on this page
> **MSP**: Managed service provider: a company that runs IT for other companies.
> **EDR**: Endpoint detection and response: modern antivirus that records activity and can stop and undo attacks.
> **MDR**: Managed detection and response: a security team watching your EDR 24x7.
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **SMB**: The Windows file-sharing protocol (port 445).
> **SOC**: Security operations center: the team that watches for and responds to attacks.
> **SIEM**: A system that collects security logs from everywhere and looks for attacks.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> *More in the [[Glossary]].*

## In more detail

Managed security for SMBs and MSPs with a 24x7 human SOC: managed EDR (on top of Defender), identity threat detection for Microsoft 365, SIEM and security awareness training.

## Main parts

- Huntress agent
- Managed EDR with Defender integration
- Managed ITDR (Microsoft 365 sign-ins and mailbox rules)
- Managed SIEM
- Incident reports with remediation steps

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`HuntressAgent, HuntressUpdater`

## Alerts you'll see

- Incident reports requiring action
- Agents offline

## See also

[[Microsoft Defender for Endpoint]] · [[Microsoft 365]] · [[Suspected ransomware]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
