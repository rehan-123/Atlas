---
type: "moc"
level: "All"
tags:
  - "moc"
created: "2026-10-18"
updated: "2026-10-18"
---

# Backup concepts

The ideas behind every backup product.

Part of [[Concepts]].

- [[3-2-1-1-0 rule]]: The modern backup rule of thumb.
- [[RPO & RTO]]: Recovery point objective and recovery time objective.
- [[Full, incremental & differential]]: The three ways to take a backup, and how chains work.
- [[Immutability & air gap]]: Backups that cannot be changed or deleted for a set period, or are physically disconnected.
- [[Backup verification]]: Proving a backup can actually be restored.
- [[VSS]]: Volume Shadow Copy Service: Windows' framework for consistent point-in-time snapshots, used by nearly every Windows backup tool.
- [[Changed block tracking]]: CBT: the hypervisor or agent tracks which disk blocks changed so incrementals read only those.
- [[Deduplication]]: Storing each unique block once to save space.
- [[Retention & GFS]]: How long restore points are kept. GFS = grandfather-father-son: daily, weekly, monthly and yearly points.
- [[Bare-metal restore]]: Restoring a whole machine, OS included, to new or empty hardware.
- [[Instant recovery]]: Booting a machine directly from its backup as a VM to cut downtime, then migrating it back to production storage.
- [[Replication vs backup]]: Replication keeps a near-live copy; backup keeps history.
- [[SaaS shared responsibility]]: Microsoft and Google keep their services running; protecting your data from deletion, attack and retention gaps is your job.
