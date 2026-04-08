# Methodology Synthesis — Extended Analysis

**Motivation questions:** AI vs other domains / Document templates / Standards structure / Drift / Human in the loop / Git usage / Weaknesses / Testing

---

## Q1 — What differences exist when implementing AI vs backend vs frontend vs API?

Each domain has its own file layout, build sequence, and validation gate. They are not unified in any project — each extends a shared `basic.md` but defines its own rules on top.

### AI / LangGraph modules

File layout:
```
contracts.py   ← schema backbone (input, output, review, persistence models)
prompt.py      ← prompt templates and variable construction only
storage.py     ← artifact paths, round management, JSON I/O only
graph.py       ← state, nodes, edges, chain wiring, Studio factory
main.py        ← CLI entry point only
```

Build sequence (order is mandatory):
1. contracts → 2. storage → 3. prompt → 4. graph (demo chain) → 5. CLI → 6. Studio → 7. real model → 8. harden

The **demo chain** is the key structural enabler — the graph must be exercisable at every step before credentials exist. Without it, testing graph topology requires live API calls.

Node taxonomy by responsibility: `load_*` (validate inputs), `run_*_llm` (only place that calls the model), `persist_*` (no logic, delegates to storage), `*_review_node` (thin breakpoint anchor), `apply_*` (validate payload, hash-check, route), `prepare_*` (context prep for regeneration).

GraphState carries only routing signals and artifact refs — never full payloads. Heavy data is on disk.

### Backend / pipeline modules (deterministic)

File layout mirrors AI but without `prompt.py`. The key distinction: deterministic functions live in `src/core/`, AI nodes live in `src/nodes/`. They never mix.

Build sequence is simpler: contracts → implementation → tests → CLI. No demo chain needed. Fail-closed is mandatory — no fallback that silently converts failure into success.

Ingestion modules (system boundary) have their own layout:
```
models.py      ← output Pydantic model (internal contract)
adapter.py     ← abstract base defining extraction contract
providers/     ← source-specific adapters
main.py        ← discovery, dispatch, idempotency check
storage.py     ← artifact paths, meta.json, idempotency state
```

Ingestion has one job: receive uncontrolled external input, validate it, produce a typed internal model. All validation at the boundary. Downstream modules never see raw input.

### Frontend / UI

Plan template structure (PhD 2.0 UI template): Spec ID + view name, Feature path, Libraries, Phase, Migration Notes, Operator Objective, Data Contract (API I/O), UI Composition and Layout (grid description with ASCII art), Styles, Files to Create, Definition of Done (checkbox list), E2E tests (TestSprite steps), Git Workflow (mandatory commit format + changelog entry + checklist update).

The UI is explicitly a **projection layer** over disk artifacts, never the source of truth. The data contract points to TypeScript types — it does not restate them. Missing data must degrade gracefully.

API endpoints follow FastAPI. They act as a data bridge to the filesystem, never as business logic. Rule from doc_methodology: "the API acts exclusively as a data bridge."

### Key cross-domain rule

Every domain follows the same contract principle: a typed Pydantic/TypeScript schema defines every boundary. The schema is the documentation. But the file layout, build sequence, and validation gates are domain-specific — not universal.

**Finding:** The methodology has a universal contract layer (schemas define all boundaries) and domain-specific implementation layer (each domain has its own file structure and build sequence). Mixing the two produces the most common drift.

---

## Q2 — What document templates exist for future_docs, plan_docs, docs? What types exist in each?

### future_docs/ — Deferred work

