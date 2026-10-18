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

# IaaS, PaaS and SaaS

> [!abstract] In one line
> Three ways to rent IT: rent the servers (IaaS), rent a platform to run your code (PaaS) or rent the finished app (SaaS).

> [!tip] Think of it like
> Pizza: make it at home (on-premises), buy a take-and-bake (IaaS), get delivery (PaaS) or eat at the restaurant (SaaS).

> [!info]+ Words on this page
> **VM**: Virtual machine: a computer that runs as software on a physical server.
> **SQL**: Structured Query Language; also short for Microsoft SQL Server.
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> *More in the [[Glossary]].*

## How it works

- **IaaS** (Infrastructure as a Service): virtual machines, disks and networks, e.g. Azure VMs, AWS EC2. You patch the OS.
- **PaaS** (Platform as a Service): the provider runs the OS and runtime, you bring the app or data, e.g. Azure SQL Database, App Service.
- **SaaS** (Software as a Service): a finished app, e.g. Microsoft 365, Salesforce. You manage users, settings and data.
- The further right you go, the less you manage, but you **always** own your identities, data and configuration.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Who patches the operating system of an Azure virtual machine?
> You do. A VM is IaaS: Microsoft runs the hardware and hypervisor, you run the OS.

> [!question]- Microsoft 365 is SaaS. Who is responsible if a user deletes their mailbox contents?
> You are. Microsoft keeps the service running; recovering deleted data is the customer's job, which is why SaaS backup exists.

## See also

[[SaaS shared responsibility]] · [[Microsoft Azure]] · [[Amazon Web Services]] · [[Microsoft 365]]
