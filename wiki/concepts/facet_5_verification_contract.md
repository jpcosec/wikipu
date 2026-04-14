---
identity:
  node_id: "doc:wiki/concepts/facet_5_verification_contract.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/methodology_synthesis.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/methodology_synthesis.md"
  source_hash: "509baf32ca0ea70f59fdc2382e05095dde9fba07ad7092c46d49ecdca431bc34"
  compiled_at: "2026-04-14T16:50:28.661855"
  compiled_from: "wiki-compiler"
---

**Question:** What does "done" mean? What proof is required?

## Details

**Question:** What does "done" mean? What proof is required?

**postulador_langgraph:** 4-level order: (1) unit/slice tests → (2) build/type-check → (3) browser or operator flow → (4) end-to-end sanity.

**doc_methodology:** TestSprite evidence required in every commit message. pre-push hook blocks push on failing tests. Done without proof doesn't exist.

**Feature creation methodology (postulador_v2):** Each execution slice must leave the codebase in a valid state. Tests written alongside or before implementation. Refactor ends with removal of legacy code and update of all documentation.

**Deterministic rebuild plan (postulador_langgraph):** One step at a time. Run deterministic tests after each step. No exceptions.

**Finding:** Done = tests pass at each step + changelog updated. Tests are not an end-gate; they are inline. A step that cannot be verified in isolation is a design problem, not a process problem. "Final" verification exists but it's a sanity check on already-verified slices, not the primary gate.

---

Generated from `raw/methodology_synthesis.md`.