#!/usr/bin/env python3
"""
Simple validation script for AI-generated engineering artifacts.

Checks include:
- SQL safety signals
- API contract marker presence
- naming convention hints
- null-handling reminders
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

UNSAFE_SQL_PATTERNS = [
    r"SELECT\s+\*\s+FROM\s+\w+\s*;",  # broad query hint
    r"\+\s*request\.",  # string concatenation from request input
    r"EXEC\s*\(",
]


def check_sql_safety(content: str) -> list[str]:
    issues: list[str] = []
    for pattern in UNSAFE_SQL_PATTERNS:
        if re.search(pattern, content, flags=re.IGNORECASE):
            issues.append(f"Potential unsafe SQL pattern matched: {pattern}")
    return issues


def check_api_contract_markers(content: str) -> list[str]:
    issues: list[str] = []
    required_markers = ["request schema", "response schema"]
    lowered = content.lower()
    for marker in required_markers:
        if marker not in lowered:
            issues.append(f"Missing API contract marker: '{marker}'")
    return issues


def check_naming_convention(content: str) -> list[str]:
    issues: list[str] = []
    # Simple heuristic: discourage mixed spaces in snake_case-like identifiers.
    if "camel case" in content.lower():
        issues.append("Found phrase 'camel case'; verify repository naming standards.")
    return issues


def check_null_handling(content: str) -> list[str]:
    issues: list[str] = []
    keywords = ["null", "none", "nil"]
    if not any(keyword in content.lower() for keyword in keywords):
        issues.append("No null-handling keywords found; verify edge case handling.")
    return issues


def validate_file(file_path: Path) -> list[str]:
    content = file_path.read_text(encoding="utf-8", errors="ignore")
    issues: list[str] = []
    issues.extend(check_sql_safety(content))
    issues.extend(check_api_contract_markers(content))
    issues.extend(check_naming_convention(content))
    issues.extend(check_null_handling(content))
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate AI-generated artifacts.")
    parser.add_argument("paths", nargs="+", help="Files to validate")
    args = parser.parse_args()

    total_issues = 0
    for raw_path in args.paths:
        path = Path(raw_path)
        if not path.exists() or not path.is_file():
            print(f"[WARN] Skipping non-file path: {path}")
            continue

        issues = validate_file(path)
        if issues:
            print(f"[FAIL] {path}")
            for issue in issues:
                print(f"  - {issue}")
            total_issues += len(issues)
        else:
            print(f"[PASS] {path}")

    if total_issues > 0:
        print(f"\nValidation completed with {total_issues} issue(s).")
        return 1

    print("\nValidation completed with no issues.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
