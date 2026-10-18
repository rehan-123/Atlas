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

# Secrets in scripts

> [!abstract] In one line
> Passwords and API keys must never be typed into scripts; scripts should fetch them from a vault at run time.

> [!tip] Think of it like
> Don't tape the house key to the front door; keep it in a lockbox only trusted people can open.

> [!info]+ Words on this page
> **RMM**: Remote monitoring and management: the MSP's main tool for watching and fixing client machines.
> **API**: A way for programs and scripts to talk to a service directly, without the web page.
> *More in the [[Glossary]].*

## How it works

- Hard-coded passwords end up in Git history, RMM logs and screenshots.
- Use a vault (Azure Key Vault, HashiCorp Vault, your RMM's secure variables, Windows Credential Manager for local use).
- Prefer **managed identities** or certificate-based app registrations over passwords.
- If a secret leaks, **rotate it**: deleting the file doesn't un-leak it.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- You find an admin password in a script committed to Git last year. Is deleting the line enough?
> No. It's still in the Git history and may have been copied. Rotate the password, then remove it from the script.

## See also

[[Azure Key Vault]] · [[HashiCorp Vault]] · [[Microsoft Graph PowerShell SDK]]
