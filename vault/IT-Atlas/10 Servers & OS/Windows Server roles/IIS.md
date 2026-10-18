---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Windows Server roles]]"
vendor: "[[Microsoft]]"
deployment: "Windows Server role"
status: "current"
agent_service: "W3SVC, WAS"
aliases:
  - "Internet Information Services"
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# IIS

> [!abstract] In plain words
> Microsoft's web server: it runs websites and web apps on Windows Server.
>
> **What kind of tool is this?** Roles are the jobs a Windows server can do: hand out IP addresses, host files, run remote desktops and so on.

**Made by:** [[Microsoft]] · **Runs:** Windows Server role · **Category:** [[Servers & Operating Systems]] › [[Windows Server roles]]

> [!info]+ Words on this page
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **HTTP**: The protocol web pages use (port 80, unencrypted).
> **TCP**: A connection-based network protocol that confirms delivery.
> **driver**: Small program that lets the operating system talk to a piece of hardware, like a printer or graphics card.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> **retention**: How long backups or logs are kept.
> *More in the [[Glossary]].*

## In more detail

Microsoft's web server: sites, bindings, application pools (w3wp.exe worker processes) and the HTTP.sys kernel driver.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`W3SVC, WAS`

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 80/TCP
- 443/TCP

## Alerts you'll see

- Site down (HTTP check fails)
- Application pool stopped (rapid-fail protection)
- Certificate expiring on a binding
- HTTP 500 and 503 errors

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| 503 Service Unavailable | The app pool is probably stopped; check the System log for WAS events and why it crashed |
| 500 errors | Check the app's own logs and the IIS log sub-status code |
| Disk filling | IIS logs are not cleaned up by default; add a retention task |

## Where to find its logs

- `C:\inetpub\logs\LogFiles`
- `C:\Windows\System32\LogFiles\HTTPERR`

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-IISAppPool
Start-WebAppPool -Name POOL
%windir%\system32\inetsrv\appcmd list apppool
iisreset /status
netsh http show sslcert
```

## See also

[[Website down]] · [[Certificate expiring]] · [[Low disk space]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
