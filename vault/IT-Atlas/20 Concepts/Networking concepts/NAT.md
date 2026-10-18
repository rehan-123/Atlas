---
type: "concept"
level: "Junior"
category: "[[Networking concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# NAT

> [!abstract] In one line
> Network Address Translation: rewriting IP addresses as traffic crosses a device.

> [!tip] Think of it like
> NAT is the company receptionist: everyone inside shares one public phone number (IP), and the receptionist forwards calls to the right desk.

> [!info]+ Words on this page
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **ZTNA**: Zero-trust network access: app-by-app access with checks on every connection, replacing a broad VPN.
> **ISP**: Internet service provider.
> **VPN**: An encrypted tunnel over the internet to a private network.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **proxy**: A middleman server that passes traffic on, for web filtering or to do work for a central server.
> **router**: Device that connects one network to another, such as the office to the internet.
> *More in the [[Glossary]].*

## How it works

- Source NAT (PAT) lets many private hosts share one public IP.
- Destination NAT (port forwarding) publishes an inside service. Every port forward is attack surface; prefer a reverse proxy or ZTNA.
- Double NAT (ISP router plus your firewall) breaks VPNs, VoIP and inbound services. Put the ISP device in bridge mode.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why should you avoid port-forwarding RDP to a server?
> It exposes RDP to the whole internet, where it gets brute-forced. Use a VPN, RD Gateway or ZTNA instead.

## See also

[[Subnetting & CIDR]] · [[IPsec]] · [[SIP]]
