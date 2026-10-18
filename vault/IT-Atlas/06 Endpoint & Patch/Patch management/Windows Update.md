---
type: "tool"
level: "Mid"
category: "[[Endpoint & Patch Management]]"
subcategory: "[[Patch management]]"
vendor: "[[Microsoft]]"
deployment: "Built into Windows"
status: "current"
agent_service: "wuauserv, BITS, TrustedInstaller"
aliases: []
tags:
  - "tool"
  - "endpoint"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Windows Update

> [!abstract] In plain words
> The built-in Windows service that downloads and installs updates. When patching fails, the cause is usually here.
>
> **What kind of tool is this?** Patching means installing updates, mostly security fixes. These tools decide what gets installed, when, and report what's missing.

**Made by:** [[Microsoft]] · **Runs:** Built into Windows · **Category:** [[Endpoint & Patch Management]] › [[Patch management]]

> [!info]+ Words on this page
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> **cache**: Saved copies of data kept to make things faster. Can go stale and cause odd problems.
> **registry**: Windows' central settings database.
> *More in the [[Glossary]].*

## In more detail

The Windows update client and services. Whatever tool you patch with, failures usually end up here.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`wuauserv, BITS, TrustedInstaller`

## Alerts you'll see

- Updates failing with an error code
- Pending reboot
- Update services disabled

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Updates fail repeatedly | Note the error code, run DISM /RestoreHealth and SFC, then reset the update cache |
| Machine stuck pending reboot | Check the pending reboot registry keys and schedule a reboot |
| Disk full during updates | Clean up WinSxS with DISM component cleanup and remove old update caches |

## Where to find its logs

- Get-WindowsUpdateLog (builds WindowsUpdate.log from ETW traces)
- `C:\Windows\Logs\CBS\CBS.log`
- System log, source WindowsUpdateClient (event 19 installed, 20 failed)

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-WindowsUpdateLog
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
net stop wuauserv & net stop bits & ren C:\Windows\SoftwareDistribution SoftwareDistribution.old & net start bits & net start wuauserv
DISM /Online /Cleanup-Image /StartComponentCleanup
```

## See also

[[WSUS]] · [[Windows Update for Business]] · [[Patch failure or pending reboot]] · [[Patch Tuesday]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
