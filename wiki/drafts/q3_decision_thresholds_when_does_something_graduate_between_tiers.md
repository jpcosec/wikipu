---
identity:
  node_id: "doc:wiki/drafts/q3_decision_thresholds_when_does_something_graduate_between_tiers.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/methodology_synthesis_addendum.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/methodology_synthesis_addendum.md"
  source_hash: "4084c2da6197485937ca035f86e9b26279ac1b2b99f034e9b01605dc9519f504"
  compiled_at: "2026-04-10T17:47:33.732570"
  compiled_from: "wiki-compiler"
---

**future_docs → plan_docs (when to promote):**

## Details

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

Generated from `raw/methodology_synthesis_addendum.md`.