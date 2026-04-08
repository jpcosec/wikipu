# Cleansing Protocol

**Explanation:** The graph has entry gates (TopologyProposal, FacetProposal) but no mechanism that runs in the other direction. Nodes accumulate without any structural self-correction. The cleansing protocol is the missing reverse pass: graph-wide anomaly detection producing `CleansingProposal` objects for human approval before any destructive or structural operation is applied.

**Reference:** `raw/cleansing_protocol.md`, `src/wiki_compiler/main.py`

**What to fix:**
1. Create `src/wiki_compiler/cleanser.py` with anomaly detectors per node type (code, doc, plan, test, config) and `CleansingProposal` + `CleansingReport` models.
2. Add a `cleanse` subcommand to `main.py` with detect and apply modes.
3. Create `tests/test_cleanser.py` with one test per anomaly type per node category.

**How to do it:**
- Anomaly types per node category are specified in `raw/cleansing_protocol.md`.
- Code nodes: duplicate IOFacet overlap, misplaced layer, split candidate (too many responsibilities in ASTFacet.signatures).
- Doc nodes: stale documents edge, duplicate abstracts, misplaced node_type, compound abstract (split candidate).
- Plan nodes: stale with no git activity and no code node connection.
- `CleansingProposal` should mirror `TopologyProposal` in structure — description, affected nodes, proposed action, requires human approval flag.
- `cleanse --detect` outputs a `CleansingReport` without modifying anything.
- `cleanse --apply` takes a report and applies approved proposals.

**Depends on:** none
