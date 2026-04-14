---
identity:
  node_id: doc:wiki/concepts/principle_6_free_text_has_a_place_but_not_a_permanent_home.md
  node_type: concept
edges:
- target_id: raw:raw/wiki_construction_principles.md
  relation_type: documents
compliance:
  status: implemented
  failing_standards: []
source:
  source_path: raw/wiki_construction_principles.md
  source_hash: adb2697fc76ec9f466878e73986e50abfad611e8104bf6edd4d6d0952660dedf
  compiled_at: '2026-04-14T16:50:28.667146'
  compiled_from: wiki-compiler
---

Free text (chat logs, brainstorm dumps, meeting notes) is valid input.

## Definition

Free text (chat logs, brainstorm dumps, meeting notes) is valid input.

## Examples

- Implementation of this concept within the Wikipu workflow.
- Application of these principles in current documentation.

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

Free text (chat logs, brainstorm dumps, meeting notes) is valid input.
It lives in raw/ while it is undigested.
It is not a wiki node. It does not get indexed. It does not get queried.

The system "digests" it by running ingest, which proposes the
structured decomposition. Until digested, the content is available
as raw source but invisible to the graph.

This creates a clear lifecycle:
    undigested (raw/)  →  proposed (wiki/drafts/)  →  structured (wiki/)

---

Generated from `raw/wiki_construction_principles.md`.
