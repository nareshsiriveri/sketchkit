#!/usr/bin/env python3
"""Clone every external plugin referenced by a Claude marketplace.json and
convert each one into a Spec-Kit extension.

The marketplace lists plugins whose `source` is either a local path (handled
separately by convert_plugins.py) or an external git repo:

  * {"source": "git-subdir", "url": ..., "path": ..., "ref": ...}
  * {"source": "url"|"github"|"git", "url": ..., "ref": ...}

For each external entry this script shallow-clones the repo (deduped + cached by
URL), locates the plugin directory, and runs the shared converter with the
plugin's *own* upstream URL recorded as attribution. Failures (dead repos,
missing subdirs, nothing convertible) are collected and reported, never fatal.

Usage:
  python scripts/import_marketplace.py --marketplace /path/to/marketplace.json \
      --cache /path/to/clone-cache
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from convert_plugins import EXT_DIR, convert_plugin, sanitize  # noqa: E402

SHA_RE = re.compile(r"^[0-9a-f]{7,40}$")
UPSTREAM = "anthropics/claude-plugins-official"


def repo_dirname(url: str) -> str:
    return sanitize(re.sub(r"\.git$", "", url).replace("https://", "").replace("/", "-"))


def clone(url: str, dest: Path, ref: str | None) -> bool:
    if dest.exists():
        return any(dest.iterdir())
    attempts = []
    if ref and not SHA_RE.match(ref):
        attempts.append(["git", "clone", "--depth", "1", "--branch", ref, url, str(dest)])
    attempts.append(["git", "clone", "--depth", "1", url, str(dest)])
    for cmd in attempts:
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        except subprocess.TimeoutExpired:
            r = None
        if r is not None and r.returncode == 0:
            return True
        if dest.exists():
            import shutil
            shutil.rmtree(dest, ignore_errors=True)
    return False


def upstream_url(entry: dict, src: dict) -> str:
    hp = entry.get("homepage")
    if hp:
        return hp
    return re.sub(r"\.git$", "", src.get("url", ""))


def find_plugin_dir(repo_root: Path, src: dict) -> Path | None:
    if src.get("source") == "git-subdir" and src.get("path"):
        cand = repo_root / src["path"]
        return cand if cand.is_dir() else None
    return repo_root if repo_root.is_dir() else None


def prepare_meta(plugin_dir: Path, entry: dict, ext_id: str) -> None:
    """Ensure plugin_dir/.claude-plugin/plugin.json exists with our chosen id.

    convert_plugin derives the extension id from plugin.json's `name`; we pin it
    to a collision-checked id and keep a human displayName + any keywords.
    """
    mdir = plugin_dir / ".claude-plugin"
    pj = mdir / "plugin.json"
    meta = {}
    if pj.exists():
        try:
            meta = json.loads(pj.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            meta = {}
    meta["name"] = ext_id
    meta.setdefault("displayName", entry.get("name", ext_id))
    if not meta.get("description"):
        meta["description"] = entry.get("description", ext_id)
    if not meta.get("version"):
        meta["version"] = "0.1.0"
    author = entry.get("author")
    if author and not meta.get("author"):
        meta["author"] = author
    mdir.mkdir(parents=True, exist_ok=True)
    pj.write_text(json.dumps(meta, indent=2), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--marketplace", required=True)
    ap.add_argument("--cache", required=True)
    args = ap.parse_args()

    market = json.loads(Path(args.marketplace).read_text(encoding="utf-8"))
    cache = Path(args.cache).resolve()
    cache.mkdir(parents=True, exist_ok=True)

    existing = {p.name for p in EXT_DIR.iterdir() if p.is_dir()}
    assigned: set[str] = set(existing)

    external = []
    for entry in market.get("plugins", []):
        src = entry.get("source")
        if isinstance(src, dict) and src.get("url"):
            external.append((entry, src))
    print(f"External plugins to import: {len(external)}")

    converted, skipped, failed = [], [], []
    clone_cache: dict[str, Path | None] = {}

    for entry, src in external:
        name = entry.get("name", "?")
        url = src["url"]
        ref = src.get("ref")
        if url not in clone_cache:
            dest = cache / repo_dirname(url)
            ok = clone(url, dest, ref)
            clone_cache[url] = dest if ok else None
            print(("  cloned " if ok else "  FAIL  ") + url)
        repo_root = clone_cache[url]
        if repo_root is None:
            failed.append((name, "clone failed", url))
            continue

        plugin_dir = find_plugin_dir(repo_root, src)
        if plugin_dir is None:
            failed.append((name, "plugin dir not found", url))
            continue

        ext_id = sanitize(name)
        base, i = ext_id, 2
        while ext_id in assigned:
            ext_id = f"{base}-{i}"
            i += 1

        try:
            prepare_meta(plugin_dir, entry, ext_id)
            result = convert_plugin(
                plugin_dir,
                attribution_url=upstream_url(entry, src),
                source_label=f"{UPSTREAM} (via {re.sub(r'.git$', '', url)})",
                default_author=(entry.get("author", {}) or {}).get("name", "")
                if isinstance(entry.get("author"), dict) else (entry.get("author") or "Unknown"),
                default_tag=entry.get("category", "claude-code"),
            )
        except Exception as exc:  # noqa: BLE001
            failed.append((name, f"convert error: {exc}", url))
            continue

        if result:
            assigned.add(ext_id)
            converted.append((ext_id, result[1]))
        else:
            skipped.append((name, url))

    print("\n==== SUMMARY ====")
    print(f"converted: {len(converted)}  ({sum(c for _, c in converted)} commands)")
    print(f"skipped (no commands/skills/agents): {len(skipped)}")
    print(f"failed: {len(failed)}")
    if failed:
        print("\nFailures:")
        for name, why, url in failed:
            print(f"  {name}: {why}  [{url}]")
    if skipped:
        print("\nSkipped (nothing convertible):")
        for name, url in skipped:
            print(f"  {name}  [{url}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
