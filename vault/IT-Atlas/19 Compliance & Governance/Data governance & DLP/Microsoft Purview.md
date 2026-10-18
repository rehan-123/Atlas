---
type: "tool"
level: "Senior"
category: "[[Compliance & Governance]]"
subcategory: "[[Data governance & DLP]]"
vendor: "[[Microsoft]]"
deployment:
status: "current"
aliases: []
tags:
  - "tool"
  - "compliance"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Microsoft Purview

> [!abstract] In plain words
> Microsoft's family of tools for finding, labelling, keeping and protecting sensitive data across Microsoft 365, including data loss prevention and eDiscovery.
>
> **What kind of tool is this?** Data governance finds where sensitive data lives, labels it and stops it leaking (data loss prevention).

**Made by:** [[Microsoft]] · **Category:** [[Compliance & Governance]] › [[Data governance & DLP]]

> [!info]+ Words on this page
> **DLP**: Data loss prevention: rules that detect and stop sensitive data leaving.
> **retention**: How long backups or logs are kept.
> *More in the [[Glossary]].*

## In more detail

Information protection (sensitivity labels), DLP policies, retention and records, eDiscovery, audit, Insider Risk and Compliance Manager, managed in the Purview portal.

## Main parts

- Sensitivity labels
- Data loss prevention
- Retention policies and labels
- eDiscovery and content search
- Audit log
- Compliance Manager

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Mailbox can't be cleaned up | A retention policy or litigation hold may be keeping items; check holds before deleting |
| User blocked from sending a file | A DLP policy matched; check the policy tip and the DLP alert |

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Connect-IPPSSession
Get-DlpCompliancePolicy
Get-RetentionCompliancePolicy
Search-UnifiedAuditLog -StartDate DATE -EndDate DATE -UserIds USER
```

## See also

[[Microsoft 365]] · [[Data classification & DLP]] · [[Mailbox full]] · [[Exchange Online]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
