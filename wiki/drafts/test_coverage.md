---
identity:
  node_id: "doc:wiki/drafts/test_coverage.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/item-component.md", relation_type: "documents"}
---

**File:** `tests/Item.test.js` (88 tests)

## Details

**File:** `tests/Item.test.js` (88 tests)

Categories:
1. **Factories & Initialization** — Create items, set modes, reset defaults
2. **Quantity Calculations** — Override precedence, bounds, context resolution
3. **Pricing Calculations** — Neto, subtotal, total with adjustments
4. **Rule Evaluation** — Conditions, errors, warnings, blocking
5. **Serialization** — toSeed(), loadFromSeed(), toDisplayObject()
6. **User Overrides** — setOverride(), clearOverride(), isUserSet()

Example test:
```javascript
test('should mark pax as user-set when overridden', async () => {
  const item = new Item(testDefinition);
  await item.initialize();

  // ACT
  item.setOverride('pax', 75);

  // ASSERT
  const state = item.toDisplayObject();
  expect(state.isUserSetPax).toBe(true);
  expect(state.userSetFields).toContain('pax');
});
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/item-component.md`.