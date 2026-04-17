---
identity:
  node_id: "doc:wiki/how_to/create_edge_relations.md"
  node_type: "how_to"
edges:
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "implements"}
  - {target_id: "doc:wiki/reference/knowledge_node_facets.md", relation_type: "extends"}
compliance:
  status: "implemented"
  failing_standards: []
---

The Edge Relation Creation protocol defines how a new "Faceted Edge" (indexed edge node relation) is evaluated for orthogonality, disambiguated by a Relation Creator agent, and structurally encoded into the knowledge graph and source code.

# How to Create a New Edge Relation (Faceted Edge)

Faceted edges are a subset of generic graph edges. While edges can relate nodes in many ways, faceted edges comply with a specific, strongly-typed semantic relation (e.g., `documents`, `implements`, `depends_on`). When a new semantic relation is needed, it must be carefully orthogonalized to prevent chaotic proliferation of overlapping verbs (like `clarifies` vs `explains`).

This protocol is executed by a specialized "Relation Creator" LLM agent instance whose sole mission is to disambiguate contradiction and manage subgraph conciliation.

## Prerequisites

- A proposed edge relation name (e.g., `clarifies`).
- Access to `src/wiki_compiler/contracts/__init__.py` where the `Edge.relation_type` Literal is defined.
- Access to `wiki/reference/knowledge_node_facets.md` where relations are documented.

## Steps

### 1. Disambiguation & Orthogonality Check
The Relation Creator agent evaluates the proposed relation against all existing relations in the `Literal` using a strict semantic boundary check. There are three possible outcomes:
- **A) Rejected:** The relation overlaps too heavily with an existing one. It is placed in the `exclusion/` zone.
- **B) Merged:** The relation is deemed a synonym of an existing one. It is merged, and existing edges are updated if necessary.
- **C) Escalated:** If there is no possible consensus, the relation proposal is placed in `desk/Gates.md` for human approval.

### 2. Subgraph Conciliation (Graph Migration)
If an existing relation is merged or deprecated in favor of the new one, the agent must execute a Subgraph Conciliation protocol. This requires executing a graph migration (via a CLI upgrade or script) to traverse the existing `knowledge_graph.json` and update all affected edges to the new relation type.

### 3. Atomic Synchronization
Once approved (or automatically disambiguated as novel and non-overlapping), the Relation Creator agent must synchronize the system in a single atomic commit:
1. **Update Contracts:** Add the new relation string to the `Edge.relation_type` Literal in `src/wiki_compiler/contracts/__init__.py`.
2. **Update Documentation:** Add the new relation and its meaning to the Edge relation types table in `wiki/reference/knowledge_node_facets.md`.
3. **Update Parsers:** If applicable, update `src/wiki_compiler/scanner.py` to correctly parse the new relation.
4. **Commit:** Ensure `wiki-compiler build` passes, then `git commit` to maintain temporal energy constraints.

## Verification

- [ ] The new relation is documented in `wiki/reference/knowledge_node_facets.md`.
- [ ] The `Literal` in `contracts.py` contains the exact new string.
- [ ] `wiki-compiler build` runs successfully without Pydantic validation errors on the new edges.
- [ ] Any merged or deprecated relations have been completely purged from existing nodes via Subgraph Conciliation.
