# Org-Wide Spec-Kit Extension Catalog

A curated, organization-wide catalog of [Spec-Kit](https://github.com/github/spec-kit)
extensions. Extension **source** lives here, CI builds it into **ZIPs published as
GitHub Release assets**, and a generated [`catalog.json`](catalog.json) lets any
Spec-Kit project discover and install the org-approved extensions.

📚 **Browse all available extensions in [`EXTENSIONS.md`](EXTENSIONS.md)** — 200 extensions, 2066 commands.

## How it fits together

```
extensions/<id>/extension.yml   ──build──►  dist/<id>-<version>.zip  ──►  GitHub Release asset
                                                       │
                                                       ▼
                                                 catalog.json  ◄── consumers point here
```

- **`catalog.json`** — schema `1.0`. Maps each extension `id` to its metadata and
  the HTTPS `download_url` of its release ZIP. This is the file consuming projects
  point at.
- **`extensions/<id>/`** — source for each extension (`extension.yml` manifest +
  command templates + resources + optional `.extensionignore`).
- **`scripts/build.py`** — packages every extension into `dist/` and regenerates
  `catalog.json`.
- **`scripts/validate.py`** — fail-closed validation of the catalog and manifests.
- **`.github/workflows/`** — `validate.yml` checks every PR; `release.yml` publishes
  ZIPs and updates `catalog.json` when you publish a GitHub Release.

## Consuming this catalog (for project teams)

Add `.specify/extension-catalogs.yml` to a Spec-Kit project (see
[`examples/.specify/extension-catalogs.yml`](examples/.specify/extension-catalogs.yml)):

```yaml
catalogs:
  - name: Sketchkit Org Catalog
    url: https://raw.githubusercontent.com/nareshsiriveri/sketchkit/main/catalog.json
    priority: 10
    install_allowed: true
    description: Curated, org-approved Spec-Kit extensions.
```

| Field | Meaning |
|-------|---------|
| `url` | HTTPS URL to `catalog.json` (required) |
| `name` | Human-readable label |
| `priority` | Sort order — **lower = higher priority** |
| `install_allowed` | Whether installs are permitted from this source |
| `description` | Optional notes |

> **Fail-closed:** if `extension-catalogs.yml` exists but lists no catalogs (or any
> catalog lacks a `url`), Spec-Kit raises a `ValidationError` rather than falling
> back to defaults.

Alternatively, set `SPECKIT_CATALOG_URL` to this catalog's URL to override all
defaults via environment variable.

## Adding an extension (for catalog maintainers)

1. Create `extensions/<id>/extension.yml` (`<id>` must match `^[a-z0-9-]+$` and the
   directory name). Spec-Kit manifests nest metadata under `extension:`,
   `requires:`, and `provides:`:

   ```yaml
   schema_version: "1.0"

   extension:
     id: my-extension
     name: "My Extension"
     version: "0.1.0"
     description: What it does.
     author: Sketchkit
     repository: https://github.com/nareshsiriveri/sketchkit
     license: MIT
     effect: read-only        # optional: read-only | read-write

   requires:
     speckit_version: ">=0.2.0"

   provides:
     commands:
       - name: speckit.my-extension.do-thing
         file: commands/speckit.my-extension.do-thing.md
         description: What this command does.

   # Optional lifecycle hooks. Keyed by event (before_/after_ {specify,plan,
   # tasks,implement,analyze,clarify,checklist,constitution,converge}); each
   # references a provided command.
   hooks:
     before_implement:
       command: speckit.my-extension.do-thing
       optional: true

   tags:
     - example
   ```

2. Add command templates under `extensions/<id>/commands/`, matching each
   `file:` path. Command files use YAML frontmatter with a `description`, and
   command names must follow `speckit.<ext-id>.<cmd>`.
3. (Optional) Add `.extensionignore` to exclude files from the ZIP.
4. Run validation locally:

   ```bash
   pip install -r requirements.txt
   python scripts/validate.py
   ```

5. Open a PR. `validate.yml` runs automatically.

## Publishing a release

1. Bump `version` in the changed `extension.yml`.
2. Publish a **GitHub Release** with a tag like `v0.1.0`.
3. `release.yml` then:
   - builds `dist/<id>-<version>.zip` for every extension,
   - regenerates `catalog.json` with `download_url`s pointing at that release,
   - uploads the ZIPs as release assets,
   - commits the updated `catalog.json` back to `main`.

To build locally (e.g. to preview):

```bash
python scripts/build.py --repo nareshsiriveri/sketchkit --tag v0.1.0
```

## Catalog schema

`catalog.json` is validated against [`catalog.schema.json`](catalog.schema.json)
and mirrors spec-kit's own `extensions/catalog.json`. Top level: `schema_version`,
`updated_at`, `catalog_url`, `extensions`. Each entry requires `id`, `name`,
`version`, `description`, `download_url` (HTTPS) plus `author`, `repository`,
`bundled`, `tags`.

## Local testing

Install an extension straight from this repo into any Spec-Kit project without
publishing — note the `--dev` flag for a local path:

```bash
specify extension add --dev /path/to/this-repo/extensions/adr-logger
specify extension list
specify extension enable coverage-gate   # hooks are opt-in
```

## First-time setup checklist

- [ ] Confirm the repo slug `nareshsiriveri/sketchkit` matches your real GitHub repo.
- [ ] Replace the `acme-hello` sample with your real extensions.
- [ ] Push to GitHub and enable Actions.
- [ ] Publish the first release to generate real `download_url`s.
