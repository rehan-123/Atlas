---
type: "tool"
level: "Senior"
category: "[[DevOps & Containers]]"
subcategory: "[[Containers & orchestration]]"
vendor: "[[Microsoft]]"
deployment: "Azure"
status: "current"
aliases:
  - "AKS"
tags:
  - "tool"
  - "devops"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Azure Kubernetes Service

> [!abstract] In plain words
> Microsoft's managed Kubernetes. Azure runs the control plane; you run and pay for the worker nodes.
>
> **What kind of tool is this?** A container packs an app with everything it needs so it runs the same anywhere. Orchestrators like Kubernetes run and restart many containers for you.

**Made by:** [[Microsoft]] · **Runs:** Azure · **Category:** [[DevOps & Containers]] › [[Containers & orchestration]]

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **container**: A packaged app with everything it needs to run, sharing the host's operating system kernel.
> **cluster**: Several servers working together so one can take over if another fails.
> **registry**: Windows' central settings database.
> *More in the [[Glossary]].*

## In more detail

Managed Kubernetes on Azure: node pools on VM scale sets, Entra ID integration, Azure CNI networking, integration with Azure Monitor Container insights.

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Nodes not ready after an upgrade | Check the node pool's provisioning state and the cluster's upgrade history in the portal |
| Pods can't pull from ACR | Attach the registry to the cluster (az aks update --attach-acr) |

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
az aks get-credentials -g RG -n CLUSTER
az aks show -g RG -n CLUSTER
az aks nodepool list -g RG --cluster-name CLUSTER
```

## See also

[[Kubernetes]] · [[Microsoft Azure]] · [[Azure Monitor]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
