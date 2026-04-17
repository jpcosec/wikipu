---
pill_type: decision
scope: domain
language: en
nature: context
bound_to: audit-auto-task
created: 2026-04-17
lifecycle: current
---

# Auto-Task Generation Decision

## Why Automate Audit → Task Flow

**Current state:** Audit finds violations, they accumulate and are forgotten.

**Desired state:** Each audit finding becomes a tracked task automatically.

## Design Choice

### Option A: Inline task creation
```python
wiki-compiler audit --auto-task
# Creates desk/tasks/audit-fix-{check_name}-{hash}.md
```

### Option B: Board update only
```python
wiki-compiler audit --track
# Updates desk/tasks/Board.md with finding IDs
```

**Chosen:** Option A — file-based tasks enable per-issue commit traceability.

## Task File Template

```markdown
---
id: audit-fix-{check_name}-{node_id_hash}
domain: compliance
status: open
priority: p2
created: {timestamp}
---

# Audit Fix: {check_name}

## Finding
{file}:{line} — {violation description}

## How to Fix
{reference to relevant code/rule}

## Validation
Run audit again, should pass
```

## Reference

- `src/wiki_compiler/auditor.py`
- `desk/tasks/Board.md`
