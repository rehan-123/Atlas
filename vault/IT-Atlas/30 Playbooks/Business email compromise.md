---
type: "playbook"
level: "Senior"
severity: "P1"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Business email compromise

> [!abstract] What this alert means
> An attacker has control of a mailbox (or a lookalike) and is using it to trick people, often into paying fake invoices.
>
> **Why it matters:** Financial loss can be immediate and permanent; attackers also hide in mailboxes using rules and forwarding.

**How urgent:** P1. See [[Severity levels]].

> [!info]+ Words on this page
> **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **message trace**: Exchange tool that shows whether an email arrived, where it went and why.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Clients or suppliers report odd payment requests
- Inbox rules that forward or delete mail
- Impossible-travel or unfamiliar sign-ins

## First 5 minutes

1. Reset the password and revoke all sessions
2. Remove malicious inbox rules, forwarding and unknown MFA methods
3. Tell the finance team and the client's bank immediately if a payment may have been made

## Find the cause

- Sign-in logs and Unified Audit Log for the first malicious sign-in
- OAuth app consents granted by the user
- Message trace for emails sent by the attacker
- Other mailboxes targeted or compromised

## Fix it

- Block attacker IPs and revoke app consents
- Enforce MFA (phishing-resistant for finance roles) and conditional access
- Notify recipients of fraudulent emails

## Ask for help (escalate) when

- Always escalate to security lead and client management
- Money transferred
- Regulated data in the mailbox (legal and notification duties)

## Write it up

Copy this into the ticket and fill it in:

```
Mailbox: 
First malicious sign-in: 
Rules/forwarding found: 
Emails sent by attacker: 
Payments affected: 
Containment steps:
```

## See also

[[Account hacked or sending spam]] · [[Microsoft Defender for Office 365]] · [[Multi-factor authentication]] · [[Microsoft Purview]]
