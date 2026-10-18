---
type: "moc"
level: "All"
tags:
  - "moc"
  - "compliance"
created: "2026-10-18"
updated: "2026-10-18"
---

# Compliance & Governance

> [!abstract] In plain words
> Compliance tools help prove to auditors and customers that security controls exist and actually work.

Proving that IT is run safely: compliance platforms, data governance, posture scoring and audit evidence. The frameworks themselves are in Concepts.

Back to [[Home]].

> [!note]- How seniors think about this area
> - Map controls once to several frameworks; much of SOC 2, ISO 27001 and NIST overlaps.
> - Automate evidence collection (access reviews, backup tests, patch reports) so audits aren't a scramble.
> - Compliance is the minimum, not the goal; focus on controls that actually reduce risk.

## [[Compliance platforms]]

These platforms map your controls to frameworks like SOC 2 or ISO 27001 and collect the evidence automatically.

- [[Vanta]]
- [[Drata]]

## [[Data governance & DLP]]

Data governance finds where sensitive data lives, labels it and stops it leaking (data loss prevention).

- [[Microsoft Purview]]
- [[Varonis]]

## [[Posture & assessment]]

Posture tools score your configuration against best practice and tell you what to fix first.

- [[Microsoft Secure Score]]
- [[CIS-CAT Pro]]

## Playbooks for this area

[[Business email compromise]]

## Database view

```dataview
TABLE vendor, subcategory, deployment, status, agent_service AS "Agent"
FROM "19 Compliance & Governance"
WHERE type = "tool"
SORT subcategory ASC, file.name ASC
```
