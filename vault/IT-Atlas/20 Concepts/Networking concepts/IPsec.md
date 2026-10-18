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

# IPsec

> [!abstract] In one line
> The standard suite for encrypted site-to-site and many remote-access VPNs.

> [!tip] Think of it like
> IPsec builds an armoured tunnel between two sites. First both ends prove who they are (phase 1), then they agree what traffic goes through (phase 2).

> [!info]+ Words on this page
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **NAT**: Network address translation: many private devices sharing one public IP.
> **VPN**: An encrypted tunnel over the internet to a private network.
> **subnet**: A range of IP addresses that form one network segment.
> **tunnel**: An encrypted connection that carries traffic across another network.
> *More in the [[Glossary]].*

## How it works

- Phase 1 (IKE SA, UDP 500, or 4500 with NAT traversal) authenticates the peers. Phase 2 (IPsec SAs, ESP) carries traffic for the defined subnets.
- Tunnels fail on mismatches: proposals (encryption, hash, DH group), pre-shared key, lifetimes, or local and remote subnets.
- "Phase 1 up, no traffic" usually means a phase 2 selector mismatch, a missing route or policy, or NAT applied to VPN traffic.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- A site-to-site VPN shows phase 1 up but no traffic passes. What do you check?
> Phase 2: the subnets and proposals must match on both ends. Also check routes, firewall policies and that no NAT is applied to VPN traffic.

## See also

[[VPN tunnel down]] · [[FortiGate]] · [[Palo Alto Networks NGFW]] · [[Cisco Secure Firewall]] · [[WireGuard]]
