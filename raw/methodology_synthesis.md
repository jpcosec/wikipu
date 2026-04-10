# Methodology Synthesis — Cross-Project Analysis

**Source projects:** docs_cotizador, docs_doc_methodology, docs_postulador_langgraph, docs_postulador_refactor, docs_postulador_ui, docs_postulador_v2
**Purpose:** Extract the methodology layer (how work was done) to distil a universal template and seed rules.

---

## Facet 1 — Plan Anatomy

**Question:** What sections does a well-formed plan always contain?

**What the projects show:**

- **postulador_langgraph** has the most complete format: TL;DR, Context, Objectives, Must have / Must not have, Verification strategy, Execution waves, Dependency matrix, Task checklist, Final verification wave.
- **doc_methodology** planning templates (UI and backend) use: Problem Statement, State Contract, Core Functions, Node Implementation, HITL Requirements, File Changes Summary, Dependencies, Testing Strategy, Rollback Plan.
- **cotizador** uses lighter agent_guideline files: Context, numbered steps, "What NOT to do".
- **postulador_refactor** documentation guide says: goal, constraints, ordered steps, open questions.

**Common core across all:**

Every well-formed plan always contains:
1. **What problem this solves** (one paragraph, mandatory)
2. **What is out of scope / must not happen** (explicit negative constraints)
3. **Ordered steps**, each narrow enough to verify independently
4. **File changes map** (what gets created, modified, deleted)
5. **Verification** — per-step or at the end, never absent

**What varies:** depth of state contracts, rollback plans, HITL gates. These are domain-specific extensions, not universal.

**Finding:** The lightest valid plan is: problem, constraints, steps, file map, verification. Everything else is specialization.

---

## Facet 2 — Documentation Lifecycle

**Question:** How does an idea move from thought to plan to code to history?

**Consistent pattern (postulador_refactor, postulador_v2, doc_methodology):**

```
idea / known problem
  → future_docs/<topic>.md     (deferred: why, proposed direction, linked TODO)
  → plan_docs/<plan>.md        (active: when prioritized, future_docs entry deleted)
  → deleted + changelog.md     (complete: plan deleted, inline TODO removed)
```

**Additional rule from doc_methodology:**
- `docs/runtime/` = current truth. Never contaminated by plan references.
- `plan/` can reference `docs/runtime/`. `docs/runtime/` cannot reference `plan/`.
- Temporal unidirectionality: the current state of the world does not point forward to an uncommitted future.

**Key invariant:** Plans are ephemeral by design. A plan that survives its completion is documentation drift. The healthy state is: plan gone, code changed, changelog updated.

**Debt decay rule (postulador_refactor):** future_docs/ entries not touched in 6 months are stale — promote, delete, or re-date. No graveyard accumulation.

---

## Facet 3 — Agent Permissions Model

**Question:** What are agents explicitly allowed vs. forbidden? How is scope enforced?

**Most sophisticated (doc_methodology) — 4 intervention templates:**

| Mode | Can write code? | Can write docs/runtime? | Can write plan/? | Notes |
|---|---|---|---|---|
| design | NO | NO | YES | Proposes architecture only |
| implement | YES | YES (promote) | NO (auto-delete) | Executes existing plan |
| sync | NO | YES (overwrite) | NO | Docs drifted behind code |
| hotfix | YES | YES (update) | NO | Bug fix, docs update mandatory |

`skip_docs=True` in hotfix creates an explicit 24-hour debt — never a silent escape.

**Lighter enforcement (cotizador):** Per-task agent_guideline files list explicit "What NOT to do" sections. Less mechanical enforcement, same intent.

**AGENTS.md approach (postulador_v2):** Convention-based: prefer small changes, follow module boundaries, update changelog for major changes, don't revive deleted legacy modules.

**Finding:** All projects enforce some version of "agents have a current mode with bounded permissions." The difference is how mechanically it's enforced. Doc_methodology's 4-template system is the most explicit and least ambiguous. The core principle is identical: **an agent always knows what it's currently allowed to touch.**

