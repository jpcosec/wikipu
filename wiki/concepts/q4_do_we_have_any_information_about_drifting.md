---
identity:
  node_id: "doc:wiki/concepts/q4_do_we_have_any_information_about_drifting.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/methodology_synthesis_extended.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/methodology_synthesis_extended.md"
  source_hash: "0eaf49dde8b77f6999c8e390207549968bc290d82d4774999f7136fecc61fb30"
  compiled_at: "2026-04-14T16:50:28.663616"
  compiled_from: "wiki-compiler"
---

Yes — and it's one of the richest areas in the data.

## Details

Yes — and it's one of the richest areas in the data.

**cotizador has the most explicit drift documentation:**

`actor-ownership-drift-diagnostics.md` is a formal drift record with:
- The intended architectural invariant
- The observed implementation (current state)
- A drift timeline with exact commit hashes and dates
- Why the drift happened (root causes: delivery pressure, parallel evolution without enforcement gate)
- Impact analysis (architectural mismatch, lifecycle ambiguity, API inconsistency, onboarding friction)
- Decision options (normalize docs to code, or converge code to docs)
- A staged convergence plan
- Acceptance criteria for "drift resolved"

**`mixin-arch/03_critique.md`** documents structural risks of the current pattern before they become problems: hidden inter-mixin coupling, namespace collision risk, composition order ambiguity, `toDisplayObject()` abstract method enforcement gap, `sendEvent()` silent no-op creating "structurally valid but functionally empty" states.

**doc_methodology explicitly names drift as the enemy:**
- The `sync` intervention template exists specifically because docs drift behind code and need a dedicated recovery mode
- `skip_docs=True` in hotfix creates an explicit 24-hour debt record — drift is tracked, not silently accepted
- The `#todo(future): the address might be missplaced` note in the documentation quality checklist is itself a live example of the drift it describes

**postulador_refactor documentation guide** has a lifecycle rule: "Documentation that describes removed behaviour must be deleted, not left as historical comment." This implies drift via comment accumulation is a known failure mode.

**Root causes of drift identified across projects:**
1. Delivery pressure causes code to move faster than documentation
2. Parallel evolution of docs and implementation without an enforcement gate
3. Plans that survive their completion become false documentation
4. Hotfixes that skip doc updates create immediate debt
5. Architecture guides written before implementation is complete describe intent, not reality

**Finding:** Drift is a named, tracked concern across all projects. The most mature project (cotizador) documents it with timestamps, root causes, and a convergence plan. The methodology should treat drift documentation as a first-class artifact — not a sign of failure, but evidence of a healthy system that knows what's wrong.

---

Generated from `raw/methodology_synthesis_extended.md`.