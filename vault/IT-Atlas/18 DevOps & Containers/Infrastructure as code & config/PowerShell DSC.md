---
type: "tool"
level: "Senior"
category: "[[DevOps & Containers]]"
subcategory: "[[Infrastructure as code & config]]"
vendor: "[[Microsoft]]"
deployment:
status: "current"
aliases:
  - "Desired State Configuration"
  - "DSC"
tags:
  - "tool"
  - "devops"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# PowerShell DSC

> [!abstract] In plain words
> PowerShell Desired State Configuration: write how a Windows server should look, and DSC makes it so.
>
> **What kind of tool is this?** Infrastructure as code means writing servers, networks and settings down in files, so building them is a repeatable command instead of a checklist.

**Made by:** [[Microsoft]] · **Category:** [[DevOps & Containers]] › [[Infrastructure as code & config]]

> [!info]+ Words on this page
> **container**: A packaged app with everything it needs to run, sharing the host's operating system kernel.
> *More in the [[Glossary]].*

## In more detail

Declarative configuration for Windows (and cross-platform DSC v3): configurations compile to MOF, the Local Configuration Manager applies and monitors drift; Azure Machine Configuration builds on it.

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-DscConfigurationStatus
Test-DscConfiguration -Detailed
Start-DscConfiguration -Path .\MOF -Wait -Verbose
```

## See also

[[PowerShell]] · [[Infrastructure as code]] · [[Group Policy]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
