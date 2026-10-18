---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Windows Server roles]]"
vendor: "[[Microsoft]]"
deployment:
status: "current"
agent_service: "Wecsvc (collector), WinRM"
aliases:
  - "WEF"
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Windows Event Forwarding

> [!abstract] In plain words
> Built-in Windows feature that sends chosen events from many PCs to one collector server, without buying a log tool.
>
> **What kind of tool is this?** Roles are the jobs a Windows server can do: hand out IP addresses, host files, run remote desktops and so on.

**Made by:** [[Microsoft]] · **Category:** [[Servers & Operating Systems]] › [[Windows Server roles]]

> [!info]+ Words on this page
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> *More in the [[Glossary]].*

## In more detail

Source-initiated subscriptions over WinRM: clients forward events matching XPath queries to a Windows Event Collector.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`Wecsvc (collector), WinRM`

## See also

[[Windows Event Log]] · [[SIEM]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
