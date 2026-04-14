# Socratic Interrogation: Facet Creation Protocol

**Input Artifact:** Proposal to create a "Facet Creation Protocol" that treats facets as "indexed edge nodes" (i.e., edge relations).

## Open Questions

### 1. Missing Constraint
**Claim:** We should have a facet creation protocol for edge relations.
**Question:** If we allow dynamic creation of new edge relations, what prevents the topology from becoming chaotic with redundant or overly-specific verbs (e.g., `clarifies`, `explains`, `details`)? Does our current `wiki-compiler propose-facet` tool (which uses 3 orthogonality checks) need to be upgraded to handle relations instead of just object metadata fields?
**Resolution:** Explicitly define the constraint on how new edge relations are evaluated for orthogonality against existing ones in `src/wiki_compiler/contracts.py`.

### 2. Unstated Assumption
**Claim:** "Remember that facet = indexed edge node"
**Question:** This assumes that edge relations and facets are fundamentally the same construct. Currently, our `Edge` schema (`relation_type`) is a `Literal` string, while Facets (like `ADRFacet`) are complex Pydantic models attached to nodes. Are we assuming we will refactor `contracts.py` so that edges themselves become addressable nodes (indexed edge nodes) that can carry facets, or are we just adding a new document on how to append a string to the `Literal`?
**Resolution:** Explicitly state whether this plan requires a graph ontology refactor (edges as nodes) or just a procedural checklist for updating the `Edge.relation_type` Literal.

### 3. Contradiction
**Claim:** Creating a new relation type protocol.
**Question:** OP-1 (Orthogonality) states that "No two elements do the same thing." If a user proposes `clarifies`, it strongly overlaps with the existing `documents` or `implements` relations. How does the protocol resolve semantic overlap between verbs without relying purely on subjective human judgment? 
**Resolution:** Define the exact mathematical or semantic boundary check for relations (e.g., Jaccard similarity of their definitions).

### 4. Undefined Edge Case
**Claim:** The protocol will allow relation alignment.
**Question:** What happens to existing nodes in the graph if we decide to merge or deprecate an old relation type (e.g., merging `clarifies` back into `documents`)? Does the protocol include a graph migration step?
**Resolution:** Add a requirement for a migration script or CLI command whenever a relation is aligned/merged.

### 5. Ownership Gap
**Claim:** Protocol for facet/relation creation.
**Question:** When a new relation is approved, there are at least three places to update: `contracts.py` (Literal type), `knowledge_node_facets.md` (documentation), and potentially the python parser (`scanner.py`). Who is responsible for synchronizing these?
**Resolution:** The protocol must enforce an atomic update to all three locations in a single commit, tracked by a checklist.
