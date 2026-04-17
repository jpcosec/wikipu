---
pill_type: warning
scope: domain
language: en
nature: context
bound_to: audit-auto-task
created: 2026-04-17
lifecycle: current
---

# Audit Auto-Task Warnings

## Do NOT

- Create duplicate tasks for same violation
- Overwrite existing open tasks (append instead)
- Create tasks for exempt/known issues
- Run --auto-task in CI without dry-run option

## Boundary Conditions

1. **Duplicate detection:** Check if `audit-fix-{check}-{node}` already exists
2. **Priority:** All audit tasks are p2 by default
3. **Domain:** Always `compliance`
4. **Lifecycle:** Tasks auto-expire at 6 months

## Anti-Patterns

- Generating 100+ tasks from one audit run (batch instead)
- Creating tasks for informational findings
- Running auto-task without reviewing output
