---
identity:
  node_id: "doc:wiki/drafts/how_each_mixin_works.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/01_system_overview.md", relation_type: "documents"}
---

### Domain Mixins

## Details

### Domain Mixins

**`Prizable(Base)`**
Adds three user-settable quantity fields — `pax`, `cantidad`, `duracion` — each with a corresponding `IsUserSet` flag and a `_default*` fallback. Provides:
- `resolveQuantities(containerContext)` — resolves each quantity using the precedence chain: user value → container-provided value → `_inheritedContext` value → item default
- `calculatePrice()` — calls the injected `_pricingFn(profile, pax, cantidad, duracion)` and stores the result in `_price`
- `setUserQuantity(field, value)` — sets a quantity as user-specified and immediately recalculates price
- `displayPrice` getter — price divided by pax (per-person view)
- `total` getter — raw `_price` value (used by `Aggregable`)

Depends on `this._inheritedContext` being present. This field is provided by `Rulable`. If composed without `Rulable`, `resolveQuantities` falls back to `{}` silently.

`Prizable` is item/leaf-oriented. Day, basket, and future kit pricing should be derived through aggregation layers, not by reusing leaf quantity semantics directly.

---

**`Aggregable(Base)`**
Adds `_children` as a `Map` keyed by child id. Provides:
- `addChild(id, child)` / `removeChild(id)` / `getChild(id)` / `getChildren()`
- `aggregate()` — iterates children, resolves each child's total (via `.aggregate().subtotal` for nested containers, `.total` for leaves, `._price` as fallback), and stores `{ subtotal, breakdown }` in `_aggregateResult`
- `subtotal` getter — last aggregated subtotal

`Rulable.propagateContext()` iterates `this._children` — so `Aggregable` must appear below `Rulable` in the composition chain for propagation to work on containers.

Flow model summary:

- Downward flow: context and rule effects travel parent -> child (`Rulable.propagateContext`).
- Upward flow: totals, warnings, and errors travel child -> parent (`Aggregable.aggregate`).

---

**`Rulable(Base)`**
Adds rule state (`_rules`, `_appliedRules`) and the inherited context bag (`_inheritedContext`). Provides:
- `setRules(rules)` — stores the rule array for later evaluation
- `receiveContext(patch)` — merges a patch into `_inheritedContext` (non-destructive; existing keys survive unless overwritten)
- `evaluateRules(evaluator?)` — iterates `_rules`, calls `evaluator(rule, context)` for each active rule, accumulates `_appliedRules`. Non-accumulating rules (`Acumulable === false`) stop evaluation after the first match.
- `propagateContext(ruleOutputs)` — merges `_inheritedContext` with `ruleOutputs`, then calls `receiveContext(merged)` on each child in `this._children`
- `getAppliedRules()` — returns a shallow copy of applied rules
- `_buildRuleContext()` — returns `{ ...this._inheritedContext }` by default; subclasses override to add their own fields to the evaluation context

The evaluator is passed at call time, not stored. This keeps the rule evaluation algorithm external and swappable.

---

**`Storable(Base)`**
Adds database identity fields: `ID_Linea`, `ID_Item`, `ID_Categoria`, `ID_Cotizacion`. Provides:
- `toStorageObject()` — throws until implemented by the concrete class
- `fromStorageObject(...)` — expected as a concrete class-level constructor/factory counterpart
- `markDirty()` / `markClean()` — dirty tracking via `_isDirty`
- `hasStorageIdentity()` — true if any ID field is non-null
- `isSaved()` — true if not dirty and has identity

---

### UI Mixins

**`Actorlike(Base)`**
Wraps an XState actor reference (`_actorRef`). Provides:
- `setActorRef(ref)` — stores the actor; accepts `null` to detach
- `sendEvent(type, payload)` — calls `_actorRef.send({ type, ...payload })`; no-ops silently if no actor is set
- `getSnapshot()` — delegates to `_actorRef.getSnapshot()`
- `subscribe(callback)` — delegates to `_actorRef.subscribe(callback)`; returns the subscription (caller owns cleanup)
- `hasActorRef` getter

All methods fail safe when `_actorRef` is null.

---

**`Alpineable(Base)`**
A single-method contract. Provides:
- `toDisplayObject()` — throws at runtime until implemented by the concrete class

This is the Alpine.js synchronization boundary. Alpine templates call `toDisplayObject()` to get a flat snapshot of all state needed for rendering.

---

**`Eventable(Base)`** 
Observer/emitter. Provides:
- `on(eventName, callback)` — registers a listener
- `emit(eventName, data)` — calls all registered listeners for the event
- `off(eventName, callback)` — removes a specific listener by reference

Backed by `_listeners = {}`, a plain object keyed by event name.

---

**`Formable(Base)`**
Form state and validation scaffold. Provides:
- `setField(name, value)` — updates `_formState`, clears any existing error for that field
- `getField(name)` / `getFormState()`
- `validate()` — throws until implemented by the concrete class
- `setFieldError(name, error)` / `getFieldError(name)` / `getFormErrors()`
- `hasErrors()` / `clearFormErrors()`

---

**`Modalable(Base)`**
Dialog lifecycle. Provides:
- `open()` / `close()` / `isOpen()`
- `setLoading(value)` / `isLoading()`
- `addError(message)` / `getErrors()` / `clearErrors()`

---

**`Serviceable(Base)`**
Service locator. Provides:
- `injectService(name, service)` — registers a named service
- `getService(name)` — retrieves by name; `undefined` if absent
- `hasService(name)` — presence check

Backed by `_services = {}`.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/01_system_overview.md`.