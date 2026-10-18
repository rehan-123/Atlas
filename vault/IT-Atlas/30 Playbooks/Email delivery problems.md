---
type: "playbook"
level: "Mid"
severity: "P2"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Email delivery problems

> [!abstract] What this alert means
> Mail isn't arriving, is bouncing back, or lands in spam.
>
> **Why it matters:** Business communication stops.

**How urgent:** P2. See [[Severity levels]].

> [!info]+ Words on this page
> **SPF**: A DNS record listing which servers may send email for a domain.
> **DKIM**: An email signature that proves a message really came from your domain and wasn't changed.
> **DMARC**: An email rule that tells receivers what to do with mail that fails SPF or DKIM checks.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **message trace**: Exchange tool that shows whether an email arrived, where it went and why.
> **quarantine**: A holding area for suspicious emails or files, so they can't do harm.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Mail not arriving or bouncing
- Queues growing
- Mail landing in spam

## First 5 minutes

1. Get an example: sender, recipient, time and any bounce (NDR) text
2. Run a message trace

## Find the cause

- NDR codes: 5.7.x is policy or authentication, 5.1.x is a bad address, 4.x.x is temporary
- SPF, DKIM or DMARC failures
- Connector or gateway problem
- Sending IP on a blocklist

## Fix it

- Fix DNS records
- Release from quarantine or adjust policy
- Fix the connector
- Request delisting after fixing the cause

## Ask for help (escalate) when

- All mail affected
- Account compromise suspected (mail being sent by an attacker)

## Write it up

Copy this into the ticket and fill it in:

```
Example message: 
Trace result: 
NDR: 
Cause: 
Action:
```

## See also

[[Exchange Online]] · [[SPF, DKIM & DMARC]] · [[Microsoft Defender for Office 365]] · [[Exchange Server]]
