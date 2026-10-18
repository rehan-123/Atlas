---
type: "moc"
level: "All"
tags:
  - "moc"
  - "networking"
created: "2026-10-18"
updated: "2026-10-18"
---

# DNS & IPAM

> [!abstract] In plain words
> These tools manage domain names (DNS) and keep track of which IP addresses are in use.

Part of [[Networking]].

- [[Infoblox]]: Enterprise DNS, DHCP and IP address management.
- [[Cloudflare DNS]]: Cloudflare's service for hosting a domain's DNS records, with built-in protection.
- [[Amazon Route 53]]: AWS's DNS hosting service.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "09 Networking/DNS & IPAM"
WHERE type = "tool"
SORT file.name ASC
```
