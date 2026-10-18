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

# Immutability & air gap

> [!abstract] In one line
> Backups that cannot be changed or deleted for a set period, or are physically disconnected.

> [!tip] Think of it like
> An immutable backup is written in ink, not pencil: nobody can rub it out until the lock expires.

> [!info]+ Words on this page
> **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
> **retention**: How long backups or logs are kept.
> **immutable**: Can't be changed or deleted until a set date, even by an admin.
> *More in the [[Glossary]].*

## How it works

- Object Lock (S3, Wasabi, B2), Veeam hardened Linux repositories, Datto Cloud and Axcient AirGap are common forms.
- Immutability protects against stolen admin credentials; MFA on backup consoles is still essential.
- Retention must be long enough to cover dwell time: attackers can sit for weeks before encrypting.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- An attacker has the backup admin's password. What still protects the data?
> Immutable or air-gapped copies, which can't be deleted even by an admin.

## See also

[[3-2-1-1-0 rule]] · [[Wasabi]] · [[Backblaze B2]] · [[Veeam Backup & Replication]] · [[Suspected ransomware]]
