---
identity:
  node_id: "doc:wiki/concepts/principle_3_composition_via_cli_not_prose.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/wiki_construction_principles.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/wiki_construction_principles.md"
  source_hash: "adb2697fc76ec9f466878e73986e50abfad611e8104bf6edd4d6d0952660dedf"
  compiled_at: "2026-04-14T16:50:28.667006"
  compiled_from: "wiki-compiler"
---

Long documents are assembles of atomic nodes via transclusion.

## Details

Long documents are assembles of atomic nodes via transclusion.
A composite node has no prose of its own — only transclusions and navigation.

You do not write a long document. You call:

    wiki-compiler compose --nodes "concept_a concept_b how_to_x" \
                          --title "Complete Guide to X" \
                          --output wiki/guides/x.md

This produces a node whose body is:
    ![[concept_a]]
    ![[concept_b]]
    ![[how_to_x]]

Composite nodes are index nodes. They exist for navigation, not for content.
Content lives in the atomic nodes.

This mirrors clean code: a function that only calls other functions,
with no logic of its own, is a composition layer. It is valid and useful.
It is not a smell. Growing it with inline prose IS a smell.

---

Generated from `raw/wiki_construction_principles.md`.