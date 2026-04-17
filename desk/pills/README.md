# Context Pills

This directory contains context pills bound to tasks. Pills provide rationale and constraints for task execution.

## Pill Types

| Type | Purpose |
|------|---------|
| `guardrail` | Constraints that must not be violated |
| `decision` | Why this approach over alternatives |
| `pattern` | Architectural pattern to follow |
| `model` | Data model or schema to use |

## Lifecycle

```
Drafted → Bound to task → Audited after step →
  → Still needed? Keep.
  → Redundant with code/docs? Delete.
  → Complete. Knowledge flows to code/docs. Delete.
```

## Existing Pills

| Pill | Type | Bound To |
|------|------|----------|
| `owl-adr-003-context.md` | decision | owl-p1-4 |
| `owl-module-structure-guardrails.md` | guardrail | owl-p1 |
| `owl-usage-patterns.md` | pattern | owl-p1 |
| `owl-model-mapping.md` | model | owl-p1, owl-p2 |
| `owl-global-constraints.md` | guardrail | owl-p1-4 (global) |
| `owl-phase2-context.md` | decision | owl-p2, owl-p3 |
| `owl-python-examples.md` | pattern | owl-p1, owl-p2 |

## Coverage Matrix

| Type/Scope | global | domain | component |
|------------|--------|--------|-----------|
| decision | | owl-phase2-context | owl-adr-003-context |
| guardrail | owl-global-constraints | | owl-module-structure |
| pattern | | | owl-usage-patterns, owl-python-examples |
| model | owl-model-mapping | | |
