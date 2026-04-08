---
identity:
  node_id: "doc:wiki/drafts/why_this_step_exists.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/0-cleanup/objectives.md", relation_type: "documents"}
---

During steps 4/5 the full quotation flow was assembled before its constituent components were individually built and verified. This left `packages/components/quotation/` as app-level assembly code living in the component library, and `apps/quotation/` as a layer of thin JS wrappers delegating to it. Both situations create confusion about what is canonical.

## Details

During steps 4/5 the full quotation flow was assembled before its constituent components were individually built and verified. This left `packages/components/quotation/` as app-level assembly code living in the component library, and `apps/quotation/` as a layer of thin JS wrappers delegating to it. Both situations create confusion about what is canonical.

---

Generated from `raw/docs_cotizador/plan/legacy/0-cleanup/objectives.md`.