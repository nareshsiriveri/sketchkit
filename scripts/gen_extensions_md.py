#!/usr/bin/env python3
"""Generate EXTENSIONS.md from catalog.json and the extension manifests.

Reads catalog.json for the canonical id/name/version/description/tags of every
published extension, and each extensions/<id>/extension.yml for the command
list, then renders the human-browsable catalog at EXTENSIONS.md.

Usage: python scripts/gen_extensions_md.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

REPO_ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = REPO_ROOT / "catalog.json"
EXT_DIR = REPO_ROOT / "extensions"
OUT_PATH = REPO_ROOT / "EXTENSIONS.md"

TABLE_DESC = 89   # table description chars before an ellipsis is appended
CMD_DESC = 80     # per-command description chars (hard cut, no ellipsis)


def table_trunc(text: str) -> str:
    text = " ".join((text or "").split())
    return text if len(text) <= TABLE_DESC else text[:TABLE_DESC].rstrip() + "…"


def cmd_trunc(text: str) -> str:
    text = " ".join((text or "").split())
    return text[:CMD_DESC]


def load_commands(ext_id: str) -> list[dict]:
    manifest_path = EXT_DIR / ext_id / "extension.yml"
    if not manifest_path.exists():
        return []
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
    return (manifest.get("provides") or {}).get("commands") or []


def main() -> int:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    extensions = catalog.get("extensions", {})

    rows = []
    for ext_id, entry in extensions.items():
        commands = load_commands(ext_id)
        rows.append({
            "id": ext_id,
            "name": entry.get("name", ext_id),
            "version": entry.get("version", ""),
            "description": entry.get("description", ""),
            "tags": entry.get("tags", []),
            "commands": commands,
        })
    rows.sort(key=lambda r: r["name"].lower())

    total_ext = len(rows)
    total_cmds = sum(len(r["commands"]) for r in rows)

    out: list[str] = []
    out.append("# Extension Catalog")
    out.append("")
    out.append("")
    out.append(f"**Total: {total_ext} extensions · {total_cmds} commands**")
    out.append("")
    out.append(f"_{total_ext} extensions available in this catalog. Generated from `catalog.json`._")
    out.append("")
    out.append("Install any extension into a Spec-Kit project:")
    out.append("")
    out.append("```bash")
    out.append('export SPECKIT_CATALOG_URL="https://raw.githubusercontent.com/nareshsiriveri/sketchkit/main/catalog.json"')
    out.append("specify extension add <id>")
    out.append("```")
    out.append("")
    out.append("| Extension | id | Ver | Commands | Description |")
    out.append("|-----------|----|-----|---------:|-------------|")
    for r in rows:
        out.append(
            f"| {r['name']} | `{r['id']}` | {r['version']} | {len(r['commands'])} | {table_trunc(r['description'])} |"
        )
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Details")
    out.append("")
    for r in rows:
        out.append("")
        out.append(f"### {r['name']} (`{r['id']}`)")
        out.append("")
        out.append(" ".join((r["description"] or "").split()))
        out.append("")
        out.append(f"- **Install:** `specify extension add {r['id']}`")
        tags = ", ".join(r["tags"]) if r["tags"] else "—"
        out.append(f"- **Version:** {r['version']} · **Tags:** {tags}")
        out.append(f"- **Commands ({len(r['commands'])}):**")
        for cmd in r["commands"]:
            name = cmd.get("name", "")
            desc = cmd_trunc(cmd.get("description", ""))
            out.append(f"  - `/{name}` — {desc}")

    OUT_PATH.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_PATH}: {total_ext} extensions, {total_cmds} commands.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
