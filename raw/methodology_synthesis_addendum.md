# Methodology Synthesis — Addendum

**Questions:** Project initialization / Navigation philosophy / Decision thresholds / Context router for agents / Real future_docs examples

---

## Q1 — Project initialization ritual: what's the canonical starting state?

The most complete answer is the 6-phase lifecycle from `entrypoint.md` (doc_methodology). It defines the Zero-Tolerance Policy: **no code change is valid unless it satisfies all 5 pillars.**

| Pillar | Requirement |
|---|---|
| Planned | Every change starts as a document in `plan/` |
| Tested | Every functional change has an E2E test |
| Documented | `docs/runtime/` reflects code reality |
| Registered | `changelog.md` and checklists updated |
| Committed | Standardized commit format for traceability |

The 6 phases in order:
1. **Planning** — create spec in `plan/[domain]/` using the appropriate template
2. **Execution** — implement using the routing matrix and agent templates
3. **Testing** — local verification + E2E (TestSprite)
4. **Documentation Closure** — promote plan to `docs/runtime/`, delete plan file, update changelog and checklist
5. **Git** — standardized commit with spec-id and TestSprite evidence
6. **Meta-Review** — human audits the session

**Phase 6 is the most important discovery in the entire data set.**

At the end of every development session, the human operator:
- Reviews what the agent (or developer) did
- Identifies friction: hallucinations, stuck states, routing failures, ambiguous rules
- Immediately patches the meta-documentation that caused the friction

The rules that govern this:
- Protocol failed → update `12_context_router_protocol.md`
- Missing keyword → inject into `11_routing_matrix.md`
- Ambiguous rule → rewrite `13_agent_intervention_templates.md`

**"No logical error or contradiction in system rules should survive the session that discovered it."**

This means the methodology is not static documentation — it is a self-correcting system. Every session that reveals a friction point produces a rule patch before the session closes. The hausordnung is not a final document; it is the current best version, always subject to improvement from the next session.

**Finding:** A project is not initialized once. It is continuously re-initialized through Phase 6. The starting state is not a template applied once — it is whatever the meta-documentation currently says after all previous session patches.

---

## Q2 — Navigation philosophy: how do you find what you need?

**The 4D matrix model (doc_methodology context router):**

The repository is a coordinate space, not a file hierarchy. Every document has exact coordinates:
- **X — Domain:** `ui`, `api`, `pipeline`, `core`, `data`, `policy`
- **Y — Stage:** `scrape → translate → extract → match → strategy → drafting → render → package`
- **Z — Layer:** `docs` or `code`
- **W — Temporal state:** `runtime` (current truth) or `plan` (future designs)

An agent never guesses file paths. It calls `fetch_context(domain='ui', stage='match', state='runtime')` and the router assembles the relevant files from the matrix. This is deterministic and auditable.

**The canonical map model (postulador_langgraph):**

The `canonical_map.md` is the human-readable navigation layer. It explicitly partitions all documents into categories with a conflict resolution rule:

- Current runtime truth (use these first)
- Current navigation / status maps
- Current policy notes
- Official specs and design references
- Active planning / migration docs

Rule: "If a document conflicts with the current runtime truth set, trust the current runtime truth set and mark the conflicting doc as target-state, planning, or historical."

**The conceptual tree (postulador_langgraph):**

Before creating or editing any document, ask 4 questions:
1. Is this current truth, plan, or subsystem detail?
2. What is its canonical home in the tree?
3. Can an existing central doc link to it instead of duplicating it?
4. If this becomes stale, should it be archived or deleted?

The tree structure:
- `docs/` = current state only. Runtime truth, policy, stable reference, operator playbooks.
- `plan/` = planning only. Plans, ADRs, execution trackers, templates.
- Code-local README files = heavy implementation detail near its code.
- Central docs summarize and link. They do not duplicate.

