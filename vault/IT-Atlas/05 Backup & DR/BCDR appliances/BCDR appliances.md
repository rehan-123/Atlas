---
type: "moc"
level: "All"
tags:
  - "moc"
  - "backup"
created: "2026-10-18"
updated: "2026-10-18"
---

# BCDR appliances

> [!abstract] In plain words
> A BCDR appliance is a box at the client's office that backs up their servers, sends copies to the cloud, and can even run a failed server as a virtual machine until it's fixed.

Part of [[Backup & DR]].

- [[Datto BCDR]]: A Datto appliance at the client's site backs up servers, copies the backups to the Datto cloud, and test-boots them to prove they work. If a server dies, its backup can run as a virtual machine.
- [[Unitrends]]: Kaseya's backup appliances (physical or virtual). They back up servers and VMs and can automatically test that recovery works.
- [[Axcient x360Recover]]: Axcient's backup appliance or cloud service. Its backups don't depend on a chain of earlier backups, so one bad file can't break them.
- [[Barracuda Backup]]: Barracuda's backup appliance with copies to the Barracuda cloud.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "05 Backup & DR/BCDR appliances"
WHERE type = "tool"
SORT file.name ASC
```
