---
type: "moc"
level: "All"
tags:
  - "moc"
  - "backup"
created: "2026-10-18"
updated: "2026-10-18"
---

# Backup & DR

Protecting data and getting it back: appliances, image and VM backup, SaaS backup, endpoint backup, enterprise platforms, cloud DR and the storage backups land on.

Back to [[Home]].

> [!note]- How seniors think about this area
> - Design from RTO/RPO per system; one policy for everything usually over-protects some and under-protects others.
> - Isolate backup credentials and infrastructure from the production domain; use immutability.
> - Measure restore success, not job success: schedule and record test restores.
> - SaaS data (Microsoft 365, Google) needs its own backup decision and documented retention.

## [[BCDR appliances]]

A BCDR appliance is a box at the client's office that backs up their servers, sends copies to the cloud, and can even run a failed server as a virtual machine until it's fixed.

- [[Datto BCDR]]
- [[Unitrends]]
- [[Axcient x360Recover]]
- [[Barracuda Backup]]

## [[Image & server backup]]

Image backup copies a whole machine (operating system, apps and data) so it can be rebuilt exactly as it was.

- [[StorageCraft ShadowProtect SPX]]
- [[Acronis Cyber Protect]]
- [[Arcserve UDP]]
- [[Cove Data Protection]]
- [[Windows Server Backup]]
- [[Synology Active Backup for Business]]

## [[VM backup]]

VM backup protects virtual machines from the host level, without installing software inside each one.

- [[Veeam Backup & Replication]]
- [[Veeam ONE]]
- [[Nakivo Backup & Replication]]
- [[Hornetsecurity VM Backup]]
- [[Proxmox Backup Server]]

## [[SaaS backup]]

SaaS backup keeps your own copy of Microsoft 365 or Google data (mail, OneDrive, SharePoint, Teams). Microsoft and Google keep the service running, but restoring deleted or encrypted data is your job.

- [[Spanning Backup]]
- [[Datto SaaS Protection]]
- [[Veeam Backup for Microsoft 365]]
- [[Dropsuite]]
- [[Microsoft 365 Backup]]
- [[AvePoint Cloud Backup]]
- [[Keepit]]

## [[Endpoint backup]]

Endpoint backup protects laptops and desktops, usually by sending copies straight to the cloud.

- [[Datto Endpoint Backup]]
- [[Veeam Agent for Microsoft Windows]]
- [[Druva]]
- [[Carbonite]]

## [[Enterprise backup]]

Enterprise backup platforms protect very large environments with many kinds of systems. You'll meet them at bigger clients.

- [[Commvault]]
- [[Rubrik]]
- [[Cohesity]]
- [[Veritas Backup Exec]]

## [[Cloud backup & DR]]

These are the backup and disaster-recovery services built into Azure and AWS, plus tools that keep a live copy of servers in another location.

- [[Azure Backup]]
- [[Azure Site Recovery]]
- [[AWS Backup]]
- [[Zerto]]

## [[Backup storage targets]]

These are the places backups get stored in the cloud. Many can lock a backup so nobody, not even an attacker with admin rights, can delete it early.

- [[Wasabi]]
- [[Backblaze B2]]
- [[Amazon S3]]
- [[Azure Blob Storage]]

## Playbooks for this area

[[Backup copy & replication lag]] · [[Backup job failed]] · [[SaaS backup failing]] · [[Screenshot verification failed]] · [[Snapshot age]]

## Database view

```dataview
TABLE vendor, subcategory, deployment, status, agent_service AS "Agent"
FROM "05 Backup & DR"
WHERE type = "tool"
SORT subcategory ASC, file.name ASC
```
