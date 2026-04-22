---
status: open
priority: p3
depends_on:
  - desk/tasks/migrate-wiki-to-sldb.md
created: 2026-04-22
assigned_to: self
---

# Add SLDB Energy Audit

Use `.sldb/documents/` for redundancy detection in energy audit.

## Why

- Hash-indexed docs for fast comparison
- Detect duplicate structure via model type
- Federated stores for cross-repo redundancy

## Implementation

1. `energy.py` reads `.sldb/documents/` index
2. Compare doc hashes for redundancy
3. Flag models with many doc instances (possible boilerplate)