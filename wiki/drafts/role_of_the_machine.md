---
identity:
  node_id: "doc:wiki/drafts/role_of_the_machine.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-1-database/machine_blueprint.md", relation_type: "documents"}
---

The DB viewer has the richest interactive state of all Phase I playgrounds. Browsing, inline-editing, and row-adding are mutually **exclusive modes** — the machine earns its place here because guards block invalid transitions (can't commit a row with validation errors) and because the async surface (GAS writes in Phase 4) is real. Without a machine, all of this would be imperative flag-juggling in Alpine.

## Details

The DB viewer has the richest interactive state of all Phase I playgrounds. Browsing, inline-editing, and row-adding are mutually **exclusive modes** — the machine earns its place here because guards block invalid transitions (can't commit a row with validation errors) and because the async surface (GAS writes in Phase 4) is real. Without a machine, all of this would be imperative flag-juggling in Alpine.

---

Generated from `raw/docs_cotizador/plan/legacy/I-1-database/machine_blueprint.md`.