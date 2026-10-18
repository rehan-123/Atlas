---
type: "moc"
level: "All"
tags:
  - "moc"
  - "networking"
created: "2026-10-18"
updated: "2026-10-18"
---

# Networking

Firewalls, switches, wireless, WAN and the services that make IP work.

Back to [[Home]].

> [!note]- How seniors think about this area
> - Design for segmentation and least access between zones from the start; retrofitting is painful.
> - Keep config backups and change logs for every network device; most outages follow a change.
> - Dual WAN with tested failover for sites that can't go down; monitor the failover link too.
> - Document IP plans, VLANs and ISP circuits before you need them during an outage.

## [[Firewalls]]

A firewall is the security guard at the edge of the network, deciding what traffic is allowed in and out. It often also handles the VPN and internet links.

- [[FortiGate]]
- [[Palo Alto Networks NGFW]]
- [[Cisco Secure Firewall]]
- [[SonicWall]]
- [[WatchGuard Firebox]]
- [[Sophos Firewall]]
- [[Check Point]]
- [[pfSense]]
- [[OPNsense]]
- [[Meraki MX]]

## [[Switching & routing]]

Switches connect devices inside a building; routers connect different networks together.

- [[Cisco Catalyst]]
- [[Meraki MS]]
- [[HPE Aruba Networking]]
- [[Juniper Networks]]
- [[MikroTik]]
- [[Extreme Networks]]

## [[Wireless]]

Wi-Fi access points and the systems that manage them.

- [[Meraki MR]]
- [[Ubiquiti UniFi]]
- [[Ruckus]]
- [[Juniper Mist]]

## [[SD-WAN]]

SD-WAN lets a site use several internet links at once and automatically moves traffic to the best one when a link is slow or down.

- [[VeloCloud]]
- [[Cisco Catalyst SD-WAN]]

## [[VPN]]

A VPN creates an encrypted tunnel over the internet, so a remote user or branch office can reach the office network safely.

- [[WireGuard]]
- [[OpenVPN]]
- [[Cisco Secure Client]]
- [[GlobalProtect]]
- [[FortiClient]]

## [[Load balancers]]

A load balancer spreads incoming traffic across several servers, so one busy or failed server doesn't take a service down.

- [[F5 BIG-IP]]
- [[NetScaler ADC]]
- [[HAProxy]]
- [[Kemp LoadMaster]]

## [[DNS & IPAM]]

These tools manage domain names (DNS) and keep track of which IP addresses are in use.

- [[Infoblox]]
- [[Cloudflare DNS]]
- [[Amazon Route 53]]

## Playbooks for this area

[[Broadcast storm or network loop]] · [[Firewall WAN down]] · [[Interface errors and packet loss]] · [[VPN tunnel down]]

## Database view

```dataview
TABLE vendor, subcategory, deployment, status, agent_service AS "Agent"
FROM "09 Networking"
WHERE type = "tool"
SORT subcategory ASC, file.name ASC
```
