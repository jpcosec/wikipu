# Verification Checklists

**Explanation:** The system has resolution protocols (OP-4, OP-5) but no machine-readable verification checklists that an agent can run through to confirm a unit of work is genuinely finished. Without checklists, "done" is subjective. An agent may close an issue without noticing a missing test, an un-updated reference doc, or a changelog gap.

**Reference:** `wiki/standards/00_house_rules.md` (OP-4, MA-5), `plan_docs/issues/Index.md` (working rule)

**What to fix:** Create `wiki/standards/checklists.md` as a catalogue of typed verification checklists — one per operation class. Each checklist is a numbered list of binary checks (pass/fail). An operation is done only when all checks pass.

**Checklists to define:**
- `issue-resolution` — the full OP-4 protocol as a checklist (tests valid?, tests added?, tests pass?, changelog updated?, issue file deleted?, committed?)
- `new-wiki-node` — node has frontmatter, abstract, required sections per node_type, edges registered in graph, compliance.status set correctly
- `new-module` — TopologyProposal approved, contracts.py defined, docstrings on all public symbols, tests added, wiki/reference node created, changelog updated
- `structural-change` — topology check passes, no orphan nodes, no cross-zone references, build passes, committed
- `session-close` — all open issues have a status, changelog reflects session work, uncommitted changes committed, trail collect done

**Each checklist entry carries:** a short description, the rule it enforces (rule_id), and the command or query that verifies it automatically where possible.

**Depends on:** none
