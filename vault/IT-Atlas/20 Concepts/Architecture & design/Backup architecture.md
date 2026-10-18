---
type: "concept"
level: "Senior"
category: "[[Architecture & design]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Backup architecture

> [!abstract] In one line
> Designing backups so they meet the RPO/RTO and survive ransomware: tiers, copies, immutability and testing.

> [!tip] Think of it like
> Spare keys: one in the kitchen drawer, one with a neighbour, one in a safe deposit box nobody can tamper with.

> [!info]+ Words on this page
> **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
> **GFS**: Grandfather-father-son: keeping daily, weekly and monthly backups for different lengths of time.
> **RPO**: Recovery point objective: the most data, measured in time, you can afford to lose.
> **RTO**: Recovery time objective: how long you can afford to be down.
> **immutable**: Can't be changed or deleted until a set date, even by an admin.
> **ransomware**: Malware that encrypts files and demands payment to unlock them.
> **retention**: How long backups or logs are kept.
> *More in the [[Glossary]].*

## How it works

- Local copy for fast restores, offsite or cloud copy for disasters, immutable or air-gapped copy for ransomware (3-2-1-1-0).
- Separate the backup system from the domain: its own credentials, MFA, ideally not domain-joined.
- Match retention to legal and business needs (GFS).
- Test restores on a schedule and record the results; a backup that hasn't been restored is a hope, not a plan.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why should the backup server not be joined to the production domain?
> If the domain is compromised, attackers can use domain admin rights to delete backups too.

## See also

[[3-2-1-1-0 rule]] · [[Immutability & air gap]] · [[Backup verification]] · [[Retention & GFS]]
