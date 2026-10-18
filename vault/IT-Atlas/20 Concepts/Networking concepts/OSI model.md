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

# OSI model

> [!abstract] In one line
> Seven-layer model used to describe where a network problem lives.

> [!tip] Think of it like
> Like the layers of sending a parcel: the box (data), the label (addresses), the van (cables). When something breaks, you work out which layer failed.

> [!info]+ Words on this page
> **NOC**: Network operations center: the team that monitors and fixes infrastructure.
> **HTTP**: The protocol web pages use (port 80, unencrypted).
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **TLS**: The encryption behind HTTPS and many other secure connections.
> **RPC**: Remote procedure call: how Windows machines ask each other to do things (uses port 135 and high ports).
> **SMB**: The Windows file-sharing protocol (port 445).
> **TCP**: A connection-based network protocol that confirms delivery.
> **UDP**: A fast network protocol that doesn't confirm delivery.
> *More in the [[Glossary]].*

## How it works

| Layer | Name | Examples | NOC question |
|---|---|---|---|
| 7 | Application | HTTP, DNS, SMTP | Does the service answer correctly? |
| 6 | Presentation | TLS, encoding | Certificate or cipher problem? |
| 5 | Session | RPC, SMB sessions | Session established? |
| 4 | Transport | TCP, UDP | Port open? |
| 3 | Network | IP, ICMP, routing | Can I ping it? Right route? |
| 2 | Data link | Ethernet, VLANs, ARP | Right VLAN? MAC learned? |
| 1 | Physical | Cables, optics, Wi-Fi radio | Link up? Errors on the port? |

Troubleshoot bottom-up when nothing works, and top-down when one app is broken but everything else works.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- A user can ping a server but its website won't load. Which layers are probably fine?
> Layers 1 to 3 (cable, local network and IP) work, because ping succeeds. Look higher: is the port open (layer 4), or is the app or its certificate failing (layer 7)?

## See also

[[TCP and UDP]] · [[ICMP]] · [[VLAN]] · [[DNS]]
