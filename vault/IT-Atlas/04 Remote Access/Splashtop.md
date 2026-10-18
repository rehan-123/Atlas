---
type: "tool"
level: "Junior"
category: "[[Remote Access]]"
vendor: "[[Splashtop]]"
deployment: "SaaS or on-prem"
status: "current"
agent_service: "Splashtop Remote Service"
aliases: []
tags:
  - "tool"
  - "remote-access"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Splashtop

> [!abstract] In plain words
> A remote control tool built into several RMMs.
>
> **What kind of tool is this?** Remote access tools let you see and control someone's screen, or log in to a server, from wherever you are.

**Made by:** [[Splashtop]] · **Runs:** SaaS or on-prem · **Category:** [[Remote Access]]

> [!info]+ Words on this page
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **SaaS**: Software as a service: apps you use online, such as Microsoft 365.
> **agent**: A small program installed on a computer that reports to, and takes orders from, a central console.
> *More in the [[Glossary]].*

## In more detail

Remote access and support with a Streamer agent; embedded in several RMMs (Syncro, Atera, others).

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`Splashtop Remote Service`

## See also

[[Syncro]] · [[Atera]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
