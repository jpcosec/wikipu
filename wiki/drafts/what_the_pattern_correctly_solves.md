---
identity:
  node_id: "doc:wiki/drafts/what_the_pattern_correctly_solves.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/03_critique.md", relation_type: "documents"}
---

**Avoids the diamond problem.** Multiple inheritance in class-based languages creates ambiguity when two superclasses define the same method. Functional mixins sidestep this entirely: each mixin is applied in a declared order, each extends the one below it, and method resolution is always unambiguous (the outermost definition wins).

## Details

**Avoids the diamond problem.** Multiple inheritance in class-based languages creates ambiguity when two superclasses define the same method. Functional mixins sidestep this entirely: each mixin is applied in a declared order, each extends the one below it, and method resolution is always unambiguous (the outermost definition wins).

**Capability declaration at the definition site.** Reading `class Foo extends Alpineable(Storable(Rulable(Prizable(Actorlike(class {})))))` conveys the full capability set without reading any implementation. This is a significant readability advantage over patterns where capabilities are accumulated via decorators, composition objects, or manual property assignment.

**Independent mixin testability.** Each mixin can be applied to a hand-crafted empty class and tested in isolation. No domain setup, no actor, no real rules engine. The test surface is small and the failure surface is narrow.

**No framework dependency.** The pattern uses plain ES2022 class fields and prototype chain mechanics. It works in any JavaScript environment — browser, Node, Deno, GAS — without a runtime library, bundler plugin, or transpiler step beyond what the project already requires.

**Role taxonomy decouples "what kind of thing" from "what it can do."** Categorizing components by role (leaf, container, modal, view) before assigning capabilities prevents ad hoc composition — where each component accumulates whatever mixins seem useful in the moment.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/03_critique.md`.