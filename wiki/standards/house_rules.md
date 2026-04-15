---
identity:
  node_id: "doc:wiki/standards/house_rules.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/concepts/wiki_construction_principles.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/knowledge_node_facets.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/cli/build.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/cli/cleanse.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/cli/curate.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/cli/ingest.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/cli/query.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/cli/scaffold.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/protocols/autopoiesis_coordinator.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/protocols/gate_loop.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/protocols/human_contributor.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/protocols/llm_agent.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/protocols/socratic.md", relation_type: "contains"}
  - {target_id: "doc:wiki/reference/protocols/trail_collect.md", relation_type: "contains"}
compliance:
  status: "implemented"
  failing_standards: []
---

The House Rules define the invariant constraints that govern the entire `wikipu` ecosystem — from identity and zone separation to code style and wiki authoring. Every rule exists to keep one or more of the system's five load-bearing elements (Autopoiesis, Wiki, Knowledge Graph, Git, CLI) coherent and non-overlapping.

# 🏠 House Rules

The canonical identity rules for the Wikipu ecosystem. This document defines what this system *is* — the invariant network of constraints that must hold regardless of what content the system contains. Rules are organized by layer. Each rule carries a `rule_id` for machine reference, a description, and the enforcement mechanism that checks it.

## Layer 1 — Identity Rules

The system is composed of five inseparable elements, each with a distinct and non-overlapping role:

| Element | Role | Question answered |
|---|---|---|
| **Autopoiesis** | the how | How does the system maintain and reproduce itself? |
| **Wiki** | the what | What does the system currently know to be true? |
| **Knowledge Graph** | the why | Why is each piece of knowledge structured the way it is — typed relationships that give nodes meaning through connection, not through content alone. |
| **Git** | the when | When did every state transition happen, and what was the prior state? |
| **CLI** | the do | How are all operations invoked deterministically by humans and agents? |

These five are the load-bearing structure. Every rule in this document exists to keep one or more of them coherent.

## Layer 1 — Identity Rules
*The invariants that define the system. Violating these means the system is no longer itself.*

**ID-1 — Orthogonality**
No two elements do the same thing. Before any new module, node, or `[[facet]]` is created, it must prove it does not duplicate or overlap with an existing one within the system's `[[topology]]`. Redundancy is a structural error, not a style preference.
`Enforced by:` TopologyProposal validation, FacetProposal orthogonality check.

**ID-2 — Minimal Energy**
When multiple valid responses to a perturbation exist, choose the one that minimizes systemic `[[energy]]`: LLM token consumption, structural complexity added to the graph, uncertainty in the resulting state, and number of new elements created (while maintaining strict orthogonality) — fully satisfying the requirement. Extend existing nodes before creating new ones.
*Clarification:* The core objective is to hold maximum knowledge in the smallest possible physical space, ensuring no false or contradicting knowledge and avoiding duplication. Highly granular, atomic composition is encouraged; structural mass is penalized primarily when it represents redundant boilerplate rather than orthogonal truth.
`Enforced by:` Autopoiesis loop coordinator pre-proposal check; graph query for overlapping intent before any TopologyProposal is submitted.

**ID-3 — Typed Contracts at Every Boundary**
All data crossing a process boundary must be a typed Pydantic model. No untyped dicts, no raw strings as data carriers, no implicit schemas. The contract IS the documentation. `Field(description=...)` is mandatory on every field — LLMs read it.
`Enforced by:` ASTFacet scanning detects untyped cross-module calls; audit checks for missing Field descriptions.

**ID-4 — Zone Separation**
The five information zones are inviolable:
- `raw/` — Inviolable. Immutable seed. Agents read, never write.
- `exclusion/` — Inviolable. The Non-Self. Untouchable by agents or the autopoietic motor.
- `wiki/` — Current Truth. The self-image of the system.
- `desk/` — Active Operational Surface.
- `drawers/` — Deferred potential.
- `src/` — The motor and sensory organs. (Formerly `future_docs/` in deprecated models).
No zone may reference or write into a zone above it in the chain. For example, `desk/` may reference `wiki/`, but `wiki/` may not reference `desk/`.
`Enforced by:` build_wiki() checks frontmatter edges for cross-zone violations; CI scan on commit.

