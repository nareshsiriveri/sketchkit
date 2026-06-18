---
description: Create a new Architecture Decision Record (ADR) in docs/adr/ from the current context.
---

# /speckit.adr-logger.new

Create a new Architecture Decision Record.

When invoked:

1. Ask for (or infer from context) the decision title.
2. Determine the next ADR number by scanning `docs/adr/` for existing
   `NNNN-*.md` files; use `0001` if none exist.
3. Write `docs/adr/<NNNN>-<kebab-title>.md` using the standard template:

   ```markdown
   # <NNNN>. <Title>

   - Status: Proposed
   - Date: <today>

   ## Context
   <Why this decision is needed.>

   ## Decision
   <What was decided.>

   ## Consequences
   <Trade-offs and follow-ups.>
   ```

4. Report the path of the created file.
