# Socratic Interrogation: Replacing Raw Node Count with a Redundancy Heuristic

**Input Artifact:** Proposal to remove the strict node/edge count penalty in the `wiki-compiler energy` calculation to encourage highly granular atomization and "multidimensional styling," replacing it with a direct measurement of redundancy and contradiction.

## Open Questions

### 1. Missing Constraint
**Claim:** We should stop penalizing raw node and edge counts to encourage minimal, highly atomic composition.
**Question:** If we remove the structural cost of $1.0$ per node and $0.2$ per edge, what prevents the system from generating millions of 1-line files? While they might be orthogonal, infinite micro-files introduce high filesystem overhead and latency. What is the new counter-balancing constraint to prevent extreme fragmentation?
**Resolution:** We must define a "Boilerplate-to-Truth" ratio constraint. A node must contain enough semantic density to justify the overhead of its Pydantic `KnowledgeNode` schema and file headers.

### 2. Unstated Assumption
**Claim:** We can find another way to measure redundancy directly instead of using node count as a proxy.
**Question:** This assumes we have a deterministic, low-energy way to calculate semantic overlap across the entire repository during every build. How exactly do we mathematically measure this redundancy without relying on expensive LLM calls or slow vector embeddings (which we rejected)?
**Resolution:** We need to design a deterministic NLP heuristic (e.g., Jaccard similarity between `SemanticFacet.intent` fields or AST structural hashing) that can run offline in $<1$ second during the `wiki-compiler energy` calculation.

### 3. Contradiction
**Claim:** We want to query only relevant sections and dynamically compose them.
**Question:** As noted previously, dynamic query-time composition contradicts **ID-6 (Traceable Causality)** and **WK-3 (Composition over Duplication)** which demand explicit, static transclusions (`![[node]]`). If we atomize heavily, do we abandon static indices for dynamic composite nodes?
**Resolution:** We must retain static indices. The "composition mechanism" must be a static compiler step (like `wiki-compiler compose`) that physically writes the composite Transclusion nodes to disk, rather than hallucinating them at query time.

### 4. Ownership Gap
**Claim:** We need to update the self-docs to make it clear that the goal is maximum knowledge in minimum physical space without duplication, not just a low file count.
**Question:** Who updates the `calculate_systemic_energy` function in `src/wiki_compiler/energy.py` once the new redundancy math is finalized?
**Resolution:** The docs will be updated immediately to clarify the philosophy, but the Python implementation of the new redundancy heuristic will be spun out into a dedicated `plan_docs/issues/unimplemented/` issue so an agent can tackle the math carefully.