Template:
```markdown
# <Title>

**Why deferred:** One sentence. What is blocking or deprioritizing this now.
**Last reviewed:** YYYY-MM-DD

## Problem / Motivation
What is wrong or missing, and why it matters. Be specific.

## Proposed Direction
High-level solution shape. Not a full spec — enough to resume context later.

## Linked TODOs
- `src/path/to/file.py` — `# TODO(future): description`
```

Types found in practice:
- **Hardening roadmap** — known fragility in a module, not urgent enough to plan now
- **New feature** — wanted capability, not yet scheduled
- **Issues / conflicts** — known system inconsistencies (logging conflicts, overlapping responsibilities)
- **Product standards** — expected future policies that haven't been formalized

Stale threshold: 6 months. A future_docs entry is either promoted, deleted, or re-dated. No exceptions.

### plan_docs/ — Active execution

Two templates coexist (backend and UI):

**Backend plan mandatory sections:** Problem Statement, State Contract (current + required state.json), Core Functions affected, Node Implementation (affected nodes + edge transitions), HITL Requirements, API Endpoints (if any), File Changes Summary, Dependencies, Testing Strategy, Rollback Plan.

**UI plan mandatory sections:** Spec ID + coordinates, Migration Notes (legacy source to extract), Operator Objective, Data Contract (API I/O), UI Composition + Layout (ASCII grid), Styles, Files to Create, Definition of Done (checkbox), E2E (TestSprite steps), Git Workflow (commit format + changelog + checklist update).

**Lightweight plan (cotizador agent_guideline):** Context, numbered steps, "What NOT to do". Used for small feature-scoped tasks where the full template is overhead.

Common to all plan types:
- What this solves
- Explicit negative constraints ("What NOT to do")
- Ordered steps
- File changes map
- Verification criteria

Plans are ephemeral — deleted when work is done.

### docs/ — Persistent reference

Types found across projects:

| Type | Content | Examples |
|---|---|---|
| **standards/code/** | Universal and domain-specific code rules | `basic.md`, `llm_langgraph_components.md`, `ingestion_layer.md` |
| **standards/docs/** | Documentation conventions, checklists, lifecycle rules | `documentation_and_planning_guide.md`, `documentation_quality_checklist.md`, `future_docs_guide.md` |
| **runtime/** | Current technical truth for each domain/stage | `graph_flow.md`, `data_management.md`, `pipeline_overview.md` |
| **reference/** | Schemas, contracts, node matrices, artifact specs | `graph_state_contract.md`, `artifact_schemas.md`, `node_io_target_matrix.md` |
| **operations/** | Runbooks, known issues, diagnostic patterns | `agent_planning_and_verification_pattern.md`, `tool_interaction_and_known_issues.md` |
| **index/** | Navigation maps, conceptual trees, canonical paths | `canonical_map.md`, `conceptual_tree.md` |
| **adrs/** | Architecture decision records | `002_documentation_consolidation.md` |

Rule from doc_methodology: `docs/runtime/` can be referenced by `plan/` but NEVER the reverse. Current truth must not point forward to uncommitted future.

---

## Q3 — What standards/rules documents exist? Is there a consistent structure?

**Standards documents across projects follow this structure:**

1. **Title** — domain + what this governs
2. **Extension declaration** — "Extends basic.md" or "Extends llm_langgraph_components.md" — explicit layering, not self-contained
3. **Numbered sections**, each with: rule statement + code example + rationale
4. **Reference implementation** pointer — a real module that exemplifies the standard

**Hierarchy observed:**

```
basic.md                         ← universal (all Python modules)
  ├── llm_langgraph_components.md    ← AI/LangGraph specific
  │     └── llm_langgraph_methodology.md  ← process guide for the above
  ├── ingestion_layer.md             ← boundary components
  └── deterministic_tools.md        ← (referenced, not read)
```

UI standards follow the same layering pattern but in TypeScript. Architecture principle docs (cotizador's `design-principles.md`) have a different structure: numbered principles, each with a statement + elaboration + "no layer should X" negative constraint.

**Consistent elements across all standards:**
- Rule statements are declarative, not procedural ("the output model is the boundary" not "you should try to make the output model the boundary")
- Every rule has an anti-pattern shown or implied
- Code examples are specific and copy-pasteable
- Rules are organized from most universal to most specific

**Missing from every project:** A single index of all standards documents. Each project has a `practices/README.md` pointing to the files, but no cross-project or cross-domain standards map. The relationships between standards (what extends what) are declared in-file, not in a registry.

---

## Q4 — Do we have any information about drifting?

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

## Q5 — Is the human considered in the overall loop?

Yes, and it's a core design assumption, not an afterthought.

**postulador / PhD 2.0** has the most explicit human model:

HITL (Human-in-the-Loop) is payload-driven, not acknowledgement-driven. The human makes an **explicit semantic decision per row** (approve / request_regeneration / reject) and submits a typed `ReviewPayload`. Pressing "Continue" without a payload is a safe no-op — the system handles it explicitly, not as an error.

Human responsibilities (from `llm_langgraph_components.md`):
- Inspect the review surface (`review/current.json`)
- Make an explicit semantic decision per row
- Provide patch evidence when requesting regeneration
- Submit a typed ReviewPayload, not just pressing Continue

System responsibilities:
- Pause at the right moment (`interrupt_before` the review node)
- Persist the review surface before pausing
- Validate payload shape and hash on resume
- Reject stale payloads (hash mismatch)
- Route deterministically from the payload — never guess intent
- Handle bare-Continue as a safe no-op

**Git hooks put the human at the merge gate:**
- Requires 1+ human approval on every PR before merge
- Even admins must follow branch protection rules
- CI must pass before human review is triggered

**The human review surface is the UI:**
The Review Workbench product brief states: "This product assumes model output is useful but not final." The UI exists for inspection, correction, confidence building, and provenance visibility. It is not a display tool — it is a semantic review and correction tool.

**cotizador** has the same principle at the component level: `@wiki_exempt` is a human-authored override. Agent guidelines include explicit "What NOT to do" sections, written by the human for the agent before each task.

**Finding:** The human is not at the end of the loop as a final reviewer. The human is at multiple points: writing plans (before agent acts), reviewing semantic outputs (during pipeline execution), approving merges (before code lands), and auditing documentation drift. The methodology assumes the human operates on artifacts, not on code directly.

---

## Q6 — How is git used?

**Commit message format (doc_methodology / PhD 2.0):**
```
<type>(<domain>): <description> (<spec-id>)

