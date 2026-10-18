---
type: "tool"
level: "Mid"
category: "[[Networking]]"
subcategory: "[[Wireless]]"
vendor: "[[Ubiquiti]]"
deployment: "Self-hosted controller, Cloud Gateway or cloud"
status: "current"
aliases:
  - "UniFi"
  - "UniFi Network"
tags:
  - "tool"
  - "networking"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Ubiquiti UniFi

> [!abstract] In plain words
> Popular, affordable Wi-Fi, switches and gateways, all managed from one UniFi app.
>
> **What kind of tool is this?** Wi-Fi access points and the systems that manage them.

**Made by:** [[Ubiquiti]] · **Runs:** Self-hosted controller, Cloud Gateway or cloud · **Category:** [[Networking]] › [[Wireless]]

> [!info]+ Words on this page
> **Wi-Fi**: Wireless network connection using radio signals.
> **TCP**: A connection-based network protocol that confirms delivery.
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **SSH**: Secure Shell: encrypted command-line login, mostly for Linux and network devices (port 22).
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Ubiquiti's UniFi ecosystem: access points, switches and gateways managed by the UniFi Network application on a Cloud Gateway, Cloud Key or self-hosted controller.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 8080/TCP device inform (adoption)
- 8443/TCP self-hosted controller UI
- 3478/UDP STUN

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Device won't adopt | Check it can reach the controller on 8080; use set-inform over SSH if discovery fails |

## See also

[[VLAN]] · [[Wireless]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
