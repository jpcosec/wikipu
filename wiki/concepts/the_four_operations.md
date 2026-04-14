---
identity:
  node_id: "doc:wiki/concepts/the_four_operations.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/cleansing_protocol.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/cleansing_protocol.md"
  source_hash: "b5b3922be9089eb922885b17d43a45d212f4078f7ed6c85a899554499a6eead5"
  compiled_at: "2026-04-14T16:50:28.657858"
  compiled_from: "wiki-compiler"
---

| Operation | Meaning | Graph consequence |

## Details

| Operation | Meaning | Graph consequence |
|---|---|---|
| Destroy | Node no longer belongs in the system | Remove node and all edges; audit dangling references first |
| Relocate | Node is valid but in the wrong place | Update node_id, parent contains edges, node_type |
| Split | Node has more than one responsibility | Replace with two atomic nodes + one index node transcluding both |
| Merge | Two nodes say the same thing | Consolidate into one canonical node; redirect all edges from dissolved node |

---

Generated from `raw/cleansing_protocol.md`.