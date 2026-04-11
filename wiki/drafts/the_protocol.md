---
identity:
  node_id: "doc:wiki/drafts/the_protocol.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/cleansing_protocol.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/cleansing_protocol.md"
  source_hash: "b5b3922be9089eb922885b17d43a45d212f4078f7ed6c85a899554499a6eead5"
  compiled_at: "2026-04-10T17:47:33.729845"
  compiled_from: "wiki-compiler"
---

Detection is automatic. Application requires explicit approval per proposal.

## Details

Detection is automatic. Application requires explicit approval per proposal.
The system never auto-destroys.

    wiki-compiler cleanse --graph knowledge_graph.json
      → CleansingReport: list[CleansingProposal]
      → each proposal: node_id, operation, rationale, preview of result

    wiki-compiler cleanse --apply proposal.json
      → executes one approved proposal
      → rebuilds affected graph region

---

Generated from `raw/cleansing_protocol.md`.