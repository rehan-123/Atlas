---
type: "concept"
level: "Junior"
category: "[[Security concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# SPF, DKIM & DMARC

> [!abstract] In one line
> Email authentication records that stop spoofing and improve delivery.

> [!tip] Think of it like
> SPF is the list of who may post letters for you, DKIM is a wax seal, DMARC says what to do with letters that fail.

> [!info]+ Words on this page
> **SPF**: A DNS record listing which servers may send email for a domain.
> **DNS**: The service that turns names (like server01.contoso.local) into IP addresses.
> **DKIM**: An email signature that proves a message really came from your domain and wasn't changed.
> **DMARC**: An email rule that tells receivers what to do with mail that fails SPF or DKIM checks.
> **quarantine**: A holding area for suspicious emails or files, so they can't do harm.
> *More in the [[Glossary]].*

## How it works

- **SPF** (TXT record): which servers may send for the domain. Keep under 10 DNS lookups.
- **DKIM**: cryptographic signature on each message, public key in DNS.
- **DMARC**: policy for failures (none, quarantine, reject) and reporting. Move to quarantine or reject once reports are clean.
- Large mailbox providers now require them for bulk senders.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Mail from your domain lands in spam at Gmail. What do you check first?
> The SPF, DKIM and DMARC results in the message headers, and the DNS records.

## See also

[[Email delivery problems]] · [[Exchange Online]] · [[DNS]] · [[Email security]]
