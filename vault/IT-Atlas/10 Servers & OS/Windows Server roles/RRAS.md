---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Windows Server roles]]"
vendor: "[[Microsoft]]"
deployment:
status: "current"
agent_service: "RemoteAccess"
aliases:
  - "Routing and Remote Access"
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# RRAS

> [!abstract] In plain words
> Routing and Remote Access Service: the Windows Server role that provides VPN, NAT and basic routing.
>
> **What kind of tool is this?** Roles are the jobs a Windows server can do: hand out IP addresses, host files, run remote desktops and so on.

**Made by:** [[Microsoft]] · **Category:** [[Servers & Operating Systems]] › [[Windows Server roles]]

> [!info]+ Words on this page
> **VPN**: An encrypted tunnel over the internet to a private network.
> **NAT**: Network address translation: many private devices sharing one public IP.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **LAN**: Local area network: the network inside a building.
> *More in the [[Glossary]].*

## In more detail

Remote Access role providing SSTP/IKEv2 VPN (including Always On VPN gateways), NAT and LAN routing.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`RemoteAccess`

## See also

[[Always On VPN]] · [[VPN]] · [[NPS]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
