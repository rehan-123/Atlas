---
type: "playbook"
level: "Mid"
severity: "P3 (P1 if already expired on a public service)"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Certificate expiring

> [!abstract] What this alert means
> A certificate on a website, VPN or other service is about to expire.
>
> **Why it matters:** When it expires, users get security errors or can't connect at all.

**How urgent:** P3 (P1 if already expired on a public service). See [[Severity levels]].

> [!info]+ Words on this page
> **MSP**: Managed service provider: a company that runs IT for other companies.
> **VPN**: An encrypted tunnel over the internet to a private network.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> **endpoint**: Any device a user works on: laptop, desktop, phone or server.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Certificate expiring within 30 days, or expired

## First 5 minutes

1. Identify where the certificate is used: it is often on more than one device (firewall, load balancer, RD Gateway, IIS, Exchange, NPS)
2. Check who owns renewal (client, MSP or vendor) and whether it auto-renews

## Find the cause

- Wildcard certificates are often installed in many places
- Internal CA certificates and CRLs expire too

## Fix it

- Renew, install on every endpoint that uses it, bind it, restart services as needed
- Automate with ACME where possible

## Ask for help (escalate) when

- Already expired on a public service
- Internal CA root or issuing CA expiring

## Write it up

Copy this into the ticket and fill it in:

```
Certificate (subject): 
Expiry: 
Where installed: 
Action: 
Verified from outside:
```

## See also

[[Certificates & PKI]] · [[SSL & TLS]] · [[IIS]] · [[RD Gateway]] · [[AD FS]] · [[AD CS]]
