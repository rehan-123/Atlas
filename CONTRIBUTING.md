# Contributing to Atlas

Thanks for helping make the atlas more useful. Good contributions are accurate, practical, and easy for a new technician to follow.

## Suggesting a change

- Search the vault first to avoid duplicate notes.
- For changing facts (product names, ownership, ports, paths, limits, and lifecycle dates), include a primary source such as vendor documentation and the date you checked it.
- Use the existing note templates and frontmatter fields. Keep Obsidian links pointed at exact note names.
- Explain a safe first check before advanced or disruptive steps. Clearly mark commands that need elevated access or can affect production.
- Keep examples fictional. Do not include customer names, real hostnames, IP addresses, account identifiers, credentials, screenshots, or incident records.
- Preserve the original wording and intent when correcting a small factual issue; describe broader rewrites in the pull request.

## Before opening a pull request

1. Explain the problem the change solves and who it helps.
2. Link sources for time-sensitive claims.
3. Check that new notes use the matching template and link into the relevant maps, tools, concepts, or playbooks.
4. Run the vault linter from the `vault/IT-Atlas/` directory: `python3 _system/vault_lint.py`.

Please do not submit secrets or personal data in an issue. If you find a security concern, follow [SECURITY.md](SECURITY.md).
