---
type: "tool"
level: "Mid"
category: "[[Virtualization & Storage]]"
subcategory: "[[VDI & app delivery]]"
vendor: "[[Microsoft]]"
deployment: "Azure"
status: "current"
aliases:
  - "AVD"
tags:
  - "tool"
  - "virtualization"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Azure Virtual Desktop

> [!abstract] In plain words
> Windows desktops that run in Azure, which users connect to from anywhere.
>
> **What kind of tool is this?** VDI gives users a desktop that actually runs in the data center or cloud, which they reach over the network.

**Made by:** [[Microsoft]] · **Runs:** Azure · **Category:** [[Virtualization & Storage]] › [[VDI & app delivery]]

> [!info]+ Words on this page
> **VDI**: Virtual desktop infrastructure: desktops that run on servers and are used remotely.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> **container**: A packaged app with everything it needs to run, sharing the host's operating system kernel.
> *More in the [[Glossary]].*

## In more detail

Microsoft's cloud VDI: host pools of Windows multi-session hosts in Azure, with FSLogix profiles on Azure Files or Azure NetApp Files.

## Main parts

- Host pools and session hosts
- Application groups and workspaces
- RD Agent and boot loader on hosts
- FSLogix profile containers
- Scaling plans

## Alerts you'll see

- Session host unavailable
- Profile load failures
- Hosts not scaling

## See also

[[FSLogix]] · [[RDS]] · [[Microsoft Azure]] · [[Windows 365]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
