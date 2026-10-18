---
type: "playbook"
level: "Mid"
severity: "P2 or P3"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Certificate trust errors

> [!abstract] What this alert means
> Clients refuse a connection because they don't trust a server's certificate.
>
> **Why it matters:** Users see warnings or apps fail completely; teaching users to click through warnings is dangerous.

**How urgent:** P2 or P3. See [[Severity levels]].

> [!info]+ Words on this page
> **VPN**: An encrypted tunnel over the internet to a private network.
> **SAN**: Storage area network: shared block storage for servers.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **browser**: The app you use to open websites: Edge, Chrome, Safari or Firefox.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Browser 'Your connection isn't private'
- App errors like 'The remote certificate is invalid'
- VPN or RADIUS sign-ins failing after a renewal

## First 5 minutes

1. Open the certificate and check the name (SAN), expiry and issuer
2. Check the full chain is sent by the server
3. Check the client clock

## Find the cause

- Missing intermediate certificate
- Internal CA root not distributed to that device (BYOD, non-domain)
- Name mismatch (accessing by IP or short name)
- Revocation list (CRL/OCSP) unreachable

## Fix it

- Install the full chain on the server
- Deploy the internal root via Group Policy or Intune
- Reissue the certificate with the right SANs

## Ask for help (escalate) when

- Public-facing service down
- Internal CA problems (expired CA certificate, broken CRL publishing)

## Write it up

Copy this into the ticket and fill it in:

```
Service: 
Error: 
Chain check: 
Cause: 
Fix:
```

## See also

[[Certificate chain troubleshooting]] · [[Certificates & PKI]] · [[Certificate expiring]] · [[AD CS]]
