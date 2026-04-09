---
identity:
  node_id: "doc:wiki/standards/00_house_rules.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/concepts/wiki_construction_principles.md", relation_type: "contains"}
  - {target_id: "doc:wiki/knowledge_node_facets.md", relation_type: "contains"}
  - {target_id: "doc:agents/librarian/intro.md", relation_type: "contains"}
compliance:
  status: "implemented"
  failing_standards: []
---

The canonical identity rules for the Wikipu ecosystem. This document defines what this system *is* — the invariant network of constraints that must hold regardless of what content the system contains. Rules are organized by layer. Each rule carries a `rule_id` for machine reference, a description, and the enforcement mechanism that checks it.

This document evolves through autopoietic cycles. Each cycle may refine, promote, or retire rules. The version is tracked by git tag. A rule that causes consistent friction should be rewritten before the session that discovered the friction closes.

---

## Layer 1 — Identity Rules
*The invariants that define the system. Violating these means the system is no longer itself.*

**ID-1 — Orthogonality**
No two elements do the same thing. Before any new module, node, or facet is created, it must prove it does not duplicate or overlap with an existing one. Redundancy is a structural error, not a style preference.
`Enforced by:` TopologyProposal validation, FacetProposal orthogonality check.

**ID-2 — Minimal Energy**
When multiple valid responses to a perturbation exist, choose the one that minimizes: LLM token consumption, structural complexity added to the graph, uncertainty in the resulting state, and number of new elements created — while fully satisfying the requirement. Extend existing nodes before creating new ones.
`Enforced by:` Autopoiesis loop coordinator pre-proposal check; graph query for overlapping intent before any TopologyProposal is submitted.

**ID-3 — Typed Contracts at Every Boundary**
All data crossing a process boundary must be a typed Pydantic model. No untyped dicts, no raw strings as data carriers, no implicit schemas. The contract IS the documentation. `Field(description=...)` is mandatory on every field — LLMs read it.
`Enforced by:` ASTFacet scanning detects untyped cross-module calls; audit checks for missing Field descriptions.

**ID-4 — Zone Separation**
The four information zones are inviolable:
- `raw/` — immutable seed. Agents read, never write.
- `wiki/` — current truth. Curated, governed, never contaminated by plan references.
- `desk/` — active operational state. Ephemeral — items deleted when resolved.
- `backlog/` — deferred ideas. Low-churn, reviewed periodically.
No zone may reference or write into a zone above it in the chain: `desk/` may reference `wiki/`; `wiki/` may not reference `desk/`.
`Enforced by:` build_wiki() checks frontmatter edges for cross-zone violations; CI scan on commit.

**ID-5 — Human Gate for Structural Changes**
The system may detect, propose, and prepare — it may not unilaterally restructure, delete, or rename elements. Any proposal with `requires_human_approval: true` requires explicit per-proposal sign-off before `--apply`. No implicit batch approvals.
`Enforced by:` cleanse --apply rejects unapproved proposals; autopoiesis coordinator pauses at desk/Gates.md.

**ID-6 — Traceable Causality**
Every element's existence must trace to a perturbation that created it. No orphan nodes, no files without a known origin. New modules require a TopologyProposal. New wiki nodes require a source (raw/, code scan, or explicit authorship). Changelog records every significant change.
`Enforced by:` Audit check for nodes with no edges and no source; changelog enforcement on commit.

**ID-7 — Self-Inclusion**
The system's own processes (CLI commands, agent protocols, the hausordnung itself) are nodes in the graph they govern. A system that cannot model itself cannot maintain itself.
`Enforced by:` wiki/reference/cli/ nodes must exist for each CLI command; build audit checks for missing self-nodes.

---

## Layer 2 — Methodology Axioms
*How work is done. Distilled from cross-project analysis of six production systems.*

**MA-1 — Separation is Non-Negotiable**
Deterministic logic, AI logic, persistence, and presentation are always separate layers. A unit that does two things is wrong by definition. This generates: contracts.py / storage separation, CLI-first architecture, pure domain core, layer ownership rules.

**MA-2 — Contracts Define All Boundaries**
Every interface — between modules, between human and agent, between current and future state — is a typed schema. The schema IS the documentation. Descriptions must be accurate because LLMs read them. This generates: Pydantic everywhere, Field(description=...) required, contracts as the only inter-module API, docstrings as specifications.

**MA-3 — Plans Are Ephemeral. Code and Changelog Are Permanent.**
A plan that survives its own completion is drift. Done = plan deleted, code changed, changelog updated. History lives in git and changelog only. There is no archive state. This generates: the desk/issues lifecycle, the 6-month stale rule on backlog, the prohibition on archive folders.

