---
identity:
  node_id: "doc:wiki/drafts/planning_rule_critical.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/README.md", relation_type: "documents"}
---

U-series plans are migration-first for backend and service contracts, not greenfield.

## Details

U-series plans are migration-first for backend and service contracts, not greenfield.

Before creating new backend behavior, each track must port and align existing persistence and integration semantics from `claps_codelab/`.

UI implementation is rebuild-native and must follow component architecture:

- Alpine templates for projection and user intent,
- XState/runtime orchestration for transitions,
- pure domain logic for calculations/rules,
- adapter boundaries for DB and external services.

Legacy UI is a behavior reference, not an implementation template.

Primary legacy references:

- `claps_codelab/Codigo.js` (GAS router functions)
- `claps_codelab/Controller_Cotizacion.js` (save/load/pdf services)
- `claps_codelab/Models.js` + `claps_codelab/SheetDB.js` (data and persistence behavior)
- `claps_codelab/Stores_App.html` + `claps_codelab/Components_Timeline.html` (behavior reference for UI flow and interaction semantics)

Architecture policy reference:

- `docs/ARCHITECTURE/legacy-ui-recovery.md`

Generated from `raw/docs_cotizador/plan/README.md`.