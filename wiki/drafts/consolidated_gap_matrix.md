---
identity:
  node_id: "doc:wiki/drafts/consolidated_gap_matrix.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md", relation_type: "documents"}
---

| ID | Category | Severity | Steps | Description | Resolution |

## Details

| ID | Category | Severity | Steps | Description | Resolution |
|---|---|---|---|---|---|
| GAP-ARCH-01 | Architecture | Blocker | 01 | No persistence boundary | Resolved in 01 |
| GAP-ARCH-02 | Architecture | High | 01 | No unified state contract | Resolved in 01 |
| GAP-ARCH-03 | Architecture | High | 01b, 03, 03a | No anchor identity model | Declared in 01b, implemented in 03 |
| GAP-IMPL-01 | Implementation | High | 01 | NodeEditor has no save/load | Resolved in 01 (pluggable persistence) |
| GAP-IMPL-02 | Implementation | High | all | Zero frontend test files | Resolved in 00 test infrastructure |
| GAP-IMPL-03 | Implementation | Medium | 01a | Layout presets local-only | Resolved in 01a |
| GAP-DEP-01 | Dependency | Blocker | 03a-f | Rich nodes before registry | 01b must complete first |
| GAP-DEP-02 | Dependency | High | 04, 04a | External data before persistence | 01 must complete first |
| GAP-SCHEMA-01 | Schema | Medium | 00c | Schema evolution / versioning | schema_version + migration functions |
| GAP-SCHEMA-02 | Schema | Medium | 00c | Cross-schema views | Define merged schema or cross-refs |
| GAP-SCHEMA-03 | Schema | Low | 00c | Schema inheritance | Deferred |
| GAP-THEME-01 | Theme | Medium | 00d | Dark mode strategy | Theme files use media queries |
| GAP-THEME-02 | Theme | Low | 00d | Theme validation warnings | Dev-mode console warnings |
| GAP-EXT-01 | Extension | Medium | 00e | Extension packaging | Deferred until first external consumer |
| GAP-EXT-02 | Extension | Low | 00e | Extension conflict resolution | Last-registered wins + warning |
| GAP-PERF-01 | Performance | Medium | 02 | Proxy edge deduplication untested at scale | Generalize dedup logic, benchmark with 20+ collapsed containers |
| GAP-PERF-02 | Performance | Medium | 01, 01a | No performance budget for large graphs (500+ nodes) | Set target: layout <500ms, render <16ms. elkjs WASM worker helps but needs benchmark |
| GAP-SPEC-01 | Spec | Medium | — | Two critical docs in Spanish only: `docs/architecture/node_editor_frontend_implementation_plan.md` and `docs/architecture/cv_graph_container_nodes_uiux_spec.md` | Translate or create English summaries |

---

Generated from `raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md`.