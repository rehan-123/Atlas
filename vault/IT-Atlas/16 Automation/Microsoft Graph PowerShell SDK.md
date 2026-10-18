---
type: "tool"
level: "Mid"
category: "[[Automation & Scripting]]"
vendor: "[[Microsoft]]"
deployment:
status: "current"
aliases:
  - "Microsoft.Graph"
  - "Graph PowerShell"
tags:
  - "tool"
  - "automation"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Microsoft Graph PowerShell SDK

> [!abstract] In plain words
> The PowerShell modules for managing Microsoft 365 and Entra ID through Microsoft Graph; they replace the retired AzureAD and MSOnline modules.
>
> **What kind of tool is this?** Scripting and automation tools let you do a task once in code and then repeat it on hundreds of machines.

**Made by:** [[Microsoft]] · **Category:** [[Automation & Scripting]]

> [!info]+ Words on this page
> **API**: A way for programs and scripts to talk to a service directly, without the web page.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> *More in the [[Glossary]].*

## In more detail

Microsoft.Graph modules: Connect-MgGraph with delegated scopes or app-only certificate auth; cmdlets map to Graph API endpoints.

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Install-Module Microsoft.Graph -Scope CurrentUser
Connect-MgGraph -Scopes 'User.Read.All','Group.Read.All'
Get-MgUser -UserId USER
Get-MgUserLicenseDetail -UserId USER
Find-MgGraphCommand -Uri '/users/{id}'
```

## Good to know

- Grant the fewest scopes you need; for unattended scripts use an app registration with a certificate, not a user account.

## See also

[[Microsoft Graph]] · [[PowerShell]] · [[Microsoft Entra ID]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
