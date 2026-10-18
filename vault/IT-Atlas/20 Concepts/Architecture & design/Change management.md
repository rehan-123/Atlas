---
type: "concept"
level: "Senior"
category: "[[Architecture & design]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Change management

> [!abstract] In one line
> Planning, approving and recording changes so they don't cause surprise outages, and can be undone.

> [!tip] Think of it like
> A pilot's pre-flight checklist and flight plan, filed before take-off.

## How it works

- Every change has: what, why, risk, test, rollback plan, owner and time window.
- **Standard** changes are pre-approved and low risk; **normal** changes go to review (CAB); **emergency** changes are approved fast and documented after.
- Communicate before and after; check monitoring once it's done.
- Most outages are caused by changes; a rollback plan is the best insurance.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- What must every change have before it's approved?
> A rollback plan, along with the risk, test and window.

## See also

[[ITIL incident, problem & change]] · [[Maintenance windows]] · [[Root cause analysis]]
