---
identity:
  node_id: "doc:wiki/faq.md"
  node_type: "faq"
edges:
  - {target_id: "doc:wiki/standards/00_house_rules.md", relation_type: "references"}
  - {target_id: "doc:wiki/how_it_works.md", relation_type: "references"}
compliance:
  status: "implemented"
  failing_standards: []
---

This FAQ answers the questions that agents and developers most commonly hit when first working with Wikipu — covering zone semantics, approval gates, topology rules, and the methodology principles that underpin the system. Read it top to bottom on first contact; jump to a specific question when you need a quick check.

**Q:** Why a knowledge graph instead of just a file tree?
**A:** A file tree encodes location but not meaning — you cannot ask it "what depends on this node?" or "does this proposed module duplicate anything?" The graph gives every node typed relationships, so both humans and agents can navigate by intent and enforce structural rules (ID-1 Orthogonality, ID-2 Minimal Energy) before touching code. Without it, redundancy and drift are only caught after the damage is done. `see_also:` [[doc:wiki/how_it_works.md]]

**Q:** What is the difference between `wiki/` and `desk/`?
**A:** `wiki/` is current truth — it contains only implemented, curated knowledge and may never reference active work. `desk/` is the operational surface — it holds boards, issues, gates, proposals, and Socratic sessions that are live and mutable. Items in `desk/` are deleted when resolved; their history survives only in git and `changelog.md`. `wiki/` may not link to `desk/`; `desk/` references `wiki/` through the graph, not through direct Markdown links. `see_also:` [[ID-4]], [[WK-5]]

**Q:** What is the difference between `wiki/` and `raw/`?
**A:** `raw/` is immutable seed material — external project docs, research, and ore that agents read but never write. `wiki/` is the curated, compiled output: nodes have frontmatter, typed edges, and compliance status, and they are kept in sync with code reality. Agents promote knowledge from `raw/` into `wiki/` through the ingest and build pipeline; they never write back into `raw/`. `see_also:` [[ID-4]]

**Q:** When does an action require human approval?
**A:** Human approval is required only when an action's effects cross the topology boundary — touching external codebases, external services, published artifacts, or shared infrastructure. Any in-topology operation that is reversible via `git revert` does not require a gate. A proposal sets `requires_human_approval: true` when its effects cannot be fully undone by a git revert, or when they propagate outside the topology. Note: until the boundary-checking logic in `cleanse --apply` is implemented, all cleansing proposals conservatively require human approval. `see_also:` [[ID-5]]

**Q:** What counts as "inside the topology"?
**A:** Inside the topology means within the boundaries of the Wikipu repository itself — `wiki/`, `desk/`, `raw/`, `backlog/`, source code, and tests that all live under the single git repo. Any change that stays within this boundary is reversible by git and can proceed without a human gate. Anything that writes to an external codebase, publishes an artifact, or calls an external service is outside the topology and requires explicit approval. `see_also:` [[ID-5]]

**Q:** Why was `00_INDEX_MOC.md` renamed to `Index.md`?
**A:** "MOC" (Map of Content) was an Obsidian-specific term with no meaning outside that tool, and the `00_` prefix was a sorting hack rather than a semantic signal. The canonical entry point for any `wiki/` domain is now simply `Index.md` — a navigational artifact listing nodes and their relationships. The `desk/` equivalent is `Board.md`. Both names are meaningful and tool-agnostic. `see_also:` [[NAV-4]]

**Q:** When should I commit?
**A:** Commit exactly once per atomic unit of resolved work: one issue closed, one coherent structural change, or a session-end trail collect. A commit is a claim that the system is valid at the granularity of one logical unit — a half-written node or an incomplete refactor does not qualify. Branches follow the same boundary: one issue or one coherent phase per branch, merged back to `main` only when the work set is complete, tests pass, and `changelog.md` is updated. `see_also:` [[OP-7]]

**Q:** What does autopoiesis mean here, practically?
**A:** Autopoiesis means the system feeds its own current state back into itself as raw ore — `wiki/` content, `00_house_rules.md`, and agent protocols are all inputs to the next generation of the system, not just its outputs. In practice: after a significant phase, tag the repo, re-seed `raw/` with the current system's own documentation, run `wiki-compiler ingest` and `build`, and revise the house rules to reflect what friction the cycle revealed. The eight steps are defined in OP-8. `see_also:` [[OP-8]], [[doc:wiki/how_to/use_autopoiesis.md]]

**Q:** How do I know if a node is current truth vs. planned?
**A:** Check the node's `compliance.status` field in frontmatter. `implemented` means code and docs match reality right now. `planned` or `scaffolding` means it describes something not yet fully built. Nodes in `desk/issues/` or `desk/proposals/` are active work; nodes in `backlog/` are deferred. Historical decisions live in ADR nodes with `adr.status: "superseded"`. Never trust a node's prose content alone — the status field is the authoritative signal. `see_also:` [[NAV-2]], [[WK-5]]

**Q:** What do I do if a rule in the hausordnung causes friction?
**A:** Encode the friction before the session closes — do not silently work around it. MA-6 (The Methodology Improves Itself) requires that every logical error or contradiction in the rules discovered during a session is resolved in that session. If a rule is wrong, revise it in `wiki/standards/00_house_rules.md`, record the change in `changelog.md`, and commit. Leaving a friction-causing rule intact after discovering it is itself a violation. `see_also:` [[MA-6]]

**Q:** What is the Socratic methodology and why does this system use it?
**A:** The Socratic method here is a structured pre-design interrogation that generates typed questions — missing constraints, unstated assumptions, contradictions, undefined edge cases, scope creep signals, and ownership gaps — before any implementation begins. The system uses it because plans that feel complete often contain contradictions or ownership gaps that only surface as failures mid-implementation; the Socratic session forces resolution upfront. A plan may not move from `desk/socratic/` to `desk/issues/` while any question remains open. `see_also:` [[doc:wiki/how_to/use_socratic_methodology.md]]

**Q:** How do I add a new module without breaking the topology?
**A:** Author a `TopologyProposal` in `desk/proposals/` before writing any code. The proposal is evaluated by `wiki-compiler` for orthogonality against the existing graph — if it returns a `CollisionReport`, revise until there are no collisions (maximum three attempts before human escalation). Once approved, scaffold with `wiki-compiler scaffold --module src/<name>` to create `contracts.py`, `__init__.py`, and `README.md`, then implement following CS-1 through CS-9. Delete the proposal and update `changelog.md` on completion. `see_also:` [[ID-1]], [[ID-6]], [[doc:wiki/how_to/design.md]]
