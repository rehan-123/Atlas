---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Windows Server roles]]"
vendor: "[[Microsoft]]"
deployment: "Windows Server role"
status: "current"
aliases:
  - "Remote Desktop Gateway"
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# RD Gateway

> [!abstract] In plain words
> Lets users reach remote desktops safely over HTTPS from outside the office, instead of opening RDP to the internet.
>
> **What kind of tool is this?** Roles are the jobs a Windows server can do: hand out IP addresses, host files, run remote desktops and so on.

**Made by:** [[Microsoft]] · **Runs:** Windows Server role · **Category:** [[Servers & Operating Systems]] › [[Windows Server roles]]

> [!info]+ Words on this page
> **HTTPS**: Encrypted HTTP (port 443).
> **RDP**: Remote Desktop Protocol: Windows' built-in remote desktop, on port 3389.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
> **TCP**: A connection-based network protocol that confirms delivery.
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **tunnel**: An encrypted connection that carries traffic across another network.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Tunnels RDP over HTTPS so remote users can reach internal hosts without exposing 3389. Supports resource authorization policies and NPS-based MFA (for example the Entra MFA NPS extension or Duo).

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 443/TCP
- 3391/UDP (UDP transport)

## Alerts you'll see

- Certificate expiring
- Gateway service down

## See also

[[RDS]] · [[RDP]] · [[NPS]] · [[Duo Security]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
