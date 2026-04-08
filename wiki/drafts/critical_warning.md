---
identity:
  node_id: "doc:wiki/drafts/critical_warning.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/implementation_status.md", relation_type: "documents"}
---

**DO NOT USE UI as Backend Orchestrator**

## Details

**DO NOT USE UI as Backend Orchestrator**

The methodology says:
> "UI is a visualization layer, never primary business logic"

Current reality forces UI to:
- Stop user visually when backend doesn't pause
- Overwrite generated files
- Trigger manual render

**This violates decoupling principles. Backend must implement proper gates before production.**

Until then:
- Document all workarounds explicitly
- Add `--skip-workaround` flag when backend is fixed
- Plan migration to remove workarounds in next sprint

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/implementation_status.md`.