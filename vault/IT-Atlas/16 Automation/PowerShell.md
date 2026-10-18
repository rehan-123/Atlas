---
type: "tool"
level: "Mid"
category: "[[Automation & Scripting]]"
vendor: "[[Microsoft]]"
deployment: "Windows PowerShell 5.1 built in; PowerShell 7 cross-platform"
status: "current"
aliases:
  - "PowerShell 7"
  - "pwsh"
  - "Windows PowerShell"
tags:
  - "tool"
  - "automation"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# PowerShell

> [!abstract] In plain words
> Windows' scripting language and command line. The single most useful skill for a Windows NOC engineer.
>
> **What kind of tool is this?** Scripting and automation tools let you do a task once in code and then repeat it on hundreds of machines.

**Made by:** [[Microsoft]] · **Runs:** Windows PowerShell 5.1 built in; PowerShell 7 cross-platform · **Category:** [[Automation & Scripting]]

> [!info]+ Words on this page
> **NOC**: Network operations center: the team that monitors and fixes infrastructure.
> **TCP**: A connection-based network protocol that confirms delivery.
> **HTTP**: The protocol web pages use (port 80, unencrypted).
> **HTTPS**: Encrypted HTTP (port 443).
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## In more detail

The Windows automation language. Windows PowerShell 5.1 ships with Windows; PowerShell 7 (pwsh) is the cross-platform successor and runs side by side.

## Network ports it uses

Firewalls between the parts of this tool must allow these:

- 5985/TCP WinRM HTTP
- 5986/TCP WinRM HTTPS

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
$PSVersionTable
Enter-PSSession -ComputerName HOST
Invoke-Command -ComputerName HOST -ScriptBlock { Get-Service }
Get-ExecutionPolicy -List
Test-WSMan HOST
```

## Good to know

- RMM scripts usually run as SYSTEM in 32-bit or 64-bit PowerShell 5.1; check which before assuming modules or paths exist.

## See also

[[Microsoft Graph]] · [[Windows command cheat sheet]] · [[Git]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
