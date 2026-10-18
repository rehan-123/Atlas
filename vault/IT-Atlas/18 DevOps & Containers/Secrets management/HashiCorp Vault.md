---
type: "tool"
level: "Senior"
category: "[[DevOps & Containers]]"
subcategory: "[[Secrets management]]"
vendor: "[[HashiCorp]]"
deployment:
status: "current"
aliases:
  - "Vault"
tags:
  - "tool"
  - "devops"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# HashiCorp Vault

> [!abstract] In plain words
> A secure vault for passwords, API keys and certificates that scripts and apps can request when they need them.
>
> **What kind of tool is this?** Secrets managers store passwords, API keys and certificates centrally, so they're never pasted into scripts.

**Made by:** [[HashiCorp]] · **Category:** [[DevOps & Containers]] › [[Secrets management]]

> [!info]+ Words on this page
> **API**: A way for programs and scripts to talk to a service directly, without the web page.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> **container**: A packaged app with everything it needs to run, sharing the host's operating system kernel.
> *More in the [[Glossary]].*

## In more detail

Secrets management with dynamic secrets, encryption as a service and PKI; must be unsealed after restart.

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| Vault is sealed after a restart | It needs its unseal keys (or auto-unseal) before anything can read secrets |

## See also

[[Azure Key Vault]] · [[Secrets in scripts]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
