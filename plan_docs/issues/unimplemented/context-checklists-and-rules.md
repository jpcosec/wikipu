# Context Checklists And Rules

**Explanation:** Context bundles should tell an agent not only what nodes matter, but also which checklist and rules govern the operation. The runtime currently ignores `wiki/standards/checklists.md` and does not attach governing rule IDs.

**Reference:** `wiki/standards/checklists.md`, `wiki/standards/00_house_rules.md`, `src/wiki_compiler/context.py`

**What to fix:** Attach operation-aware verification checklists and governing rule IDs to context bundles.

**How to do it:**
1. Define operation-to-checklist mapping.
2. Parse checklist content into a structured bundle shape.
3. Add tests for each supported operation type.

**Depends on:** `plan_docs/issues/unimplemented/context-router-contract.md`
