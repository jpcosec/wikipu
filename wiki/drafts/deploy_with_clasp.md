---
identity:
  node_id: "doc:wiki/drafts/deploy_with_clasp.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/DEPLOYMENT/gas-bundling.md", relation_type: "documents"}
---

```bash

## Details

```bash
# one-time setup
clasp login
clasp create --type webapp --title "CotizadorLodge Rebuild"

# then for each deploy
npm run build
clasp push
```

In Apps Script editor, deploy as a Web App after pushing.

Generated from `raw/docs_cotizador/docs/DEPLOYMENT/gas-bundling.md`.