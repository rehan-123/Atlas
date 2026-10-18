---
type: "moc"
level: "All"
tags:
  - "moc"
  - "networking"
created: "2026-10-18"
updated: "2026-10-18"
---

# Switching & routing

> [!abstract] In plain words
> Switches connect devices inside a building; routers connect different networks together.

Part of [[Networking]].

- [[Cisco Catalyst]]: Cisco's main switch range. Its commands are the ones most network tutorials teach.
- [[Meraki MS]]: Cisco Meraki's switches, managed from the web dashboard.
- [[HPE Aruba Networking]]: HPE's switches and Wi-Fi (Aruba).
- [[Juniper Networks]]: Routers, switches, firewalls and Mist Wi-Fi, now part of HPE.
- [[MikroTik]]: Cheap, powerful routers common at ISPs and small offices.
- [[Extreme Networks]]: Enterprise switches and Wi-Fi.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "09 Networking/Switching & routing"
WHERE type = "tool"
SORT file.name ASC
```
