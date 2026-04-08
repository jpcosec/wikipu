---
identity:
  node_id: "doc:wiki/drafts/4_recommended_migration_order.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/02_migration/api_migration_and_gap_analysis.md", relation_type: "documents"}
---

```

## Details

```
M-1  Path migration (v1→v2, CQRS structure, view discriminators)   2h
M-2  Gate decision generalisation                                   3h
──── At this point: UI works end-to-end with real API for read + HITL ────
M-3  Pipeline execution commands (scrape, run)                      1d
M-4  System endpoints (orchestration, scrapers, Neo4j sync)         4h
M-5  Archive / delete / explorer write                              3h
──── Backend complete ────
F-1  Wire all frontend hooks to real API (remove mock paths)        3h
F-2  Implement Application Context view (B3b)                       1d
F-3  Real-time status polling + error trace display                 4h
F-4  Match coverage summary + evidence bank linkage                 3h
F-5  Extract difficulty/category/confidence chips                   2h
F-6  Generate Documents diff view                                   4h
──── Full parity with dev branch vision ────
```

---

Generated from `raw/docs_postulador_ui/plan/02_migration/api_migration_and_gap_analysis.md`.