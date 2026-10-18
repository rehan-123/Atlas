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

# Subnetting & CIDR

> [!abstract] In one line
> How IP ranges are written and split.

> [!tip] Think of it like
> A subnet is a street; the IP address is the house number on it. /24 means a street with 256 house numbers.

> [!info]+ Words on this page
> **DHCP**: The service that hands out IP addresses to devices automatically.
> **NAT**: Network address translation: many private devices sharing one public IP.
> **ISP**: Internet service provider.
> **VPN**: An encrypted tunnel over the internet to a private network.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **subnet**: A range of IP addresses that form one network segment.
> *More in the [[Glossary]].*

## How it works

- `/24` = 255.255.255.0 = 256 addresses (254 usable). `/23` = 512. `/25` = 128. `/30` = 4 (2 usable, point-to-point links).
- Private ranges (RFC 1918): 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16.
- 169.254.0.0/16 (APIPA) means the machine did not get a DHCP lease.
- 100.64.0.0/10 is carrier-grade NAT: an ISP is doing NAT in front of you, so inbound port forwards will not work.
- Overlapping subnets between sites break site-to-site VPNs. Check before connecting two networks.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- A PC has the address 169.254.10.5. What does that tell you?
> It didn't get an address from DHCP, so it gave itself one. Check DHCP and the network connection.

> [!question]- How many usable addresses are in a /24?
> 254 (256 minus the network address and the broadcast address).

## See also

[[DHCP]] · [[NAT]] · [[IPsec]]
