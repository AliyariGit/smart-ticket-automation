# CLAUDE.md

## Purpose
This repository contains reusable AI engineering workflow assets for enterprise delivery teams.

## Operating Principles
1. Prefer deterministic, reusable prompts over one-off chat requests.
2. Keep outputs constrained to existing architecture and coding standards.
3. Validate AI-generated outputs before merge.
4. Preserve legacy business behavior during modernization.

## Engineering Rules
- Match existing naming conventions in each codebase.
- Respect API contracts and schema constraints.
- Use parameterized SQL only; never generate dynamic unsafe SQL.
- Preserve null-handling and boundary-case behavior from legacy systems.
- Generate tests for critical business logic and migration deltas.

## Legacy Modernization Notes
- Extract business logic first, then refactor.
- Document assumptions explicitly in migration plans.
- For Delphi/.NET migrations, keep behavior parity checkpoints for each module.

## Review Checklist for AI Output
- Contract compatibility validated
- SQL safety checks passed
- Naming/style checks passed
- Regression-risk scan completed
- Test coverage added or updated
