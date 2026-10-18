---
type: "tool"
level: "Mid"
category: "[[Networking]]"
subcategory: "[[VPN]]"
vendor:
deployment: "Built into Linux; clients for all platforms"
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

# WireGuard

> [!abstract] In plain words
> A modern, simple and fast VPN.
>
> **What kind of tool is this?** A VPN creates an encrypted tunnel over the internet, so a remote user or branch office can reach the office network safely.

**Runs:** Built into Linux; clients for all platforms · **Category:** [[Networking]] › [[VPN]]

> [!info]+ Words on this page
> **VPN**: An encrypted tunnel over the internet to a private network.
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **tunnel**: An encrypted connection that carries traffic across another network.
> **branch**: A separate line of changes in Git, merged back into main after review.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Modern, minimal VPN protocol using public keys and UDP. Built into Linux and used under Tailscale, Twingate-style products and many firewalls.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 51820/UDP default

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
wg show
```

## See also

[[OpenVPN]] · [[IPsec]] · [[VPN tunnel down]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
