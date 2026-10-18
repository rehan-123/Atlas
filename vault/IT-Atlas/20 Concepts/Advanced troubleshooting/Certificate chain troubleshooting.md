---
type: "concept"
level: "Senior"
category: "[[Advanced troubleshooting]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Certificate chain troubleshooting

> [!abstract] In one line
> Fixing 'certificate not trusted' errors by checking the whole chain from the server certificate up to a trusted root.

> [!tip] Think of it like
> A reference letter that's only trusted if the referee is someone you already trust, or is vouched for by someone you do.

> [!info]+ Words on this page
> **SAN**: Storage area network: shared block storage for servers.
> **AD**: Active Directory, the Windows directory of users, computers and groups.
> **certificate**: A digital ID card that proves a website or device is who it claims to be and enables encryption.
> **browser**: The app you use to open websites: Edge, Chrome, Safari or Firefox.
> *More in the [[Glossary]].*

## How it works

- A certificate is trusted only if every intermediate up to a trusted root is available and valid.
- Common causes: missing intermediate on the server, expired intermediate, wrong name (SAN), clock wrong, revocation check blocked.
- Tools: browser certificate viewer, `certutil -verify -urlfetch FILE.cer`, `openssl s_client -connect HOST:443 -showcerts`.
- Internal AD CS certificates need the internal root in clients' trusted store (Group Policy does this for domain PCs).

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- A site works in Chrome on PCs but fails on some phones with 'not trusted'. Likely cause?
> The server isn't sending the intermediate certificate; PCs fetch it themselves, some phones don't.

## See also

[[Certificates & PKI]] · [[AD CS]] · [[Certificate expiring]] · [[Certificate trust errors]]
