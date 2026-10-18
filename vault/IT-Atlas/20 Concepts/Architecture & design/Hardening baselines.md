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

# Hardening baselines

> [!abstract] In one line
> Agreed secure settings for each type of system, applied automatically and checked for drift.

> [!tip] Think of it like
> A checklist for locking up a building at night, the same for every branch.

> [!info]+ Words on this page
> **SMB**: The Windows file-sharing protocol (port 445).
> **LAPS**: A Windows feature that gives each PC its own rotating local admin password.
> **hardening**: Changing default settings to remove unnecessary features and close security gaps.
> **branch**: A separate line of changes in Git, merged back into main after review.
> *More in the [[Glossary]].*

## How it works

- Sources: CIS Benchmarks, Microsoft security baselines (Group Policy and Intune), vendor hardening guides.
- Apply with Group Policy, Intune, DSC or Ansible; measure with Secure Score or CIS-CAT.
- Typical items: disable SMBv1, enforce SMB signing, LAPS for local admin, restrict PowerShell remoting, remove legacy protocols.
- Test in a pilot first: some settings break old apps.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Where can you get a ready-made hardening baseline for Windows?
> Microsoft security baselines or the CIS Benchmarks.

## See also

[[CIS Controls]] · [[CIS-CAT Pro]] · [[Group Policy]] · [[SMB signing and versions]]
