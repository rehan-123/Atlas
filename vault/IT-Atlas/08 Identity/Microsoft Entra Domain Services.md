---
type: "tool"
level: "Mid"
category: "[[Identity & Access]]"
vendor: "[[Microsoft]]"
deployment:
status: "current"
aliases:
  - "Entra Domain Services"
  - "Azure AD DS"
tags:
  - "tool"
  - "identity"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Microsoft Entra Domain Services

> [!abstract] In plain words
> A managed domain in Azure for old apps that need Kerberos, LDAP or Group Policy, without running your own domain controllers.
>
> **What kind of tool is this?** Identity tools hold user accounts and decide who can sign in to what. When identity breaks, nobody can work.

**Made by:** [[Microsoft]] · **Category:** [[Identity & Access]]

> [!info]+ Words on this page
> **LDAP**: The protocol apps use to look up users and groups in a directory.
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **domain controller**: A server running Active Directory that checks logins.
> *More in the [[Glossary]].*

## In more detail

Managed AD DS-compatible domain synced one-way from Entra ID; supports domain join, LDAP, Kerberos/NTLM and Group Policy; you aren't Domain Admin.

## See also

[[Active Directory]] · [[Microsoft Entra ID]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