---

## Facet 4 — Architectural Invariants

**Question:** What layer/module rules appear in every project?

**Cotizador:**
- UI (projection/intent) → orchestration (transitions) → domain (pure logic) → adapters (I/O)
- No layer absorbs another's responsibility
- Pure domain: no DB access, no UI state reads, no transport concerns

**Doc_methodology (PhD 2.0):**
- CLI > API > UI: all functionality born as deterministic CLI function first
- Deterministic functions (core/) are always separate from AI/LangGraph nodes (nodes/)

**Postulador_refactor / postulador_v2:**
- `contracts.py` — all schemas, the boundary between modules
- `storage.py` — all file I/O, no business logic
- `main.py` — CLI entry point only, no business logic
- `graph.py` — orchestration only

**Universal invariant across all projects:**

> Deterministic logic is always separate from AI logic. AI logic is always separate from I/O. I/O is always separate from presentation. Every boundary is defined by a typed contract.

**The consistent physical expression of this rule:**
- `contracts.py` exists in every Python project
- The domain core can always be tested without an LLM, a database, or a UI

---

## Facet 5 — Verification Contract

**Question:** What does "done" mean? What proof is required?

**postulador_langgraph:** 4-level order: (1) unit/slice tests → (2) build/type-check → (3) browser or operator flow → (4) end-to-end sanity.

**doc_methodology:** TestSprite evidence required in every commit message. pre-push hook blocks push on failing tests. Done without proof doesn't exist.

**Feature creation methodology (postulador_v2):** Each execution slice must leave the codebase in a valid state. Tests written alongside or before implementation. Refactor ends with removal of legacy code and update of all documentation.

**Deterministic rebuild plan (postulador_langgraph):** One step at a time. Run deterministic tests after each step. No exceptions.

**Finding:** Done = tests pass at each step + changelog updated. Tests are not an end-gate; they are inline. A step that cannot be verified in isolation is a design problem, not a process problem. "Final" verification exists but it's a sanity check on already-verified slices, not the primary gate.

---

## Facet 6 — Debt Topology

**Question:** How is deferred work stored, aged, and promoted? What prevents accumulation?

**Consistent answer (postulador_refactor, postulador_v2, doc_methodology):**

- Deferred work lives in `future_docs/` with: why it's deferred, proposed direction, last-reviewed date.
- Inline `# TODO(future): <description> — see future_docs/<file>.md` at the exact code location.
- 6-month stale threshold: untouched entries must be promoted, deleted, or re-dated.
- When prioritized: promote to `plan_docs/`, delete `future_docs/` entry simultaneously.
- When complete: delete plan, remove inline TODO, update changelog.

**What prevents accumulation:** The 6-month rule + the fact that plans are automatically deleted on completion. There is no "archive" state. Resolved = deleted from the repo. History lives in git log and changelog.md.

---

## Facet 7 — Code Style Axioms

**Question:** What conventions appear in every project without being discussed — the assumed rules?

Across all Python projects:
- `from __future__ import annotations` at the top of every module
- Module docstring: one paragraph, executive summary of the module's role
- Every public class, method, function has a structured docstring
- `contracts.py` / Pydantic models are the only legitimate way to pass data between modules
- `Field(description=...)` is dual-purpose: human + LLM readable, always semantic and specific
- Domain-specific exceptions defined at the top of the relevant file. Never bare `Exception` for flow control.
- Never swallow errors silently. Log with context, re-raise with `from e`.
- `LogTag` shared vocabulary — never hardcoded emoji strings
- `changelog.md` updated on every significant change
- Comments only for non-obvious invariants or workflow decisions

**Finding:** These are assumed so deeply that they rarely appear in explicit rules documents — they show up in code examples and templates. They need to be stated explicitly in the seed rules because they're invisible to a newcomer.

---

## Facet 8 — Inter-Project Divergence

**Question:** Where do projects contradict each other? Which version is better?

