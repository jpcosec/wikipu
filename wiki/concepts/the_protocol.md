---
identity:
  node_id: "doc:wiki/concepts/the_protocol.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/socratic_protocol.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/socratic_protocol.md"
  source_hash: "1ecd4801eb5667e7d2265db07683a47f662dafe281c76a92522cdfe19f2a5a99"
  compiled_at: "2026-04-14T16:50:28.664794"
  compiled_from: "wiki-compiler"
---

1. **Input**: a plan file, a node, or a proposed design.

## Details

1. **Input**: a plan file, a node, or a proposed design.
2. **Interrogation**: generate questions by type, each linked to the specific claim or section that prompted it.
3. **Output**: a structured Q&A artifact stored in `desk/socratic/`. Each question is an item on the Board. It is unresolved until a human (or agent with authority) provides an answer.
4. **Resolution**: when a question is answered, the answer is encoded — either in the relevant doc, in the hausordnung, or as a new issue. The item is deleted from the Board.
5. **Promotion**: once all questions for a given plan are resolved, the plan moves to `desk/issues/` for implementation.

---

Generated from `raw/socratic_protocol.md`.