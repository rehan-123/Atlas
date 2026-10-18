---
type: "moc"
level: "All"
tags:
  - "moc"
  - "compliance"
created: "2026-10-18"
updated: "2026-10-18"
---

# Compliance platforms

> [!abstract] In plain words
> These platforms map your controls to frameworks like SOC 2 or ISO 27001 and collect the evidence automatically.

Part of [[Compliance & Governance]].

- [[Vanta]]: A platform that connects to your cloud and IT tools and tracks your readiness for audits like SOC 2 and ISO 27001.
- [[Drata]]: A compliance automation platform, similar to Vanta, that collects audit evidence automatically.

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "19 Compliance & Governance/Compliance platforms"
WHERE type = "tool"
SORT file.name ASC
```
