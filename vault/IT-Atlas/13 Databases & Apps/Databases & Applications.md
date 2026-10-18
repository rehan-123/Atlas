---
type: "moc"
level: "All"
tags:
  - "moc"
  - "databases"
created: "2026-10-18"
updated: "2026-10-18"
---

# Databases & Applications

> [!abstract] In plain words
> Databases store an application's data in an organized way. Many line-of-business apps depend on one.

Database engines and server applications that commonly sit under NOC monitoring.

Back to [[Home]].

> [!note]- How seniors think about this area
> - Know each app's owner, vendor support contact and backup method; line-of-business apps are often the last thing documented.
> - Use application-aware backups and test database restores, including transaction log chains.
> - Plan upgrades with the vendor: many apps pin specific SQL or .NET versions.

## Tools

- [[Microsoft SQL Server]]: Microsoft's database server. Many business apps, and many IT tools, store their data in it.
- [[MySQL & MariaDB]]: Free databases behind many websites and apps.
- [[PostgreSQL]]: A free, powerful database used by many apps.
- [[Exchange Server]]: Microsoft's on-site email server. Old versions are out of support and are a big security risk.
- [[Oracle Database]]: A large commercial database used by big business applications.
- [[MongoDB]]: A popular database that stores data as flexible JSON-like documents instead of tables.
- [[Redis]]: A very fast in-memory data store, often used as a cache in front of a database.
- [[QuickBooks Desktop]]: Accounting software many small businesses run on a shared server; a common source of help desk tickets.

## Playbooks for this area

[[Email delivery problems]] · [[High memory]] · [[Low disk space]] · [[SQL Server problems]]

## Database view

```dataview
TABLE vendor, deployment, status, agent_service AS "Agent"
FROM "13 Databases & Apps"
WHERE type = "tool"
SORT file.name ASC
```
