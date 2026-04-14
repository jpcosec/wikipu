---
identity:
  node_id: "doc:wiki/concepts/synthesis_what_these_5_questions_add_to_the_distillation.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/methodology_synthesis_addendum.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/methodology_synthesis_addendum.md"
  source_hash: "4084c2da6197485937ca035f86e9b26279ac1b2b99f034e9b01605dc9519f504"
  compiled_at: "2026-04-14T16:50:28.662811"
  compiled_from: "wiki-compiler"
---

**Addition to the 5 axioms:**

## Details

**Addition to the 5 axioms:**

**Axiom 6 (confirmed): The methodology improves itself.**
Phase 6 (meta-review) is not optional. Every session ends with a human audit that patches the rules which caused friction. The hausordnung is the current best version of the rules, not the final version. When a rule causes confusion, it is rewritten before the session closes. This is the mechanism that prevents the methodology from going stale.

**New finding — the missing document type:**
The current methodology covers: future_docs (formal deferred work) and raw/ (immutable ore). But it has no category for "architectural hypothesis" — an idea that's too large to be a deferred item and too unrefined to be raw ore. The product_standard.md informal note lives in this gap. The hausordnung should define this type explicitly, or route it to a specific location (e.g., `raw/thinking/` as a named sub-sanctuary before formalization).

**New finding — navigation is a first-class concern, not an afterthought:**
Every mature project has an explicit navigation layer: canonical maps, conceptual trees, routing matrices. These are not documentation — they are the index that makes documentation usable. A project without a navigation layer forces every reader (human or agent) to discover structure by exploration, which produces inconsistent mental models. The navigation layer should be designed before content accumulates, not added after the fact.

**New finding — the routing matrix is the missing link in wikipu:**
The context router protocol is exactly what the `query-server-runtime` issue in wikipu is asking for. The difference is that the doc_methodology implements it as a coordinate-based retrieval system with a JSON routing matrix, not as a free-form graph query. This is a simpler and more deterministic design than a full structured query language. It may be a better first implementation of the Librarian agent's tool interface.

Generated from `raw/methodology_synthesis_addendum.md`.