---
type: "tool"
level: "Senior"
category: "[[DevOps & Containers]]"
subcategory: "[[Secrets management]]"
vendor: "[[Microsoft]]"
deployment:
status: "current"
aliases: []
tags:
  - "tool"
  - "devops"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Azure Key Vault

> [!abstract] In plain words
> Azure's safe for secrets, encryption keys and certificates, with access controlled by Entra ID.
>
> **What kind of tool is this?** Secrets managers store passwords, API keys and certificates centrally, so they're never pasted into scripts.

**Made by:** [[Microsoft]] · **Category:** [[DevOps & Containers]] › [[Secrets management]]

> [!info]+ Words on this page
> **API**: A way for programs and scripts to talk to a service directly, without the web page.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> **container**: A packaged app with everything it needs to run, sharing the host's operating system kernel.
> *More in the [[Glossary]].*

## In more detail

Managed secrets, keys and certificates with RBAC or access policies, soft delete and purge protection; apps use managed identities to read secrets.

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Get-AzKeyVaultSecret -VaultName VAULT -Name NAME -AsPlainText
az keyvault secret show --vault-name VAULT -n NAME
```

## Good to know

- Turn on soft delete and purge protection so a deleted secret can be recovered.

## See also

[[HashiCorp Vault]] · [[Microsoft Azure]] · [[Secrets in scripts]] · [[Certificates & PKI]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
