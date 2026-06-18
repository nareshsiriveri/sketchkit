#!/usr/bin/env python3
"""Build extension ZIPs and (re)generate catalog.json.

For every directory under `extensions/` that contains an `extension.yml`,
this script:
  1. Packages the directory into `dist/<id>-<version>.zip`, honoring
     `.extensionignore` (gitignore-style patterns).
  2. Computes the GitHub Releases download URL for that ZIP.
  3. Writes a catalog.json (schema_version "1.0") mapping id -> metadata.

Usage:
  python scripts/build.py --repo YOUR-ORG/speckit-extension-catalog --tag v0.1.0

In CI, --repo defaults to $GITHUB_REPOSITORY and --tag to the release tag.
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import os
import sys
import zipfile
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

REPO_ROOT = Path(__file__).resolve().parent.parent
EXT_DIR = REPO_ROOT / "extensions"
DIST_DIR = REPO_ROOT / "dist"
CATALOG_PATH = REPO_ROOT / "catalog.json"

RELEASE_URL = "https://github.com/{repo}/releases/download/{tag}/{zip_name}"


def load_ignore_patterns(ext_path: Path) -> list[str]:
    ignore_file = ext_path / ".extensionignore"
    patterns: list[str] = []
    if ignore_file.exists():
        for line in ignore_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                patterns.append(line)
    # Never ship the ignore file itself.
    patterns.append(".extensionignore")
    return patterns


def is_ignored(rel_posix: str, patterns: list[str]) -> bool:
    for pat in patterns:
        clean = pat.rstrip("/")
        # Directory pattern: match the dir or anything under it.
        if pat.endswith("/") and (
            fnmatch.fnmatch(rel_posix, clean)
            or fnmatch.fnmatch(rel_posix, f"{clean}/*")
            or f"/{clean}/" in f"/{rel_posix}/"
        ):
            return True
        if fnmatch.fnmatch(rel_posix, clean):
            return True
        # Match basename (e.g. "*.pyc").
        if fnmatch.fnmatch(os.path.basename(rel_posix), clean):
            return True
    return False


def build_extension(ext_path: Path, repo: str, tag: str) -> tuple[str, dict]:
    manifest_path = ext_path / "extension.yml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}

    ext_id = manifest.get("id")
    version = manifest.get("version")
    if not ext_id or not version:
        raise ValueError(f"{manifest_path}: 'id' and 'version' are required")
    if ext_id != ext_path.name:
        raise ValueError(
            f"{manifest_path}: id '{ext_id}' must match directory '{ext_path.name}'"
        )

    patterns = load_ignore_patterns(ext_path)
    zip_name = f"{ext_id}-{version}.zip"
    zip_path = DIST_DIR / zip_name

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    file_count = 0
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(ext_path.rglob("*")):
            if path.is_dir():
                continue
            rel = path.relative_to(ext_path).as_posix()
            if is_ignored(rel, patterns):
                continue
            zf.write(path, rel)
            file_count += 1

    if file_count == 0:
        raise ValueError(f"{ext_path}: no files to package after .extensionignore")

    entry = {
        "id": ext_id,
        "name": manifest.get("name", ext_id),
        "version": str(version),
        "description": manifest.get("description", ""),
        "download_url": RELEASE_URL.format(repo=repo, tag=tag, zip_name=zip_name),
    }
    print(f"  built {zip_name} ({file_count} files)")
    return ext_id, entry


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo",
        default=os.environ.get("GITHUB_REPOSITORY", "YOUR-ORG/speckit-extension-catalog"),
        help="GitHub org/repo used to build release download URLs.",
    )
    parser.add_argument(
        "--tag",
        default=os.environ.get("RELEASE_TAG", "v0.1.0"),
        help="Release tag the ZIP assets are attached to.",
    )
    args = parser.parse_args()

    if not EXT_DIR.exists():
        sys.exit(f"No extensions directory at {EXT_DIR}")

    extensions: dict[str, dict] = {}
    for ext_path in sorted(p for p in EXT_DIR.iterdir() if p.is_dir()):
        if not (ext_path / "extension.yml").exists():
            continue
        print(f"Packaging {ext_path.name}...")
        ext_id, entry = build_extension(ext_path, args.repo, args.tag)
        extensions[ext_id] = entry

    if not extensions:
        sys.exit("No extensions found (each needs extensions/<id>/extension.yml)")

    catalog = {"schema_version": "1.0", "extensions": extensions}
    CATALOG_PATH.write_text(json.dumps(catalog, indent=2) + "\n", encoding="utf-8")
    print(f"\nWrote {CATALOG_PATH} with {len(extensions)} extension(s).")
    print(f"ZIPs in {DIST_DIR}/ — repo={args.repo} tag={args.tag}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
