---
identity:
  node_id: "doc:wiki/drafts/summary.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md", relation_type: "documents"}
---

The legacy architecture is a **layered, modular monorepo** with:

## Details

The legacy architecture is a **layered, modular monorepo** with:

1. **Clear separation** of database, calculations, and orchestration
2. **Pluggable components** (stores, rules, calculation engines)
3. **Pure functions** for calculations (testable, fast, reusable)
4. **Single orchestrator** (XState) that owns state and I/O
5. **Minimal dependencies** (xstate + json-logic-js only)
6. **Single bundle output** (IIFE for browser + GAS)

This design enables **easy testing**, **flexible deployment**, and **maintainable code** across 5 independent packages.

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md`.