---
identity:
  node_id: "doc:wiki/drafts/high_level_architecture.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md", relation_type: "documents"}
---

```

## Details

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                         CLAPS CODELAB MONOREPO ARCHITECTURE                         │
└─────────────────────────────────────────────────────────────────────────────────────┘

                              📦 BUNDLER ENTRY POINT
                         bundling/createCotizadorActor.js
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
                    ▼               ▼               ▼
            ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
            │   Frontend   │  │    XState    │  │   Database   │
            │   Package    │  │   Package    │  │   Package    │
            └──────────────┘  └──────────────┘  └──────────────┘
                    │               │               │
                    │               │               │
            AlpineXState      Quotation        TableStore
            Bridge.js         Machine.js       (+ LocalInit)
                    │               │               │
                    ▼               ▼               ▼
        ┌─────────────────────────────────────────────────┐
        │  XState Orchestrator (Wires everything together)│
        │  ┌───────────────────────────────────────────┐  │
        │  │ context.store (Database layer)            │  │
        │  │ context.catalog (Reference data)          │  │
        │  │ context.lineas (Quotation items)          │  │
        │  │ context.totals (Computed pricing)         │  │
        │  └───────────────────────────────────────────┘  │
        └────────────┬──────────────────────────────────┬─┘
                     │                                  │
        ┌────────────▼──────────────┐     ┌────────────▼──────────────┐
        │   Domain Package (Phase B) │     │   Pricing Package (Legacy)│
        │   ┌──────────────────────┐│     │   ┌──────────────────────┐│
        │   │ • Catalog            ││     │   │ • Pipeline (6-stage) ││
        │   │ • Basket             ││     │   │ • RulesEngine (9+)   ││
        │   │ • Item               ││     │   │ • Adapters           ││
        │   │ • Category           ││     │   │ • Formatting         ││
        │   │ • RulesCoordinator   ││     │   │ • Defaults           ││
        │   │ • Mixins (Rulable,   ││     │   │ • Manual Overrides   ││
        │   │   Prizable, etc.)    ││     │   └──────────────────────┘│
        │   └──────────────────────┘│     └────────────────────────────┘
        └────────────┬───────────────┘
                     │
        ┌────────────▼──────────────────┐
        │  Pure Calculation Functions   │
        │  (No side effects, no I/O)    │
        │  • Quantity resolution        │
        │  • Price calculations         │
        │  • Rule evaluation (JSON-Lgc) │
        │  • Display formatting         │
        └───────────────────────────────┘
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md`.