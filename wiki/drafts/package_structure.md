---
identity:
  node_id: "doc:wiki/drafts/package_structure.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md", relation_type: "documents"}
---

### 1. **Database Package** (`packages/database/`)

## Details

### 1. **Database Package** (`packages/database/`)

**Responsibility:** Persistence layer with pluggable stores

**Key Components:**
- `IStore.js` — Abstract store interface (defines API contract)
- `ModelFactory.js` — Auto-generates 11 models from schema
- `Config_Schema.js` — Single source of truth (11 tables)
- `stores/` — Three implementations:
  - `InMemoryStore` (testing, no I/O)
  - `FileStore` (local development)
  - `GasSheetStore` (Google Sheets in production)

**Models (auto-generated):**
- CLIENTES, CATEGORIAS, ITEMS, SERVICIOS, CONTRATOS
- RUTAS, OFERTAS, PAGOS, COTIZACIONES, REGLAS_NEGOCIO, PROPIEDADES

**Tests:** 5/5 ✅ (includes CSV seed migration)

---

### 2. **Pricing Package** (`packages/pricing/`)

**Responsibility:** Pure calculation pipeline (legacy, 148 tests)

**Architecture:** 6-stage pure function pipeline

```
Input → expand() → defaults() → pricing() → adjustments() → manual() → taxes() → Output
```

**Stages:**
1. **expand()** — Normalize input, create lineas array
2. **defaults()** — Apply schema defaults
3. **pricing()** — Calculate base prices from catalog
4. **adjustments()** — Apply volume/time discounts
5. **manual()** — Handle user manual overrides
6. **taxes()** — Calculate taxes (IVA, etc.)

**Rules Engine:** 9 pluggable action types
- DESCUENTO_PORCENTAJE, DESCUENTO_MONTO, RESTRICCION_UI
- RESTRICCION_ITEM, EXTRA_MONTO, EXTRA_PORCENTAJE
- EXTRA_LINEA, BLOQUEAR, MENSAJES

**Key Features:**
- Zero external dependencies (pure JS)
- 100% deterministic (same input → same output)
- Event-driven mock layer for testing
- JSON-Logic expression evaluation

**Tests:** 110/148 ✅ (38 pre-existing failures)

---

### 3. **XState Package** (`packages/xstate/`)

**Responsibility:** Orchestration & state machine (owns all DB access)

**Key Files:**
- `quotationMachineBlueprint.js` — Machine definition (states, transitions)
- `adapters/actions.js` — 15+ state mutation actions
- `adapters/guards.js` — 8+ transition guard conditions
- `adapters/services.js` — Async service definitions (DB calls)
- `runtime/createActor.js` — XState v5 actor runtime

**Machine States:**
- `uninitialized` → `idle` → `handling` → `recalculating`
- Parallel regions for concurrent processing
- Context caching for reference data

**Context Structure:**
```javascript
{
  definition: { /* config */ },
  store: IStore,              // Database reference
  catalog: { /* ref data */ }, // Cached at init
  lineas: [ /* items */ ],     // Quotation line items
  totals: { /* computed */ },  // Pricing results
  appliedRules: [ /* rules */ ],
  userSetFields: Set,
  errors: [], warnings: []
}
```

**Key Behavior:**
- Single point of all database access
- Loads reference data once at INIT, caches in context
- Passes calculated data as parameters to pricing engine
- 59% fewer DB calls vs. v1 implementation

**Tests:** 59/59 ✅

---

### 4. **Domain Package** (`packages/domain/`)

**Responsibility:** Object-oriented domain models (Phase B, new)

**Classes:**
- `Catalog` — Collection of categories & items
- `Basket` — Container of quotation line items
- `Item` — Single quotation item with pricing
- `Kit` — Bundled items
- `Category` — Item grouping with pricing profiles
- `DayCategory` — Category per-day breakdown
- Base classes: `ItemBase`, `ContainerBase`

**Mixins:**
- `Rulable` — Rule evaluation capability
- `Prizable` — Pricing calculation
- `Aggregable` — Total computation
- `XStateable` — XState integration
- `Alpineable` — Alpine.js binding

**Features:**
- Self-calculating items (profile fallback if not overridden)
- Tree-structured containers (Basket → DayCategory → Item/Kit)
- Rule inheritance (context flows down, aggregation flows up)
- Dual-write for backward compatibility (basket → lineas/totals sync)

**Tests:** 553/553 ✅ (100%)

---

### 5. **Frontend Package** (`packages/frontend/`)

**Responsibility:** UI bridge between XState and Alpine.js

**Key Components:**
- `AlpineXStateBridge.js` — Bidirectional sync
  - `sendEvent(name, payload)` — User input → XState
  - `syncToAlpine()` — State → UI
  - `mapContextToDisplay()` — Convert context to UI format

- HTML component templates (5 templates)
- Local actor factory for testing
- Mock GAS shim for offline testing

**Sync Flow:**
1. User interacts with Alpine.js UI
2. Alpine fires event via bridge
3. Bridge sends event to XState actor
4. XState updates context (calculations, DB calls)
5. Bridge pulls new context
6. Alpine re-renders with new data

**Tests:** 12/12 ✅

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md`.