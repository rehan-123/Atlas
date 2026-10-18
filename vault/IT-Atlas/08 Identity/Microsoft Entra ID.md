---
type: "tool"
level: "Mid"
category: "[[Identity & Access]]"
vendor: "[[Microsoft]]"
deployment: "Cloud"
status: "current"
aliases:
  - "Azure AD"
  - "Azure Active Directory"
  - "AAD"
  - "Entra"
tags:
  - "tool"
  - "identity"
as_of: "2026-06"
verified:
created: "2026-10-18"
updated: "2026-10-18"
---

# Microsoft Entra ID

> [!abstract] In plain words
> Microsoft's cloud directory (formerly Azure AD). Every Microsoft 365 sign-in goes through it.
>
> **What kind of tool is this?** Identity tools hold user accounts and decide who can sign in to what. When identity breaks, nobody can work.

**Made by:** [[Microsoft]] · **Runs:** Cloud · **Category:** [[Identity & Access]]

> [!info]+ Words on this page
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **Conditional Access**: Microsoft Entra rules that allow or block sign-ins based on user, device, location and risk.
> **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
> *More in the [[Glossary]].*

## In more detail

Microsoft's cloud identity (formerly Azure AD): users, groups, app registrations, Conditional Access, MFA, sign-in and audit logs, and Privileged Identity Management.

## Main parts

- Users, groups and devices
- Conditional Access
- Authentication methods and MFA
- App registrations and enterprise apps
- Sign-in and audit logs
- Privileged Identity Management (P2)

## Alerts you'll see

- Risky sign-ins
- MFA registration gaps
- Conditional Access failures
- Global admin changes
- App consent grants

## When it breaks: what to check first

| Problem | Check this first |
|---|---|
| User cannot sign in | Read the sign-in log entry: the failure reason and the Conditional Access tab show why |
| Hybrid join not working | dsregcmd /status on the device and Entra Connect device sync settings |

## Handy commands

Words in CAPITALS are placeholders: replace them with your own values before running.

```
Connect-MgGraph -Scopes 'User.Read.All','AuditLog.Read.All'
Get-MgUser -UserId UPN
dsregcmd /status
```

## See also

[[Microsoft Entra Connect]] · [[Microsoft Graph]] · [[Microsoft 365]] · [[Multi-factor authentication]] · [[Zero Trust]]

## Field notes

Add your own tips, client quirks and fixes here as you learn.
