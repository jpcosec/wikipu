---
pill_type: pattern
scope: domain
language: en
nature: context
bound_to: audit-auto-task
created: 2026-04-17
lifecycle: current
---

# Audit → Task Generation Pattern

## Implementation Steps

1. Add `--auto-task` flag to audit command
2. When violations found, call `_create_audit_task(finding)`
3. Task ID format: `audit-fix-{check_name}-{node_id_hash}`
4. Update Board.md summary

## Code Structure

```python
# auditor.py
def _create_audit_task(finding: AuditFinding) -> Path:
    task_id = f"audit-fix-{finding.check_name}-{hash(finding.node_id)}"
    task_file = desk/tasks/{task_id}.md
    # Write task file from template
    return task_file

def run_audit(...) -> AuditReport:
    findings = _run_checks(...)
    if args.auto_task:
        for finding in findings:
            _create_audit_task(finding)
    return AuditReport(findings=findings)
```

## Validation

```bash
wiki-compiler audit --auto-task
ls desk/tasks/audit-fix-*.md  # Should list new tasks
```

## Reference

- `src/wiki_compiler/auditor.py`
- `desk/tasks/Board.md`
