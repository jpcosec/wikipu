---
identity:
  node_id: "doc:wiki/drafts/how_mixins_solve_style_drift.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixins-style-drift-assessment.md", relation_type: "documents"}
---

Style drift appears when each component invents its own lifecycle and API. Mixins reduce drift by turning style into code-level constraints:

## Details

Style drift appears when each component invents its own lifecycle and API. Mixins reduce drift by turning style into code-level constraints:

1. **Role templates:** leaf domain, container domain, modal controller, UI container, presentational view.
2. **Capability bundles:** each role gets the same minimal behavior set.
3. **Stable public contracts:** `toDisplayObject()`, event surface, optional actor bridge are consistently present.
4. **Testable invariants:** base/mixin contract tests can fail quickly when a component diverges.

If adopted as canonical, mixins become the enforcement mechanism for style consistency.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixins-style-drift-assessment.md`.