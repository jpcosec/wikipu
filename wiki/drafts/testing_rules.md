---
identity:
  node_id: "doc:wiki/drafts/testing_rules.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/rules-engine-integration.md", relation_type: "documents"}
---

### Unit Test Pattern

## Details

### Unit Test Pattern

```javascript
import { RulesCoordinator } from '../coordinator.js';

describe('RulesCoordinator', () => {
  test('should apply MULTIPLY rule when condition matches', () => {
    // ARRANGE
    const rule = {
      ruleId: 'R001',
      scope: 'ITEM',
      actionType: 'MULTIPLY',
      condition: { ">": [{ "var": "pax" }, 150] },
      payload: { factor: 1.15 },
      priority: 10,
      acumulable: false,
      active: true,
    };

    const coordinator = new RulesCoordinator('ITEM', [rule]);

    // ACT
    const snapshot = { pax: 175 };
    const result = coordinator.evaluate(snapshot);

    // ASSERT
    expect(result.appliedRules).toHaveLength(1);
    expect(result.appliedRules[0].ruleId).toBe('R001');
    expect(result.isAvailable).toBe(true);  // Not blocking
  });

  test('should block when ERROR action matches', () => {
    const rule = {
      ruleId: 'R002',
      scope: 'ITEM',
      actionType: 'ERROR',
      condition: { "<": [{ "var": "pax" }, 10] },
      payload: { message: 'Min 10 pax' },
      priority: 5,
      acumulable: true,
      active: true,
    };

    const coordinator = new RulesCoordinator('ITEM', [rule]);

    const snapshot = { pax: 5 };
    const result = coordinator.evaluate(snapshot);

    expect(result.appliedRules).toHaveLength(1);
    expect(result.errors).toHaveLength(1);
    expect(result.isAvailable).toBe(false);  // BLOCKED!
  });
});
```

### Integration Test Pattern

```javascript
import { Item } from '../Item.js';

test('item should become unavailable when blocking rule applies', async () => {
  // ARRANGE: Item with blocking rule
  const definition = {
    itemId: 'COFFEE_01',
    kind: 'EXTRA',
    rules: [
      {
        ruleId: 'R001',
        scope: 'ITEM',
        actionType: 'ERROR',
        condition: { "<": [{ "var": "pax" }, 10] },
        payload: { message: 'Min 10 pax for coffee' },
        priority: 5,
        acumulable: true,
        active: true,
      }
    ]
  };

  const item = new Item(definition);
  await item.initialize();

  // ACT: Set pax to 5 (below minimum)
  item.setOverride('pax', 5);

  // ASSERT
  const state = item.toDisplayObject();
  expect(state.available).toBe(false);
  expect(state.errors).toHaveLength(1);
  expect(state.errors[0].message).toBe('Min 10 pax for coffee');
});
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/rules-engine-integration.md`.