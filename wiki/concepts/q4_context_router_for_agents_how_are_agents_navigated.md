---
identity:
  node_id: "doc:wiki/concepts/q4_context_router_for_agents_how_are_agents_navigated.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/methodology_synthesis_addendum.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/methodology_synthesis_addendum.md"
  source_hash: "4084c2da6197485937ca035f86e9b26279ac1b2b99f034e9b01605dc9519f504"
  compiled_at: "2026-04-14T16:50:28.662712"
  compiled_from: "wiki-compiler"
---

**The core protocol (doc_methodology):**

## Details

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

Generated from `raw/methodology_synthesis_addendum.md`.