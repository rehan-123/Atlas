---
type: "moc"
level: "All"
tags:
  - "moc"
created: "2026-10-18"
updated: "2026-10-18"
---

# Tool database

All 348 tools as one table. Needs the Dataview plugin; a CSV copy is in `_system/noc-atlas.csv`.

Back to [[Home]].

```dataview
TABLE category, subcategory, vendor, deployment, status, agent_service AS "Agent", verified
FROM ""
WHERE type = "tool"
SORT category ASC, subcategory ASC, file.name ASC
```

## Filter examples

```dataview
TABLE vendor, category FROM "" WHERE type = "tool" AND contains(string(vendor), "Kaseya")
```

```dataview
TABLE category, agent_service FROM "" WHERE type = "tool" AND agent_service
```
