---
status: open
priority: p3
depends_on: []
created: 2026-04-22
assigned_to: self
---

# Integrate sldb with wiki-compiler ingest

Allow `wiki-compiler ingest` to read from `.sldb/` store.

## Why

- sldb store is a structured index
- Can ingest structured docs from federated stores
- Unified ingestion source

## Implementation

1. `ingest.py` reads from `.sldb/documents/`
2. `sldb store check` pre-ingest validation
3. Track ingestion in `knowledge_graph.json`