**ID-5 — Human Gate at the Topology Boundary**
Human approval is required only for operations that affect entities outside the system's own topology — external codebases, external services, published artifacts, or shared infrastructure. Inside the topology, any operation that respects the core rules is permitted without a gate, provided it is reversible. Reversibility is guaranteed by git: every in-topology change can be undone. A proposal with `requires_human_approval: true` is one whose effects cannot be fully reversed by a git revert, or whose effects propagate outside the topology boundary. No implicit batch approvals for gated proposals.
`Enforced by:` cleanse --apply checks topology boundary before requiring approval; autopoiesis coordinator pauses at desk/Gates.md only for boundary-crossing proposals.
`Status:` boundary-checking logic in cleanse --apply is not yet implemented — pending `unimplemented/cleansing-protocol.md` (task 6). Until then, all cleansing proposals require human approval as a conservative fallback.

**ID-6 — Traceable Causality**
Every element's existence must trace to a perturbation that created it. No orphan nodes, no files without a known origin. New modules require a TopologyProposal. New wiki nodes require a source (raw/, code scan, or explicit authorship). Changelog records every significant change.
`Enforced by:` Audit check for nodes with no edges and no source; changelog enforcement on commit.

**ID-7 — Self-Inclusion**
The system's own processes (CLI commands, agent protocols, the hausordnung itself) are nodes in the graph they govern. A system that cannot model itself cannot maintain itself.
`Enforced by:` wiki/reference/cli/ nodes must exist for each CLI command; build audit checks for missing self-nodes.

**ID-8 — Total Queryability**
Everything within the system's workspace must be queryable by the CLI and eventually absorbable into the knowledge graph's topology. If an element (file, data, or code) cannot be expressed as a topological truth or used to maintain the system, it is "Not-Self" and must be relocated to the `exclusion/` folder.
`Enforced by:` `wiki-compiler energy` (Not-Self elements outside exclusion/ increase uncertainty energy); audit check for unqueryable files.

---

## Layer 2 — Methodology Axioms
*How work is done. Distilled from cross-project analysis of six production systems.*

**MA-1 — Separation is Non-Negotiable**
Deterministic logic, AI logic, persistence, and presentation are always separate layers. A unit that does two things is wrong by definition. This generates: contracts.py / storage separation, CLI-first architecture, pure domain core, layer ownership rules.

**MA-2 — Contracts Define All Boundaries**
Every interface — between modules, between human and agent, between current and future state — is a typed schema. The schema IS the documentation. Descriptions must be accurate because LLMs read them. This generates: Pydantic everywhere, Field(description=...) required, contracts as the only inter-module API, docstrings as specifications.

**MA-3 — Plans Are Ephemeral. Code and Changelog Are Permanent.**
A plan that survives its own completion is drift. Done = plan deleted, code changed, changelog updated. History lives in git and changelog only. There is no archive state. This generates: the desk/tasks lifecycle, the 6-month stale rule on drawers/, the prohibition on archive folders.

**MA-4 — Agents Operate Within Explicit, Bounded Permission Frames**
At every moment, an agent's scope is known: what it can create, what it can modify, what it cannot touch. Mode determines scope. Four modes:
- `design` — may write desk/proposals/ only. No code, no wiki/runtime.
- `implement` — may write code and promote wiki nodes. Deletes the plan on completion.
- `sync` — may overwrite wiki/ nodes to match code reality. No new code.
- `hotfix` — may fix code and update docs. Doc update is mandatory, not optional.
`Enforced by:` agent system prompts; Librarian intro.md protocol.

**MA-5 — Verification Is Inline, Not Deferred**
A step that cannot be verified in isolation is a design problem. Tests run at each slice, not at the end. Each slice leaves the codebase in a valid state. No step is done until its test passes.
`Enforced by:` pre-push hook; task resolution protocol requires tests before changelog update.

**MA-6 — The Methodology Improves Itself**
Every session ends with a trail collect step. Friction discovered during a session — wrong rules, missing constraints, ambiguous definitions — is encoded before the session closes. No logical error or contradiction in the rules should survive the session that discovered it. This is Phase 6 of the development lifecycle.
`Enforced by:` autopoiesis loop coordinator trail collect step; session log.

---

## Layer 3 — Navigation Rules
*How the system is traversed by humans and agents.*

**NAV-1 — The Graph Is the Routing System**
Agents navigate by graph traversal and facet query, not by guessing file paths or scanning directories. The routing matrix is not a coordinate space — it is the graph itself. Node IDs and edge types are the coordinates. `get_node`, `get_ancestors`, `get_descendants`, `StructuredQuery` + `FacetFilter` are the navigation primitives.
`Enforced by:` Librarian protocol (agents must query before reading); wiki-compiler query CLI.

