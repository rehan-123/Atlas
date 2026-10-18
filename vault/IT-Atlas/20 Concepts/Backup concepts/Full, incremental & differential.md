---
type: "concept"
level: "Junior"
category: "[[Backup concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Full, incremental & differential

> [!abstract] In one line
> The three ways to take a backup, and how chains work.

> [!tip] Think of it like
> Full: photocopy the whole book. Incremental: copy only pages changed since the last copy. Differential: copy all pages changed since the last full copy.

> [!info]+ Words on this page
> **incremental**: A backup of only what changed since the last backup.
> *More in the [[Glossary]].*

## How it works

- **Full**: everything. **Incremental**: changes since the last backup of any kind. **Differential**: changes since the last full.
- Incremental chains depend on every link; one corrupt file can break every later point. Products manage this with synthetic fulls, consolidation (ImageManager), inverse chains (Datto) or chain-free designs (Axcient).
- **Synthetic full**: a new full built on the backup storage from existing data, without reading production again.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why is a broken incremental chain dangerous?
> Every later backup depends on it, so restore points after the break may be unusable.

## See also

[[StorageCraft ShadowProtect SPX]] · [[Datto BCDR]] · [[Axcient x360Recover]] · [[Changed block tracking]]
