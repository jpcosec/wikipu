---
identity:
  node_id: "doc:wiki/drafts/step_05_validation_test_impact_map.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md", relation_type: "documents"}
---

### 1. Architecture Logic

## Details

### 1. Architecture Logic

Operational contract. Every implementation task declares its impact dimensions before coding.

**Impact dimensions:** State contracts, persistence, rendering, interaction, schema, theme.

**Verification matrix:**

| If you change... | Verify... |
|---|---|
| State contract | All views load. Undo/redo. Save/load round-trip. |
| Schema format | All schemas parse. Editor loads. Views execute. |
| Node renderer | All 4 modes. Fallback works. Theme data-* present. |
| Container behavior | Collapse/expand. Proxy edges. Drag interactions. Tree sync. |
| Anchor model | Creation. Edit survival. Stale detection. Undo. |
| Data ingestion | MERGE correct. Idempotent. Provenance. View queries. |
| CSS theme | Default renders all types. Overrides apply. No unstyled elements. |
| Extension | Registration works. Activation rules correct. Mount/unmount clean. |

### 2. Objectives

1. Every PR references impact dimensions
2. Tests organized by impact dimension
3. Regression risk bounded before coding
4. Map maintained as living document

### 3. Don'ts

- **Don't treat as optional.** It's a gate.
- **Don't organize tests by file path only.** Impact-based groups.
- **Don't let it go stale.** Update with every step.

### 4. Known Gaps & Open Questions

- **GAP-IMPL-02** (High): Zero frontend test files currently exist. Bootstrap required.

### 5. Library Decision Matrix

N/A — uses Vitest + @testing-library/react + Playwright (all committed).

### 6. Test Plan

- **Unit**: Impact dimension map is complete (all steps covered). Each dimension has at least one verification entry.
- **Component**: Test runner config works, sample test passes.
- **Integration**: Full CI pipeline runs all test suites.

### 7. Review Checklist

- [ ] Verification matrix covers all impact dimensions
- [ ] Every PR template includes impact dimension field
- [ ] Tests are organized by impact dimension
- [ ] Map is updated with each new step implementation
- [ ] Test infrastructure (Vitest + Testing Library + Playwright) bootstrapped and passing

---

Generated from `raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md`.