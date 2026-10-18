---
type: "concept"
level: "Mid"
category: "[[Networking concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# MTU

> [!abstract] In one line
> Maximum transmission unit: the largest packet a link carries without fragmenting (1500 bytes on Ethernet).

> [!tip] Think of it like
> MTU is the biggest box that fits through the door. Tunnels shrink the door, so big boxes get stuck.

> [!info]+ Words on this page
> **IPsec**: A set of protocols for encrypted VPN tunnels.
> **tunnel**: An encrypted connection that carries traffic across another network.
> *More in the [[Glossary]].*

## How it works

- Tunnels (IPsec, GRE, PPPoE) add overhead, so the effective MTU drops. Symptoms: small things work, large transfers or some websites hang.
- Test: `ping -f -l 1472 host` on Windows (1472 + 28 bytes of headers = 1500). Lower the size until it passes.
- Fix with MSS clamping on the firewall or a lower MTU on the tunnel interface.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Over a VPN, small pages load but big downloads hang. What's a likely cause?
> An MTU problem; fix it with MSS clamping or a lower MTU on the tunnel.

## See also

[[IPsec]] · [[OSPF]]
