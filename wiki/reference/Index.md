---
identity:
  node_id: "doc:wiki/reference/Index.md"
  node_type: "index"
edges:
  - {target_id: "doc:wiki/reference/faq.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/knowledge_node_facets.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/cli/build.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/cli/cleanse.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/cli/curate.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/cli/ingest.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/cli/query.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/cli/scaffold.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/cli/status.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/cli/validate_wiki.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/protocols/autopoiesis_coordinator.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/protocols/gate_loop.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/protocols/llm_agent.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/protocols/human_contributor.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/protocols/socratic.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/protocols/trail_collect.md", relation_type: "contains"}
compliance:
  status: "implemented"
  failing_standards: []
---

This index gathers lookup-oriented pages: command references, schema references, FAQs, and audience protocols. Use reference nodes when you already know the subject and need the exact fields, commands, or operating constraints.

# Reference Index

| Area | Purpose |
|---|---|
| `faq.md` | Quick answers to recurring onboarding questions |
| `knowledge_node_facets.md` | Node, edge, and facet vocabulary |
| `cli/` | Command-level reference for `wiki-compiler`, including validation surfaces |
| `protocols/` | Audience-specific operating protocols |
