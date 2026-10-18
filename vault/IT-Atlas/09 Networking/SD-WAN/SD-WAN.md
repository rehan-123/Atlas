---
type: "moc"
level: "All"
tags:
  - "moc"
  - "networking"
created: "2026-10-18"
updated: "2026-10-18"
---

# SD-WAN

> [!abstract] In plain words
> SD-WAN lets a site use several internet links at once and automatically moves traffic to the best one when a link is slow or down.

Part of [[Networking]].

- [[VeloCloud]]: SD-WAN, previously sold as VMware SD-WAN.
- [[Cisco Catalyst SD-WAN]]: Cisco's SD-WAN product.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "09 Networking/SD-WAN"
WHERE type = "tool"
SORT file.name ASC
```
