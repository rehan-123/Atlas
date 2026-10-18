---
type: "moc"
level: "All"
tags:
  - "moc"
  - "virtualization"
created: "2026-10-18"
updated: "2026-10-18"
---

# Storage arrays & NAS

> [!abstract] In plain words
> Storage arrays and NAS boxes are dedicated machines full of disks that store data for servers and users.

Part of [[Virtualization & Storage]].

- [[Synology NAS]]: A popular network storage box for small businesses, also often used as a backup target.
- [[QNAP NAS]]: A network storage box for small businesses.
- [[NetApp ONTAP]]: NetApp's enterprise storage system.
- [[Dell PowerVault ME]]: Dell's entry-level shared storage for small server clusters.
- [[Dell PowerStore]]: Dell's mid-range storage system.
- [[HPE MSA]]: HPE's entry-level shared storage for small server clusters.
- [[HPE Alletra]]: HPE's storage family, including the former Nimble arrays.
- [[Lenovo ThinkSystem DE-Series]]: Lenovo's shared storage arrays. Replacement drives must be the exact supported part.
- [[Pure Storage FlashArray]]: Fast all-flash storage arrays.
- [[TrueNAS]]: Free and paid NAS software built on the ZFS file system.
- [[Storage Spaces Direct]]: Windows' way to pool the disks of several clustered servers into shared storage.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "11 Virtualization & Storage/Storage arrays & NAS"
WHERE type = "tool"
SORT file.name ASC
```
