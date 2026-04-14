---
identity:
  node_id: "doc:wiki/concepts/principle_1_single_responsibility.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/wiki_construction_principles.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/wiki_construction_principles.md"
  source_hash: "adb2697fc76ec9f466878e73986e50abfad611e8104bf6edd4d6d0952660dedf"
  compiled_at: "2026-04-14T16:50:28.666914"
  compiled_from: "wiki-compiler"
---

Each wiki node answers exactly one question or defines exactly one concept.

## Details

Each wiki node answers exactly one question or defines exactly one concept.
If you cannot state the node's purpose in one sentence, it needs to be split.

The test: can you transclude this node into two different parent documents
and have it make sense in both contexts? If yes, it is atomic.
If it only makes sense in one context, it is probably not atomic — it is
a section of a larger document masquerading as a node.

---

Generated from `raw/wiki_construction_principles.md`.