---
identity:
  node_id: "doc:wiki/drafts/migration_vs_runtime_docs.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/11_routing_matrix.md", relation_type: "documents"}
---

| Type | Location | Purpose | Example |

## Details

| Type | Location | Purpose | Example |
|------|----------|---------|---------|
| **Runtime** | `docs/runtime/ui/` | Target state - UI after merge | `architecture.md`, `views.md`, `components.md` |
| **Runtime** | `docs/runtime/api/` | Target state - FastAPI backend | `README.md` |
| **Runtime** | `docs/runtime/pipeline/` | Target state - LangGraph orchestration | `README.md`, `node_matrix.md` |
| **Runtime** | `docs/runtime/core/` | Target state - Deterministic functions | `README.md` |
| **Runtime** | `docs/runtime/cli/` | Target state - Operator entrypoints | `README.md` |
| **Plan/Migration** | `plan/01_ui/specs/` | How to get there - migration path | `B3_match.md`, `00_architecture.md` |
| **Merge Plan** | `docs/seed/plan/UI_REDESIGN_MERGE_PLAN.md` | Executable merge instructions | Pre-merge audit, compatibility check |

**Rule**: `plan/` docs → `docs/runtime/` after successful merge (promotion workflow)

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/11_routing_matrix.md`.