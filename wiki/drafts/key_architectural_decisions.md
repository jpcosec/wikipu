---
identity:
  node_id: "doc:wiki/drafts/key_architectural_decisions.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md", relation_type: "documents"}
---

### ✅ Separation of Concerns

## Details

### ✅ Separation of Concerns

Each package has **one clear responsibility** and owns its interface:

| Package | Responsibility | Contract |
|---------|---|---|
| Database | Persistence with pluggable stores | `IStore` interface (5 methods) |
| Pricing | Pure calculation pipeline | `pipeline(header, lineas, catalog, rules)` → results |
| Domain | Object-oriented domain models | Classes with mixins |
| XState | Orchestration & state management | Machine blueprint + adapters |
| Frontend | UI synchronization | `AlpineXStateBridge` (sendEvent, syncToAlpine) |

### ✅ Pluggable Layers

**Stores:** Switch at runtime based on environment
- `InMemoryStore` — Fast testing (no I/O)
- `FileStore` — Local development (fs-based)
- `GasSheetStore` — Production (Google Sheets)

**Rules Engine:** JSON-Logic expressions
- Build-time evaluable
- No runtime expression evaluation
- Cache-friendly

**Calculations:** Two available engines
- Legacy `Pricing.pipeline()` (148 tests)
- New `Domain` models (553 tests)
- Switchable via `quotationAdapters`

### ✅ Monorepo with Single Bundle Output

- **5 independent packages** (each has own `package.json`, `node_modules`)
- **Shared nothing** (no cross-package imports except through adapters)
- **Single IIFE bundle** (`dist/quotation-engine.iife.js`)
- **Offline testable** (local init tables for dev without GAS)
- **Deployable** (`clasp push` to Google Apps Script)

### ✅ Pure Calculation Functions

**Pricing & Domain** are **pure functions**:
- ✅ No side effects (no DB access)
- ✅ No I/O operations
- ✅ Testable without mocking
- ✅ Reusable in any context
- ✅ Fast (synchronous)
- ✅ Deterministic (same input → same output)

**XState owns all I/O:**
- Database access
- File operations
- Async operations
- Complex state transitions

### ✅ Single Source of Truth

| File | Controls |
|------|----------|
| `Config_Schema.js` | 11 table definitions → all models auto-generated |
| `quotationMachine.xstate.js` | All state, transitions, actions, guards |
| `Pricing.pipeline.js` | 6-stage calculation flow |
| `Domain classes` | Object structure & behavior |

Change schema → all models regenerate automatically.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/LEGACY_ARCHITECTURE.md`.