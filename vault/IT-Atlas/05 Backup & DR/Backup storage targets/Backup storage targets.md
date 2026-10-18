---
type: "moc"
level: "All"
tags:
  - "moc"
  - "backup"
created: "2026-10-18"
updated: "2026-10-18"
---

# Backup storage targets

> [!abstract] In plain words
> These are the places backups get stored in the cloud. Many can lock a backup so nobody, not even an attacker with admin rights, can delete it early.

Part of [[Backup & DR]].

- [[Wasabi]]: Cheap cloud storage often used to hold backups, with an option to lock them so they can't be deleted.
- [[Backblaze B2]]: Cheap cloud storage often used as a backup target.
- [[Amazon S3]]: AWS's storage service for files of any size, with options from fast to very cheap archive.
- [[Azure Blob Storage]]: Azure's storage service for files, also used as a backup target.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "05 Backup & DR/Backup storage targets"
WHERE type = "tool"
SORT file.name ASC
```
