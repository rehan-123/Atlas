---
type: "moc"
level: "All"
tags:
  - "moc"
  - "compliance"
created: "2026-10-18"
updated: "2026-10-18"
---

# Data governance & DLP

> [!abstract] In plain words
> Data governance finds where sensitive data lives, labels it and stops it leaking (data loss prevention).

Part of [[Compliance & Governance]].

- [[Microsoft Purview]]: Microsoft's family of tools for finding, labelling, keeping and protecting sensitive data across Microsoft 365, including data loss prevention and eDiscovery.
- [[Varonis]]: Software that maps who can access which files and spots unusual access, such as ransomware or an insider copying data.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "19 Compliance & Governance/Data governance & DLP"
WHERE type = "tool"
SORT file.name ASC
```
