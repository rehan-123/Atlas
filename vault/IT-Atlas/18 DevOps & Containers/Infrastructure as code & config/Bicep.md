---
type: "tool"
level: "Senior"
category: "[[DevOps & Containers]]"
subcategory: "[[Infrastructure as code & config]]"
vendor: "[[Microsoft]]"
deployment:
status: "current"
aliases: []
tags:
  - "tool"
  - "devops"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Bicep

> [!abstract] In plain words
> Microsoft's simple language for describing Azure resources in files and deploying them repeatably.
>
> **What kind of tool is this?** Infrastructure as code means writing servers, networks and settings down in files, so building them is a repeatable command instead of a checklist.

**Made by:** [[Microsoft]] · **Category:** [[DevOps & Containers]] › [[Infrastructure as code & config]]

> [!info]+ Words on this page
> **container**: A packaged app with everything it needs to run, sharing the host's operating system kernel.
> *More in the [[Glossary]].*

## In more detail

Domain-specific language that compiles to ARM templates; deployed with az deployment group create; supports modules and what-if previews.

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
az deployment group what-if -g RG -f main.bicep
az deployment group create -g RG -f main.bicep
```

## See also

[[Terraform]] · [[Infrastructure as code]] · [[Microsoft Azure]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
