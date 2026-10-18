---
type: "reference"
level: "All"
tags:
  - "reference"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Network device command cheat sheet

Equivalent first-look commands on common network platforms.

| Task | Cisco IOS-XE | FortiGate | PAN-OS | Junos |
|---|---|---|---|---|
| Version | `show version` | `get system status` | `show system info` | `show version` |
| Interfaces | `show ip interface brief` | `get system interface physical` | `show interface all` | `show interfaces terse` |
| Routes | `show ip route` | `get router info routing-table all` | `show routing route` | `show route` |
| Logs | `show logging` | `execute log display` | `show log system` | `show log messages` |
| ARP | `show ip arp` | `get system arp` | `show arp all` | `show arp` |
| VPN | `show crypto ikev2 sa` | `get vpn ipsec tunnel summary` | `show vpn ike-sa` | `show security ike security-associations` |
| HA | `show redundancy` | `get system ha status` | `show high-availability state` | `show chassis cluster status` |
| Sessions | `show ip nat translations` | `diagnose sys session list` | `show session all` | `show security flow session` |
| Packet trace | `packet-tracer` (ASA) | `diagnose debug flow` | `test security-policy-match` | `show security match-policies` |
