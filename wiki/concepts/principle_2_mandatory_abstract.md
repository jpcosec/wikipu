---
identity:
  node_id: doc:wiki/concepts/principle_2_mandatory_abstract.md
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
  compiled_at: '2026-04-14T16:50:28.666960'
  compiled_from: wiki-compiler
---

Every node opens with a 1-3 sentence abstract. This is the node's interface —

## Definition

Every node opens with a 1-3 sentence abstract.

## Examples

- Self-contained (readable without the rest of the node)
- Declarative (states what the node IS, not what it CONTAINS)
- Machine-extractable (first paragraph after the YAML frontmatter, before any heading)

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

Every node opens with a 1-3 sentence abstract. This is the node's interface —
what gets indexed, what the context command uses to rank relevance, what
an LLM reads before deciding whether to go deeper.

The abstract must be:
- Self-contained (readable without the rest of the node)
- Declarative (states what the node IS, not what it CONTAINS)
- Machine-extractable (first paragraph after the YAML frontmatter, before any heading)

The abstract is a first-class field. Its absence is an audit violation.

---

Generated from `raw/wiki_construction_principles.md`.
