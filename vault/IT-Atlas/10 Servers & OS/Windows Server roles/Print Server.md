---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Windows Server roles]]"
vendor: "[[Microsoft]]"
deployment: "Windows Server role"
status: "current"
agent_service: "Spooler"
aliases: []
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Print Server

> [!abstract] In plain words
> A Windows server that shares printers with everyone.
>
> **What kind of tool is this?** Roles are the jobs a Windows server can do: hand out IP addresses, host files, run remote desktops and so on.

**Made by:** [[Microsoft]] · **Runs:** Windows Server role · **Category:** [[Servers & Operating Systems]] › [[Windows Server roles]]

> [!info]+ Words on this page
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **spooler**: The Windows service that queues print jobs before they go to the printer.
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> **domain controller**: A server running Active Directory that checks logins.
> *More in the [[Glossary]].*

## In more detail

Windows print serving through the Print Spooler service, with drivers and queues shared to clients.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`Spooler`

## Alerts you'll see

- Spooler stopped or crashing
- Queues stuck

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Jobs stuck | Stop the Spooler, clear C:\Windows\System32\spool\PRINTERS, start the Spooler |
| Spooler crashes | Usually a bad driver; isolate drivers or remove the offending one |

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Restart-Service Spooler
Get-Printer
Get-PrintJob -PrinterName PRINTER
```

## Good to know

- 2021 PrintNightmare (CVE-2021-34527) allowed remote code execution through the spooler. Disable the Spooler on servers that do not print, especially domain controllers.

## See also

[[Windows service stopped]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
