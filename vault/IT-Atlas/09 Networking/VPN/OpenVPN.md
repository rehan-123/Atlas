---
type: "tool"
level: "Mid"
category: "[[Networking]]"
subcategory: "[[VPN]]"
vendor:
deployment: "Open source; Access Server and CloudConnexa are commercial"
status: "current"
aliases: []
tags:
  - "tool"
  - "networking"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# OpenVPN

> [!abstract] In plain words
> A long-standing open-source VPN.
>
> **What kind of tool is this?** A VPN creates an encrypted tunnel over the internet, so a remote user or branch office can reach the office network safely.

**Runs:** Open source; Access Server and CloudConnexa are commercial · **Category:** [[Networking]] › [[VPN]]

> [!info]+ Words on this page
> **VPN**: An encrypted tunnel over the internet to a private network.
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **TCP**: A connection-based network protocol that confirms delivery.
> **tunnel**: An encrypted connection that carries traffic across another network.
> **branch**: A separate line of changes in Git, merged back into main after review.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

TLS-based VPN, widely supported on firewalls such as pfSense.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 1194/UDP default (also often 443/TCP)

## See also

[[WireGuard]] · [[pfSense]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
