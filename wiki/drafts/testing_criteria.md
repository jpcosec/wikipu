---
identity:
  node_id: "doc:wiki/drafts/testing_criteria.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/U-1-save/objectives.md", relation_type: "documents"}
---

**Automated:**

## Details

**Automated:**

```bash
npm test
```

**Manual (sandbox + GAS preview):**

- [ ] Create quotation with entries across multiple days.
- [ ] Save succeeds and returns visible quotation ID.
- [ ] Load by ID returns expected header + detail rows.
- [ ] Behavior matches legacy save/load expectations.

---

Generated from `raw/docs_cotizador/plan/U-1-save/objectives.md`.