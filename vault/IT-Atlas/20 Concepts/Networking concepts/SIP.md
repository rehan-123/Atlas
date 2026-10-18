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

# SIP

> [!abstract] In one line
> Session Initiation Protocol sets up VoIP calls; RTP carries the audio.

> [!tip] Think of it like
> SIP sets up the phone call (the dialling); RTP carries the actual voices.

> [!info]+ Words on this page
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **TCP**: A connection-based network protocol that confirms delivery.
> **TLS**: The encryption behind HTTPS and many other secure connections.
> **NAT**: Network address translation: many private devices sharing one public IP.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **jitter**: How much delay varies from packet to packet. Bad for voice and video.
> **latency**: Delay: how long data takes to get from A to B.
> **bandwidth**: How much data a link can carry per second.
> *More in the [[Glossary]].*

## How it works

- SIP on UDP or TCP 5060 (5061 with TLS). RTP on a wide UDP port range defined by the PBX.
- One-way audio is almost always NAT or firewall: SIP ALG rewriting packets, or RTP ports not allowed. Disable SIP ALG on most firewalls.
- Call quality depends on jitter, latency and loss, not just bandwidth.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- A caller can hear you but you can't hear them. What's the usual cause?
> NAT or firewall problems: often SIP ALG on the firewall, or the RTP ports being blocked.

## See also

[[3CX]] · [[Microsoft Teams Phone]] · [[NAT]] · [[QoS]] · [[Voice quality problems]]
