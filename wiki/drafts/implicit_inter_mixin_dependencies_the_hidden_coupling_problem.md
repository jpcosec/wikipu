---
identity:
  node_id: "doc:wiki/drafts/implicit_inter_mixin_dependencies_the_hidden_coupling_problem.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/03_critique.md", relation_type: "documents"}
---

This is the most serious structural risk in the pattern.

## Details

This is the most serious structural risk in the pattern.

**The Prizable → Rulable dependency.** A pricing mixin's quantity resolution reads an inherited context field that is initialized and managed by a separate rules mixin. There is no declaration of this dependency anywhere in the pricing mixin's interface. If an engineer applies the pricing mixin without the rules mixin, the missing field resolves to a safe default — and the component behaves incorrectly in a way that produces no error and may not be detected until runtime.

**The container propagation dependency.** A rules mixin's propagation method iterates a children collection that is initialized and managed by a separate aggregation mixin. On a leaf (no aggregation mixin), the optional chain produces `undefined` and the loop is silently skipped — correct behavior on a leaf, but the absence of a runtime error means the dependency is invisible. If propagation were expected on the leaf for some reason, there would be no diagnostic output.

The system works correctly today because the base class compositions happen to always pair the right mixins. This is a convention, not a contract. Future developers composing new base classes — or applying mixins directly to concrete classes — have no mechanical guardrail to prevent silent miscomposition.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/03_critique.md`.