**NAV-2 — Temporal State Is a Facet, Not an Axis**
Current truth, planned state, deferred state, and historical state are expressed as `ComplianceFacet.status` values and node_id prefixes — not as a separate coordinate axis. Agents scope queries by temporal state using facet filters.
- Current truth: `compliance.status = "implemented"`, no `desk/` or `drawers/` prefix
- Active: task in `desk/tasks/` or proposal in `desk/proposals/`
- Deferred: item in `drawers/`
- Historical: ADR node with `adr.status = "superseded"`

**NAV-3 — Read the Graph First, Markdown Second**
Agents do not read dozens of Markdown files sequentially. They query the graph for structure and relationships, then read individual Markdown files only when human-readable prose or ADR history is needed. `raw/` is never written to by agents.

**NAV-4 — Canonical Entry Points**
Every domain has exactly one canonical entry point file. Two types exist, distinguished by zone:

- **`Index.md`** — used in `wiki/` domains. A navigational artifact: lists the nodes in the domain, their relationships, and links to sub-domains. Read-only operational state — it reflects what is true, not what is being worked on. Replaces the deprecated `00_INDEX_MOC.md` name (MOC was an Obsidian-specific term with no meaning outside that tool).
- **`Board.md`** — used in `desk/` domains. An operational artifact: tracks active work items, their phases, dependencies, and parallelization. Mutable — it is updated as work progresses and items are resolved.

Agents start at the entry point for the relevant zone, not from a directory listing. Humans use the same entry points. Neither file may reference the other zone (`Index.md` never links to `desk/`; `Board.md` never links to `wiki/` nodes directly — only through the graph).
`Enforced by:` build audit checks that every wiki/ domain has an Index.md; OP-2 enforces Board.md structure.

---

## Layer 4 — Operational Rules
*How active work is structured and tracked.*

**OP-1 — The Desk Is the Operational Surface**
All active work lives in `desk/`. Boards track domain work trees. Gates register HITL blocks. `desk/Gates.md` is the central monitor — the single surface that shows all open human decisions across all boards.

**OP-2 — Board Structure Is Invariant**
Every Board (`Board.md`) contains: current state summary, priority roadmap with phases, dependency summary, parallelization map. Items are files in subdirectories. Resolved items are deleted, not archived. History lives in git and changelog.

**OP-3 — Gate Resolution Is Explicit**
A gate entry in `desk/Gates.md` is removed only when: the human has explicitly approved or rejected the proposal AND the resolution has been applied AND the changelog has been updated. Implicit resolution (gate line deleted without a trace) is not valid.

**OP-4 — Issue Resolution Protocol**
When an task is resolved:
1. Check whether any existing test is no longer valid — delete it if needed.
2. Add new tests for the new behaviour.
3. Run the relevant tests — all must pass.
4. Update `changelog.md`.
5. Delete the task file AND remove it from `Index.md`.
6. Commit with a message that names what was fixed.

**Default rule:** non-trivial implementation or documentation work starts from an task file in `desk/tasks/`. The only exception is a consciously declared structural/docs-only change that does not modify runtime code or tests.

**OP-5 — Atomization**
Every unit of work — task, proposal, or task — must be independently completable by a single agent in a single session and independently verifiable without knowledge of sibling units.

The test: can this unit be handed to a subagent as a self-contained deliverable? If completing it requires knowing about or modifying the same files as another unit, or if its "done" state can only be verified in combination with another unit, it is not atomic.

Split when: a unit has more than 3–4 steps that could fail independently. Extract the shared concern into a parent or sibling unit with an explicit `depends_on` link. Never split for organizational neatness — only when failure modes are genuinely independent.

This rule applies to wiki nodes via WK-1 (Single Responsibility) and to code modules via CS-9. The same principle governs all levels of the system.
`Enforced by:` task atomization check in Stage 2.2 of `wiki/standards/tasks_lifecycle.md`; contradiction check (Stage 2.3) ensures splits don't create overlap.

**OP-6 — Clean Tree Before Editing**
Do not start editing while the worktree has unstaged or untracked files. First bring the tree back to a deliberate state by committing, stashing, deleting, or otherwise resolving the pending changes.

