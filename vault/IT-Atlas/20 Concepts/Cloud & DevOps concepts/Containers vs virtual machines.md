---
type: "concept"
level: "Mid"
category: "[[Cloud & DevOps concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Containers vs virtual machines

> [!abstract] In one line
> A VM pretends to be a whole computer with its own OS; a container shares the host's OS and packs just the app.

> [!tip] Think of it like
> A VM is a separate house with its own plumbing; a container is a flat in a block, sharing the building's pipes.

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **container**: A packaged app with everything it needs to run, sharing the host's operating system kernel.
> *More in the [[Glossary]].*

## How it works

- A **VM** has its own kernel and boots like a PC; heavy but strongly isolated.
- A **container** shares the host kernel; starts in seconds and uses less memory.
- Containers are meant to be **disposable**: data goes in volumes or databases, not inside the container.
- Most real setups use both: containers running inside VMs.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why does a Linux container need a Linux kernel to run?
> Containers share the host's kernel instead of bringing their own, so the kernel must match.

## See also

[[Docker]] · [[Kubernetes]] · [[Hypervisors]]
