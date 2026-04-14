---
identity:
  node_id: doc:wiki/concepts/q7_what_weaknesses_exist_across_implementations.md
  node_type: concept
edges:
- target_id: raw:raw/methodology_synthesis_extended.md
  relation_type: documents
compliance:
  status: implemented
  failing_standards: []
source:
  source_path: raw/methodology_synthesis_extended.md
  source_hash: 0eaf49dde8b77f6999c8e390207549968bc290d82d4774999f7136fecc61fb30
  compiled_at: '2026-04-14T16:50:28.663773'
  compiled_from: wiki-compiler
---

Discovered from explicit critique documents and diagnostic files — not inferred.

## Definition

Discovered from explicit critique documents and diagnostic files — not inferred.

## Examples

- Implementation of this concept within the Wikipu workflow.
- Application of these principles in current documentation.

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

Discovered from explicit critique documents and diagnostic files — not inferred.

### 1. The hidden coupling problem (cotizador mixins)
Prizable → Rulable inter-mixin dependency is implicit. Applying the pricing mixin without the rules mixin produces incorrect behavior with no runtime error. Convention masquerading as contract. No mixin `requires` declarations. This pattern scales poorly: at 10+ mixins, a new developer has no mechanical way to know which mixin combinations are valid.

### 2. Silent no-ops creating structurally valid but functionally empty states (cotizador)
`sendEvent()` silently no-ops when `_actorRef` is null. A component that is never wired to an actor can appear functional — forms fill, rules evaluate, prices calculate — but no state transitions occur. No diagnostic is emitted. `toDisplayObject()` enforcement happens at render time, not construction time — a component can pass all tests and fail only in browser rendering.

### 3. Architecture drifts from documentation without a gate (cotizador)
The "actor-owned class" invariant was clearly stated but not mechanically enforced. Code diverged from it under delivery pressure. The gap was only caught via a retrospective diagnostic document, not by any automated check.

### 4. Demo chain as a test gap (postulador AI modules)
Real usage against Studio reveals issues that unit tests miss, specifically because tests inject state directly while Studio users click buttons. The bare-Continue case (resume with no payload) was discovered through Studio, not tests. The methodology acknowledges this but has no structural solution — it's listed as a known class of issues to watch for.

### 5. Schema version absence (postulador AI modules)
`schema_version` field is listed as a future_docs item on the persistence model. Artifacts are written without version fields. If the schema evolves, there is no way to detect or handle format mismatches on load. This is a known deferred debt.

### 6. Documentation quality checklist contains its own drift (`#todo(future): the address might be missplaced`)
The quality checklist that is supposed to prevent drift has an inline TODO marking its own potential inaccuracy. A meta-observation: the tool that enforces quality is itself subject to the quality decay it polices.

### 7. LLM rescue caching gap (postulador ingestion)
The ingestion standards specify that LLM-generated extraction schemas should be cached after first success — but the cache is explicitly not committed (`schema_cache/` in .gitignore). If the cache is cleared (environment reset, new machine), the LLM re-runs on the same inputs with potentially different outputs. Determinism within a session, non-determinism across sessions.

### 8. Plan scope creep is structurally possible
The backend planning template has no explicit size constraint. postulador plans have grown to include 200+ line dependency matrices. There is no rule that splits a plan when it exceeds a certain scope. The cotizador approach (one feature = one plan folder with phases as separate files) is more discipline-enforcing but it's not stated as a rule anywhere.

---

Generated from `raw/methodology_synthesis_extended.md`.
