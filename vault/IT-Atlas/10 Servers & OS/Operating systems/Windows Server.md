---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Operating systems]]"
vendor: "[[Microsoft]]"
deployment: "On-prem or cloud"
status: "current"
aliases:
  - "Windows Server 2016"
  - "Windows Server 2019"
  - "Windows Server 2022"
  - "Windows Server 2025"
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Windows Server

> [!abstract] In plain words
> Microsoft's server operating system. Always check whether a server's version is still supported.
>
> **What kind of tool is this?** The operating systems you'll support: Windows Server, Windows 10 and 11, Linux and macOS.

**Made by:** [[Microsoft]] · **Runs:** On-prem or cloud · **Category:** [[Servers & Operating Systems]] › [[Operating systems]]

> [!info]+ Words on this page
> **CPU**: The processor, the part of a computer that does the calculations.
> **threshold**: The value that triggers an alert.
> *More in the [[Glossary]].*

## In more detail

Microsoft's server OS. Check every server's version against its support lifecycle; unsupported servers stop getting security updates.

## Alerts you'll see

- Unexpected reboots (events 41 and 6008)
- Disk, CPU and memory thresholds
- Service failures
- Pending reboot
- Unsupported OS version

## Where to find its logs

- Event Viewer: System, Application, Security
- `C:\Windows\Logs\CBS\CBS.log`

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-ComputerInfo | Select-Object OsName, OsVersion, OsLastBootUpTime
Get-WinEvent -FilterHashtable @{LogName='System'; Level=1,2; StartTime=(Get-Date).AddDays(-1)}
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 5
```

## See also

[[Windows client]] · [[Product lifecycle dates]] · [[Windows Event ID reference]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
