# Context Pills

This directory contains context pills bound to tasks. Pills provide rationale and constraints for task execution.

## Pill Types

| Type | Purpose |
|------|---------|
| `guardrail` | Constraints that must not be violated |
| `decision` | Why this approach over alternatives |
| `pattern` | Architectural pattern to follow |
| `model` | Data model or schema to use |
| `warning` | When to NOT do something |
| `tip` | Quick operational hints |
| `reference` | Links to docs |
| `example` | Concrete code snippets |

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
| `owl-adr-003-context.md` | decision | owl-p1-4 ✅ |
| `owl-module-structure-guardrails.md` | guardrail | owl-p1 ✅ |
| `owl-usage-patterns.md` | pattern | owl-p1 ✅ |
| `owl-model-mapping.md` | model | owl-p1, owl-p2 ✅ |
| `owl-global-constraints.md` | guardrail | owl-p1-4 (global) ✅ |
| `owl-phase2-context.md` | decision | owl-p2, owl-p3 ✅ |
| `owl-python-examples.md` | pattern | owl-p1, owl-p2 ✅ |
| `pirate-teaching-guardrails.md` | guardrail | pirate-teach |
| `pirate-teaching-pattern.md` | pattern | pirate-teach |
| `audit-auto-task-decision.md` | decision | audit-auto-task |
| `audit-auto-task-pattern.md` | pattern | audit-auto-task |
| `audit-auto-task-warnings.md` | warning | audit-auto-task |
| `workflow-reconcile-decision.md` | decision | reconcile-workflow |
| `workflow-reconcile-pattern.md` | pattern | reconcile-workflow |
| `global-tips.md` | tip | global |
| `global-reference.md` | reference | global |
| `global-examples.md` | example | global |
| `global-warnings.md` | warning | global |

## Coverage Matrix

| Type/Scope | global | domain | component |
|------------|--------|--------|-----------|
| decision | | owl-phase2-context, audit-auto-task, workflow-reconcile | owl-adr-003-context |
| guardrail | owl-global-constraints, global-warnings | pirate-teaching-guardrails | owl-module-structure |
| pattern | | pirate-teaching-pattern, audit-auto-task-pattern, workflow-reconcile-pattern | owl-usage-patterns, owl-python-examples |
| model | owl-model-mapping | | |
| warning | global-warnings | audit-auto-task-warnings | |
| tip | global-tips | | |
| reference | global-reference | | |
| example | global-examples | | |
