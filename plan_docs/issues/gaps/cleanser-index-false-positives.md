# Cleanser False Positives on Index Nodes

**Explanation:** `wiki-compiler cleanse --detect` proposes 51 `split` operations, all targeting `Index.md` nodes and other navigational artifacts. The `_compound_abstract_proposals` detector flags any `doc:` node whose abstract has more than one sentence and contains dual-purpose language. Index nodes are by design navigational: their abstracts list the domains they cover, which naturally reads as multi-topic. The detector has no exemption for `node_type: "index"` (or any other navigational type), so it fires on every index in the wiki. This makes `cleanse --detect` output noisy and unactionable — a real compound-abstract problem would be invisible among the false positives.

**Reference:** `src/wiki_compiler/cleanser.py` (`_compound_abstract_proposals`, `_has_dual_purpose_language`), `src/wiki_compiler/contracts.py` (`KnowledgeNode.identity.node_type`)

**What to fix:** Exempt navigational node types (`index`, `reference`) from the compound-abstract detector. These types are explicitly allowed multi-topic abstracts by the wiki construction principles.

**How to do it:**
1. In `_compound_abstract_proposals`, add a guard: skip nodes where `node.identity.node_type in {"index", "reference"}`.
2. Re-run `wiki-compiler cleanse --detect` and confirm the proposal count drops significantly and remaining proposals are plausible.
3. Add a unit test: a mock graph with one `index` node and one genuine compound `concept` node should produce exactly one proposal (for the concept), not two.

**Depends on:** `none`
