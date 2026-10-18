---
type: "moc"
level: "All"
tags:
  - "moc"
  - "networking"
created: "2026-10-18"
updated: "2026-10-18"
---

# Wireless

> [!abstract] In plain words
> Wi-Fi access points and the systems that manage them.

Part of [[Networking]].

- [[Meraki MR]]: Cisco Meraki's Wi-Fi access points.
- [[Ubiquiti UniFi]]: Popular, affordable Wi-Fi, switches and gateways, all managed from one UniFi app.
- [[Ruckus]]: Business Wi-Fi access points and switches, often used in hotels, schools and large venues.
- [[Juniper Mist]]: A cloud-managed Wi-Fi platform that uses AI (Marvis) to explain why users have connection problems.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "09 Networking/Wireless"
WHERE type = "tool"
SORT file.name ASC
```
