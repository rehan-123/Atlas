---
type: "tool"
level: "Mid"
category: "[[Virtualization & Storage]]"
subcategory: "[[Hypervisors]]"
vendor: "[[Nutanix]]"
deployment: "Hyperconverged appliances or software"
status: "current"
aliases:
  - "Prism"
tags:
  - "tool"
  - "virtualization"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Nutanix AHV

> [!abstract] In plain words
> Virtualization and storage in one system, managed through a web console called Prism.
>
> **What kind of tool is this?** A hypervisor lets one physical server run many virtual machines (VMs), each acting like its own computer.

**Made by:** [[Nutanix]] · **Runs:** Hyperconverged appliances or software · **Category:** [[Virtualization & Storage]] › [[Hypervisors]]

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **hypervisor**: Software that runs virtual machines on a physical server.
> **appliance**: A dedicated box (or virtual machine) built to do one job, such as backup or firewall.
> *More in the [[Glossary]].*

## In more detail

Hyperconverged infrastructure with Nutanix's AHV hypervisor, managed by Prism Element and Prism Central.

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
ncc health_checks run_all
acli vm.list
ncli cluster info
```

## See also

[[VMware vSphere]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