**The "docs/ test":** A document belongs in `docs/` only if it answers one of: what exists now, how it works now, how an operator uses it now, what's a stable reference needed across the repo. If mostly future-looking, speculative, or historical — it does not belong in `docs/`.

**Finding:** Navigation is designed for two different readers. The 4D matrix is for AI agents — deterministic coordinate-based retrieval. The canonical map and conceptual tree are for humans — conflict resolution rules, ownership rules, and a "before you create a file" checklist. Both point at the same invariant: current truth is separated from everything else at the navigation layer, not just the storage layer.

---

## Q3 — Decision thresholds: when does something graduate between tiers?

**future_docs → plan_docs (when to promote):**
- Item enters active execution (someone decides to work on it now)
- The `future_docs/` entry is deleted at the same moment, not after
- The plan replaces it — they never coexist

**Implicit triggers for promotion (inferred from real examples):**
- A blocker clears that was preventing the work
- The item becomes the main bottleneck for a higher-priority goal
- 6-month stale threshold forces re-evaluation: promote or delete

**plan_docs → deleted (when a plan closes):**
Explicit close conditions from the 5-pillar rule: all tests pass + docs/runtime/ updated + changelog entry + checklist marked + commit made. When all 5 pillars are satisfied, the plan is deleted. There is no "archive" state — closed plans live in git history only.

**When a hotfix vs. a full plan:**
The decision matrix from the context router is the clearest statement:
- Is there a bug to fix? → hotfix (no plan required)
- Is there an existing plan? → implement
- Want to propose something new? → design (creates a plan)
- Did code drift from docs? → sync (no plan required)

**When a plan is required vs. optional:**
From `feature_creation_methodology.md`: the 5-step methodology is **mandatory** for:
1. Any new top-level package or major subsystem
2. Any refactor that changes ownership or location of core logic
3. Any feature integrating multiple execution backends or third-party services

For small, localized changes within an existing architecture: a simple `plan_docs/` entry is sufficient — no full methodology cycle.

**The "too risky to proceed" signal:**
If any of the 5 pillars cannot be satisfied (can't write tests, can't update docs, unclear scope), the change is too risky to make. Not "proceed carefully" — do not proceed. The pillar system is a go/no-go gate, not a checklist of aspirations.

---

## Q4 — Context router for agents: how are agents navigated?

**The core protocol (doc_methodology):**

Agents are given a system prompt that defines:
- Their identity ("PhD 2.0 Architect, autonomous developer agent")
- Their tools (5 tools: fetch_context, sync_code_to_docs, implement_plan, draft_plan, hotfix)
- Their domains and stages (coordinate vocabulary)
- Their rules (ALWAYS acquire lock before writing, hotfix REQUIRES doc update, implement_plan DELETES the plan)
- A decision matrix (is there a bug? is there a plan? want to propose? did code drift?)

The agent's first action on any task is **intercept and identify coordinates** — what domain, what stage, what intent. Then **decide workflow** (which of the 4 modes). Then **gather context** using `fetch_context` with those coordinates. Only then execute.

Agents never read files directly by path. They request coordinates and the router assembles context. This prevents hallucinated file paths and ensures the agent's view of the codebase matches the routing matrix.

