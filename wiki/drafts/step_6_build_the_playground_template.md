---
identity:
  node_id: "doc:wiki/drafts/step_6_build_the_playground_template.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-3-category/agent_guideline.md", relation_type: "documents"}
---

File: `packages/components/category/ui/CategoryStandalone.html`

## Details

File: `packages/components/category/ui/CategoryStandalone.html`

Follow the three-zone structure from `html_playground_draft.html`:
- **Zone 1** (External State): category selector, paxGlobal/dia/hora inputs, add-item dropdown
- **Zone 2** (Component Display): category header with name + subtotal, then a list of item cards — each card is a **placeholder** showing the item name and total, not the full Item playground
- **Zone 3** (Debug): toDisplayObject() JSON dump

The item cards in Zone 2 are simple `<div>` elements showing `item.nome` and `item.total`. They are **not** the full ItemStandalone component. That integration comes in Phase II (step 9 — environment + item).

---

Generated from `raw/docs_cotizador/plan/legacy/I-3-category/agent_guideline.md`.