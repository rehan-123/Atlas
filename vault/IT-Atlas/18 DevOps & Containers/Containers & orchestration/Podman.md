---
type: "tool"
level: "Senior"
category: "[[DevOps & Containers]]"
subcategory: "[[Containers & orchestration]]"
vendor: "[[Red Hat]]"
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

# Podman

> [!abstract] In plain words
> A Docker-compatible container tool from Red Hat that doesn't need a background service or root.
>
> **What kind of tool is this?** A container packs an app with everything it needs so it runs the same anywhere. Orchestrators like Kubernetes run and restart many containers for you.

**Made by:** [[Red Hat]] · **Category:** [[DevOps & Containers]] › [[Containers & orchestration]]

> [!info]+ Words on this page
> **CLI**: Command-line interface: typing commands instead of clicking.
> **container**: A packaged app with everything it needs to run, sharing the host's operating system kernel.
> *More in the [[Glossary]].*

## In more detail

Daemonless, rootless container engine with a Docker-compatible CLI; common on RHEL and Fedora.

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
podman ps -a
podman logs CONTAINER
podman generate systemd --name CONTAINER
```

## See also

[[Docker]] · [[Red Hat Enterprise Linux]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
