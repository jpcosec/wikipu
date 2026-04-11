---
identity:
  node_id: "doc:wiki/drafts/facet_4_architectural_invariants.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/methodology_synthesis.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/methodology_synthesis.md"
  source_hash: "509baf32ca0ea70f59fdc2382e05095dde9fba07ad7092c46d49ecdca431bc34"
  compiled_at: "2026-04-10T17:47:33.732043"
  compiled_from: "wiki-compiler"
---

**Question:** What layer/module rules appear in every project?

## Details

**Question:** What layer/module rules appear in every project?

**Cotizador:**
- UI (projection/intent) → orchestration (transitions) → domain (pure logic) → adapters (I/O)
- No layer absorbs another's responsibility
- Pure domain: no DB access, no UI state reads, no transport concerns

**Doc_methodology (PhD 2.0):**
- CLI > API > UI: all functionality born as deterministic CLI function first
- Deterministic functions (core/) are always separate from AI/LangGraph nodes (nodes/)

**Postulador_refactor / postulador_v2:**
- `contracts.py` — all schemas, the boundary between modules
- `storage.py` — all file I/O, no business logic
- `main.py` — CLI entry point only, no business logic
- `graph.py` — orchestration only

**Universal invariant across all projects:**

> Deterministic logic is always separate from AI logic. AI logic is always separate from I/O. I/O is always separate from presentation. Every boundary is defined by a typed contract.

**The consistent physical expression of this rule:**
- `contracts.py` exists in every Python project
- The domain core can always be tested without an LLM, a database, or a UI

---

Generated from `raw/methodology_synthesis.md`.