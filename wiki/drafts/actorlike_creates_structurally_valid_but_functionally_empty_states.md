---
identity:
  node_id: "doc:wiki/drafts/actorlike_creates_structurally_valid_but_functionally_empty_states.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/03_critique.md", relation_type: "documents"}
---

`sendEvent()` silently no-ops when `_actorRef` is null. This is a pragmatic defensive choice — it prevents crashes during construction, testing without an actor, or teardown. But it means a component that has never had an actor set can be "used" as if it works: state changes are made, methods are called, and no error surfaces. The component simply never communicates.

## Details

`sendEvent()` silently no-ops when `_actorRef` is null. This is a pragmatic defensive choice — it prevents crashes during construction, testing without an actor, or teardown. But it means a component that has never had an actor set can be "used" as if it works: state changes are made, methods are called, and no error surfaces. The component simply never communicates.

Any component whose correct behavior depends on actor communication has no safety net. If `setActorRef` is accidentally omitted during wiring, the component will appear to function — forms can be filled, rules can be evaluated, prices can be calculated — but no state transitions happen and no events reach the machine.

A `requireActorRef()` method that throws when `_actorRef` is null would let components opt into strict wiring assertions.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/03_critique.md`.