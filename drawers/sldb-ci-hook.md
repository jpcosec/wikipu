---
status: open
priority: p1
depends_on:
  - desk/tasks/finish-sldb-models.md
  - desk/tasks/migrate-wiki-to-sldb.md
created: 2026-04-22
assigned_to: self
---

# Add SLDB Store Check to Pre-Commit Hook

Integrate `sldb store check` into git pre-commit hook for CI.

## Why

- Catch doc drift before commit
- Verify hash cascade integrity
- Ensure all tracked docs validate

## Implementation

Add to `.git/hooks/pre-commit`:

```bash
sldb store check || exit 1
```

Or integrate via `pre-commit` framework.