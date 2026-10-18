---
type: "guide"
level: "Junior"
area: "[[Internet & Wi-Fi problems]]"
tags:
  - "guide"
  - "help-desk"
created: "2026-10-18"
updated: "2026-10-18"
---

# VPN won't connect

> [!abstract] What's going on
> The VPN app fails to connect, or connects but nothing at the office opens.

> [!tip] Think of it like
> A private tunnel from your home to the office. If either entrance is blocked, or your pass is expired, you can't get through.

**Who can fix it:** Anyone can do the first steps; a tech does the rest. · **Area:** [[Internet & Wi-Fi problems]]

> [!info]+ Words on this page
> **VPN**: An encrypted tunnel over the internet to a private network.
> **MFA**: Multi-factor authentication: password plus a second proof, such as a phone prompt.
> **Wi-Fi**: Wireless network connection using radio signals.
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **NOC**: Network operations center: the team that monitors and fixes infrastructure.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> **tunnel**: An encrypted connection that carries traffic across another network.
> **port**: A numbered door on a device that a specific service listens on, for example 443 for HTTPS or 3389 for RDP.
> *More in the [[Glossary]].*

## Try this first

Anyone can do these, and they fix most cases.

1. Check your home internet works first.
2. Quit the VPN app fully and open it again; restart the PC.
3. Check your password hasn't expired and approve the MFA prompt on your phone.
4. Try a different network (phone hotspot) to rule out a hotel or public Wi-Fi block.

## If you're the tech

Words in CAPITALS are placeholders: replace them with your own values.

- Read the client's error and log (FortiClient, GlobalProtect, Cisco Secure Client).
- Check the user's account and group on the firewall or identity provider.
- Check the VPN gateway's certificate and the client version.
- Connected but no access: check split tunnel routes and DNS on the VPN adapter (`ipconfig /all`).

## Common causes and fixes

| Cause | Fix |
|---|---|
| Expired password or MFA not approved | Reset the password; re-register MFA. |
| Network blocks VPN ports | Try another network. |
| Outdated VPN client | Update the client. |
| Gateway problem | Escalate to the NOC (VPN tunnel down). |

## Escalate when

- Several remote users can't connect
- The VPN gateway or firewall is down
- The gateway certificate has expired

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

> [!question]- VPN connects but no internal sites open by name. What do you check?
> DNS on the VPN adapter: the PC must use the internal DNS servers while connected.

## See also

[[VPN]] · [[FortiClient]] · [[GlobalProtect]] · [[Cisco Secure Client]] · [[VPN tunnel down]] · [[Multi-factor authentication]]

## Field notes

Add your own tips and client quirks here.
