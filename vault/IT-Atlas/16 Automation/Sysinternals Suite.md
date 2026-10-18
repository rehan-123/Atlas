---
type: "tool"
level: "Mid"
category: "[[Automation & Scripting]]"
vendor: "[[Microsoft]]"
deployment: "Standalone tools"
status: "current"
aliases:
  - "Sysinternals"
  - "Procmon"
  - "Process Explorer"
tags:
  - "tool"
  - "automation"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Sysinternals Suite

> [!abstract] In plain words
> Free Microsoft troubleshooting tools, like Process Explorer (a powerful Task Manager) and Process Monitor.
>
> **What kind of tool is this?** Scripting and automation tools let you do a task once in code and then repeat it on hundreds of machines.

**Made by:** [[Microsoft]] · **Runs:** Standalone tools · **Category:** [[Automation & Scripting]]

> [!info]+ Words on this page
> **Task Manager**: Windows tool (Ctrl+Shift+Esc) that shows running apps and what's using CPU, memory and disk.
> *More in the [[Glossary]].*

## In more detail

Microsoft's troubleshooting toolkit: Process Explorer, Process Monitor, Autoruns, TCPView, PsExec, RAMMap and more.

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
procmon.exe /AcceptEula
autorunsc.exe -a * -c -h -s
psexec -s -i cmd.exe
tcpview.exe
```

## See also

[[High CPU]] · [[High memory]] · [[Windows command cheat sheet]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
