---
type: "tool"
level: "Junior"
category: "[[Remote Access]]"
vendor: "[[AnyDesk]]"
deployment: "SaaS or on-prem"
status: "current"
agent_service: "AnyDesk"
aliases: []
tags:
  - "tool"
  - "remote-access"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# AnyDesk

> [!abstract] In plain words
> A lightweight remote control tool, also often abused by scammers.
>
> **What kind of tool is this?** Remote access tools let you see and control someone's screen, or log in to a server, from wherever you are.

**Made by:** [[AnyDesk]] · **Runs:** SaaS or on-prem · **Category:** [[Remote Access]]

> [!info]+ Words on this page
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **TCP**: A connection-based network protocol that confirms delivery.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> **ransomware**: Malware that encrypts files and demands payment to unlock them.
> *More in the [[Glossary]].*

## In more detail

Lightweight remote desktop tool popular for ad-hoc support.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`AnyDesk`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 80, 443 and 6568/TCP outbound

## Good to know

- February 2024: AnyDesk disclosed a breach of its production systems and revoked its code-signing certificate. Update old clients.
- Heavily abused by scammers and ransomware operators. Watch for unexpected installs.

## See also

[[TeamViewer]] · [[Atera]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
