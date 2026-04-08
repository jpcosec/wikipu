---
identity:
  node_id: "doc:wiki/drafts/development_scripts.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/cli/README.md", relation_type: "documents"}
---

### `scripts/dev.sh`

## Details

### `scripts/dev.sh`

Starts UI + API in one terminal.

```bash
./scripts/dev.sh
```

### `scripts/dev-all.sh`

Starts full stack: Neo4j + API + UI.

```bash
./scripts/dev-all.sh
# or with Neo4j explicitly
START_NEO4J=1 ./scripts/dev-all.sh
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/cli/README.md`.