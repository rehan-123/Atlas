---
type: "tool"
level: "Mid"
category: "[[Endpoint & Patch Management]]"
subcategory: "[[UEM & MDM]]"
vendor: "[[Microsoft]]"
deployment: "Cloud"
status: "current"
aliases:
  - "Intune"
  - "Endpoint Manager"
tags:
  - "tool"
  - "endpoint"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Microsoft Intune

> [!abstract] In plain words
> Microsoft's cloud tool for managing laptops and phones: it enrols devices, pushes settings and apps, and checks they're compliant.
>
> **What kind of tool is this?** Device management tools enrol laptops and phones, push settings and apps to them, and check they meet security rules.

**Made by:** [[Microsoft]] · **Runs:** Cloud · **Category:** [[Endpoint & Patch Management]] › [[UEM & MDM]]

> [!info]+ Words on this page
> **UEM**: Unified endpoint management: managing all kinds of devices from one tool.
> **MDM**: Mobile device management: enrolling and controlling phones and laptops.
> **Autopilot**: Windows Autopilot: sets up a new company laptop automatically when the user first signs in.
> **Conditional Access**: Microsoft Entra rules that allow or block sign-ins based on user, device, location and risk.
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> *More in the [[Glossary]].*

## In more detail

Microsoft's cloud UEM: enrollment, compliance and configuration policies, app deployment, Windows Update rings and Autopilot for Windows, macOS, iOS and Android.

## Main parts

- Enrollment (Autopilot, automatic enrollment, Apple ADE)
- Compliance policies feeding Conditional Access
- Configuration profiles and settings catalog
- Apps (Win32 .intunewin, Microsoft Store, LOB)
- Intune Management Extension for scripts and Win32 apps
- Update rings and feature update policies

## Alerts you'll see

- Non-compliant devices
- App install failures
- Devices not checked in
- Enrollment failures

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Win32 app fails | Read IntuneManagementExtension.log and AgentExecutor.log; check detection rules |
| Device not enrolling | Run dsregcmd /status for join state and check the enrollment restrictions |
| Policy not applying | Check assignment groups, filters and conflicts in the device's configuration status |

## Where to find its logs

- `C:\ProgramData\Microsoft\IntuneManagementExtension\Logs`
- Event Viewer: Microsoft > Windows > DeviceManagement-Enterprise-Diagnostics-Provider

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
dsregcmd /status
mdmdiagnosticstool.exe -out C:\Temp\MDMDiag
```

## See also

[[Windows Autopilot]] · [[Microsoft Entra ID]] · [[Windows Update for Business]] · [[Jamf Pro]] · [[Patch My PC]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
