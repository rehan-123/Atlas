---
type: "concept"
level: "Senior"
category: "[[Advanced troubleshooting]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Process Monitor tracing

> [!abstract] In one line
> Watching every file, registry and process action an app makes, to find what it's failing on.

> [!tip] Think of it like
> Following someone through a building and writing down every door they tried and which ones were locked.

> [!info]+ Words on this page
> **registry**: Windows' central settings database.
> *More in the [[Glossary]].*

## How it works

- Sysinternals Process Monitor (procmon) records file, registry, network and process events live.
- Filter by process name, then look for **ACCESS DENIED**, **NAME NOT FOUND** and **PATH NOT FOUND** near the moment of failure.
- Great for: apps failing only for some users, install errors, permission problems.
- It records a lot: capture for a short time, then save and filter.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- An app works for admins but not users. What does procmon usually reveal?
> An ACCESS DENIED on a file or registry key the app needs, which users don't have rights to.

## See also

[[Sysinternals Suite]] · [[App crashes or won't open]]
