---
description: List all Architecture Decision Records and their current status.
---

# /speckit.adr-logger.list

List every ADR in the project.

When invoked:

1. Scan `docs/adr/` for `NNNN-*.md` files.
2. For each, read the title line and the `Status:` field.
3. Print a table: number, title, status, date — sorted by number.
4. If `docs/adr/` does not exist, say so and suggest `/speckit.adr-logger.new`.
