---
identity:
  node_id: "doc:wiki/drafts/testing_pattern.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md", relation_type: "documents"}
---

Tests follow the **Arrange-Act-Assert** pattern:

## Details

Tests follow the **Arrange-Act-Assert** pattern:

```javascript
describe('MyComponent', () => {
  let component;

  beforeEach(async () => {
    // ARRANGE: Create and initialize component
    component = new MyComponent(testDefinition);
    await component.initialize();
  });

  test('should calculate values correctly', () => {
    // ACT: Trigger calculation
    component.setOverride('field', testValue);
    
    // ASSERT: Verify result
    const state = component.toDisplayObject();
    expect(state.calculations).toMatchObject(expectedResult);
  });

  test('should block when rule error applies', async () => {
    // ARRANGE: Component with blocking rule
    component = new MyComponent({
      ...testDefinition,
      rules: [{ actionType: 'ERROR', condition: /* ... */ }]
    });
    await component.initialize();

    // ACT: Trigger condition
    component.setOverride('field', blockedValue);

    // ASSERT: Check blocking
    const state = component.toDisplayObject();
    expect(state.available).toBe(false);
    expect(state.errors).toHaveLength(1);
  });
});
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/component-architecture.md`.