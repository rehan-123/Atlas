---
type: "moc"
level: "All"
tags:
  - "moc"
  - "compliance"
created: "2026-10-18"
updated: "2026-10-18"
---

# Posture & assessment

> [!abstract] In plain words
> Posture tools score your configuration against best practice and tell you what to fix first.

Part of [[Compliance & Governance]].

- [[Microsoft Secure Score]]: A score in the Microsoft Defender portal that shows how well your Microsoft 365 tenant is secured, with a ranked list of fixes.
- [[CIS-CAT Pro]]: A scanner that checks a machine's settings against the CIS Benchmarks and reports what doesn't match.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "19 Compliance & Governance/Posture & assessment"
WHERE type = "tool"
SORT file.name ASC
```
