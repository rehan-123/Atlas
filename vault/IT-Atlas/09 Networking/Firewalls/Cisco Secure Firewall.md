---
type: "tool"
level: "Mid"
category: "[[Networking]]"
subcategory: "[[Firewalls]]"
vendor: "[[Cisco]]"
deployment: "Appliance or VM"
status: "current"
aliases:
  - "Cisco ASA"
  - "Firepower"
  - "FTD"
  - "ASA"
tags:
  - "tool"
  - "networking"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Cisco Secure Firewall

> [!abstract] In plain words
> Cisco's firewall family, including the older ASA.
>
> **What kind of tool is this?** A firewall is the security guard at the edge of the network, deciding what traffic is allowed in and out. It often also handles the VPN and internet links.

**Made by:** [[Cisco]] · **Runs:** Appliance or VM · **Category:** [[Networking]] › [[Firewalls]]

> [!info]+ Words on this page
> **VPN**: An encrypted tunnel over the internet to a private network.
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **appliance**: A dedicated box (or virtual machine) built to do one job, such as backup or firewall.
> *More in the [[Glossary]].*

## In more detail

Cisco's firewall family: the classic ASA software and Firepower Threat Defense (FTD), managed by FMC, FDM or Security Cloud Control.

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
show interface ip brief
show failover
show crypto ikev2 sa
show crypto ipsec sa
show conn count
packet-tracer input inside tcp 10.0.0.10 12345 8.8.8.8 443
```

## See also

[[Cisco Catalyst]] · [[Cisco Secure Client]] · [[IPsec]] · [[VPN tunnel down]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
