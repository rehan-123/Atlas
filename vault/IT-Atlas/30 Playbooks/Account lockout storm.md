---
type: "playbook"
level: "Mid"
severity: "P2"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Account lockout storm

> [!abstract] What this alert means
> Lots of accounts, or one account over and over, are getting locked out.
>
> **Why it matters:** It's either a device with an old saved password, or someone guessing passwords.

**How urgent:** P2. See [[Severity levels]].

> [!info]+ Words on this page
> **RDP**: Remote Desktop Protocol: Windows' built-in remote desktop, on port 3389.
> **VPN**: An encrypted tunnel over the internet to a private network.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Many lockouts (event 4740) in a short time
- Users repeatedly locked out

## First 5 minutes

1. Find the source: event 4740 on the PDC emulator lists the caller computer
2. Check whether it is one user (stale credentials) or many (attack)

## Find the cause

- One user: old password saved on a phone, mapped drive, scheduled task or service
- Many users from one source: password spraying or a brute-force attack (RDP, VPN, OWA)

## Fix it

- Clear stale credentials on the source device
- Block the attacking IP and close exposed services
- Enforce MFA

## Ask for help (escalate) when

- Many accounts targeted
- Any successful logon from the attacking source

## Write it up

Copy this into the ticket and fill it in:

```
Accounts: 
Source (caller computer / IP): 
Cause: 
Action:
```

## See also

[[Active Directory]] · [[Kerberos]] · [[RDP]] · [[Suspected ransomware]]
