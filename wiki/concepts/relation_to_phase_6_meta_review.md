---
identity:
  node_id: "doc:wiki/concepts/relation_to_phase_6_meta_review.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/trail_collect.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/trail_collect.md"
  source_hash: "b5310580e40950c0da96febcf8d445391a89da95cb9c5c05c5157e3032195588"
  compiled_at: "2026-04-14T16:50:28.665703"
  compiled_from: "wiki-compiler"
---

Phase 6 from the methodology synthesis:

## Details

Phase 6 from the methodology synthesis:

> "At the end of every development session, the human operator reviews what the agent did, identifies friction — hallucinations, stuck states, routing failures, ambiguous rules — and immediately patches the meta-documentation that caused the friction."

Trail collect is the agent-side complement. Phase 6 is the human reviewing what the agent did. Trail collect is the agent extracting what it learned and encoding it before the session closes. Together they close the loop: nothing the session discovered should be lost.

---

Generated from `raw/trail_collect.md`.