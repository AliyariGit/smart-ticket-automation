# AGENTS.md

## Scope
Use this file as operational context for AI coding agents working in this repository.

## Agent Workflow
1. Read `CLAUDE.md` before generating code or plans.
2. Use `prompt-template-library.md` templates whenever possible.
3. Run `enterprise_ai_validation_script.py` on generated artifacts.
4. Produce a short change summary with risks and assumptions.

## Output Requirements
- Keep implementation simple and reviewable.
- Prefer explicit assumptions over hidden behavior.
- Flag uncertain legacy logic instead of inventing rules.

## Validation Requirements
- API payloads follow declared contracts.
- SQL is parameterized and includes guardrails.
- Null and edge-case handling is explicit.
- Naming conventions remain consistent.
