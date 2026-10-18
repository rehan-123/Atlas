---
type: "tool"
level: "Mid"
category: "[[Networking]]"
subcategory: "[[Firewalls]]"
vendor: "[[Palo Alto Networks]]"
deployment: "Appliance, VM or cloud"
status: "current"
aliases:
  - "PAN-OS"
  - "Palo Alto firewall"
  - "PA-series"
tags:
  - "tool"
  - "networking"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Palo Alto Networks NGFW

> [!abstract] In plain words
> Palo Alto's firewall, common in larger companies. It recognises apps and users, not just ports.
>
> **What kind of tool is this?** A firewall is the security guard at the edge of the network, deciding what traffic is allowed in and out. It often also handles the VPN and internet links.

**Made by:** [[Palo Alto Networks]] · **Runs:** Appliance, VM or cloud · **Category:** [[Networking]] › [[Firewalls]]

> [!info]+ Words on this page
> **VPN**: An encrypted tunnel over the internet to a private network.
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **NAT**: Network address translation: many private devices sharing one public IP.
> **HA**: High availability: designed so one failure doesn't cause downtime.
> **CPU**: The processor, the part of a computer that does the calculations.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **appliance**: A dedicated box (or virtual machine) built to do one job, such as backup or firewall.
> **tunnel**: An encrypted connection that carries traffic across another network.
> *More in the [[Glossary]].*

## In more detail

Next-generation firewall running PAN-OS with App-ID, User-ID and Content-ID. Managed centrally with Panorama or Strata Cloud Manager; GlobalProtect for remote access.

## Main parts

- PAN-OS
- App-ID, User-ID and Content-ID
- Security and NAT policy
- GlobalProtect portal and gateway
- Panorama
- HA pairs

## Alerts you'll see

- HA state change
- Interface or tunnel down
- Dataplane CPU high
- GlobalProtect connection failures

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
show system info
show interface all
show high-availability state
show vpn ike-sa
show vpn ipsec-sa
show session all filter source 10.0.0.10
show running resource-monitor
```

## See also

[[GlobalProtect]] · [[Prisma Access]] · [[IPsec]] · [[VPN tunnel down]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
