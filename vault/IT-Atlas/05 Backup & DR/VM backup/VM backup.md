---
type: "moc"
level: "All"
tags:
  - "moc"
  - "backup"
created: "2026-10-18"
updated: "2026-10-18"
---

# VM backup

> [!abstract] In plain words
> VM backup protects virtual machines from the host level, without installing software inside each one.

Part of [[Backup & DR]].

- [[Veeam Backup & Replication]]: The most common tool for backing up virtual machines (VMware and Hyper-V). It can also test-boot backups and start a VM straight from its backup.
- [[Veeam ONE]]: Watches Veeam and the virtual servers and reports problems and capacity.
- [[Nakivo Backup & Replication]]: A cheaper alternative to Veeam that can even run on a NAS.
- [[Hornetsecurity VM Backup]]: Simple VM backup for Hyper-V and VMware, formerly called Altaro.
- [[Proxmox Backup Server]]: The backup server for Proxmox virtual machines.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "05 Backup & DR/VM backup"
WHERE type = "tool"
SORT file.name ASC
```
