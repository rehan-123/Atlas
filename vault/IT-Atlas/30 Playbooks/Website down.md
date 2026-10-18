---
type: "playbook"
level: "Mid"
severity: "P1 or P2"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Website down

> [!abstract] What this alert means
> A website isn't answering properly.
>
> **Why it matters:** Customers or staff can't use it.

**How urgent:** P1 or P2. See [[Severity levels]].

> [!info]+ Words on this page
> **HTTP**: The protocol web pages use (port 80, unencrypted).
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **TLS**: The encryption behind HTTPS and many other secure connections.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- HTTP check failing
- Users report site down

## First 5 minutes

1. Check from outside (another network or an uptime service)
2. Check DNS, TLS certificate and the HTTP status code

## Find the cause

- DNS not resolving or pointing to the wrong IP
- Certificate expired
- Web server or app pool stopped (503)
- App error (500)
- Firewall or load balancer change

## Fix it

- Fix DNS or the certificate
- Restart the app pool or service
- Roll back a recent change

## Ask for help (escalate) when

- Customer-facing site down for more than 15 minutes

## Write it up

Copy this into the ticket and fill it in:

```
URL: 
Status code: 
Down since: 
Cause: 
Action:
```

## See also

[[IIS]] · [[Certificate expiring]] · [[DNS]] · [[Uptime Kuma]] · [[Synthetic monitoring]]
