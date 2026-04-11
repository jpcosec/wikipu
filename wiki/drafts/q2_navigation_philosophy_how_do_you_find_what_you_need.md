---
identity:
  node_id: "doc:wiki/drafts/q2_navigation_philosophy_how_do_you_find_what_you_need.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/methodology_synthesis_addendum.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/methodology_synthesis_addendum.md"
  source_hash: "4084c2da6197485937ca035f86e9b26279ac1b2b99f034e9b01605dc9519f504"
  compiled_at: "2026-04-10T17:47:33.732521"
  compiled_from: "wiki-compiler"
---

**The 4D matrix model (doc_methodology context router):**

## Details

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

Generated from `raw/methodology_synthesis_addendum.md`.