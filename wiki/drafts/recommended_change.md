---
identity:
  node_id: "doc:wiki/drafts/recommended_change.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/issues/profile_input_loading_node.md", relation_type: "documents"}
---

Introduce a dedicated pipeline node for profile loading, for example:

## Details

Introduce a dedicated pipeline node for profile loading, for example:

- `load_profile`

Suggested responsibility:

- resolve profile source (`profile_evidence_ref`, env var, or default path)
- normalize the payload into the canonical shape
- persist the normalized artifact
- expose only the normalized ref/state needed by downstream nodes

Possible flow:

```text
scrape
  -> translate
  -> extract_bridge
  -> load_profile
  -> match_skill
```

Or, if requirements extraction and profile loading should be grouped differently:

```text
translate
  -> extract_requirements
  -> load_profile
  -> match_skill
```

Generated from `raw/docs_postulador_refactor/future_docs/issues/profile_input_loading_node.md`.