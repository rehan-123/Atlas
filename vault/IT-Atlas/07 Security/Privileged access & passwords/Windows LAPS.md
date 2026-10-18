---
type: "tool"
level: "Mid"
category: "[[Security]]"
subcategory: "[[Privileged access & passwords]]"
vendor: "[[Microsoft]]"
deployment: "Built into Windows (April 2023 updates onward)"
status: "current"
aliases: []
tags:
  - "tool"
  - "security"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Windows LAPS

> [!abstract] In plain words
> Built into Windows: gives every computer a different local admin password, changes it regularly, and stores it in Active Directory or Entra ID.
>
> **What kind of tool is this?** These tools store passwords safely and control who can use admin accounts.

**Made by:** [[Microsoft]] · **Runs:** Built into Windows (April 2023 updates onward) · **Category:** [[Security]] › [[Privileged access & passwords]]

> [!info]+ Words on this page
> **LAPS**: A Windows feature that gives each PC its own rotating local admin password.
> *More in the [[Glossary]].*

## In more detail

Built-in Local Administrator Password Solution: rotates a local admin password per device and stores it in Entra ID or Active Directory. Replaces the legacy Microsoft LAPS add-on.

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-LapsADPassword -Identity COMPUTER -AsPlainText
Get-LapsAADPassword -DeviceIds DEVICEID -IncludePasswords -AsPlainText
Invoke-LapsPolicyProcessing
```

## See also

[[Active Directory]] · [[Microsoft Entra ID]] · [[Least privilege]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