- Run `git status --short` before starting a new implementation slice.
- If the tree is dirty, stop and resolve the pending state before editing any tracked or untracked file.
- A new editing session begins only from a clean tree.

`Enforced by:` agent workflow discipline; local git hygiene before any edit.

**OP-7 — Git Commit Cadence and Branching**
Git encodes state transitions at two levels of granularity: commits (atomic units) and branches (in-progress work streams). Together they make every stable state of the system recoverable and every change attributable.

**Commit = one atomic task resolved, or one coherent structural change.**
- One commit closes exactly one task (per OP-4 step 6). The commit message names the task.
- Structural wiki changes (new node, deleted node, edge modification) that are not tied to an task get their own commit.
- Session-end trail collect gets a commit even if no task was resolved.
- Do not commit on every file save. A commit is a claim that the system is valid and self-consistent at the granularity of one logical unit. A half-written node or an incomplete refactor is not a commit boundary.
- If runtime code or tests change, the default expectation is: linked task, changelog update, and branch name `task/<name>` or `phase/<name>`.

**Branch = one task or one coherent phase of work.**
- Every task or closely related group of tasks gets its own branch: `task/<name>` or `phase/<n>`.
- Work happens on branches. `main` is never the active development surface.
- Branch from `main`. Merge back to `main` only when the work set is complete, tests pass, and changelog is updated.

**Main = stable state milestone.**
- `main` is a claim that the entire system is coherent: all current-phase tasks resolved, all tests pass, no open structural debt in the work set.
- Merging to `main` marks a stable checkpoint — the equivalent of a version boundary, even without a tag.
- Never commit directly to `main` during active development.

Commit message format: imperative verb + what changed + why if non-obvious.
`Enforced by:` branch protection on main; pre-push hook verifies tests pass before merge; session log records last commit SHA and active branch; `wiki-compiler check-workflow` verifies task/changelog/branch discipline before commit.

**OP-8 — The Autopoietic Cycle**
Periodically (at minimum after each significant development phase):
1. `git tag v<n>` — snapshot the current state.
2. Clear processed ore from `raw/` (external project docs, obsolete seeds).
3. Evaluate: what is redundant, lacking, or upgradeable in the current system.
4. Research new sources if needed (papers, analogous systems, internet).
5. Put the current system's state (including this hausordnung) back into `raw/` as ore.
6. Run `wiki-compiler ingest` + `build` to regenerate the seed wiki.
7. Write a new version of the hausordnung incorporating what the cycle revealed.
8. Commit.

**OP-9 — Build Synchronization (Commit-After-Build)**
Any operation that modifies the Knowledge Graph (`knowledge_graph.json`) via `wiki-compiler build` must result in an immediate atomic commit. The graph must never be left in a drifted state relative to the `wiki/` source. Build outputs are not "artifacts" to be ignored; they are the compiled truth of the system and must be synchronized on every change.
`Enforced by:` `check-workflow` (ensures `knowledge_graph.json` is not drifted); `MA-5` (verification is inline).

**OP-10 — The Socratic Design Method**
Every proposed plan, node draft, or architectural design must be interrogated using the Socratic method before any implementation begins. The agent or human must generate typed questions (missing constraints, unstated assumptions, contradictions, undefined edge cases, scope creep signals, ownership gaps) and track them in `desk/socratic/Board.md`. A plan cannot move to `desk/tasks/` for execution until every open question on the board is explicitly answered and the resolution is structurally encoded into the topology (e.g., via house rule updates, wiki node changes, or plan revisions).
`Enforced by:` Agent system prompt circuit breakers; manual audit of `desk/socratic/` before task promotion.

---

## Layer 5 — Code Style
*Language-agnostic conventions. Apply to all source code in this project regardless of where it lives or what language it is written in. Language-specific enforcement tools and adaptations are listed per rule where they differ; see `wiki/standards/languages/` for per-language style guides.*

**CS-1** — Every module/file has a one-paragraph docstring or header comment: executive summary of the module's role.
**CS-2** — Every public class, method, and function has a structured docstring or doc comment.
**CS-3** — Typed contracts at every module boundary. No untyped dicts, no raw strings as data carriers, no implicit schemas. The contract IS the documentation.
**CS-4** — Contract field descriptions must be semantic and accurate — they are read by LLMs. Omitting a description is a documentation error.
**CS-5** — Domain-specific exceptions or error types defined at the top of the relevant file. Never bare/generic exception types for flow control.
**CS-6** — Never swallow errors silently. Log with context, re-raise or propagate with cause preserved.
**CS-7** — Comments only for non-obvious invariants or workflow decisions. No narrative comments restating what the code does.
**CS-8** — `changelog.md` updated on every significant change.
**CS-9** — Functions that use too many local variables are probably classes. Code should be self-explanatory. Avoid long functions — use helpers to simplify reading.

