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

# DHCP

> [!abstract] In one line
> Hands out IP addresses and options (gateway, DNS, domain) to clients.

> [!tip] Think of it like
> DHCP is the receptionist who hands every new visitor a desk number (IP address) when they arrive, and takes it back when they leave.

> [!info]+ Words on this page
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **VLAN**: A virtual network that separates traffic on the same physical switches.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **Wi-Fi**: Wireless network connection using radio signals.
> **LAN**: Local area network: the network inside a building.
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **router**: Device that connects one network to another, such as the office to the internet.
> *More in the [[Glossary]].*

## How it works

- The DORA exchange: Discover, Offer, Request, Acknowledge. Clients use UDP 68, servers UDP 67.
- DHCP is broadcast, so other VLANs need an IP helper or DHCP relay on the router or firewall.
- A 169.254.x.x address means no lease was obtained.
- Lease time matters: short leases on guest Wi-Fi, longer on wired LANs. Exhausted scopes are often caused by long leases on busy guest networks.
- Rogue DHCP servers (a consumer router plugged in backwards) hand out wrong gateways. DHCP snooping on switches prevents this.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- What are the four DHCP steps?
> Discover, Offer, Request, Acknowledge (DORA).

> [!question]- Phones on a new VLAN get no address, but PCs on the main VLAN do. What's the likely cause?
> The new VLAN has no DHCP relay (IP helper) pointing at the DHCP server, or no scope exists for it.

## See also

[[Windows DHCP Server]] · [[DHCP scope exhausted]] · [[VLAN]]
