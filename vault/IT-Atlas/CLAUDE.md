# CLAUDE.md — IT Atlas

You maintain the IT Atlas (originally the NOC Atlas): an Obsidian knowledge base of everyday IT troubleshooting and every technology a NOC (network operations center) engineer at an MSP works with. The owner is Rehan Khan, Advanced System Administrator at IT By Design. Accuracy matters more than volume: engineers act on these notes during incidents.

## Structure
| Folder | Holds | `type` |
|---|---|---|
| `00 Home/` | Home and Tool database | `moc` |
| `01 RMM/` … `16 Automation/` | Tools, one folder per category, subfolders per subcategory | `tool` |
| `17 Help Desk/<area>/` | Everyday problems and fixes, for beginners | `guide` |
| `18 DevOps & Containers/`, `19 Compliance & Governance/` | Tools, like the other category folders | `tool` |
| `00 Home/Career tracks/` | Junior, Sysadmin and Senior tracks | `track` |
| `20 Concepts/<subcategory>/` | Protocols and fundamentals (including IT basics and help desk skills) | `concept` |
| `30 Playbooks/` | Alert-to-resolution procedures | `playbook` |
| `40 Reference/` | Ports, event IDs, logs, cheat sheets, lifecycles | `reference` |
| `50 Vendors/` | One note per vendor | `vendor` |
| `90 Templates/` | Templates. Don't edit unless asked. | — |
| `_system/` | Lint script and CSV export | — |

Each category folder has a category note with the same name as the category (for example `05 Backup & DR/Backup & DR.md`), and each subcategory folder has a note with the subcategory's name. These are the maps of content.

## Adding a tool
1. Check it doesn't exist: search file names and `aliases`.
2. Pick the category and subcategory from the existing folders. Do not invent a new category; ask Rehan if nothing fits.
3. Create it from `90 Templates/Tool.md` in the subcategory folder. Fill `category`, `subcategory` and `vendor` as quoted wikilinks.
4. If the vendor has no note in `50 Vendors/`, create one from `Vendor.md` (unless the vendor name equals the product name).
5. Add the tool to its subcategory note's list, with its one-line summary.
6. Link it to the concepts and playbooks it relates to, and add it to relevant playbooks' Related lines.
7. Agent service names, ports and log paths also appear in the generated reference sheets (`Agent & service names`, `Log locations`, `Port reference`). Add a row there too.

## Adding a help desk guide
1. Pick the area folder in `17 Help Desk/`; don't invent a new area without asking Rehan.
2. Create it from `90 Templates/Help desk guide.md`. Keep the section headings.
3. **Try this first** must be safe for a non-technical user. Technical checks go under **If you're the tech**.
4. Add it to the area note's table, and link related tools, concepts and guides.

## Levels
Every note has `level:` Junior, Mid, Senior or All. Junior = L1 help desk/NOC, Mid = L2 sysadmin, Senior = L3 senior/architect. Set it on every new note; when unsure, ask Rehan.

## Accuracy rules
- Never invent ports, service names, file paths, CLI commands, event IDs or dates. If you are not sure, leave it out or mark it "(verify)".
- Facts that change (ownership, product names, pricing, lifecycle dates, limits) need a source. When you verify a note, set `verified: YYYY-MM-DD` and add a `source:` property with the URL.
- Prefer vendor documentation over blogs and forums.
- Keep `as_of` as the month the content reflects.
- Never delete a note. If a product is retired, set `status: retired` and say what replaced it.

## Writing style
- Short, practical and plain: written for a new tech mid-incident. Bullets over prose.
- Every failure gets a first check, not just a description.
- Commands go in code blocks with placeholders in CAPS (HOST, USER, VMID).
- Sentence-case headings. Use the exact section headings from the templates.

## Writing for new techs
The readers are new L1/L2 NOC technicians. Write plainly.
- Every tool needs a one- or two-sentence plain-English entry in the **In plain words** box: what it is and why a NOC tech cares. No unexplained acronyms there.
- Every concept needs a **Think of it like** analogy and at least one **Check yourself** question with its answer in a collapsed `> [!question]-` callout.
- Every playbook starts with **What this alert means** and **Why it matters**.
- When a page uses a term a beginner might not know, add it to the Glossary, and to the "Words on this page" box if you edit that by hand.
- Prefer short sentences, everyday words and concrete examples. Put technical depth under **In more detail**.

## Linking rules
- Use `[[wikilinks]]` only. Link names must match note file names exactly (aliases do not resolve links).
- Every tool links to its category, subcategory and vendor (frontmatter) and to at least one concept or playbook (body).
- Never rename a note without updating every link to it.

## Field notes
The `## Field notes` section on each tool belongs to Rehan. Only add to it when he gives you something to record, and never remove what is there.

## After every change
Run the lint script and fix broken links and missing fields: `python3 _system/vault_lint.py` on Mac or Linux, or `powershell -ExecutionPolicy Bypass -File _system\vault_lint.ps1` on Windows. If the vault is a git repo, commit with `atlas: <what changed>`.
