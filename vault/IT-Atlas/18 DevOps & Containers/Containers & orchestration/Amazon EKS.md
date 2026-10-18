---
type: "tool"
level: "Senior"
category: "[[DevOps & Containers]]"
subcategory: "[[Containers & orchestration]]"
vendor: "[[Amazon Web Services]]"
deployment: "AWS"
status: "current"
aliases:
  - "EKS"
  - "Elastic Kubernetes Service"
tags:
  - "tool"
  - "devops"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Amazon EKS

> [!abstract] In plain words
> Amazon's managed Kubernetes service on AWS.
>
> **What kind of tool is this?** A container packs an app with everything it needs so it runs the same anywhere. Orchestrators like Kubernetes run and restart many containers for you.

**Made by:** [[Amazon Web Services]] · **Runs:** AWS · **Category:** [[DevOps & Containers]] › [[Containers & orchestration]]

> [!info]+ Words on this page
> **container**: A packaged app with everything it needs to run, sharing the host's operating system kernel.
> *More in the [[Glossary]].*

## In more detail

Managed Kubernetes on AWS: managed control plane, managed node groups or Fargate, IAM roles for service accounts.

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
aws eks update-kubeconfig --name CLUSTER --region REGION
aws eks describe-cluster --name CLUSTER
```

## See also

[[Kubernetes]] · [[Amazon Web Services]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
