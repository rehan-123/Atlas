---
type: "moc"
level: "All"
tags:
  - "moc"
created: "2026-10-18"
updated: "2026-10-18"
---

# Architecture & design

How senior engineers design systems that stay up, recover fast and stay secure.

Part of [[Concepts]].

- [[High availability vs disaster recovery]]: High availability keeps a service running through a single failure; disaster recovery brings it back after losing a whole site.
- [[Tiered administration]]: Separating admin accounts by what they can touch, so a compromised workstation can't lead straight to domain admin.
- [[Network segmentation]]: Splitting a network into zones with firewall rules between them, so one infected device can't reach everything.
- [[Hybrid identity models]]: How on-premises Active Directory and Microsoft Entra ID are linked: password hash sync, pass-through authentication or federation.
- [[Backup architecture]]: Designing backups so they meet the RPO/RTO and survive ransomware: tiers, copies, immutability and testing.
- [[Patch rings]]: Rolling out updates in waves: a small test group first, then pilot users, then everyone, with time to catch problems.
- [[Capacity planning]]: Watching growth trends so you buy or scale before you run out of disk, CPU, licences or bandwidth.
- [[Change management]]: Planning, approving and recording changes so they don't cause surprise outages, and can be undone.
- [[Disaster recovery planning]]: A written, tested plan for bringing the business back after losing a site, a system or the whole network.
- [[Hardening baselines]]: Agreed secure settings for each type of system, applied automatically and checked for drift.
- [[Single sign-on]]: Signing in once with your company account to reach many apps, using SAML or OpenID Connect.
- [[Documentation standards]]: What good IT documentation contains so anyone on shift can support a client without asking around.
