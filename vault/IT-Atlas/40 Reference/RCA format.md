---
type: "reference"
level: "All"
tags:
  - "reference"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# RCA format

An 8-point root cause analysis format for NOC incidents.

1. **Incident summary**: one paragraph, plain language.
2. **Impact**: who and what was affected, for how long.
3. **Timeline**: timestamps with time zone, from first signal to full recovery.
4. **Detection**: how it was noticed (alert, user, vendor) and how long that took.
5. **Investigation**: what was checked, what was ruled out, and the evidence.
6. **Root cause**: the confirmed cause. If not confirmed, say so and state what evidence would confirm it.
7. **Resolution**: what restored service.
8. **Prevention and follow-ups**: actions with owners and dates.

Avoid blame. "Human error" is never a root cause; the system that allowed the error is.
