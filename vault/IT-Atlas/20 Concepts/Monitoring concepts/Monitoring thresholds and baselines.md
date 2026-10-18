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

# Monitoring thresholds and baselines

> [!abstract] In one line
> Set thresholds from what is normal for that system, not from defaults.

> [!tip] Think of it like
> A baseline is a person's normal heart rate; the threshold is when the doctor should worry. Normal differs per patient.

> [!info]+ Words on this page
> **CPU**: The processor, the part of a computer that does the calculations.
> **threshold**: The value that triggers an alert.
> *More in the [[Glossary]].*

## How it works

- Measure a baseline first (a week or a month) and alert on meaningful deviation.
- Use duration: "CPU above 90% for 15 minutes", not one sample.
- Use percentages and absolute values together for disks: 10% free on 4 TB is still 400 GB.
- Warning should mean "act this week", critical should mean "act now". If nobody acts on a warning, delete it.

## Check yourself

Answer in your head first, then click to reveal.

> [!question]- Why alert on 'CPU above 90% for 15 minutes' instead of 'CPU above 90%'?
> Short spikes are normal. Requiring a duration avoids alerts nobody needs to act on.

## See also

[[Alert fatigue]] · [[Low disk space]] · [[High CPU]]
