---
identity:
  node_id: "doc:wiki/Index.md"
  node_type: "index"
edges:
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "contains"}
  - {target_id: "doc:wiki/how_to/Index.md", relation_type: "contains"}
  - {target_id: "doc:wiki/standards/artifacts/Index.md", relation_type: "contains"}
  - {target_id: "doc:wiki/standards/languages/Index.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/Index.md", relation_type: "contains"}
  - {target_id: "doc:wiki/concepts/Index.md", relation_type: "contains"}
compliance:
  status: "implemented"
  failing_standards: []
---

This is the front page of the Wikipu wiki. Start here when you need to understand where standards, workflows, reference material, concepts, and architectural decisions live.

# Wikipu Index

| Area | Purpose | Start here |
|---|---|---|
| Standards | Invariant rules, schemas, lifecycle definitions | `wiki/standards/house_rules.md` |
| How-to | Step-by-step workflows for operating in the repo | `wiki/how_to/Index.md` |
| Reference | Commands, facets, FAQs, and lookup material | `wiki/reference/Index.md` |
| Concepts | Explanatory architecture and system meaning | `wiki/concepts/Index.md` |
| ADRs | Durable design decisions and supersessions | `wiki/adrs/` |

Use root `wiki/` as an entry surface, not as a dumping ground. If a new document is not a front page artifact, place it according to `wiki/standards/document_topology.md`.
