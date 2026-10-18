---
type: "playbook"
level: "Senior"
severity: "P2 (P1 if widespread)"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# Kerberos authentication failures

> [!abstract] What this alert means
> Users or services can't authenticate with Kerberos, so access to file shares, SQL or web apps fails or falls back to NTLM.
>
> **Why it matters:** Kerberos underpins almost every sign-in in a domain; failures look random and spread quickly.

**How urgent:** P2 (P1 if widespread). See [[Severity levels]].

> [!info]+ Words on this page
> **DC**: Domain controller: a server running Active Directory.
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **IP**: Internet Protocol address: a device's address on the network, like 192.168.1.20.
> **SPN**: Service principal name: the name Kerberos uses to find which account runs a service.
> **SQL**: Structured Query Language; also short for Microsoft SQL Server.
> **hardening**: Changing default settings to remove unnecessary features and close security gaps.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> *More in the [[Glossary]].*

## You'll see this when

- Users get repeated credential prompts for internal sites or shares
- Service logs show 'KRB_AP_ERR_MODIFIED' or 'The target principal name is incorrect'
- DC events 4771 or KDC errors spike

## First 5 minutes

1. Check the time on client, server and DCs (w32tm /query /status); more than 5 minutes apart breaks Kerberos
2. Confirm the client uses the DNS name of the service, not an IP or alias without an SPN
3. Run klist on the client to see whether a service ticket was issued

## Find the cause

- Duplicate SPNs: setspn -X; missing SPN for a service account: setspn -L ACCOUNT
- Service account password changed but service still uses the old one
- Alias (CNAME) used without a matching SPN
- Encryption type mismatch after hardening (RC4 disabled, account only supports RC4)

## Fix it

- Fix time sync from the PDC emulator outwards
- Register or remove SPNs (setspn -S / setspn -D) on the right account
- Update the service's stored password and restart it
- Purge tickets (klist purge) and retest

## Ask for help (escalate) when

- Many users across sites affected
- krbtgt or DC account problems suspected
- Signs of ticket forging or unusual 4769 volume (possible attack)

## Write it up

Copy this into the ticket and fill it in:

```
Affected service/users: 
Time skew checked: 
SPN findings: 
Root cause: 
Fix: 
Verified with klist:
```

## See also

[[Kerberos]] · [[Kerberos troubleshooting]] · [[NTP]] · [[Time drift]] · [[Active Directory]]