**MA-4 — Agents Operate Within Explicit, Bounded Permission Frames**
At every moment, an agent's scope is known: what it can create, what it can modify, what it cannot touch. Mode determines scope. Four modes:
- `design` — may write desk/proposals/ only. No code, no wiki/runtime.
- `implement` — may write code and promote wiki nodes. Deletes the plan on completion.
- `sync` — may overwrite wiki/ nodes to match code reality. No new code.
- `hotfix` — may fix code and update docs. Doc update is mandatory, not optional.
`Enforced by:` agent system prompts; Librarian intro.md protocol.

**MA-5 — Verification Is Inline, Not Deferred**
A step that cannot be verified in isolation is a design problem. Tests run at each slice, not at the end. Each slice leaves the codebase in a valid state. No step is done until its test passes.
`Enforced by:` pre-push hook; issue resolution protocol requires tests before changelog update.

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
- Current truth: `compliance.status = "implemented"`, no `desk/` prefix
- Planned: node in `desk/issues/` or `desk/proposals/`
- Deferred: node in `backlog/`
- Historical: ADR node with `adr.status = "superseded"`

**NAV-3 — Read the Graph First, Markdown Second**
Agents do not read dozens of Markdown files sequentially. They query the graph for structure and relationships, then read individual Markdown files only when human-readable prose or ADR history is needed. `raw/` is never written to by agents.

**NAV-4 — MOCs as Deterministic Entry Points**
Every domain has a `00_INDEX_MOC.md` or `Board.md` as its canonical entry point. Agents start there, not from a directory listing. Humans use the same entry points.

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
When an issue is resolved:
1. Check whether any existing test is no longer valid — delete it if needed.
2. Add new tests for the new behaviour.
3. Run the relevant tests — all must pass.
4. Update `changelog.md`.
5. Delete the issue file AND remove it from `Board.md`.
6. Commit with a message that names what was fixed.

**OP-5 — The Autopoietic Cycle**
Periodically (at minimum after each significant development phase):
1. `git tag v<n>` — snapshot the current state.
2. Clear processed ore from `raw/` (external project docs, obsolete seeds).
3. Evaluate: what is redundant, lacking, or upgradeable in the current system.
4. Research new sources if needed (papers, analogous systems, internet).
5. Put the current system's state (including this hausordnung) back into `raw/` as ore.
6. Run `wiki-compiler ingest` + `build` to regenerate the seed wiki.
7. Write a new version of the hausordnung incorporating what the cycle revealed.
8. Commit.

---

## Layer 5 — Code Style
*The assumed conventions made explicit. These apply to all Python source in `src/`.*

**CS-1** — `from __future__ import annotations` at the top of every module.
**CS-2** — Every module has a one-paragraph docstring: executive summary of the module's role.
**CS-3** — Every public class, method, and function has a structured docstring.
**CS-4** — `contracts.py` / Pydantic models are the only legitimate way to pass data between modules.
**CS-5** — `Field(description=...)` on every Pydantic field. Descriptions must be semantic and accurate — they are read by LLMs.
**CS-6** — Domain-specific exceptions defined at the top of the relevant file. Never bare `Exception` for flow control.
**CS-7** — Never swallow errors silently. Log with context, re-raise with `from e`.
**CS-8** — Comments only for non-obvious invariants or workflow decisions. No narrative comments restating what the code does.
**CS-9** — `changelog.md` updated on every significant change.
**CS-10** — Functions that use too many local variables are probably classes. Code should be self-explanatory. Avoid long functions — use helpers to simplify reading.

`Enforced by:` docstring-coverage audit; ruff linting; ASTFacet scanning.

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
Each `node_type` has a required section structure:
- `concept`: Abstract → Definition → Examples → Related Concepts
- `doc_standard`: Abstract → Rule/Schema → Fields → Usage Examples
- `how_to`: Abstract → Prerequisites → Steps → Verification

**WK-5 — Current Truth Separation**
`wiki/` contains only current state. It never references `desk/` (active work) or `backlog/` (deferred). If a node describes something planned but not yet implemented, its `compliance.status` must reflect that (`planned` or `scaffolding`). A node with `status: "implemented"` is a claim that the code and docs match reality.

**WK-6 — Reference Docs Are Derived**
`wiki/reference/` nodes are generated from or kept in sync with source code. They document what exists, not what is planned. If the source changes, the reference doc must be updated in the same commit.

---

## Violation Examples

- Writing agent output back into `raw/`.
- Creating a module by hand without a validated TopologyProposal.
- Storing graph-only edits that disappear on the next `build`.
- Marking a node `status: "implemented"` when the code does not exist.
- Promoting a draft that duplicates an existing wiki concept.
- Applying a cleansing proposal without explicit per-proposal approval.
- Leaving a gate open in `desk/Gates.md` with no activity for more than one cycle.
- Closing an issue without updating tests and changelog.
- A rule in this document causing consistent friction and surviving the session that discovered it.
