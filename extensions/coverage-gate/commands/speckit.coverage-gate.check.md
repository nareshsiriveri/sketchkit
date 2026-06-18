---
description: Report current test coverage and whether it meets the configured threshold.
---

# /speckit.coverage-gate.check

Check the project's test coverage against the threshold.

When invoked:

1. Read the threshold from the `COVERAGE_MIN` environment variable
   (default `80`).
2. Locate a coverage report (`coverage.xml`, `coverage.json`, or `.coverage`).
   If none exists, tell the user to run their test suite with coverage first.
3. Report the current total coverage percentage and whether it is at or above
   the threshold.
4. If below, list the files with the lowest coverage as suggested next steps.
