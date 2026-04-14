---
identity:
  node_id: "doc:wiki/concepts/phase_1_build_the_raw_graph_structure.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/graph_construction_process.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/graph_construction_process.md"
  source_hash: "5cce04b66b0ac2624ccae799d5a8d22e00e6b9dd15ccc31cb63eb7dcb12cfaa9"
  compiled_at: "2026-04-14T16:50:28.660749"
  compiled_from: "wiki-compiler"
---

The raw graph answers only: **what exists, and what points to what.**

## Details

The raw graph answers only: **what exists, and what points to what.**

Every file, directory, code construct, and doc becomes a node.
Every detectable reference between them becomes an edge — imports, file includes,
transclusions, co-mentions. No meaning is assigned yet. NetworkX holds this as a
pure topology: a skeleton of the system.

```
dir:src  --contains-->  file:src/scanner.py
file:src/scanner.py  --depends_on-->  file:src/contracts.py
doc:wiki/how_it_works.md  --transcludes-->  doc:wiki/standards/00_house_rules.md
```

At this stage the graph is a map of existence and reference only.
An LLM could walk it but couldn't understand what anything does.

**Sources for the raw graph:**
- Directory tree walk → `contains` edges
- Python `import` statements → `depends_on` edges
- Markdown `![[transclusion]]` syntax → `transcludes` edges
- YAML frontmatter `edges:` declarations → any relation type

---

Generated from `raw/graph_construction_process.md`.