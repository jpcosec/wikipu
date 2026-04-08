---
identity:
  node_id: "doc:wiki/drafts/1_canonical_component_structure.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/04_best_practices.md", relation_type: "documents"}
---

The following shows a complete Domain Leaf component — a priceable, ruleable unit with storage identity and actor integration. This is the reference implementation for any `ItemBase`-derived class.

## Details

The following shows a complete Domain Leaf component — a priceable, ruleable unit with storage identity and actor integration. This is the reference implementation for any `ItemBase`-derived class.

```js
import { ItemBase } from '../common/base/domain/ItemBase.js';

export class ProductItem extends ItemBase {
  // ── Identity ─────────────────────────────────────────────────────────────
  // ID_Linea, ID_Item, ID_Categoria, ID_Cotizacion inherited from Storable

  // ── Own state ────────────────────────────────────────────────────────────
  Nombre = null;
  _profile = null;       // set via fromDefinition or fromSeed
  _category = null;      // denormalized for display

  // ── Lifecycle ────────────────────────────────────────────────────────────

  /**
   * Factory: create from a resolved database definition.
   * This is how a newly loaded item is wired up.
   */
  static fromDefinition(def, { pricingFn, evaluator }) {
    const item = new ProductItem();
    item.ID_Item       = def.ID_Item;
    item.ID_Categoria  = def.ID_Categoria;
    item.Nombre        = def.Nombre;
    item._profile      = def.pricingProfile;
    item._category     = def.categoria;

    // Default quantities from definition
    item._defaultPax      = def.defaultPax ?? null;
    item._defaultCantidad = def.defaultCantidad ?? 1;
    item._defaultDuracion = def.defaultDuracion ?? null;

    // Inject behavior (never hardcode algorithms inside the class)
    item._pricingFn = pricingFn;
    item._evaluator = evaluator;

    item.setRules(def.rules ?? []);

    return item;
  }

  /**
   * Factory: rehydrate from a persisted seed (e.g., from storage).
   */
  static fromSeed(seed, { pricingFn, evaluator }) {
    const item = ProductItem.fromDefinition(seed.def, { pricingFn, evaluator });

    // Restore user-set quantities
    if (seed.pax !== undefined)      { item.pax = seed.pax; item.paxIsUserSet = true; }
    if (seed.cantidad !== undefined)  { item.cantidad = seed.cantidad; item.cantidadIsUserSet = true; }
    if (seed.duracion !== undefined)  { item.duracion = seed.duracion; item.duracionIsUserSet = true; }

    // Restore storage identity
    item.ID_Linea      = seed.ID_Linea ?? null;
    item.ID_Cotizacion = seed.ID_Cotizacion ?? null;
    item.markClean();

    return item;
  }

  // ── Wiring (called after construction, from the owner/container) ──────────

  /**
   * Called by the parent container when an actor is available.
   * setActorRef is inherited from Actorlike.
   */
  wire(actorRef) {
    return this.setActorRef(actorRef);
  }

  // ── Required abstract method implementations ───────────────────────────────

  /**
   * Alpineable contract: flat snapshot for Alpine.js reactive rendering.
   * Return only what the template needs — never return internal state directly.
   */
  toDisplayObject() {
    return {
      id:          this.ID_Item,
      nombre:      this.Nombre,
      categoria:   this._category?.Nombre ?? null,

      // Quantities
      pax:         this.pax,
      cantidad:    this.cantidad,
      duracion:    this.duracion,
      paxIsUserSet:      this.paxIsUserSet,
      cantidadIsUserSet: this.cantidadIsUserSet,
      duracionIsUserSet: this.duracionIsUserSet,

      // Pricing
      price:        this.displayPrice,
      total:        this.total,

      // Rules
      appliedRules: this.getAppliedRules(),

      // Status
      isSaved:      this.isSaved(),
    };
  }

  /**
   * Storable contract: object suitable for writing to the database.
   * Include only fields the schema defines — do not leak internal fields.
   */
  toStorageObject() {
    return {
      ID_Linea:      this.ID_Linea,
      ID_Item:       this.ID_Item,
      ID_Categoria:  this.ID_Categoria,
      ID_Cotizacion: this.ID_Cotizacion,
      pax:           this.paxIsUserSet ? this.pax : null,
      cantidad:      this.cantidadIsUserSet ? this.cantidad : null,
      duracion:      this.duracionIsUserSet ? this.duracion : null,
    };
  }

  /**
   * Rulable hook: enrich the context passed to the rule evaluator.
   * Always call super._buildRuleContext() and spread it.
   */
  _buildRuleContext() {
    return {
      ...super._buildRuleContext(),   // includes _inheritedContext
      ID_Item:      this.ID_Item,
      ID_Categoria: this.ID_Categoria,
      profile:      this._profile,
      pax:          this.pax,
      cantidad:     this.cantidad,
      duracion:     this.duracion,
    };
  }

  // ── Convenience serialization for persistence ─────────────────────────────

  toSeed() {
    return {
      def: {
        ID_Item:        this.ID_Item,
        ID_Categoria:   this.ID_Categoria,
        Nombre:         this.Nombre,
        pricingProfile: this._profile,
        categoria:      this._category,
        defaultPax:     this._defaultPax,
        defaultCantidad: this._defaultCantidad,
        defaultDuracion: this._defaultDuracion,
        rules:          this._rules,
      },
      pax:           this.paxIsUserSet ? this.pax : undefined,
      cantidad:      this.cantidadIsUserSet ? this.cantidad : undefined,
      duracion:      this.duracionIsUserSet ? this.duracion : undefined,
      ID_Linea:      this.ID_Linea,
      ID_Cotizacion: this.ID_Cotizacion,
    };
  }
}
```

**Wiring pattern at call site:**

```js
// In the parent container (or mounting logic):
const item = ProductItem.fromDefinition(resolvedDef, { pricingFn, evaluator });

// Actor is wired separately — it may not exist at construction time
const actorRef = createActor(itemMachine, { input: { itemId: item.ID_Item } });
item.wire(actorRef);
actorRef.start();

// First update cycle
item
  .receiveContext(containerContext)
  .evaluateRules(evaluator)
  .resolveQuantities()
  .calculatePrice();
```

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/04_best_practices.md`.