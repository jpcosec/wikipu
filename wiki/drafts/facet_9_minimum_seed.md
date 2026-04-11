---
identity:
  node_id: "doc:wiki/drafts/facet_9_minimum_seed.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/methodology_synthesis.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/methodology_synthesis.md"
  source_hash: "509baf32ca0ea70f59fdc2382e05095dde9fba07ad7092c46d49ecdca431bc34"
  compiled_at: "2026-04-10T17:47:33.732234"
  compiled_from: "wiki-compiler"
---

**Question:** What is the smallest set of rules that generates the rest?

## Details

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

Generated from `raw/methodology_synthesis.md`.