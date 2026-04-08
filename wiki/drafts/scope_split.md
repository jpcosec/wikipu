---
identity:
  node_id: "doc:wiki/drafts/scope_split.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/legacy-ui-recovery.md", relation_type: "documents"}
---

### 1) Backend Compatibility (Migration-First)

## Details

### 1) Backend Compatibility (Migration-First)

These areas are migration-first and must preserve legacy semantics:

- GAS function compatibility and fallback method families.
- Save/load payload and response contracts.
- Persistence table behavior and shape compatibility (`COTIZACIONES`, `LINEA_DETALLE`, related fields).
- Save-first PDF orchestration contract (`save -> generate by quotation ID`).

Goal: same external behavior for persisted quotation workflows.

### 2) Frontend Implementation (Rebuild-Native)

These areas must follow rebuild architecture, not legacy UI implementation style:

- Alpine templates render state and dispatch user intent only.
- Runtime or component APIs own state mutations and transitions.
- Screen/state/event mapping remains explicit and documented.
- No direct storage or GAS transport calls from template logic.
- Component-level interaction contracts are reused across screens.

Goal: modern, testable UI architecture while preserving user-visible behavior.

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/legacy-ui-recovery.md`.