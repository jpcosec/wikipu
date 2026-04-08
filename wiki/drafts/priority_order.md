---
identity:
  node_id: "doc:wiki/drafts/priority_order.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/GUIDES/writing-rules.md", relation_type: "documents"}
---

Rules are evaluated in ascending `Prioridad` order. Lower number = evaluated first.

## Details

Rules are evaluated in ascending `Prioridad` order. Lower number = evaluated first.

```
10  ← blocking capacity checks (ERROR)
20  ← blocking time/date checks (ERROR)
30  ← warnings (WARNING)
50  ← surcharges and modifiers (MULTIPLY, ADD_FIXED)
```

If multiple rules match, all are recorded (unless a non-accumulative rule stops evaluation).

---

Generated from `raw/docs_cotizador/docs/GUIDES/writing-rules.md`.