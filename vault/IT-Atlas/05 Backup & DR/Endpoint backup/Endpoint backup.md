---
type: "moc"
level: "All"
tags:
  - "moc"
  - "backup"
created: "2026-10-18"
updated: "2026-10-18"
---

# Endpoint backup

> [!abstract] In plain words
> Endpoint backup protects laptops and desktops, usually by sending copies straight to the cloud.

Part of [[Backup & DR]].

- [[Datto Endpoint Backup]]: Backs up PCs and servers straight to the Datto cloud, with no appliance on site.
- [[Veeam Agent for Microsoft Windows]]: Veeam's backup agent for physical Windows machines.
- [[Druva]]: A cloud backup service for laptops, servers and Microsoft 365, with nothing to install on site except agents.
- [[Carbonite]]: Simple cloud backup for small businesses, now owned by OpenText.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "05 Backup & DR/Endpoint backup"
WHERE type = "tool"
SORT file.name ASC
```
