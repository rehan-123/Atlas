---
type: "moc"
level: "All"
tags:
  - "moc"
  - "virtualization"
created: "2026-10-18"
updated: "2026-10-18"
---

# Server hardware management

> [!abstract] In plain words
> Out-of-band controllers are tiny computers inside a server that let you see its health and console even when Windows is down.

Part of [[Virtualization & Storage]].

- [[Dell iDRAC]]: The management chip in Dell servers: shows hardware health and gives remote console even if Windows is down.
- [[HPE iLO]]: The management chip in HPE servers: hardware health logs and remote console.
- [[Lenovo XClarity Controller]]: The management chip in Lenovo servers.
- [[Supermicro IPMI]]: The management chip in Supermicro servers.
- [[Hardware RAID controllers]]: The card inside a server that combines several disks so one failed disk doesn't lose data.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "11 Virtualization & Storage/Server hardware management"
WHERE type = "tool"
SORT file.name ASC
```
