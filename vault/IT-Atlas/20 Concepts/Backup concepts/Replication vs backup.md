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

# Replication vs backup

> [!abstract] In one line
> Replication keeps a near-live copy; backup keeps history.

> [!tip] Think of it like
> Replication is a mirror: it copies mistakes instantly. Backup is a photo album: you can go back in time.

> [!info]+ Words on this page
> **RTO**: Recovery time objective: how long you can afford to be down.
> **DR**: Disaster recovery: getting systems back after a major failure.
> **replication**: Copying data or changes to another place, continuously or on a schedule.
> **retention**: How long backups or logs are kept.
> *More in the [[Glossary]].*

## How it works

- Replication copies corruption and encryption instantly. Only backups with retention let you go back to before the attack.
- Use replication for a low RTO and backup for recoverability; most DR plans need both.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Ransomware encrypts a server that's replicated every 15 minutes. Is the replica safe?
> Probably not: the encryption gets copied too. You need backups with history.

## See also

[[Zerto]] · [[Azure Site Recovery]] · [[RPO & RTO]]
