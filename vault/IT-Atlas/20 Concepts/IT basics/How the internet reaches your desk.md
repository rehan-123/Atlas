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

# How the internet reaches your desk

> [!abstract] In one line
> From the internet provider, through the firewall and switches, to your Wi-Fi or cable.

> [!tip] Think of it like
> Water to your tap: the water company (ISP), the main valve (firewall), the pipes (switches) and the tap (Wi-Fi or cable).

> [!info]+ Words on this page
> **ISP**: Internet service provider.
> **Wi-Fi**: Wireless network connection using radio signals.
> **DHCP**: The service that hands out IP addresses to devices automatically.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **router**: Device that connects one network to another, such as the office to the internet.
> *More in the [[Glossary]].*

## How it works

- **Internet provider (ISP)** brings the line into the building.
- **Router or firewall** connects the office to the internet and blocks what shouldn't come in.
- **Switches** connect cables in the office; **access points** provide Wi-Fi.
- **DHCP** gives your PC an IP address; **DNS** turns names like microsoft.com into addresses.
- When something fails, work from your PC outwards: cable or Wi-Fi, then IP address, then gateway, then DNS, then internet.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- A PC shows an address starting 169.254. Which part of the chain failed?
> DHCP: the PC didn't get an address from the network.

## See also

[[IP addresses]] · [[Wi-Fi basics]] · [[DNS]] · [[DHCP]] · [[No internet]]
