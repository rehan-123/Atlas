---
type: "moc"
level: "All"
tags:
  - "moc"
  - "backup"
created: "2026-10-18"
updated: "2026-10-18"
---

# Image & server backup

> [!abstract] In plain words
> Image backup copies a whole machine (operating system, apps and data) so it can be rebuilt exactly as it was.

Part of [[Backup & DR]].

- [[StorageCraft ShadowProtect SPX]]: Takes image backups of servers. A companion tool, ImageManager, combines and checks the backup files and copies them offsite.
- [[Acronis Cyber Protect]]: Backup and antivirus in one agent, managed from Acronis' cloud console.
- [[Arcserve UDP]]: Arcserve's backup software for servers and VMs.
- [[Cove Data Protection]]: N-able's cloud backup: data goes straight to N-able's cloud, with an optional local copy for faster restores.
- [[Windows Server Backup]]: The basic backup tool built into Windows Server.
- [[Synology Active Backup for Business]]: Free backup software that runs on a Synology NAS and backs up PCs, servers, VMs and Microsoft 365.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "05 Backup & DR/Image & server backup"
WHERE type = "tool"
SORT file.name ASC
```
