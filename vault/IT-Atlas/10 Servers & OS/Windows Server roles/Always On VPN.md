---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Windows Server roles]]"
vendor: "[[Microsoft]]"
deployment:
status: "current"
aliases: []
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Always On VPN

> [!abstract] In plain words
> A Windows VPN that connects automatically before or after sign-in, so remote laptops act as if they're in the office.
>
> **What kind of tool is this?** Roles are the jobs a Windows server can do: hand out IP addresses, host files, run remote desktops and so on.

**Made by:** [[Microsoft]] · **Category:** [[Servers & Operating Systems]] › [[Windows Server roles]]

> [!info]+ Words on this page
> **VPN**: An encrypted tunnel over the internet to a private network.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **NAT**: Network address translation: many private devices sharing one public IP.
> **tunnel**: An encrypted connection that carries traffic across another network.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> *More in the [[Glossary]].*

## In more detail

Windows VPN profiles (device and user tunnels) deployed by Intune or ProfileXML, using IKEv2 or SSTP to RRAS or third-party gateways, usually with certificate authentication.

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Device tunnel won't connect | Check the machine certificate (from AD CS) is valid and the device tunnel uses IKEv2 |
| Error 809 | IKEv2 UDP 500/4500 blocked on the path, or fragmentation; check firewall and NAT |

## Where to find its logs

- Event Viewer: Application log, source RasClient

## See also

[[RRAS]] · [[AD CS]] · [[Microsoft Intune]] · [[VPN won't connect]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
