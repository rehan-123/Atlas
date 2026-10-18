---
type: "tool"
level: "Mid"
category: "[[Cloud & SaaS]]"
subcategory: "[[Public cloud]]"
vendor: "[[Microsoft]]"
deployment: "Cloud"
status: "current"
aliases:
  - "Azure"
tags:
  - "tool"
  - "cloud"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Microsoft Azure

> [!abstract] In plain words
> Microsoft's public cloud.
>
> **What kind of tool is this?** Public clouds rent out servers, storage and networking by the hour from huge data centers.

**Made by:** [[Microsoft]] · **Runs:** Cloud · **Category:** [[Cloud & SaaS]] › [[Public cloud]]

> [!info]+ Words on this page
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> *More in the [[Glossary]].*

## In more detail

Microsoft's public cloud: subscriptions and resource groups, VMs, virtual networks and NSGs, storage, plus Azure Monitor and Azure Arc for hybrid.

## Alerts you'll see

- VM availability and metrics
- Budget and cost alerts
- Service health incidents
- Backup and ASR job status

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Connect-AzAccount
Get-AzVM -Status
az login
az vm list -d -o table
```

## See also

[[Azure Monitor]] · [[Azure Arc]] · [[Azure Backup]] · [[Azure Virtual Desktop]] · [[Azure Blob Storage]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
