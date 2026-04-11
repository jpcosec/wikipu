---
identity:
  node_id: "doc:wiki/drafts/phase_3_query_for_documentation_quality.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/graph_construction_process.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/graph_construction_process.md"
  source_hash: "5cce04b66b0ac2624ccae799d5a8d22e00e6b9dd15ccc31cb63eb7dcb12cfaa9"
  compiled_at: "2026-04-10T17:47:33.731516"
  compiled_from: "wiki-compiler"
---

The structured graph can now be interrogated as a cross-reference engine.

## Details

The structured graph can now be interrogated as a cross-reference engine.
Quality gaps appear as structural anomalies — places where the two layers disagree.

**Coverage gaps** — code that exists but has no documentation edge:
```
code nodes  WHERE  no incoming edge WITH relation_type="documents"
→ undocumented modules
```

**Semantic gaps** — nodes that exist but have no meaning attached:
```
code nodes  WHERE  SemanticFacet IS NULL  OR  raw_docstring IS NULL
→ missing docstrings
```

**I/O gaps** — data flowing without a type contract:
```
IOFacet nodes  WHERE  schema_ref IS NULL  AND  medium != "network"
→ untyped disk I/O
```

**Compliance violations** — nodes failing specific house rules:
```
nodes  WHERE  ComplianceFacet.failing_standards IS NOT EMPTY
→ standards breaches
```

**Stale documentation** — docs pointing to code that no longer exists:
```
edges WITH relation_type="documents"  WHERE  target_id NOT IN graph.nodes
→ dead references
```

**Orphaned plans** — future_docs entries with no corresponding code node:
```
doc nodes in future_docs/  WHERE  no outgoing edge to any code node
→ forgotten backlog items
```

---

Generated from `raw/graph_construction_process.md`.