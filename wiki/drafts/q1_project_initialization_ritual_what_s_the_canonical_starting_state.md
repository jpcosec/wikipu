---
identity:
  node_id: "doc:wiki/drafts/q1_project_initialization_ritual_what_s_the_canonical_starting_state.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/methodology_synthesis_addendum.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/methodology_synthesis_addendum.md"
  source_hash: "4084c2da6197485937ca035f86e9b26279ac1b2b99f034e9b01605dc9519f504"
  compiled_at: "2026-04-10T17:47:33.732472"
  compiled_from: "wiki-compiler"
---

The most complete answer is the 6-phase lifecycle from `entrypoint.md` (doc_methodology). It defines the Zero-Tolerance Policy: **no code change is valid unless it satisfies all 5 pillars.**

## Details

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

Generated from `raw/methodology_synthesis_addendum.md`.