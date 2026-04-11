---
identity:
  node_id: "doc:wiki/drafts/what_is_exempt.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/cleansing_protocol.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/cleansing_protocol.md"
  source_hash: "b5b3922be9089eb922885b17d43a45d212f4078f7ed6c85a899554499a6eead5"
  compiled_at: "2026-04-10T17:47:33.729694"
  compiled_from: "wiki-compiler"
---

Three zones are excluded from cleansing scrutiny:

## Details

Three zones are excluded from cleansing scrutiny:

| Zone | Why exempt |
|---|---|
| raw/ | Sanctuary — immutable source material, never authored by the system |
| logs/ | Execution subproduct — transient by nature, not part of the knowledge model |
| data/outputs/ | Runtime artifact — produced by execution, not authored |

Everything else is in scope. This includes code files, test files,
config files, plan_docs, future_docs, wiki docs, and module READMEs.

---

Generated from `raw/cleansing_protocol.md`.