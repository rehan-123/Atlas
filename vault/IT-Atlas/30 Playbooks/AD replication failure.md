---
type: "playbook"
level: "Senior"
severity: "P2"
tags:
  - "playbook"
created: "2026-10-18"
updated: "2026-10-18"
---

# AD replication failure

> [!abstract] What this alert means
> Domain controllers have stopped copying changes to each other.
>
> **Why it matters:** Password changes, new users and Group Policy stop spreading, causing confusing login problems.

**How urgent:** P2. See [[Severity levels]].

> [!info]+ Words on this page
> **DC**: Domain controller: a server running Active Directory.
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **RPC**: Remote procedure call: how Windows machines ask each other to do things (uses port 135 and high ports).
> **replication**: Copying data or changes to another place, continuously or on a schedule.
> **escalate**: Hand a problem to a more senior person or team, with your notes.
> **domain controller**: A server running Active Directory that checks logins.
> *More in the [[Glossary]].*

## You'll see this when

- repadmin or monitoring reports replication errors
- Event 2042, 1311 or 1988 on a DC

## First 5 minutes

1. Run `repadmin /replsummary` to see which DCs and how long
2. Check that DCs can resolve each other in DNS and reach each other on RPC

## Find the cause

- DNS: DCs pointing at external DNS or missing _msdcs records
- Network or firewall blocking RPC between sites
- Time skew
- A DC past the tombstone lifetime (event 2042) must not simply be reconnected

## Fix it

- Fix DNS settings and register records (`ipconfig /registerdns`, restart Netlogon)
- Open RPC between DCs
- Fix time sync on the PDC emulator
- Force replication: `repadmin /syncall /AdeP`

## Ask for help (escalate) when

- Tombstone lifetime exceeded
- Lingering objects
- Only one DC healthy

## Write it up

Copy this into the ticket and fill it in:

```
DCs affected: 
Error: 
Last success: 
Cause: 
Action: 
repadmin /replsummary after:
```

## See also

[[Active Directory]] · [[DNS]] · [[NTP]] · [[FSMO roles]]
