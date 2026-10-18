---
type: "tool"
level: "Senior"
category: "[[DevOps & Containers]]"
subcategory: "[[Containers & orchestration]]"
vendor: "[[CNCF]]"
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

# Helm

> [!abstract] In plain words
> A package manager for Kubernetes: one command installs an app with all its Kubernetes pieces.
>
> **What kind of tool is this?** A container packs an app with everything it needs so it runs the same anywhere. Orchestrators like Kubernetes run and restart many containers for you.

**Made by:** [[CNCF]] · **Category:** [[DevOps & Containers]] › [[Containers & orchestration]]

> [!info]+ Words on this page
> **container**: A packaged app with everything it needs to run, sharing the host's operating system kernel.
> *More in the [[Glossary]].*

## In more detail

Kubernetes package manager: charts bundle templated manifests; releases track what's installed and allow rollback.

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
helm list -A
helm upgrade --install NAME CHART -n NS -f values.yaml
helm rollback NAME REVISION -n NS
helm history NAME -n NS
```

## See also

[[Kubernetes]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
