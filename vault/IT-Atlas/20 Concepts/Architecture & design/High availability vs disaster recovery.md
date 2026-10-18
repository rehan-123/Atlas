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

# High availability vs disaster recovery

> [!abstract] In one line
> High availability keeps a service running through a single failure; disaster recovery brings it back after losing a whole site.

> [!tip] Think of it like
> HA is a spare tyre in the car; DR is a second car parked across town.

> [!info]+ Words on this page
> **HA**: High availability: designed so one failure doesn't cause downtime.
> **RAID**: Combining several disks so one failed disk doesn't lose data. Not a backup.
> **DC**: Domain controller: a server running Active Directory.
> **DR**: Disaster recovery: getting systems back after a major failure.
> **RTO**: Recovery time objective: how long you can afford to be down.
> **RPO**: Recovery point objective: the most data, measured in time, you can afford to lose.
> **cluster**: Several servers working together so one can take over if another fails.
> **failover**: Automatically switching to a backup system when the main one fails.
> *More in the [[Glossary]].*

## How it works

- **HA**: redundancy inside a site (clusters, RAID, dual power, two DCs). Failover in seconds or minutes.
- **DR**: a second site or cloud copy, recovered within the agreed **RTO** and losing no more than the **RPO**.
- HA does not protect against deletion, corruption or ransomware: those replicate instantly. You still need backups.
- Design from the business's RTO and RPO, not from the technology.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- A two-node cluster replicates instantly. Does it protect against ransomware?
> No. Encrypted data replicates too. Only isolated, versioned backups protect against that.

> [!question]- What two numbers should drive a DR design?
> RTO (how fast it must be back) and RPO (how much data can be lost).

## See also

[[RPO & RTO]] · [[Failover Clustering]] · [[Replication vs backup]] · [[Disaster recovery planning]]
