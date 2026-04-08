---
identity:
  node_id: "doc:wiki/drafts/1_baseline_inventory_the_audit.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_v2/docs/standards/feature_creation_methodology.md", relation_type: "documents"}
---

**Definition:** Establishing a "source of truth" and a baseline for comparison before touching code.

## Details

**Definition:** Establishing a "source of truth" and a baseline for comparison before touching code.

### Requirements:
- **Map the Current State:** Identify every file, module, and data artifact involved in the change.
- **Dependency Audit:** Trace how data flows into and out of the affected area.
- **Test Baseline:** Run all existing tests in the target area. If tests are missing or broken, fix them or write "capture tests" to document current behavior.
- **Issue Inventory:** List known bugs, "fragility" points, and technical debt in the current implementation.

**Goal:** To ensure no existing responsibility is lost and to have a baseline to prove the new implementation is correct.

---

Generated from `raw/docs_postulador_v2/docs/standards/feature_creation_methodology.md`.