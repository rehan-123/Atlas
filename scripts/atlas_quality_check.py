#!/usr/bin/env python3
"""Lightweight static QA for Atlas documentation and local landing-page links.

Run from the repository root:
    python3 scripts/atlas_quality_check.py

This intentionally avoids network requests and does not execute installer scripts,
embedded JavaScript, community plugins, or any production operations.
"""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".html", ".css", ".js", ".json", ".svg", ".py", ".ps1", ".sh", ".txt", ".csv", ".yml", ".yaml"}
SKIP_PARTS = {".git", "node_modules"}
THIRD_PARTY_PREFIXES = (
    "vault/IT-Atlas/.obsidian/plugins/",
)
# Construct the known branding typo from pieces so this regression checker
# does not flag its own source.
TYPO = re.compile(r"\b" + "atlas" + "t" + r"\b", re.IGNORECASE)
failures: list[str] = []
checked = 0


def should_scan(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if any(part in SKIP_PARTS for part in path.relative_to(ROOT).parts):
        return False
    if any(rel.startswith(prefix) for prefix in THIRD_PARTY_PREFIXES):
        return False
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return False
    # Embedded community-plugin/runtime payloads are not project-authored copy.
    if rel.startswith("vault/IT-Atlas/.obsidian/"):
        return False
    return True


for file_path in ROOT.rglob("*"):
    if not file_path.is_file() or not should_scan(file_path):
        continue
    try:
        content = file_path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    # The interactive demo intentionally embeds a large content JSON payload.
    # Its source notes are scanned separately; omit the serialized data so that
    # this check validates authored UI copy rather than duplicated generated text.
    if file_path.suffix.lower() == ".html":
        content = re.sub(
            r'<script\s+type="application/json"\s+id="itb-data">.*?</script>',
            "",
            content,
            flags=re.IGNORECASE | re.DOTALL,
        )
        content = re.sub(r"url\(\s*data:[^)]*\)", "url([embedded-font-data])", content, flags=re.IGNORECASE)
    if file_path.suffix.lower() == ".md":
        for raw in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", content):
            target = raw.strip().split()[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("//") or target.startswith("#") or not parsed.path:
                continue
            local = (file_path.parent / unquote(parsed.path)).resolve()
            if not local.exists():
                failures.append(
                    f"Markdown image target missing: {file_path.relative_to(ROOT)} -> {target}"
                )

    checked += 1
    payload_lines_skipped = 0
    for line_no, line in enumerate(content.splitlines(), start=1):
        # Install/update scripts and embedded fonts may carry generated payloads.
        if len(line) > 100_000:
            payload_lines_skipped += 1
            continue
        if TYPO.search(line):
            failures.append(f"Brand spelling: {file_path.relative_to(ROOT)}:{line_no}")
    if payload_lines_skipped:
        print(f"Skipped {payload_lines_skipped} generated payload line(s): {file_path.relative_to(ROOT)}")

# Parse repository-owned SVGs as XML to catch broken markup.
for svg_path in ROOT.rglob("*.svg"):
    if not should_scan(svg_path):
        continue
    try:
        ET.parse(svg_path)
    except (ET.ParseError, OSError) as exc:
        failures.append(f"Invalid SVG {svg_path.relative_to(ROOT)}: {exc}")

# Public installers may ship ONLY the IT Atlas vault and its plugin. A private vault
# (client notes, incident records, tickets) must never be embedded in a script here.
ALLOWED_PAYLOAD_ROOTS = {"IT-Atlas", "gesture-graph"}


def installer_payload_roots(data: bytes) -> list[tuple[str, set[str]]]:
    """Top-level folders of every archive embedded in an installer script."""
    import base64
    import io
    import tarfile
    import zipfile

    found = []
    for match in re.finditer(rb"<#([A-Z]+)_BEGIN\s*(.*?)\s*\1_END#>", data, re.S):
        raw = base64.b64decode(re.sub(rb"\s", b"", match.group(2)))
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            found.append((match.group(1).decode(), {name.split("/")[0] for name in archive.namelist()}))
    marker = re.search(rb"^__[A-Z_]*BELOW__\r?\n", data, re.M)
    if marker:
        raw = base64.b64decode(re.sub(rb"\s", b"", data[marker.end():]))
        with tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz") as archive:
            found.append((marker.group(0).decode().strip(), {name.split("/")[0] for name in archive.getnames()}))
    return found


for installer in sorted(ROOT.glob("*-it-atlas.*")):
    try:
        payloads = installer_payload_roots(installer.read_bytes())
    except Exception as exc:  # an unreadable payload fails the check; it never passes silently
        failures.append(f"Installer payload unreadable: {installer.name} ({type(exc).__name__})")
        continue
    if not payloads:
        failures.append(f"Installer has no embedded vault: {installer.name}")
    for tag, roots in payloads:
        extra = sorted(roots - ALLOWED_PAYLOAD_ROOTS)
        if extra:
            failures.append(f"Installer {installer.name} embeds {extra} ({tag}); only the IT Atlas vault may ship publicly")


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, str]] = []
        self.ids: set[str] = set()
        self.fragments: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(attributes["id"] or "")
        for attr in ("href", "src"):
            value = attributes.get(attr)
            if value:
                self.links.append((attr, value))
                if attr == "href" and value.startswith("#"):
                    self.fragments.append(value[1:])

# Validate README HTML attributes and inline fragments, then its standard Markdown links.
readme_path = ROOT / "README.md"
if readme_path.exists():
    readme = readme_path.read_text(encoding="utf-8")
    parser = LinkParser()
    parser.feed(readme)
    for fragment in parser.fragments:
        if fragment and fragment not in parser.ids:
            failures.append(f"README fragment not found in README HTML: #{fragment}")
    for attr, target in parser.links:
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith("//") or target.startswith("#") or not parsed.path:
            continue
        local = (ROOT / unquote(parsed.path)).resolve()
        if not local.exists():
            failures.append(f"README {attr} target missing: {target}")

    md_targets = re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", readme)
    for raw in md_targets:
        target = raw.strip().split()[0].strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith("//") or target.startswith("#") or not parsed.path:
            continue
        local = (ROOT / unquote(parsed.path)).resolve()
        if not local.exists():
            failures.append(f"README Markdown target missing: {target}")
else:
    failures.append("README.md missing")

print(f"Text files checked for branding typo: {checked}")
print("SVG files parsed, installer payloads checked, README local links checked.")
if failures:
    print(f"FAIL: {len(failures)} issue(s)")
    for failure in failures:
        print(f"  - {failure}")
    sys.exit(1)
print("PASS: no branding typo, invalid SVG, private installer payload, or missing README local target found.")
