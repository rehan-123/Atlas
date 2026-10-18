---
type: "moc"
level: "All"
tags:
  - "moc"
  - "automation"
created: "2026-10-18"
updated: "2026-10-18"
---

# Automation & Scripting

> [!abstract] In plain words
> Scripting and automation tools let you do a task once in code and then repeat it on hundreds of machines.

Languages, tools and platforms used to automate NOC work.

Back to [[Home]].

> [!note]- How seniors think about this area
> - Make scripts idempotent (safe to run twice), log what they did and support -WhatIf.
> - Store code in Git, review changes, test on a pilot group before fleet-wide runs.
> - Never hard-code secrets; use vaults, managed identities or the RMM's secure variables.

## Tools

- [[PowerShell]]: Windows' scripting language and command line. The single most useful skill for a Windows NOC engineer.
- [[Bash]]: The command line and scripting language on Linux.
- [[Python]]: A general programming language, good for working with APIs and data.
- [[Ansible]]: Applies the same configuration to many servers at once from a simple text file.
- [[Terraform]]: Builds cloud resources from text files, so they can be recreated exactly.
- [[Rewst]]: An automation platform for MSPs: it connects the PSA, RMM and Microsoft 365 to automate things like onboarding a new user.
- [[Power Automate]]: Microsoft's drag-and-drop automation for Microsoft 365 and other apps.
- [[n8n]]: A drag-and-drop automation tool you can host yourself.
- [[Azure Automation]]: Runs PowerShell scripts on a schedule from Azure.
- [[Git]]: Keeps every version of your scripts, so you can see what changed and undo mistakes.
- [[Sysinternals Suite]]: Free Microsoft troubleshooting tools, like Process Explorer (a powerful Task Manager) and Process Monitor.
- [[Windows Admin Center]]: Manages Windows servers from a web browser.
- [[Microsoft Graph PowerShell SDK]]: The PowerShell modules for managing Microsoft 365 and Entra ID through Microsoft Graph; they replace the retired AzureAD and MSOnline modules.
- [[Azure Logic Apps]]: Azure's drag-and-drop workflow service for automating tasks between apps, like Power Automate but for IT and developers.
- [[ImmyBot]]: An MSP tool that sets up new computers and keeps their software and settings in a defined state.

## Playbooks for this area

[[High CPU]] · [[High memory]]

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "16 Automation"
WHERE type = "tool"
SORT file.name ASC
```
