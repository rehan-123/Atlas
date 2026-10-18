---
type: "lesson"
level: "Junior"
tags:
  - "learning"
created: "2026-10-18"
updated: "2026-10-18"
---

# Week 6 - Backup and recovery

> [!abstract] This week
> Understand how backups work, why they fail, and how to prove they can be restored.

## Read these, in order

- [ ] [[3-2-1-1-0 rule]]
- [ ] [[RPO & RTO]]
- [ ] [[Full, incremental & differential]]
- [ ] [[VSS]]
- [ ] [[Immutability & air gap]]
- [ ] [[Backup verification]]
- [ ] [[Backup & DR]]
- [ ] [[Backup job failed]]
- [ ] [[VSS writer failure]]
- [ ] [[SaaS shared responsibility]]

## Practice

- [ ] Run `vssadmin list writers` on a server and check every writer says 'Stable' with 'No error'.
- [ ] In your backup console, find the last successful backup for one server and work out its RPO right now.
- [ ] Do a supervised test restore of a single file.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- A backup job succeeded. Does that prove you can restore?
> No. Only a test restore or boot test proves it.

> [!question]- Which backup copy protects against an attacker with admin rights?
> An immutable or air-gapped copy.

---
Part of the [[Learning path]]. Previous: [[Week 5 - Monitoring and the RMM]]. Next: [[Week 7 - Security basics]].
