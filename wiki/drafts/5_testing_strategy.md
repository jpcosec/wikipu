---
identity:
  node_id: "doc:wiki/drafts/5_testing_strategy.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/04_best_practices.md", relation_type: "documents"}
---

The mixin pattern enables testing at five distinct layers. Each layer tests a different scope. **Write tests for every layer** — passing mixin tests do not guarantee a working component.

## Details

The mixin pattern enables testing at five distinct layers. Each layer tests a different scope. **Write tests for every layer** — passing mixin tests do not guarantee a working component.

### Layer 1: Mixin Unit Tests

**Purpose:** Verify that a single mixin's methods do exactly what they document, with no dependencies on other mixins.

**What to test:**
- Each method's return value and side effects in isolation
- Chaining (every mutation method returns `this`)
- Edge cases: empty inputs, null values, boundary values

**What NOT to test:**
- Interaction with other mixins (that's Layer 2)
- Real pricing functions or business logic (that's Layer 3)

**Good test:**
```js
describe('Rulable', () => {
  const makeBase = () => new (class extends Rulable(class {}) {})();

  it('receiveContext merges patch without replacing existing keys', () => {
    const b = makeBase();
    b.receiveContext({ a: 1 });
    b.receiveContext({ b: 2 });
    expect(b._inheritedContext).toEqual({ a: 1, b: 2 });
  });

  it('evaluateRules stops at first non-accumulating rule', () => {
    const b = makeBase();
    b.setRules([
      { ID_Regla: 'R1', Activo: true, Acumulable: false },
      { ID_Regla: 'R2', Activo: true, Acumulable: true },
    ]);
    b.evaluateRules(() => ({ tipo: 'MATCH' }));
    expect(b.getAppliedRules()).toHaveLength(1);
    expect(b.getAppliedRules()[0].ruleId).toBe('R1');
  });
});
```

### Layer 2: Base Class Composition Tests

**Purpose:** Verify that the specified mixin composition produces the correct merged API, and that implicit inter-mixin dependencies work.

**What to test:**
- All expected methods exist on a base class instance
- Chaining works across mixin boundaries
- Implicit dependencies (`_inheritedContext` from Rulable visible to Prizable)
- Abstract methods throw until overridden

**What NOT to test:**
- Business logic, real pricing, real rules

**Good test:**
```js
describe('ItemBase composition', () => {
  class TestItem extends ItemBase {
    toDisplayObject() { return {}; }
    toStorageObject() { return {}; }
  }

  it('has all expected methods from all five mixins', () => {
    const item = new TestItem();
    expect(item.setActorRef).toBeTypeOf('function');   // Actorlike
    expect(item.resolveQuantities).toBeTypeOf('function'); // Prizable
    expect(item.receiveContext).toBeTypeOf('function');    // Rulable
    expect(item.markDirty).toBeTypeOf('function');         // Storable
    expect(item.toDisplayObject).toBeTypeOf('function');   // Alpineable
  });

  it('Prizable.resolveQuantities reads _inheritedContext set by Rulable', () => {
    const item = new TestItem();
    item.receiveContext({ pax: 50 });
    item.resolveQuantities();
    expect(item.pax).toBe(50);
  });

  it('chaining works across mixin boundaries', () => {
    const item = new TestItem();
    const result = item.receiveContext({}).evaluateRules(() => null).resolveQuantities().calculatePrice();
    expect(result).toBe(item);
  });
});
```

### Layer 3: Component Integration Tests

**Purpose:** Verify the concrete component class works correctly with real injected functions in the full domain lifecycle.

**What to test:**
- `fromDefinition` creates a correctly wired instance
- `fromSeed` / `toSeed` round-trip correctly
- `_buildRuleContext` returns the expected enriched context
- Full update cycle produces correct `total`
- User quantity overrides take precedence over context values

**What NOT to test:**
- Actor lifecycle (that's Layer 4)
- Alpine rendering (that's Layer 5)

**Good test:**
```js
describe('ProductItem integration', () => {
  const pricingFn = (profile, pax, cantidad) =>
    profile.porPersona * (pax ?? 0) * (cantidad ?? 1);

  const def = {
    ID_Item: 'I1', ID_Categoria: 'C1', Nombre: 'Cena',
    pricingProfile: { porPersona: 100 },
    categoria: { Nombre: 'Alimentos' },
    defaultPax: null, defaultCantidad: 1, defaultDuracion: null,
    rules: []
  };

  it('calculates price from received context', () => {
    const item = ProductItem.fromDefinition(def, { pricingFn, evaluator: () => null });
    item.receiveContext({ pax: 80 }).evaluateRules(() => null).resolveQuantities().calculatePrice();
    expect(item.total).toBe(8000);  // 100 × 80 × 1
  });

  it('user pax overrides context pax', () => {
    const item = ProductItem.fromDefinition(def, { pricingFn, evaluator: () => null });
    item.setUserQuantity('pax', 50);
    item.receiveContext({ pax: 80 }).resolveQuantities().calculatePrice();
    expect(item.pax).toBe(50);
    expect(item.total).toBe(5000);
  });

  it('toSeed / fromSeed round-trips user overrides', () => {
    const item = ProductItem.fromDefinition(def, { pricingFn, evaluator: () => null });
    item.setUserQuantity('pax', 30);
    const restored = ProductItem.fromSeed(item.toSeed(), { pricingFn, evaluator: () => null });
    expect(restored.pax).toBe(30);
    expect(restored.paxIsUserSet).toBe(true);
  });
});
```

### Layer 4: Container Integration Tests

**Purpose:** Verify the full tree — container + children — with context propagation and aggregation working end-to-end.

**What to test:**
- Container correctly propagates context to all children
- `aggregate()` sums child totals correctly
- Adding/removing children updates the aggregate
- Children that don't match container rules still receive base context

**What NOT to test:**
- Actor wiring (test domain objects directly without actors)
- Alpine rendering

**Good test:**
```js
describe('Container + children propagation', () => {
  it('propagates environment context to all children', () => {
    const container = new ProductContainer();
    const child1 = ProductItem.fromDefinition(def1, deps);
    const child2 = ProductItem.fromDefinition(def2, deps);

    container.addChild('c1', child1);
    container.addChild('c2', child2);

    container.receiveContext({ pax: 100, dia: '2026-06-15' });
    container.propagateContext({});

    expect(child1._inheritedContext.pax).toBe(100);
    expect(child2._inheritedContext.pax).toBe(100);
    expect(child1._inheritedContext.dia).toBe('2026-06-15');
  });

  it('aggregate() sums all child totals after full cycle', () => {
    const container = new ProductContainer();
    // Two items with known totals
    child1.receiveContext({ pax: 10 }).resolveQuantities().calculatePrice();
    child2.receiveContext({ pax: 20 }).resolveQuantities().calculatePrice();
    container.addChild('c1', child1).addChild('c2', child2);
    const result = container.aggregate();
    expect(result.subtotal).toBe(child1.total + child2.total);
  });
});
```

### Layer 5: E2E / Acceptance Tests

**Purpose:** Verify the full stack — actor lifecycle, Alpine reactive binding, user gestures — in a browser-like environment.

**Tools:** Playwright, Cypress, or a JSDOM-based Alpine test helper.

**What to test:**
- User clicks "add item" → item appears in DOM with correct price
- User changes a quantity → price updates reactively in the DOM
- Container total updates when a child changes
- Removing an item removes it from the DOM and updates the total
- Session environment change propagates to all visible items

**What NOT to test:**
- Internal domain calculations (tested in Layers 1-4)
- Machine state transitions in isolation (tested separately)

**Good test (Playwright):**
```js
test('adding an item renders it with correct price', async ({ page }) => {
  await page.goto('/quotation-sandbox');
  await page.click('[data-action="add-item"][data-item-id="I1"]');
  const priceCell = page.locator('[data-item-id="I1"] [data-field="price"]');
  await expect(priceCell).toHaveText('$100');
});

test('changing pax updates item price reactively', async ({ page }) => {
  await page.goto('/quotation-sandbox');
  await page.click('[data-action="add-item"][data-item-id="I1"]');
  await page.fill('[data-item-id="I1"] [data-field="pax-input"]', '50');
  await page.keyboard.press('Tab');
  await expect(page.locator('[data-item-id="I1"] [data-field="total"]')).toHaveText('$5000');
});
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/04_best_practices.md`.