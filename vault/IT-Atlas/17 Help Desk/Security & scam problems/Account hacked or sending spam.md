---
type: "guide"
level: "Mid"
area: "[[Security & scam problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# Account hacked or sending spam

> [!abstract] What's going on
> People receive strange emails from the user, or there are sign-ins the user didn't make.

> [!tip] Think of it like
> Someone copied your house key: change the locks, check what they took or left behind (rules), and find how they got the copy.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Security & scam problems]]

> [!info]+ Words on this page
> **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Tell IT now. Don't just change your own password and hope.
2. Warn colleagues not to open the emails that were sent from your account.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Reset the password and revoke sessions.
- Check and remove attacker MFA methods.
- Look for inbox rules that delete or forward mail (`Get-InboxRule -Mailbox USER`) and mailbox forwarding (`Get-Mailbox USER | Select ForwardingSmtpAddress`).
- Review sign-in and audit logs to find what was accessed; check for app consents.
- Unblock sending only after the account is clean.

## Common causes and fixes

| Cause | Fix |
|---|---|
| Password phished | Reset, revoke, remove rules. |
| MFA prompt approved by mistake | Reset; remove attacker MFA method. |
| Password reused from another site breach | Reset; teach password manager use. |

## Escalate when

- Data or payments may have been affected
- Several accounts are compromised
- An admin account is involved

## Write it up

Copy this into the ticket and fill it in:

```
User and contact: 
Device: 
Problem (in their words): 
Exact error message: 
Started when / what changed: 
What I checked: 
What fixed it: 
User confirmed it's fixed (yes/no): 
```

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why check inbox rules on a hacked account?
> Attackers often add rules that hide replies or forward mail, so the user doesn't notice.

## See also

[[Clicked a phishing link]] · [[Multi-factor authentication]] · [[Microsoft Entra ID]] · [[Exchange Online]] · [[Passwords and password managers]]

## Field notes

Add your own tips and client quirks here.
