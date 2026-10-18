---
type: "tool"
level: "Mid"
category: "[[Servers & Operating Systems]]"
subcategory: "[[Windows Server roles]]"
vendor: "[[Microsoft]]"
deployment:
status: "current"
agent_service: "mpssvc"
aliases:
  - "Windows Firewall"
tags:
  - "tool"
  - "servers"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Windows Defender Firewall

> [!abstract] In plain words
> The firewall built into every Windows PC and server, with separate rules for domain, private and public networks.
>
> **What kind of tool is this?** Roles are the jobs a Windows server can do: hand out IP addresses, host files, run remote desktops and so on.

**Made by:** [[Microsoft]] · **Category:** [[Servers & Operating Systems]] › [[Windows Server roles]]

> [!info]+ Words on this page
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **DC**: Domain controller: a server running Active Directory.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

Host firewall with Domain/Private/Public profiles, inbound and outbound rules, managed by Group Policy or Intune.

## Service to check

If this tool stops reporting, check that this Windows service is running (`Get-Service` in PowerShell, or services.msc):

`mpssvc`

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| App works with the firewall off | Add a specific inbound rule for its port or program instead of turning the firewall off |
| Server shows Public profile | Network Location Awareness didn't detect the domain; restart the NlaSvc service or check DNS to the DCs |

## Where to find its logs

- `%windir%\System32\LogFiles\Firewall\pfirewall.log (if logging enabled)`

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-NetFirewallProfile | Select Name, Enabled
Get-NetConnectionProfile
New-NetFirewallRule -DisplayName NAME -Direction Inbound -Protocol TCP -LocalPort PORT -Action Allow
```

## See also

[[Firewalls]] · [[Group Policy]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
