---
identity:
  node_id: "doc:wiki/drafts/6_folder_structure_proposal.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/04_best_practices.md", relation_type: "documents"}
---

```

## Details

```
packages/components/product/
│
├── ProductItem.js                       ← Concrete class (extends ItemBase)
│                                          Implements: toDisplayObject, toStorageObject,
│                                          _buildRuleContext, fromDefinition, fromSeed, toSeed
│
├── STATE_CONTRACT.md                    ← Input/output contract (read before editing)
│                                          Documents: what fields enter via receiveContext,
│                                          what toDisplayObject() returns, what actor events exist
│
├── machine/
│   └── productMachine.js                ← XState machine definition
│                                          Contains: states, transitions, guards, actions
│                                          Does NOT import ProductItem directly
│
├── domain/
│   ├── index.js                         ← Re-exports all pure functions
│   ├── pricing.js                       ← pricingFn(profile, pax, cantidad, duracion) → number
│   ├── quantity.js                      ← resolveDefaultQuantities(def) → {pax, cantidad, duracion}
│   └── formatting.js                    ← formatPrice(cents) → string
│
├── ui/
│   └── Product.html                     ← Alpine.js template
│                                          Reads only from toDisplayObject() output keys
│
├── db/
│   └── resolveProductDefinition.js      ← Database join: item + category + rules → normalized def
│                                          Only file that knows raw DB field names
│
└── tests/
    ├── ProductItem.base.test.js          ← Layer 2: base class composition
    ├── ProductItem.integration.test.js   ← Layer 3: real pricingFn + evaluator, no actor
    ├── ProductContainer.integration.test.js ← Layer 4: container + children propagation
    └── product.e2e.test.js               ← Layer 5: Playwright/browser tests
```

> Note: Layer 1 mixin unit tests live in `packages/components/common/mixins/` alongside the mixin source files, not inside each component folder — they test the mixin in isolation, not the component.

### Rationale

**`ProductItem.js` at root** — The class is the component's public API. Placing it at the top level makes imports clean: `import { ProductItem } from '../product/ProductItem.js'`.

**`machine/`** — The XState machine is separate from the domain class because the machine can be tested without DOM or Alpine, and machine definitions may be inspected by visualization tools. Keeping them separate also prevents circular imports: the machine should receive the domain object via actor context input, not import it directly.

**`domain/`** — Pure functions importable anywhere: tests, the machine, other components. No classes, no state, no I/O. Each file exports one function family. `index.js` re-exports all of them for convenience.

**`ui/`** — Alpine templates are static HTML files. Separating them from JS enables design tools to open them without a build step. The template references only keys that `toDisplayObject()` returns — never internal class fields.

**`db/`** — The database join is isolated here because it is the only code that knows the raw schema field names (e.g., `ID_Item`, `Def_Precio_PP`, `Nombre`). Everything else uses the normalized definition shape. Schema migrations are a one-file change.

**`STATE_CONTRACT.md`** — The most important file for maintainability. Documents what inputs the component accepts (via `receiveContext`), what it outputs (via `toDisplayObject`), and what actor events exist. Any developer should read this before editing any other file in the folder.

**`tests/`** — One file per test layer. This makes it immediately clear which kind of test you're reading, and gives each layer an independent pass/fail signal in CI.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/04_best_practices.md`.