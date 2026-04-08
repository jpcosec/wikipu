---
identity:
  node_id: "doc:wiki/drafts/step_5_promote_clientselector_html.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/0-cleanup/agent_guideline.md", relation_type: "documents"}
---

The `apps/quotation/components/ClientSelector.html` is the rich production template. The `packages/components/quotation/modals/ClientSelector.html` is a 10-line stub. Replace the stub.

## Details

The `apps/quotation/components/ClientSelector.html` is the rich production template. The `packages/components/quotation/modals/ClientSelector.html` is a 10-line stub. Replace the stub.

```bash
cp apps/quotation/components/ClientSelector.html \
   packages/components/quotation/modals/ClientSelector.html
rm apps/quotation/components/ClientSelector.html
```

Run tests. Expected: still passing (HTML files are not imported in tests).

---

Generated from `raw/docs_cotizador/plan/legacy/0-cleanup/agent_guideline.md`.