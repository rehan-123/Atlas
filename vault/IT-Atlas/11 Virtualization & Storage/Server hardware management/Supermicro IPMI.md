---
type: "tool"
level: "Mid"
category: "[[Virtualization & Storage]]"
subcategory: "[[Server hardware management]]"
vendor: "[[Supermicro]]"
deployment: "Out-of-band controller"
status: "current"
aliases:
  - "IPMI"
  - "BMC"
tags:
  - "tool"
  - "virtualization"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Supermicro IPMI

> [!abstract] In plain words
> The management chip in Supermicro servers.
>
> **What kind of tool is this?** Out-of-band controllers are tiny computers inside a server that let you see its health and console even when Windows is down.

**Made by:** [[Supermicro]] · **Runs:** Out-of-band controller · **Category:** [[Virtualization & Storage]] › [[Server hardware management]]

> [!info]+ Words on this page
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **VLAN**: A virtual network that separates traffic on the same physical switches.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Supermicro's BMC with IPMI and Redfish. ipmitool reads its event log and sensors.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 623/UDP IPMI

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
ipmitool sel list
ipmitool sensor list
ipmitool chassis status
```

## Good to know

- Never expose BMCs to the internet; keep them on a management VLAN.

## See also

[[Hardware RAID controllers]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
