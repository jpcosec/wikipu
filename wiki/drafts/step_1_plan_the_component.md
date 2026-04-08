---
identity:
  node_id: "doc:wiki/drafts/step_1_plan_the_component.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/GUIDES/creating-a-component.md", relation_type: "documents"}
---

### Define the responsibility

## Details

### Define the responsibility

What does this component do? Keep it **singular and focused**.

```
Good: "Display and manage quantity selection"
Bad:  "Display, manage, validate, save, and export quantity with analytics"
```

### Identify states

What states will the component occupy?

```
Example: QuantitySelector
- IDLE           (waiting for user input)
- VALIDATING     (checking bounds)
- CONFIRMED      (user accepted)
- ERROR          (invalid input)
```

### List events

What events trigger state changes?

```
- SET_VALUE
- INCREMENT
- DECREMENT
- RESET
- VALIDATE
```

### Define context

What data does the component hold?

```javascript
{
  definition: { min, max, step },
  value: number,
  prevValue: number,
  error: string | null,
}
```

---

Generated from `raw/docs_cotizador/docs/GUIDES/creating-a-component.md`.