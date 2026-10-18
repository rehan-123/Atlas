---
type: "tool"
level: "Senior"
category: "[[DevOps & Containers]]"
subcategory: "[[Containers & orchestration]]"
vendor: "[[CNCF]]"
deployment: "On-premises or managed (AKS, EKS, GKE)"
status: "current"
aliases:
  - "K8s"
tags:
  - "tool"
  - "devops"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Kubernetes

> [!abstract] In plain words
> Software that runs lots of containers across many servers, restarts them when they crash and spreads the load. Often shortened to K8s.
>
> **What kind of tool is this?** A container packs an app with everything it needs so it runs the same anywhere. Orchestrators like Kubernetes run and restart many containers for you.

**Made by:** [[CNCF]] · **Runs:** On-premises or managed (AKS, EKS, GKE) · **Category:** [[DevOps & Containers]] › [[Containers & orchestration]]

> [!info]+ Words on this page
> **HTTP**: The protocol web pages use (port 80, unencrypted).
> **CPU**: The processor, the part of a computer that does the calculations.
> **container**: A packaged app with everything it needs to run, sharing the host's operating system kernel.
> **cluster**: Several servers working together so one can take over if another fails.
> **kubectl**: The command-line tool for managing Kubernetes clusters.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> **registry**: Windows' central settings database.
> *More in the [[Glossary]].*

## In more detail

Container orchestrator: a control plane schedules pods onto worker nodes, services give pods stable addresses, deployments roll out new versions and restart failed pods.

## Main parts

- Pod: one or more containers scheduled together
- Deployment: keeps N copies of a pod running and rolls out updates
- Service: a stable address for a set of pods
- Ingress: HTTP routing from outside the cluster
- Namespace: a folder-like boundary for resources
- kubectl: the command-line tool

## Alerts you'll see

- Pods in CrashLoopBackOff
- Nodes NotReady
- Persistent volume claims pending
- Certificate expiry on the control plane (self-managed clusters)

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| CrashLoopBackOff | kubectl logs POD --previous shows why the last run died |
| Pending pods | kubectl describe pod POD: usually not enough CPU/memory or an unbound volume |
| ImagePullBackOff | Wrong image name or tag, or missing registry credentials |

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
kubectl get pods -A
kubectl describe pod POD -n NS
kubectl logs POD -n NS --previous
kubectl get nodes
kubectl rollout restart deployment/NAME -n NS
kubectl get events -n NS --sort-by=.lastTimestamp
```

## See also

[[Docker]] · [[Azure Kubernetes Service]] · [[Amazon EKS]] · [[Helm]] · [[Containers vs virtual machines]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
