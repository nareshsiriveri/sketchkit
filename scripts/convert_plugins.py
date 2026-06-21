#!/usr/bin/env python3
"""Convert Claude Code marketplace plugins into Spec-Kit extensions.

Reads a cloned plugin marketplace (e.g. anthropics/financial-services) and, for
every plugin (a directory containing `.claude-plugin/plugin.json`), generates a
Spec-Kit extension under `extensions/<plugin-name>/`:

  * The whole plugin tree (commands/, skills/, agents/, references, scripts) is
    copied so resources are bundled in the published ZIP.
  * Each plugin command  -> command `speckit.<ext>.<cmd>`        (file: commands/...)
  * Each skill SKILL.md   -> command `speckit.<ext>.<skill>`      (file: skills/.../SKILL.md)
  * Each agent .md        -> command `speckit.<ext>.agent-<name>` (file: agents/...)

Name collisions are disambiguated (a skill sharing a command's name gets a
`-skill` suffix). Spec-Kit requires command names to match
`^speckit\\.[a-z0-9-]+\\.[a-z0-9-]+$`, so segments are sanitized to [a-z0-9-].

Usage:
  python scripts/convert_plugins.py --src /path/to/marketplace [--attribution-url URL]
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

import json

REPO_ROOT = Path(__file__).resolve().parent.parent
EXT_DIR = REPO_ROOT / "extensions"

SEG_RE = re.compile(r"[^a-z0-9-]+")


def sanitize(seg: str) -> str:
    seg = SEG_RE.sub("-", seg.lower())
    seg = re.sub(r"-+", "-", seg).strip("-")
    return seg or "cmd"


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    try:
        data = yaml.safe_load(text[3:end]) or {}
        return data if isinstance(data, dict) else {}
    except yaml.YAMLError:
        return {}


def ensure_description(path: Path, fallback: str) -> str:
    """Return the file's frontmatter description, injecting one if absent."""
    text = path.read_text(encoding="utf-8", errors="replace")
    fm = read_frontmatter(path)
    desc = (fm.get("description") or "").strip()
    if desc:
        return desc
    desc = fallback.strip() or "Spec-Kit command."
    if text.startswith("---"):
        # Insert description into existing frontmatter block.
        text = text.replace("---", f"---\ndescription: {json.dumps(desc)}", 1)
    else:
        text = f"---\ndescription: {json.dumps(desc)}\n---\n\n{text}"
    path.write_text(text, encoding="utf-8")
    return desc


def short(text: str, limit: int = 200) -> str:
    text = " ".join((text or "").split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def convert_plugin(
    plugin_dir: Path,
    attribution_url: str,
    source_label: str,
    default_author: str,
    default_tag: str,
) -> tuple[str, int] | None:
    meta = json.loads((plugin_dir / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    raw_id = meta.get("name") or plugin_dir.name
    ext_id = sanitize(raw_id)
    dest = EXT_DIR / ext_id
    if dest.exists():
        shutil.rmtree(dest)

    # Copy the whole plugin tree except the Claude-specific manifest dir.
    shutil.copytree(
        plugin_dir, dest,
        ignore=shutil.ignore_patterns(".claude-plugin", ".git"),
    )

    plugin_desc = meta.get("description", ext_id)
    commands: list[dict] = []
    used: set[str] = set()

    def add(seg: str, file_rel: str, desc: str):
        seg = sanitize(seg)
        base, i = seg, 2
        while seg in used:
            seg = f"{base}-{i}"
            i += 1
        used.add(seg)
        commands.append({
            "name": f"speckit.{ext_id}.{seg}",
            "file": file_rel,
            "description": short(desc or plugin_desc),
        })

    # 1) Real plugin commands.
    cmd_dir = dest / "commands"
    for f in sorted(cmd_dir.rglob("*.md")) if cmd_dir.is_dir() else []:
        desc = ensure_description(f, plugin_desc)
        add(f.stem, f.relative_to(dest).as_posix(), desc)

    # 2) Skills -> commands (suffix on collision with a command).
    skills_dir = dest / "skills"
    if skills_dir.is_dir():
        for skill_md in sorted(skills_dir.rglob("SKILL.md")):
            name = skill_md.parent.name
            seg = sanitize(name)
            if seg in used:
                seg = f"{seg}-skill"
            desc = ensure_description(skill_md, plugin_desc)
            add(seg, skill_md.relative_to(dest).as_posix(), desc)

    # 3) Agents -> commands (namespaced under agent-).
    agents_dir = dest / "agents"
    for f in sorted(agents_dir.rglob("*.md")) if agents_dir.is_dir() else []:
        desc = ensure_description(f, plugin_desc)
        add(f"agent-{f.stem}", f.relative_to(dest).as_posix(), desc)

    if not commands:
        shutil.rmtree(dest)
        print(f"  SKIP {ext_id}: no commands/skills/agents to convert")
        return None

    author = (meta.get("author") or {})
    author_name = author.get("name") if isinstance(author, dict) else (author or "")

    manifest = {
        "schema_version": "1.0",
        "extension": {
            "id": ext_id,
            "name": meta.get("displayName") or meta.get("name") or ext_id,
            "version": str(meta.get("version", "0.1.0")),
            "description": short(plugin_desc, 300),
            "author": author_name or default_author,
            "license": "Apache-2.0",
            "repository": attribution_url,
        },
        "requires": {"speckit_version": ">=0.2.0"},
        "provides": {"commands": commands},
        "tags": meta.get("keywords") or [default_tag],
    }

    text = (
        f"# Converted from a Claude Code plugin in {source_label}\n"
        f"# Source: {attribution_url}\n"
        "# License: Apache-2.0\n\n"
        + yaml.safe_dump(manifest, sort_keys=False, default_flow_style=False, width=100)
    )
    (dest / "extension.yml").write_text(text, encoding="utf-8")
    print(f"  OK   {ext_id}: {len(commands)} command(s)")
    return ext_id, len(commands)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--src", required=True, help="Path to the cloned marketplace repo (or its plugins/ dir)")
    parser.add_argument(
        "--attribution-url",
        default="https://github.com/anthropics/financial-services",
        help="Upstream repository URL recorded in each manifest.",
    )
    parser.add_argument(
        "--source-label",
        default="anthropics/financial-services",
        help="Human-readable source repo label for the manifest header comment.",
    )
    parser.add_argument(
        "--default-author",
        default="Anthropic FSI",
        help="Author recorded when a plugin.json omits one.",
    )
    parser.add_argument(
        "--default-tag",
        default="financial-services",
        help="Tag applied when a plugin.json declares no keywords.",
    )
    args = parser.parse_args()

    src = Path(args.src).resolve()
    plugin_jsons = sorted(src.rglob(".claude-plugin/plugin.json"))
    if not plugin_jsons:
        sys.exit(f"No plugins (.claude-plugin/plugin.json) found under {src}")

    EXT_DIR.mkdir(parents=True, exist_ok=True)
    converted, total_cmds = 0, 0
    for pj in plugin_jsons:
        plugin_dir = pj.parent.parent
        result = convert_plugin(
            plugin_dir,
            args.attribution_url,
            args.source_label,
            args.default_author,
            args.default_tag,
        )
        if result:
            converted += 1
            total_cmds += result[1]

    print(f"\nConverted {converted}/{len(plugin_jsons)} plugins, {total_cmds} commands total.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
