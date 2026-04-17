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
| `owl-adr-003-context.md` | decision | owl-phase1-4 |
