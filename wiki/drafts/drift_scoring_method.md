---
identity:
  node_id: "doc:wiki/drafts/drift_scoring_method.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixins-style-drift-assessment.md", relation_type: "documents"}
---

Drift score: `0` (no drift) to `100` (severe drift).

## Details

Drift score: `0` (no drift) to `100` (severe drift).

Each component gets up to 25 points in each deficit dimension:

1. **Mixin integration deficit** (expected base/mixins not used)
2. **Actor ownership deficit** (actor not owned by the component class)
3. **Runtime path deficit** (component exists but is bypassed in active flow)
4. **API/style deficit** (public surface diverges from canonical style)

Total drift = sum of the four deficits.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixins-style-drift-assessment.md`.