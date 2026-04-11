---
identity:
  node_id: "doc:wiki/drafts/q5_what_do_real_future_docs_entries_look_like_are_the_rules_followed.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/methodology_synthesis_addendum.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/methodology_synthesis_addendum.md"
  source_hash: "4084c2da6197485937ca035f86e9b26279ac1b2b99f034e9b01605dc9519f504"
  compiled_at: "2026-04-10T17:47:33.732664"
  compiled_from: "wiki-compiler"
---

**logging_layer_conflicts.md (postulador_refactor) — well-formed entry:**

## Details

**logging_layer_conflicts.md (postulador_refactor) — well-formed entry:**
- Why deferred: "not the main blocker for current API-backed pipeline execution"
- Last reviewed: 2026-03-29
- Problem: specific — 4 enumerated mixing styles, clear impact analysis
- Proposed direction: 5 concrete numbered steps
- No linked TODOs (could be a gap, or they weren't added yet)

This is exactly what the template asks for. Short, specific, actionable when prioritized.

**extract_understand_node.md (postulador_refactor) — well-formed entry:**
- Why deferred: "current focus is pipeline orchestration"
- Last reviewed: 2026-03-29
- Contains the full output contract (Pydantic model with field-level detail)
- Describes what the refactored branch needs (specific rewrite instruction)
- Lists other dev branch nodes to port
- Has a linked TODO

This is denser than the template — it includes the full schema definition so that when someone picks it up, they have everything needed to start. The template is a floor, not a ceiling.

**product_standard.md (postulador_v2) — informal note:**
This is raw thinking, not a formal future_docs entry. It reads as stream of consciousness: "i think that all of them but match hardening are part of the same bigger problem..." and sketches a vision for a unified architecture. It does not follow the template format.

This reveals something important: future_docs/ in practice accepts two kinds of entries:
1. **Formal entries** — template-compliant, specific problem + proposed direction + linked TODO + last-reviewed date. These are ready to promote to plan_docs when prioritized.
2. **Seed notes** — informal sketches of larger architectural directions, not yet refined enough for a formal plan. These are thinking-in-progress, not deferred-but-ready.

The methodology only defines the first type. The second type exists in practice but has no formal status. It represents the gap between "raw/ as ore" and "future_docs/ as deferred work" — a category for ideas that are neither raw material nor ready-to-act deferred items.

**Finding:** The template is followed for specific, scoped items. For larger architectural visions that span multiple modules, an informal note exists but has no defined lifecycle. This is a gap — the current methodology has no document type for "architectural hypothesis not yet decomposed into actionable items." It ends up in future_docs/ as an informal note or never written down at all.

---

Generated from `raw/methodology_synthesis_addendum.md`.