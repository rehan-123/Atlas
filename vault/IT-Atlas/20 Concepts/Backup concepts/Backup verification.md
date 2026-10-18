---
type: "concept"
level: "Mid"
category: "[[Backup concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Backup verification

> [!abstract] In one line
> Proving a backup can actually be restored.

> [!tip] Think of it like
> A fire drill for backups: practice the restore before you need it.

> [!info]+ Words on this page
> **RTO**: Recovery time objective: how long you can afford to be down.
> *More in the [[Glossary]].*

## How it works

- "Job succeeded" only means data was written.
- Automated boot tests: Datto screenshot verification, Veeam SureBackup, Unitrends Recovery Assurance, Cove Recovery Testing.
- Schedule real file and full-system test restores and record the time taken (that is your real RTO).

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Does 'backup job succeeded' mean you can restore?
> No. It only means data was written. Test-boot or test-restore to prove it.

## See also

[[Datto BCDR]] · [[Veeam Backup & Replication]] · [[Unitrends]] · [[Screenshot verification failed]]