- <component 1>
- <component 2>
- TestSprite: Passed | ID-123
```

`<type>`: feat, fix, docs, refactor, chore
`<domain>`: ui, pipeline, core, api, data, policy
`<spec-id>`: mandatory — traces the commit back to the plan that authorized it

**Commit format (postulador UI):**
```
feat(ui): implement <view name> (<spec-id>)

- <component 1>
- <component 2>
- Connected to <hook names>
```
Plus a changelog entry and a checklist mark in `index_checklist.md`.

**Enforcement (doc_methodology):**
- `commit-msg` hook: blocks commit without valid format or TestSprite evidence
- `pre-push` hook: blocks push if `pytest`, `npm run typecheck`, or `npm run lint` fail
- GitHub branch protection: requires 1+ approval, CI must pass, no bypass even for admins

**postulador (lighter):** `pytest` as the mandatory verification baseline. No commit-msg hook, but changelog update is mandatory for major changes.

**Tracking docs are updated in the same commit as implementation changes** (postulador_langgraph refactor governance rule). No split "update docs later" commits.

**Branch conventions:** Not explicitly documented in any project. Implied: feature branches, PR-based workflow, no direct pushes to main.

**Git as audit trail:** The drift diagnostics doc (cotizador) uses exact commit hashes and dates to reconstruct the timeline of when and why architecture diverged. Git is the source of truth for historical decisions, not a separate changelog tool (though changelog.md is maintained for human-readable summaries).

**Finding:** Git is used as both an enforcement mechanism (hooks) and an audit trail (commit history documents what changed and why, commit messages reference the spec that authorized the change). The `(spec-id)` in commit messages is the link between git history and the planning system.

---

## Q7 — What weaknesses exist across implementations?

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

## Q8 — How are things tested?

**Per domain:**

**Deterministic (backend/core):** Standard pytest unit tests. Each function tested in isolation. No real DB, no real LLM. Domain functions are pure — inputs in, outputs out, no side effects. Tests verify behavior against contracts, not implementation details.

**LangGraph / AI modules:** 
Minimum required test cases per module:
1. Approve flow (run → persist → pause → resume with approval → complete)
2. Regeneration flow (review requests regen → context prepared → second round runs)
3. Rejection flow (review rejects → graph ends cleanly)
4. Stale hash rejection (resume with hash mismatch → rejected)
5. Bare-Continue safety (resume with no payload → returns to pending state without crash)

Tests use `InMemorySaver` and injected fake chains — never the real model. CLI tests patch `build_graph` to inject the fake app. Demo chain must produce structurally valid output (passes `with_structured_output` validation).

**Ingestion:**
- Each ingestion run is idempotent — tests verify that re-running produces the same output, not a duplicate
- Partial failure handling: tests verify that one failed record doesn't abort the batch
- LLM rescue path: rescue is only triggered on explicit failure, never speculatively
- Validation at boundary: missing mandatory fields raise domain exceptions, not generic errors

**UI / Frontend:**
Two layers:
1. Type checking (`npm run typecheck`) — TypeScript validates all contracts at compile time
2. E2E tests via TestSprite — real browser flows verifying specific user actions and expected outcomes

The UI testing philosophy is: if a behavior can only be verified in a real browser, verify it in a real browser. No synthetic assertions for UI rendering behavior. TestSprite evidence is required in the commit message — testing is not optional or separable from shipping.

**Documentation quality testing:**
`scripts/validate_doc_links.py` validates that all file references in READMEs point to existing files. Broken links are a CI failure. This is the only automated documentation test found across projects.

**Integration / cross-layer:**
Not explicitly defined as a test category in any project. The closest equivalent is the Studio verification checklist (can the graph load without credentials? does it pause at the right node? does resume route correctly?) — but this is manual, not automated.

**Test pyramid shape implied across projects:**
- Many unit tests (contracts, pure functions, storage round-trips)
- Some graph topology tests (demo chain, approve/reject/regen flows)
- Some E2E tests (TestSprite for UI flows)
- No dedicated integration tests between backend and UI layers

**Finding:** Testing is domain-specific and has explicit minimum coverage contracts per domain. The weakest layer is cross-domain integration — no project has a stated policy for testing the full pipeline from ingestion through AI through UI through human review as a single flow. Studio verification partially fills this gap but it's manual and not tracked as a test artifact.
