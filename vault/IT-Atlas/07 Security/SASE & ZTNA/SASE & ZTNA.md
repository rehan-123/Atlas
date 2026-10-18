---
type: "moc"
level: "All"
tags:
  - "moc"
  - "security"
created: "2026-10-18"
updated: "2026-10-18"
---

# SASE & ZTNA

> [!abstract] In plain words
> These cloud services replace the old office VPN: users get to the apps they're allowed to use, from anywhere, with security checks on every connection.

Part of [[Security]].

- [[Zscaler]]: Cloud security that filters internet traffic and gives secure access to company apps without a traditional VPN.
- [[Cloudflare Zero Trust]]: Cloudflare's service for secure access to company apps and filtered internet browsing.
- [[Netskope]]: Cloud security that filters web and cloud app use.
- [[Twingate]]: A simple VPN replacement that only gives users access to the apps they need.
- [[Prisma Access]]: Palo Alto's cloud security service for remote users and branches.
- [[Cato SASE Cloud]]: A cloud service that combines SD-WAN, firewall and secure remote access, so sites and users connect through Cato's network.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "07 Security/SASE & ZTNA"
WHERE type = "tool"
SORT file.name ASC
```
