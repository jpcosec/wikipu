---
identity:
  node_id: doc:wiki/concepts/the_facetproposal_gate.md
  node_type: concept
edges:
- target_id: raw:raw/facet_orthogonalization.md
  relation_type: documents
compliance:
  status: implemented
  failing_standards: []
source:
  source_path: raw/facet_orthogonalization.md
  source_hash: 09c124cfbbf2a74ec7fb10ea1638c9348b6707bf3430cdba774567b11f3bac27
  compiled_at: '2026-04-14T16:50:28.659161'
  compiled_from: wiki-compiler
---

Before any new facet is registered, a FacetProposal must pass three checks:

## Definition

Before any new facet is registered, a FacetProposal must pass three checks:.

## Examples

- Implementation of this concept within the Wikipu workflow.
- Application of these principles in current documentation.

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

Before any new facet is registered, a FacetProposal must pass three checks:

### Check 1: Question collision
Tokenise the proposed question and compare via Jaccard similarity against all existing
facet questions. Threshold: 0.3. Above it → the proposed question overlaps an existing one.
Resolution: add a field to the existing facet, or sharpen the proposed question.

### Check 2: Field name collision
Check all proposed field names against every field in every registered facet.
A collision means the data point already exists somewhere in the graph.
Resolution: rename the field, or use the existing facet's field directly.

### Check 3: Compound answerability
The proposer must submit their best StructuredQuery attempt to answer the question
using only existing facets. If the query returns results, the information already exists.
Resolution: use the StructuredQuery — it IS the answer, no new facet needed.

If all three checks pass → the facet is genuinely new. Register it.
If any check fails → the axes aren't orthogonal. 3 attempts, then human review.

Generated from `raw/facet_orthogonalization.md`.
