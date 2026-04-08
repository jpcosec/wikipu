---
identity:
  node_id: "doc:wiki/drafts/testing_granularity_problem.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/03_critique.md", relation_type: "documents"}
---

The pattern enables testing at three layers:

## Details

The pattern enables testing at three layers:

1. **Mixin tests** — isolated, minimal base, mock injected functions. These work well.
2. **Base class tests** — verify that the correct methods exist and that simple chains produce correct results. Typically use a thin test subclass.
3. **Component integration tests** — use real injected functions, real rules, possibly a real actor.

The gap is between layers 2 and 3. A component can pass all mixin tests and all base class tests, yet fail when assembled with real injected functions and a real actor — because the integration path, specifically the sequencing of `setRules`, `setActorRef`, `receiveContext`, `evaluateRules`, `resolveQuantities`, and `calculatePrice`, was never exercised together.

There is no test layer that covers "mixin composition + real injected functions + actor lifecycle." The architecture does not prevent this layer from being written, but it does not encourage it either.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/03_critique.md`.