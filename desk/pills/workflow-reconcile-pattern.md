---
pill_type: pattern
scope: domain
language: en
nature: context
bound_to: reconcile-workflow-structure
created: 2026-04-17
lifecycle: current
---

# Workflow Reconciliation Pattern

## Migration Steps

1. **Create wiki/reference/workflows/**
   ```bash
   mkdir -p wiki/reference/workflows
   ```

2. **Move instructions**
   ```
   workflow/instructions/supervisor.md → wiki/reference/workflows/supervisor.md
   workflow/instructions/executor.md → wiki/reference/workflows/executor.md
   workflow/instructions/pill-audit.md → wiki/reference/workflows/pill-audit.md
   workflow/instructions/context_compiler.md → wiki/reference/workflows/context-compiler.md
   ```

3. **Create ontology anchor**
   ```
   wiki/concepts/workflow.md
   # Defines workflow:* classes, references workflows/*
   ```

4. **Deprecate old files**
   ```
   workflow/AGENTS.md → add "DEPRECATED" header
   workflow/STANDARDS.md → add "DEPRECATED" header
   ```

5. **Update gitignore**
   ```
   # Add: workflow/instructions/*
   ```

6. **Update AGENTS.md**
   ```
   → Point to wiki/ontology
   ```

## Verification

```bash
ls wiki/reference/workflows/  # Should have 4 files
grep DEPRECATED workflow/AGENTS.md  # Should match
```
