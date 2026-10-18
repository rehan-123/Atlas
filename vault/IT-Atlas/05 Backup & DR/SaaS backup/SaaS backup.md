---
type: "moc"
level: "All"
tags:
  - "moc"
  - "backup"
created: "2026-10-18"
updated: "2026-10-18"
---

# SaaS backup

> [!abstract] In plain words
> SaaS backup keeps your own copy of Microsoft 365 or Google data (mail, OneDrive, SharePoint, Teams). Microsoft and Google keep the service running, but restoring deleted or encrypted data is your job.

Part of [[Backup & DR]].

- [[Spanning Backup]]: Backs up Microsoft 365 (mail, OneDrive, SharePoint, Teams) and Google Workspace, so deleted or encrypted data can be restored. Each user needs a licence to be protected.
- [[Datto SaaS Protection]]: Kaseya's Microsoft 365 and Google Workspace backup, formerly called Backupify.
- [[Veeam Backup for Microsoft 365]]: Veeam's Microsoft 365 backup, which you run yourself or buy through a provider.
- [[Dropsuite]]: Microsoft 365 and Google Workspace backup sold through MSPs.
- [[Microsoft 365 Backup]]: Microsoft's own backup service for SharePoint, OneDrive and Exchange, paid for by usage.
- [[AvePoint Cloud Backup]]: Microsoft 365 and Google Workspace backup from AvePoint.
- [[Keepit]]: SaaS backup that stores your Microsoft 365 and other data in its own separate cloud.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "05 Backup & DR/SaaS backup"
WHERE type = "tool"
SORT file.name ASC
```
