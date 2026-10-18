---
type: "moc"
level: "All"
tags:
  - "moc"
  - "networking"
created: "2026-10-18"
updated: "2026-10-18"
---

# Firewalls

> [!abstract] In plain words
> A firewall is the security guard at the edge of the network, deciding what traffic is allowed in and out. It often also handles the VPN and internet links.

Part of [[Networking]].

- [[FortiGate]]: Fortinet's firewall, very common at MSP clients. It also handles VPNs and switching between multiple internet links.
- [[Palo Alto Networks NGFW]]: Palo Alto's firewall, common in larger companies. It recognises apps and users, not just ports.
- [[Cisco Secure Firewall]]: Cisco's firewall family, including the older ASA.
- [[SonicWall]]: A firewall common in small and mid-sized businesses.
- [[WatchGuard Firebox]]: WatchGuard's firewall for small and mid-sized businesses.
- [[Sophos Firewall]]: Sophos' firewall, which works together with its antivirus.
- [[Check Point]]: An enterprise firewall vendor.
- [[pfSense]]: A free, open-source firewall you install on your own hardware.
- [[OPNsense]]: A free, open-source firewall, similar to pfSense.
- [[Meraki MX]]: Cisco Meraki's firewall, managed entirely from a web dashboard.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "09 Networking/Firewalls"
WHERE type = "tool"
SORT file.name ASC
```
