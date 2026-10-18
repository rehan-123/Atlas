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

# Cloud cost management

> [!abstract] In one line
> Cloud bills grow quietly; tagging, right-sizing and shutting things down are how you control them.

> [!tip] Think of it like
> A phone bill: unused subscriptions keep charging until someone cancels them.

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **snapshot**: A saved point in time of a VM or disk. Not a backup, and it grows the longer you keep it.
> *More in the [[Glossary]].*

## How it works

- Tag every resource with owner, client and environment.
- Right-size VMs from real usage; most are over-provisioned.
- Shut down or schedule non-production resources; delete orphaned disks, IPs and snapshots.
- Use reservations or savings plans for steady workloads; set budgets and alerts.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Name two common sources of wasted cloud spend.
> Oversized VMs, and orphaned resources like unattached disks, old snapshots and unused public IPs.

## See also

[[Microsoft Azure]] · [[Amazon Web Services]] · [[Capacity planning]]
