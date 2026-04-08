---
identity:
  node_id: "doc:wiki/drafts/deployment.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md", relation_type: "documents"}
---

### Local Testing

## Details

### Local Testing
```bash
npm run build:bundle
npm run test:integration
```

### Google Apps Script
```bash
npm run build:gas
clasp push  # Pushes to GAS project
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md`.