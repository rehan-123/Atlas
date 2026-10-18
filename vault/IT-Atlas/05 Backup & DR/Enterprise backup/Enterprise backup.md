---
type: "moc"
level: "All"
tags:
  - "moc"
  - "backup"
created: "2026-10-18"
updated: "2026-10-18"
---

# Enterprise backup

> [!abstract] In plain words
> Enterprise backup platforms protect very large environments with many kinds of systems. You'll meet them at bigger clients.

Part of [[Backup & DR]].

- [[Commvault]]: A big enterprise backup platform that protects almost every kind of system.
- [[Rubrik]]: Enterprise backup focused on recovering quickly from ransomware.
- [[Cohesity]]: Enterprise backup and data management, now combined with Veritas' NetBackup business.
- [[Veritas Backup Exec]]: Long-standing Windows backup software, often used with tape drives.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "05 Backup & DR/Enterprise backup"
WHERE type = "tool"
SORT file.name ASC
```
