---
type: "tool"
level: "Mid"
category: "[[Security]]"
subcategory: "[[Application control]]"
vendor: "[[Microsoft]]"
deployment:
status: "current"
agent_service: "AppIDSvc"
aliases: []
tags:
  - "tool"
  - "security"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# AppLocker

> [!abstract] In plain words
> A Windows feature that only lets approved programs run, using rules by publisher, path or file hash.
>
> **What kind of tool is this?** Application control only lets approved programs run, so unknown or malicious software is blocked by default.

**Made by:** [[Microsoft]] · **Category:** [[Security]] › [[Application control]]

## In more detail

Windows application allowlisting by publisher, path or hash, managed by Group Policy; App Control for Business is the stronger successor.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`AppIDSvc`

## Where to find its logs

- Event Viewer: Applications and Services Logs > Microsoft > Windows > AppLocker

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-AppLockerPolicy -Effective -Xml
Get-WinEvent -LogName 'Microsoft-Windows-AppLocker/EXE and DLL' -MaxEvents 20
```

## See also

[[App Control for Business]] · [[ThreatLocker]] · [[Group Policy]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
