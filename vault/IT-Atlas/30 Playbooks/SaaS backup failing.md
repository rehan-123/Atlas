---
type: "playbook"
level: "Mid"
severity: "P3 (P2 if tenant-wide)"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# SaaS backup failing

> [!abstract] What this alert means
> Microsoft 365 or Google Workspace backups are failing for some or all users.
>
> **Why it matters:** Deleted or encrypted mail and files can't be restored for those users.

**How urgent:** P3 (P2 if tenant-wide). See [[Severity levels]].

> [!info]+ Words on this page
> **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
> **API**: A way for programs and scripts to talk to a service directly, without the web page.
> **EWS**: Exchange Web Services, an older way for apps to access mailboxes. Microsoft is retiring it in Exchange Online.
> **tenant**: One organization's own space in a cloud service such as Microsoft 365.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Microsoft 365 or Google Workspace backup errors
- Users or sites unprotected

## First 5 minutes

1. Check whether it is one user, one service (mail, OneDrive, SharePoint) or the whole tenant
2. Check for re-authorization or consent prompts in the backup portal

## Find the cause

- Tenant-wide failure: app consent revoked, service account disabled or MFA added to it, or a Microsoft API change (for example the EWS retirement)
- Single user: mailbox moved, license removed, or user deleted
- Coverage gaps: new users or shared mailboxes not auto-assigned

## Fix it

- Re-authorize the backup app with a Global Admin and confirm consent
- Fix auto-assignment rules and license counts
- Re-run the backup and confirm

## Ask for help (escalate) when

- Tenant-wide failure for more than 24 hours
- Unprotected users who hold critical data

## Write it up

Copy this into the ticket and fill it in:

```
Tenant: 
Scope (users / services): 
Error: 
Action: 
Coverage after fix:
```

## See also

[[SaaS backup]] · [[Spanning Backup]] · [[Microsoft Graph]] · [[Exchange Online]] · [[SaaS shared responsibility]]
