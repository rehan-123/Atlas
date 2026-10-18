---
type: "moc"
level: "All"
tags:
  - "moc"
  - "networking"
created: "2026-10-18"
updated: "2026-10-18"
---

# Load balancers

> [!abstract] In plain words
> A load balancer spreads incoming traffic across several servers, so one busy or failed server doesn't take a service down.

Part of [[Networking]].

- [[F5 BIG-IP]]: A high-end load balancer for big web applications.
- [[NetScaler ADC]]: A load balancer and remote access gateway, often in front of Citrix (formerly Citrix ADC).
- [[HAProxy]]: A free, fast load balancer.
- [[Kemp LoadMaster]]: A load balancer often used in front of Exchange and remote desktop servers.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "09 Networking/Load balancers"
WHERE type = "tool"
SORT file.name ASC
```
