---
type: "tool"
level: "Mid"
category: "[[Cloud & SaaS]]"
subcategory: "[[Public cloud]]"
vendor: "[[Microsoft]]"
deployment: "Agent on non-Azure servers"
status: "current"
agent_service: "himds (Azure Connected Machine Agent)"
aliases: []
tags:
  - "tool"
  - "cloud"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Azure Arc

> [!abstract] In plain words
> Lets you manage on-site servers from Azure, as if they were Azure VMs.
>
> **What kind of tool is this?** Public clouds rent out servers, storage and networking by the hour from huge data centers.

**Made by:** [[Microsoft]] · **Runs:** Agent on non-Azure servers · **Category:** [[Cloud & SaaS]] › [[Public cloud]]

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> *More in the [[Glossary]].*

## In more detail

Projects on-prem and other-cloud servers into Azure so they can use Azure Monitor, Update Manager, Defender and policy.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`himds (Azure Connected Machine Agent)`

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
azcmagent show
azcmagent check
```

## See also

[[Microsoft Azure]] · [[Azure Monitor]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
