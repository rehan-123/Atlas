---
type: "moc"
level: "All"
tags:
  - "moc"
  - "backup"
created: "2026-10-18"
updated: "2026-10-18"
---

# Cloud backup & DR

> [!abstract] In plain words
> These are the backup and disaster-recovery services built into Azure and AWS, plus tools that keep a live copy of servers in another location.

Part of [[Backup & DR]].

- [[Azure Backup]]: Azure's built-in backup for Azure VMs, and for on-site servers through a small agent.
- [[Azure Site Recovery]]: Keeps a live copy of servers in Azure so you can switch over if the main site fails.
- [[AWS Backup]]: AWS's built-in backup service for AWS resources.
- [[Zerto]]: Copies virtual machines to another site every few seconds, so very little data is lost in a disaster.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "05 Backup & DR/Cloud backup & DR"
WHERE type = "tool"
SORT file.name ASC
```
