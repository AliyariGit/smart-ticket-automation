# Prompt Template Library

Reusable prompt templates for engineering workflows.

## 1) API Scaffolding
**Template**
> Create a [language/framework] API endpoint for [feature].
> Constraints: follow [style guide], keep response contract stable, include validation and error handling.
> Inputs: [request schema]. Outputs: [response schema].
> Include tests for happy path, validation failure, and dependency failure.

## 2) SQL Optimization
**Template**
> Optimize this SQL query for performance while preserving behavior.
> Constraints: keep result set identical, use indexes where available, avoid unsafe dynamic SQL.
> Provide: optimized query, reasoning, and rollback option.

## 3) Legacy Code Explanation
**Template**
> Explain this legacy code in plain engineering language.
> Include: business rules inferred, edge cases, dependencies, and risks if refactored.
> Output sections: Summary, Inputs/Outputs, Decision Logic, Side Effects, Risks.

## 4) Migration Planning
**Template**
> Produce a phased migration plan from [legacy stack] to [target stack].
> Constraints: preserve behavior, minimize downtime, include parity checkpoints and rollback strategy.
> Output: phase-by-phase tasks, risks, test strategy, and exit criteria.

## 5) Test Generation
**Template**
> Generate unit/integration tests for [module/function].
> Cover: normal flow, null handling, boundary values, invalid inputs, and regression cases.
> Return tests and a coverage gap summary.

## 6) Support Ticket Classification
**Template**
> Classify this support ticket into [categories] and assign severity [P1-P4].
> Provide route target, confidence score, and rationale in 3 bullets.

## 7) Legacy Regression Risk Scan
**Template**
> Review this change for regression risk in legacy behavior.
> Flag: contract drift, null behavior changes, numeric rounding differences, date/time parsing changes.
> Return: risk matrix with mitigation steps.
