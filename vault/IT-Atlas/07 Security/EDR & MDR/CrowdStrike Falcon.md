---
type: "tool"
level: "Mid"
category: "[[Security]]"
subcategory: "[[EDR & MDR]]"
vendor: "[[CrowdStrike]]"
deployment: "SaaS"
status: "current"
agent_service: "CSFalconService"
aliases: []
tags:
  - "tool"
  - "security"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# CrowdStrike Falcon

> [!abstract] In plain words
> A widely used security agent. Famous for a faulty update in July 2024 that crashed millions of Windows PCs worldwide.
>
> **What kind of tool is this?** EDR is modern antivirus: it records what happens on each computer and can stop and undo attacks. MDR adds a team of security people who watch it 24x7.

**Made by:** [[CrowdStrike]] · **Runs:** SaaS · **Category:** [[Security]] › [[EDR & MDR]]

> [!info]+ Words on this page
> **EDR**: Endpoint detection and response: modern antivirus that records activity and can stop and undo attacks.
> **MDR**: Managed detection and response: a security team watching your EDR 24x7.
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **XDR**: Extended detection and response: EDR that also watches email, identity and cloud.
> **BSOD**: Blue screen of death: Windows crashed.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **safe mode**: A way to start Windows or an app with only the basics, to find what's causing a problem.
> *More in the [[Glossary]].*

## In more detail

Cloud-native EDR/XDR with a lightweight sensor, threat intelligence and the Falcon Complete MDR service.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`CSFalconService`

## Alerts you'll see

- Detections and incidents
- Sensors in reduced functionality mode
- Sensors not seen recently

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
sc query csagent
```

## Good to know

- 19 July 2024: a faulty Falcon channel file (291) crashed about 8.5 million Windows machines into BSOD loops. Recovery meant booting to safe mode or WinRE to delete the file, slowed down where BitLocker recovery keys were not to hand.

## See also

[[SentinelOne]] · [[BitLocker]] · [[EDR threat detected]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
