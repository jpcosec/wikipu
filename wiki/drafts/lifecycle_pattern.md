---
identity:
  node_id: "doc:wiki/drafts/lifecycle_pattern.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md", relation_type: "documents"}
---

All components follow this pattern:

## Details

All components follow this pattern:

```
┌──────────────────┐
│  INITIALIZATION  │
│ - Load config    │
│ - Create machine │
│ - Mount HTML     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│   READY/IDLE     │
│ - Listen events  │
│ - Sync UI        │
└────────┬─────────┘
         │
    ┌────┴─────┬──────────┬──────────┐<!-- This should be more generic for description of component-->
    │           │          │          │
    ▼           ▼          ▼          ▼
  USER      CALCULATE  EVALUATE    SAVE
  INPUT     CHANGES    RULES       STATE
    │           │          │          │
    └────────┬──┴──────┬───┴──────┬───┘
             │         │          │
             └────┬────┴────┬─────┘
                  │         │
                  ▼         ▼
          UPDATE CONTEXT   SYNC UI
```

### Key Phases

1. **INITIALIZATION** — Factory function creates DOM, mounts machine, initializes context
2. **IDLE** — Waiting for user interaction or external events
3. **HANDLING** — Processing events (user input, rule evaluation, calculations)
4. **SYNCING** — Pushing calculated state back to UI
5. **SAVING** — Persisting or exposing state to parent container

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md`.