**Python-specific:**
- `from __future__ import annotations` at the top of every module.
- `contracts.py` / Pydantic models are the only legitimate way to pass data between modules.
- `Field(description=...)` on every Pydantic field.
- Re-raise with `from e` to preserve exception chains.
- `Enforced by:` docstring-coverage audit; ruff linting; ASTFacet scanning.

**TypeScript/JavaScript-specific:**
- All cross-module data uses typed interfaces or Zod schemas, never plain objects.
- JSDoc on every exported symbol.
- `Enforced by:` tsc --strict; ESLint.

---

## Layer 6 — Wiki and Documentation Rules
*How knowledge nodes are authored and maintained.*

**WK-1 — Single Responsibility**
Each wiki node answers exactly one question or defines exactly one concept. If the node's purpose cannot be stated in one sentence, it must be split. Test: can this node be transcluded into two different parent documents and make sense in both? If not, it is not atomic.

**WK-2 — Mandatory Abstract**
Every node starts with a 1–3 sentence paragraph that states the node's intent. This is not a heading — it is the first plain-text content after the frontmatter. It must stand alone as a summary.

**WK-3 — Composition over Duplication**
Use `![[node_name]]` transclusion to embed shared concepts. Never copy content from another node into a new one. If the same fact must appear in two places, it belongs in a third node that both transclude.

**WK-4 — Node Templates by Type**
Each artifact type has a canonical schema defining its frontmatter fields and required body sections. See `wiki/standards/artifacts/` for the full definition of each. Summary of `node_type` body structures:
- `concept`: Abstract → Definition → Examples → Related Concepts
- `doc_standard`: Abstract → Schema → Fields → Usage Examples
- `how_to`: Abstract → Prerequisites → Steps → Verification
- `adr`: Abstract → Context → Decision → Rationale → Consequences
- `reference`: Abstract → Overview → Commands / API → Examples
- `faq`: Abstract → Q&A pairs

**WK-5 — Current Truth Separation**
`wiki/` contains only current state. It never references `desk/` (active work) or `drawers/` (deferred). If a node describes something planned but not yet implemented, its `compliance.status` must reflect that (`planned` or `scaffolding`). A node with `status: "implemented"` is a claim that the code and docs match reality.

**WK-6 — Reference Docs Are Derived**
`wiki/reference/` nodes are generated from or kept in sync with source code. They document what exists, not what is planned. If the source changes, the reference doc must be updated in the same commit.

**WK-7 — Draft Promotion Requires Curation**
A draft may be promoted from `wiki/drafts/` into `wiki/` only when it has a clear single-purpose abstract, a non-fallback `node_type`, repository relevance, and no duplicate canonical node already covering the same concept.

`Enforced by:` `wiki-compiler curate --score`; human or agent review before `wiki-compiler curate --promote`.

---

## Violation Examples

- Writing agent output back into `raw/`.
- Creating a module by hand without a validated TopologyProposal.
- Storing graph-only edits that disappear on the next `build`.
- Marking a node `status: "implemented"` when the code does not exist.
- Promoting a draft that duplicates an existing wiki concept.
- Applying a cleansing proposal without explicit per-proposal approval.
- Leaving a gate open in `desk/Gates.md` with no activity for more than one cycle.
- Closing an task without updating tests and changelog.
- A rule in this document causing consistent friction and surviving the session that discovered it.

## Rule Schema

Each rule has: a `rule_id` (e.g. `ID-1`, `MA-2`, `WK-3`), a short name, a prose description, and an `Enforced by:` annotation naming the mechanism that checks it.

## Fields

| Field | Description |
|---|---|
| `rule_id` | Unique identifier combining layer prefix and number (e.g. `ID-1`) |
| `name` | Short descriptive name for the rule |
| `description` | Full prose statement of what the rule requires |
| `enforced_by` | Mechanism or tool that checks compliance with this rule |

## Usage Examples

_See each layer section above for concrete rule definitions._
