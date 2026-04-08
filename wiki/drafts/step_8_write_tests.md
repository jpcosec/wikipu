---
identity:
  node_id: "doc:wiki/drafts/step_8_write_tests.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/GUIDES/creating-a-component.md", relation_type: "documents"}
---

**File:** `tests/MyComponent.test.js`

## Details

**File:** `tests/MyComponent.test.js`

```javascript
import { describe, test, expect, beforeEach } from 'vitest';
import { MyComponent } from '../MyComponent.js';

describe('MyComponent', () => {
  let component;

  beforeEach(async () => {
    // ARRANGE: Create and initialize
    component = new MyComponent({
      initial: 0,
      min: -10,
      max: 100,
      step: 1,
    });
    await component.initialize();
  });

  test('should initialize with given value', () => {
    // ASSERT
    expect(component.getValue()).toBe(0);
    expect(component.isValid()).toBe(true);
  });

  test('should increment value', () => {
    // ACT
    component.increment();

    // ASSERT
    expect(component.getValue()).toBe(1);
  });

  test('should decrement value', () => {
    // ACT
    component.decrement();

    // ASSERT
    expect(component.getValue()).toBe(-1);
  });

  test('should validate bounds (max)', () => {
    // ACT
    component.setValue(150);

    // ASSERT (invalid because > max)
    expect(component.isValid()).toBe(false);
    expect(component.getError()).toBeTruthy();
  });

  test('should validate bounds (min)', () => {
    // ACT
    component.setValue(-20);

    // ASSERT (invalid because < min)
    expect(component.isValid()).toBe(false);
  });

  test('should reset to initial value', () => {
    // ARRANGE
    component.setValue(50);

    // ACT
    component.reset();

    // ASSERT
    expect(component.getValue()).toBe(0);
    expect(component.isValid()).toBe(true);
  });

  test('should serialize and restore state', () => {
    // ARRANGE
    component.setValue(42);
    const seed = component.toSeed();

    // Create new instance
    const component2 = new MyComponent({ initial: 0, min: 0, max: 100 });
    await component2.initialize();

    // ACT
    component2.loadFromSeed(seed);

    // ASSERT
    expect(component2.getValue()).toBe(42);
  });
});
```

---

Generated from `raw/docs_cotizador/docs/GUIDES/creating-a-component.md`.