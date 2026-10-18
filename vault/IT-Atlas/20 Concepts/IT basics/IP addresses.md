---
type: "concept"
level: "Junior"
category: "[[IT basics]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# IP addresses

> [!abstract] In one line
> The number every device needs to talk on a network, like a phone number.

> [!tip] Think of it like
> Phone numbers for computers. The gateway is the switchboard that connects calls outside the building.

> [!info]+ Words on this page
> **DHCP**: The service that hands out IP addresses to devices automatically.
> *More in the [[Glossary]].*

## How it works

- Looks like `192.168.1.25`. The **gateway** (often ending .1 or .254) is the way out of the local network.
- Private addresses (192.168.x.x, 10.x.x.x, 172.16-31.x.x) are used inside offices and homes.
- `ipconfig` (Windows) or `ifconfig` (Mac) shows your address.
- 169.254.x.x means the device couldn't get an address from DHCP.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- What does `ipconfig /all` tell you?
> The PC's IP address, subnet mask, gateway, DNS servers and whether DHCP is on.

## See also

[[How the internet reaches your desk]] · [[Subnetting & CIDR]] · [[DHCP]] · [[Printer offline]]