**Content nature sub-axis:**
`fetch_context` can also filter by nature: `philosophy` (why it exists), `implementation` (how it's built), `development` (how to extend it), `testing` (tests and contracts), `expected_behavior` (edge cases). This means an agent working on a bug can request only `expected_behavior` context for the affected domain/stage, rather than everything.

**The routing matrix (not read but inferred):**
`docs/index/routing_matrix.json` is the machine-readable registry that maps coordinates to file paths. Every document in the repository has an entry with: domain, stage, nature, doc_path, target_code (glob patterns for source files). This is the index the router uses — not a hardcoded path list but a queryable registry.

**Finding:** The context router solves a real problem: agents with full file system access tend to hallucinate paths or read irrelevant files. By restricting agents to coordinate-based retrieval, the system guarantees that the agent's working context is exactly what the routing matrix says it should be — no more, no less. The routing matrix is the authoritative map; the files are the territory.

---

## Q5 — What do real future_docs entries look like? Are the rules followed?

**logging_layer_conflicts.md (postulador_refactor) — well-formed entry:**
- Why deferred: "not the main blocker for current API-backed pipeline execution"
- Last reviewed: 2026-03-29
- Problem: specific — 4 enumerated mixing styles, clear impact analysis
- Proposed direction: 5 concrete numbered steps
- No linked TODOs (could be a gap, or they weren't added yet)

This is exactly what the template asks for. Short, specific, actionable when prioritized.

**extract_understand_node.md (postulador_refactor) — well-formed entry:**
- Why deferred: "current focus is pipeline orchestration"
- Last reviewed: 2026-03-29
- Contains the full output contract (Pydantic model with field-level detail)
- Describes what the refactored branch needs (specific rewrite instruction)
- Lists other dev branch nodes to port
- Has a linked TODO

This is denser than the template — it includes the full schema definition so that when someone picks it up, they have everything needed to start. The template is a floor, not a ceiling.

**product_standard.md (postulador_v2) — informal note:**
This is raw thinking, not a formal future_docs entry. It reads as stream of consciousness: "i think that all of them but match hardening are part of the same bigger problem..." and sketches a vision for a unified architecture. It does not follow the template format.

This reveals something important: future_docs/ in practice accepts two kinds of entries:
1. **Formal entries** — template-compliant, specific problem + proposed direction + linked TODO + last-reviewed date. These are ready to promote to plan_docs when prioritized.
2. **Seed notes** — informal sketches of larger architectural directions, not yet refined enough for a formal plan. These are thinking-in-progress, not deferred-but-ready.

The methodology only defines the first type. The second type exists in practice but has no formal status. It represents the gap between "raw/ as ore" and "future_docs/ as deferred work" — a category for ideas that are neither raw material nor ready-to-act deferred items.

**Finding:** The template is followed for specific, scoped items. For larger architectural visions that span multiple modules, an informal note exists but has no defined lifecycle. This is a gap — the current methodology has no document type for "architectural hypothesis not yet decomposed into actionable items." It ends up in future_docs/ as an informal note or never written down at all.

---

## Synthesis: What these 5 questions add to the distillation

**Addition to the 5 axioms:**

**Axiom 6 (confirmed): The methodology improves itself.**
Phase 6 (meta-review) is not optional. Every session ends with a human audit that patches the rules which caused friction. The hausordnung is the current best version of the rules, not the final version. When a rule causes confusion, it is rewritten before the session closes. This is the mechanism that prevents the methodology from going stale.

**New finding — the missing document type:**
The current methodology covers: future_docs (formal deferred work) and raw/ (immutable ore). But it has no category for "architectural hypothesis" — an idea that's too large to be a deferred item and too unrefined to be raw ore. The product_standard.md informal note lives in this gap. The hausordnung should define this type explicitly, or route it to a specific location (e.g., `raw/thinking/` as a named sub-sanctuary before formalization).

**New finding — navigation is a first-class concern, not an afterthought:**
Every mature project has an explicit navigation layer: canonical maps, conceptual trees, routing matrices. These are not documentation — they are the index that makes documentation usable. A project without a navigation layer forces every reader (human or agent) to discover structure by exploration, which produces inconsistent mental models. The navigation layer should be designed before content accumulates, not added after the fact.

**New finding — the routing matrix is the missing link in wikipu:**
The context router protocol is exactly what the `query-server-runtime` issue in wikipu is asking for. The difference is that the doc_methodology implements it as a coordinate-based retrieval system with a JSON routing matrix, not as a free-form graph query. This is a simpler and more deterministic design than a full structured query language. It may be a better first implementation of the Librarian agent's tool interface.
