---
identity:
  node_id: doc:wiki/concepts/what_gets_collected.md
  node_type: concept
edges:
- target_id: raw:raw/trail_collect.md
  relation_type: documents
compliance:
  status: implemented
  failing_standards: []
source:
  source_path: raw/trail_collect.md
  source_hash: b5310580e40950c0da96febcf8d445391a89da95cb9c5c05c5157e3032195588
  compiled_at: '2026-04-14T16:50:28.665612'
  compiled_from: wiki-compiler
---

Not everything is worth keeping. Trail collect is not a transcript archive — it is a distillation. The artifacts worth preserving:

## Definition

Not everything is worth keeping.

## Examples

- Implementation of this concept within the Wikipu workflow.
- Application of these principles in current documentation.

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

Not everything is worth keeping. Trail collect is not a transcript archive — it is a distillation. The artifacts worth preserving:

| Artifact Type | Destination |
|---|---|
| Design decision resolved | Encode in the relevant doc, issue, or hausordnung |
| Gap discovered | Create an issue in `desk/issues/` |
| Ambiguity resolved (Q&A) | Encode inline in the relevant doc or `desk/socratic/` resolution |
| Correction (agent was wrong) | Update the source of the wrong assumption |
| Rule that caused friction | Rewrite the rule in the hausordnung |
| New concept identified | Write to `raw/` as a seed |

Raw session logs stay in the assistant's memory system. Trail collect extracts only the durable facts — the delta between "what the system knew before the session" and "what it knows now."

---

Generated from `raw/trail_collect.md`.
