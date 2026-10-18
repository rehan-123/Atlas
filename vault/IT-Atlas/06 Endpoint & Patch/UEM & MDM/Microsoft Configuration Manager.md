---
type: "tool"
level: "Mid"
category: "[[Endpoint & Patch Management]]"
subcategory: "[[UEM & MDM]]"
vendor: "[[Microsoft]]"
deployment: "On-prem"
status: "current"
aliases:
  - "SCCM"
  - "MECM"
  - "ConfigMgr"
tags:
  - "tool"
  - "endpoint"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Microsoft Configuration Manager

> [!abstract] In plain words
> Microsoft's on-site tool for managing Windows PCs (often called SCCM).
>
> **What kind of tool is this?** Device management tools enrol laptops and phones, push settings and apps to them, and check they meet security rules.

**Made by:** [[Microsoft]] · **Runs:** On-prem · **Category:** [[Endpoint & Patch Management]] › [[UEM & MDM]]

> [!info]+ Words on this page
> **UEM**: Unified endpoint management: managing all kinds of devices from one tool.
> **MDM**: Mobile device management: enrolling and controlling phones and laptops.
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> *More in the [[Glossary]].*

## In more detail

On-prem Windows management (SCCM/MECM): software and update deployment, OS deployment, inventory and compliance. Often co-managed with Intune.

## Main parts

- Site server and site database
- Distribution points
- Software update point (uses WSUS)
- Configuration Manager client

## Where to find its logs

- `C:\Windows\CCM\Logs (client)`
- Site server logs in the installation folder's Logs directory

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
CMTrace.exe to read logs
```

## See also

[[WSUS]] · [[Microsoft Intune]] · [[Patch My PC]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
