---
status: open
priority: p2
depends_on:
  - desk/tasks/finish-sldb-models.md
created: 2026-04-22
assigned_to: self
---

# Integrate sldb with wiki-compiler scaffold

Make `wiki-compiler scaffold` use SLDB models instead of manual templates.

## Why

- New docs automatically tracked in `.sldb/documents/`
- Roundtrip validation at creation time
- Consistent structure from the start

## Implementation

1. `scaffold.py` calls `sldb model add` on model registration
2. `scaffold.py` calls `sldb doc add` on document creation
3. Remove manual template rendering

## Verification

```bash
wiki-compiler scaffold concept "Test Doc"
# Should create and track in sldb store
sldb store check  # Should pass
```