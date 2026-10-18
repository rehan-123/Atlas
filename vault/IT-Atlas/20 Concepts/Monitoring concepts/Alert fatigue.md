---
type: "concept"
level: "Junior"
category: "[[Monitoring concepts]]"
aliases: []
tags:
  - "concept"
as_of: "2026-06"
created: "2026-10-18"
updated: "2026-10-18"
---

# Alert fatigue

> [!abstract] In one line
> When too many low-value alerts train people to ignore all alerts.

> [!tip] Think of it like
> The boy who cried wolf: too many false alarms and people stop listening to the real one.

## How it works

- Every alert should be actionable, owned and tied to a playbook.
- Review the noisiest alerts monthly: tune, auto-remediate or delete.
- Correlate: one site down should raise one alert, not one per device behind the firewall (use parent and child dependencies).
- Measure: alerts per technician per shift, and the percentage closed with no action.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- What should happen to an alert that nobody ever acts on?
> Tune it, automate the fix, or delete it.

## See also

[[Monitoring thresholds and baselines]] · [[PagerDuty]] · [[MTTA & MTTR]]
