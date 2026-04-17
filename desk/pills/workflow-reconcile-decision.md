---
pill_type: decision
scope: domain
language: en
nature: context
bound_to: reconcile-workflow-structure
created: 2026-04-17
lifecycle: current
---

# Workflow Reconciliation Decision

## The Problem

Two parallel structures exist:
- `workflow/` — Supervisor/Executor/Pill/Board
- `wiki/standards/` — OP-1-10/WK/NAV/ID rules

## Why Reconcile

1. **Duplication** — Two sources of truth for agent protocols
2. **Drift** — Rules diverge over time
3. **Complexity** — Agents must consult both

## Chosen Approach

**Merge toward wiki/ontology** — wikipu is the canonical structure.

| From workflow/ | Becomes in wiki/ |
|-----------------|------------------|
| AGENTS.md | Deprecated → wiki/concepts/workflow.md |
| STANDARDS.md | Deprecated → wiki/standards/ (absorbed) |
| instructions/* | wiki/reference/workflows/* |
| init_instructions.md | Keep (bootstrap use) |

## OWL Modeling

Per ADR-004, model as ontology:
```
workflow:Supervisor → OWL class
workflow:Executor → OWL class
workflow:Ritual → OWL class
```

## Reference

- `wiki/adrs/004_workflow_as_ontology.md`
- `wiki/standards/house_rules.md`