**Divergence 1: Agent control granularity**
- Doc_methodology: mechanical enforcement via git hooks + 4-template system with tooling (DocMutator auto-manages file lifecycles, TestSprite required in commits)
- Postulador: AGENTS.md + convention, no hard enforcement
- Cotizador: per-task agent_guideline, enforcement by human review only

**Verdict:** Doc_methodology is the most explicit and least ambiguous. The 4-template model eliminates the question "am I allowed to touch this?" at every moment. However, it requires tooling (DocMutator, TestSprite) that adds overhead. The minimal viable version is the 4-mode permission model without requiring the exact tooling.

**Divergence 2: Plan scope**
- Cotizador: atomic feature-scoped plans (`plan/<feature>/` folder with phases as separate files). One feature = one plan.
- Postulador: larger multi-phase plans with dependency matrices in single documents.
- Doc_methodology: domain + stage coordinates every piece of work.

**Verdict:** Cotizador's atomic feature folders are the most agent-friendly. A single plan document that runs 200+ lines becomes a context problem. Phases-as-files allows parallel execution and incremental completion. The postulador wave model is good for dependency tracking but creates large monolithic documents.

**Divergence 3: How docs point to code**
- Postulador_refactor: docs point to file paths, links are validated by CI
- Cotizador: docs describe behavior, code is the authority, no link validation
- Doc_methodology: strict temporal unidirectionality (docs/runtime/ never references plan/)

**Verdict:** Doc_methodology's unidirectionality rule is the clearest. The postulador's link validation is good engineering but adds CI overhead. The minimum viable version: docs/runtime/ references code, never plan/. Plan references docs/runtime/. This is unambiguous and requires no tooling.

---

## Facet 9 — Minimum Seed

**Question:** What is the smallest set of rules that generates the rest?

After tracing all patterns, five axioms generate the entire methodology:

**Axiom 1: Separation is non-negotiable.**
Deterministic logic, AI logic, persistence, and presentation are always separate layers. A unit that does two things is wrong by definition. This generates: contracts.py, storage.py, main.py separation; CLI-first architecture; pure domain core; layer ownership rules.

**Axiom 2: Contracts define all boundaries.**
Every interface — between modules, between human and agent, between current and future state — is a typed schema. The schema IS the documentation. Descriptions must be accurate because LLMs read them. This generates: Pydantic everywhere, Field(description=...) required, contracts as the only inter-module API, docstrings as specifications.

**Axiom 3: Plans are ephemeral. Code and changelog are permanent.**
A plan that survives its own completion is drift. Done = plan deleted, code changed, changelog updated. This generates: the future_docs → plan_docs → deleted lifecycle, the 6-month stale rule, the prohibition on archive folders, the "history lives in git and changelog" principle.

**Axiom 4: Agents operate within explicit, bounded permission frames.**
At every moment, an agent's scope is known: what it can create, what it can modify, what it cannot touch. Mode determines scope. This generates: the 4-template intervention model (design/implement/sync/hotfix), per-task agent guidelines, "What NOT to do" sections in plans, the prohibition on agents bypassing git hooks.

**Axiom 5: Verification is inline, not deferred.**
A step that cannot be verified in isolation is a design problem. Tests run at each slice, not at the end. This generates: test-driven alongside implementation, the 4-level verification order, the one-step-at-a-time execution rule, the requirement that each slice leaves the codebase valid.

---

## What Doesn't Fit Any Axiom Yet

**The critique pattern (cotizador mixin-arch/03_critique.md):** The codebase has a practice of writing explicit architectural critiques — documents that identify the failure modes, hidden coupling, and scalability cliffs of current patterns BEFORE they become problems. This is distinct from future_docs/ (which tracks known deferred work) and ADRs (which record decisions). It's a structural risk register. No other project does this explicitly, but it may be the most valuable artifact in the cotizador docs. Worth considering as Axiom 6.

**Proposed Axiom 6: Known architectural risks are documented explicitly.**
Every non-trivial architectural decision has a companion critique: what it correctly solves, what its hidden costs are, what a better implementation would look like. This is not pessimism — it's the precondition for evolving architecture without losing institutional memory.
