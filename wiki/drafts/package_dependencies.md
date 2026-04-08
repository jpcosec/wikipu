---
identity:
  node_id: "doc:wiki/drafts/package_dependencies.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md", relation_type: "documents"}
---

```

## Details

```
database/
    ├── IStore.js (abstract)
    │   ├── InMemoryStore
    │   ├── FileStore
    │   └── GasSheetStore
    │
    ├── ModelFactory.js
    └── Config_Schema.js (11 tables, single source of truth)

pricing/ ─────────┐
    ├── pipeline/ │
    ├── rules/    ├─→ LEGACY (still used for calculations)
    ├── adapters/ │
    └── formatting

domain/ ──────────┐
    ├── classes/ │
    ├── mixins/  ├─→ PHASE B (new architecture)
    ├── rules/   │
    └── RulesCoordinator

xstate/
    ├── Orchestration/
    │   ├── quotationMachine.xstate.js (blueprint)
    │   ├── adapters/ (actions, guards, services)
    │   └── runtime/ (XState v5 actor system)
    │
    └── depends on: database, domain OR pricing (switchable)

frontend/
    ├── Bridge/ (AlpineXStateBridge)
    ├── UI components
    └── depends on: xstate, domain OR pricing

bundling/ (Monorepo root)
    ├── entry.js (exports APIs)
    ├── createCotizadorActor.js (factory)
    ├── rollup.config.mjs (browser bundling)
    └── generated/ (auto-generated local data)
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md`.