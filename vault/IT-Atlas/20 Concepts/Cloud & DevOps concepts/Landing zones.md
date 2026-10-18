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

# Landing zones

> [!abstract] In one line
> A ready-made, secure starting layout for a cloud tenant: subscriptions, networks, identity and policies set up before workloads move in.

> [!tip] Think of it like
> Laying roads, water and electricity before building houses on a plot.

> [!info]+ Words on this page
> **tenant**: One organization's own space in a cloud service such as Microsoft 365.
> *More in the [[Glossary]].*

## How it works

- Defines management groups and subscriptions, hub-and-spoke networking, logging, policies and access.
- Microsoft's Cloud Adoption Framework and AWS Control Tower provide reference designs.
- Building it first avoids every project inventing its own network and permissions.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why build a landing zone before migrating the first server?
> So networking, identity, logging and policies are consistent and secure from day one instead of retrofitted.

## See also

[[Microsoft Azure]] · [[Amazon Web Services]] · [[Network segmentation]]
