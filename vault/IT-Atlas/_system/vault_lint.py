#!/usr/bin/env python3
"""Atlas lint: broken wikilinks, orphans, missing frontmatter. Run from the vault root."""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".obsidian", ".claude", ".git", ".trash", "_system", "90 Templates"}
SKIP_FILES = {"CLAUDE.md"}
REQUIRED = {"_all": ["type", "tags"], "tool": ["category", "status", "created", "updated"], "concept": ["category"],
            "playbook": ["severity"], "guide": ["area"], "reference": [], "vendor": [], "moc": []}
LINK = re.compile(r"\[\[([^\]\|#\^]+)(?:[#\^][^\]\|]*)?(?:\|[^\]]*)?\]\]")
CODE = re.compile(r"```.*?```", re.S)
notes = {}
for dp, dns, fns in os.walk(ROOT):
    dns[:] = [d for d in dns if d not in SKIP_DIRS]
    for f in fns:
        if f.endswith(".md") and f not in SKIP_FILES:
            if f[:-3] in notes:
                print(f"Duplicate note name: {f[:-3]}")
            notes[f[:-3]] = os.path.relpath(os.path.join(dp, f), ROOT)
def front(t):
    if not t.startswith("---"): return None
    end = t.find("\n---", 3)
    if end < 0: return None
    d, key = {}, None
    for line in t[3:end].splitlines():
        if re.match(r"^\s+-", line) and key: d[key] = (d[key] or "") + line.strip()
        elif ":" in line and not line.startswith(" "):
            key, _, v = line.partition(":"); key = key.strip(); d[key] = v.strip()
    return d
out_l = {n: set() for n in notes}; in_l = {n: set() for n in notes}
broken, missing = [], []
for n, rel in notes.items():
    t = open(os.path.join(ROOT, rel), encoding="utf-8").read()
    for m in LINK.findall(CODE.sub("", t)):
        m = m.strip()
        if m in notes: in_l[m].add(n); out_l[n].add(m)
        else: broken.append((rel, m))
    if rel == "Start here.md": continue
    fmd = front(t)
    if fmd is None: missing.append((rel, "no frontmatter")); continue
    for k in REQUIRED["_all"] + REQUIRED.get(fmd.get("type", "").strip('"'), []):
        if k not in fmd or fmd[k] in ("", None): missing.append((rel, f"missing '{k}'"))
orphans = [notes[n] for n in notes if not out_l[n] and not in_l[n]]
nolinks_in = [notes[n] for n in notes if not in_l[n] and n not in ("Home", "Start here")]
by_type = {}
for n, rel in notes.items():
    t = open(os.path.join(ROOT, rel), encoding="utf-8").read()
    ty = (front(t) or {}).get("type", "none").strip('"'); by_type[ty] = by_type.get(ty, 0) + 1
print("Notes scanned:", len(notes), "|", ", ".join(f"{k}: {v}" for k, v in sorted(by_type.items())))
print(f"\nBroken links ({len(broken)}):"); [print(f"  {r} -> [[{t}]]") for r, t in sorted(broken)]
print(f"\nFrontmatter problems ({len(missing)}):"); [print(f"  {r}: {m}") for r, m in sorted(missing)]
print(f"\nOrphans ({len(orphans)}):"); [print("  " + o) for o in sorted(orphans)]
print(f"\nNothing links here ({len(nolinks_in)}):"); [print("  " + o) for o in sorted(nolinks_in)]
sys.exit(1 if broken or missing else 0)
