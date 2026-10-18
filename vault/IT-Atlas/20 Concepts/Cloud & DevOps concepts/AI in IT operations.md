---
type: "concept"
level: "Mid"
category: "[[Cloud & DevOps concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# AI in IT operations

> [!abstract] In one line
> Using AI assistants to summarize tickets, write scripts and search knowledge, with a human checking the result.

> [!tip] Think of it like
> A very fast junior colleague: great first drafts, but a senior signs off before anything goes live.

## How it works

- Good uses: summarizing long ticket threads, drafting user replies, explaining logs, drafting scripts, searching documentation.
- Always review generated commands before running them, especially anything that deletes or changes permissions.
- Never paste client passwords, keys or personal data into tools that aren't approved for it.
- Copilots respect existing permissions, so oversharing in SharePoint becomes visible through AI: fix permissions first.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- An AI tool suggests a PowerShell command to clean up mailboxes. What do you do before running it?
> Read and understand it, test it on one item or with -WhatIf, and make sure there's a backup or a way to undo.

## See also

[[Microsoft 365 Copilot]] · [[ChatGPT Enterprise]] · [[Microsoft Copilot Studio]]
