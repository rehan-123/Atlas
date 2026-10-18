---
type: "moc"
level: "All"
tags:
  - "moc"
  - "identity"
created: "2026-10-18"
updated: "2026-10-18"
---

# Identity & Access

> [!abstract] In plain words
> Identity tools hold user accounts and decide who can sign in to what. When identity breaks, nobody can work.

Directories, sync, authentication and certificates. When identity breaks, everything breaks.

Back to [[Home]].

> [!note]- How seniors think about this area
> - Identity is the new perimeter: phishing-resistant MFA for admins, conditional access for everyone.
> - Separate admin accounts, use just-in-time elevation (PIM) and tier the environment.
> - Automate joiner/mover/leaver processes; stale accounts and group memberships are the usual audit finding.
> - Plan for break-glass accounts excluded from conditional access, monitored and tested.

## Tools

- [[Active Directory]]: The on-site directory of users, computers and groups in a Windows domain. Domain controllers run it, and almost every login in the office depends on it.
- [[Microsoft Entra ID]]: Microsoft's cloud directory (formerly Azure AD). Every Microsoft 365 sign-in goes through it.
- [[Microsoft Entra Connect]]: Copies users and passwords from on-site Active Directory to Entra ID every 30 minutes, so people have one account for both (formerly Azure AD Connect).
- [[Entra Cloud Sync]]: A lighter, cloud-managed alternative to Entra Connect.
- [[AD FS]]: An older on-site system that handles sign-ins to cloud apps for Active Directory users. Being replaced by Entra ID.
- [[AD CS]]: Windows' own certificate authority. It issues the digital certificates used for Wi-Fi, VPN and servers.
- [[Group Policy]]: Settings pushed from Active Directory to every domain computer and user: password rules, mapped drives, security settings and more.
- [[NPS]]: Windows' RADIUS server: it checks usernames and passwords when people join Wi-Fi or VPN.
- [[Okta]]: A cloud sign-in service: one login (with MFA) for many apps.
- [[Duo Security]]: Adds a phone approval (MFA) step to VPN, RDP and Windows logins.
- [[JumpCloud]]: A cloud directory for companies with a mix of Windows, Mac and Linux.
- [[Microsoft Entra Privileged Identity Management]]: Lets admins switch on their admin rights only when needed and for a limited time, with approval and a reason.
- [[Microsoft Entra Domain Services]]: A managed domain in Azure for old apps that need Kerberos, LDAP or Group Policy, without running your own domain controllers.
- [[Microsoft Authenticator]]: Microsoft's phone app for approving sign-ins, showing codes and signing in without a password.
- [[Ping Identity]]: An enterprise single sign-on and identity platform, often found in large companies alongside or instead of Okta.

## Playbooks for this area

[[AD replication failure]] · [[Account lockout storm]] · [[Certificate expiring]] · [[Certificate trust errors]] · [[DNS resolution failure]] · [[Domain controller failure]] · [[Entra Connect sync errors]] · [[Group Policy not applying]] · [[High memory]] · [[Kerberos authentication failures]]

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "08 Identity"
WHERE type = "tool"
SORT file.name ASC
```
