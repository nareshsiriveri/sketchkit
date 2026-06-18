#!/usr/bin/env python3
"""coverage-gate lifecycle hook.

Fails (non-zero exit) if total test coverage is below COVERAGE_MIN (default 80).
Reads a Cobertura-style coverage.xml if present; otherwise warns and passes so
the hook never blocks a project that hasn't wired up coverage yet.
"""
from __future__ import annotations

import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def main() -> int:
    threshold = float(os.environ.get("COVERAGE_MIN", "80"))
    report = Path("coverage.xml")

    if not report.exists():
        print("coverage-gate: no coverage.xml found — skipping (run tests with coverage).")
        return 0

    try:
        root = ET.parse(report).getroot()
        line_rate = float(root.get("line-rate", "0"))
    except (ET.ParseError, ValueError) as exc:
        print(f"coverage-gate: could not parse coverage.xml: {exc}")
        return 0

    pct = line_rate * 100
    if pct + 1e-9 < threshold:
        print(f"coverage-gate: FAIL — coverage {pct:.1f}% < threshold {threshold:.0f}%")
        return 1

    print(f"coverage-gate: OK — coverage {pct:.1f}% >= threshold {threshold:.0f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
