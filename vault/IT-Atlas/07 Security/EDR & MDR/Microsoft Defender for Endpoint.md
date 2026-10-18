---
type: "tool"
level: "Mid"
category: "[[Security]]"
subcategory: "[[EDR & MDR]]"
vendor: "[[Microsoft]]"
deployment: "Cloud with built-in Windows sensor"
status: "current"
aliases:
  - "MDE"
  - "Defender for Business"
  - "Microsoft Defender Antivirus"
tags:
  - "tool"
  - "security"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Microsoft Defender for Endpoint

> [!abstract] In plain words
> Microsoft's security product built into Windows. It is the antivirus plus attack detection and response, managed from the Defender portal.
>
> **What kind of tool is this?** EDR is modern antivirus: it records what happens on each computer and can stop and undo attacks. MDR adds a team of security people who watch it 24x7.

**Made by:** [[Microsoft]] · **Runs:** Cloud with built-in Windows sensor · **Category:** [[Security]] › [[EDR & MDR]]

> [!info]+ Words on this page
> **EDR**: Endpoint detection and response: modern antivirus that records activity and can stop and undo attacks.
> **MDR**: Managed detection and response: a security team watching your EDR 24x7.
> **KQL**: Kusto Query Language, used to search logs in Sentinel, Defender and Azure Monitor.
> **SMB**: The Windows file-sharing protocol (port 445).
> **GPO**: Group Policy Object: a bundle of settings pushed to Windows computers and users.
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> **vulnerability**: A weakness an attacker can use.
> **onboarding**: Setting up a new starter's accounts, access and devices.
> *More in the [[Glossary]].*

## In more detail

Microsoft's EDR built into Windows: Defender Antivirus, attack surface reduction, EDR with Live Response and Advanced Hunting (KQL). Defender for Business is the SMB edition.

## Main parts

- Microsoft Defender Antivirus
- EDR sensor (SENSE service)
- Attack surface reduction rules
- Automated investigation and response
- Live Response
- Advanced Hunting (KQL)
- Defender Vulnerability Management

## Alerts you'll see

- Alerts and incidents in the Defender portal
- Devices with outdated signatures or impaired sensor
- Tamper protection disabled

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Sensor not reporting | Check the SENSE service and onboarding state; confirm proxy access to Defender URLs |
| Real-time protection off | Get-MpComputerStatus; look for a third-party AV registered or a GPO turning it off |

## Where to find its logs

- Event Viewer: Microsoft > Windows > Windows Defender > Operational

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-MpComputerStatus
Update-MpSignature
Get-MpThreatDetection
```

## See also

[[Microsoft Sentinel]] · [[Microsoft Intune]] · [[EDR threat detected]] · [[EDR vs MDR vs XDR]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
