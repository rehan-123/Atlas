---
type: "concept"
level: "Mid"
category: "[[Windows & identity concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Windows Event Log

> [!abstract] In one line
> Where Windows records what happened: System, Application, Security and many Applications and Services logs.

> [!tip] Think of it like
> The black-box flight recorder of Windows.

> [!info]+ Words on this page
> **DC**: Domain controller: a server running Active Directory.
> *More in the [[Glossary]].*

## How it works

- Levels: Critical, Error, Warning, Information, plus Audit Success and Failure in Security.
- Query fast with `Get-WinEvent -FilterHashtable` instead of scrolling Event Viewer.
- Logs roll over at their size limit; increase Security log size on DCs so evidence survives.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Which three logs should you check first?
> System, Application and Security.

## See also

[[Windows Event ID reference]] · [[Windows command cheat sheet]]
