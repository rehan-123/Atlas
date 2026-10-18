---
type: "playbook"
level: "Mid"
severity: "P2"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# VPN tunnel down

> [!abstract] What this alert means
> A VPN connection between sites, or for remote users, isn't working.
>
> **Why it matters:** People can't reach resources at the other site.

**How urgent:** P2. See [[Severity levels]].

> [!info]+ Words on this page
> **WAN**: Wide area network: links between sites, or to the internet.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **UDP**: A fast network protocol that doesn't confirm delivery.
> **NAT**: Network address translation: many private devices sharing one public IP.
> **VPN**: An encrypted tunnel over the internet to a private network.
> **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
> **tunnel**: An encrypted connection that carries traffic across another network.
> **firmware**: The software built into hardware such as firewalls, disks and servers.
> *More in the [[Glossary]].*

## You'll see this when

- Site-to-site tunnel down
- Remote users cannot connect

## First 5 minutes

1. Check both WANs are up
2. Check phase 1 and phase 2 status on both ends
3. Ask whether anything changed on either side (IP, firmware, proposals)

## Find the cause

- Phase 1 down: peer IP, PSK or proposal mismatch, UDP 500 and 4500 blocked
- Phase 2 down: subnet or proposal mismatch
- Tunnel up but no traffic: routes, policies or NAT on VPN traffic
- Remote access: certificate expiry, MFA service, IP pool exhausted

## Fix it

- Correct the mismatch
- Bring the tunnel down and up
- Fix routes or policies

## Ask for help (escalate) when

- Third-party end needs changes
- Many remote users affected

## Write it up

Copy this into the ticket and fill it in:

```
Tunnel: 
Phase 1 / 2 state: 
Error: 
Cause: 
Action:
```

## See also

[[IPsec]] · [[FortiGate]] · [[Palo Alto Networks NGFW]] · [[Cisco Secure Firewall]] · [[WireGuard]]
