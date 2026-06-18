#!/usr/bin/env python3
"""Validate catalog.json and every extension manifest.

Checks:
  * catalog.json has schema_version "1.0" and a non-empty extensions map.
  * Each catalog entry has id/name/version/description/download_url.
  * ids match ^[a-z0-9-]+$, versions look like semver, download_urls are HTTPS.
  * Each extensions/<id>/extension.yml exists, id matches the directory, and
    declares at least one command or hook.

Exit code is non-zero if any check fails (fail-closed for CI).

Usage: python scripts/validate.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

REPO_ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = REPO_ROOT / "catalog.json"
EXT_DIR = REPO_ROOT / "extensions"

ID_RE = re.compile(r"^[a-z0-9-]+$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+([-+].+)?$")
REQUIRED_FIELDS = ("id", "name", "version", "description", "download_url")


def main() -> int:
    errors: list[str] = []

    if not CATALOG_PATH.exists():
        print(f"FAIL: {CATALOG_PATH} not found")
        return 1

    try:
        catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"FAIL: catalog.json is not valid JSON: {exc}")
        return 1

    if catalog.get("schema_version") != "1.0":
        errors.append("catalog: schema_version must be the string \"1.0\"")

    extensions = catalog.get("extensions")
    if not isinstance(extensions, dict) or not extensions:
        errors.append("catalog: 'extensions' must be a non-empty object")
        extensions = {}

    for key, entry in extensions.items():
        if not ID_RE.match(key):
            errors.append(f"catalog['{key}']: key must match ^[a-z0-9-]+$")
        if not isinstance(entry, dict):
            errors.append(f"catalog['{key}']: entry must be an object")
            continue
        for field in REQUIRED_FIELDS:
            if not entry.get(field):
                errors.append(f"catalog['{key}']: missing required field '{field}'")
        if entry.get("id") and entry["id"] != key:
            errors.append(f"catalog['{key}']: id '{entry['id']}' != map key")
        if entry.get("version") and not SEMVER_RE.match(str(entry["version"])):
            errors.append(f"catalog['{key}']: version '{entry['version']}' is not semver")
        url = entry.get("download_url", "")
        if url and not url.startswith("https://"):
            errors.append(f"catalog['{key}']: download_url must be HTTPS")

    # Validate source manifests.
    if EXT_DIR.exists():
        for ext_path in sorted(p for p in EXT_DIR.iterdir() if p.is_dir()):
            manifest_path = ext_path / "extension.yml"
            if not manifest_path.exists():
                errors.append(f"{ext_path.name}: missing extension.yml")
                continue
            manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
            ext_id = manifest.get("id")
            if ext_id != ext_path.name:
                errors.append(
                    f"{manifest_path}: id '{ext_id}' must match directory '{ext_path.name}'"
                )
            if ext_id and not ID_RE.match(str(ext_id)):
                errors.append(f"{manifest_path}: id must match ^[a-z0-9-]+$")
            version = manifest.get("version")
            if not version or not SEMVER_RE.match(str(version)):
                errors.append(f"{manifest_path}: version '{version}' is not semver")
            if not manifest.get("commands") and not manifest.get("hooks"):
                errors.append(f"{manifest_path}: must declare at least one command or hook")

    if errors:
        print(f"FAIL: {len(errors)} problem(s):")
        for err in errors:
            print(f"  - {err}")
        return 1

    print(f"OK: catalog.json valid, {len(extensions)} extension(s) checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
