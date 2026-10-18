---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Windows Server roles]]"
vendor: "[[Microsoft]]"
deployment:
status: "current"
agent_service: "WDSServer"
aliases:
  - "WDS"
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Windows Deployment Services

> [!abstract] In plain words
> A Windows Server role that lets new PCs start from the network (PXE) and install Windows.
>
> **What kind of tool is this?** Roles are the jobs a Windows server can do: hand out IP addresses, host files, run remote desktops and so on.

**Made by:** [[Microsoft]] · **Category:** [[Servers & Operating Systems]] › [[Windows Server roles]]

> [!info]+ Words on this page
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **Autopilot**: Windows Autopilot: sets up a new company laptop automatically when the user first signs in.
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **DHCP**: The service that hands out IP addresses to devices automatically.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

PXE boot and network image deployment; often paired with MDT or Configuration Manager; being replaced by cloud provisioning like Autopilot.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`WDSServer`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 67/UDP, 69/UDP TFTP, 4011/UDP (PXE)

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| PXE boot times out | Check DHCP options or IP helpers point to the WDS server, and the WDS service is running |

## See also

[[Windows Autopilot]] · [[Microsoft Configuration Manager]] · [[DHCP]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
