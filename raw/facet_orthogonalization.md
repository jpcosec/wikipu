# Facet Orthogonalization

## The Problem

Facets accumulate over time. Without a gate, you end up with:
- Redundant facets answering the same question from two angles
- Under-specified facets whose questions overlap partially
- Facets that could be expressed as compound queries over existing ones

This is the same problem as correlated variables in a dataset — the axes aren't independent.

## The PCA Analogy

In PCA you rotate correlated variables onto orthogonal principal components.
In the facet system you do the same: find the truly independent questions,
redefine the facets as those questions, rebuild.

The rebuild is free because facets are always derived from source truth (code, docs, git).
The graph is a cached view. Re-orthogonalization = redefine the lenses, re-run the build.

## Signals That Re-Orthogonalization Is Needed

1. **Co-occurrence** — two facets always appear together on the same nodes → may be one dimension
2. **Repeated compound queries** — the same filter combination keeps appearing → hidden dimension
3. **Overlapping audit checks** — two checks with different `related_facet` values detect the same problem

## The FacetProposal Gate

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

## Re-Orthogonalization Process

When drift is detected:

1. List all facet questions on the table
2. Find overlapping spaces (co-occurrence, repeated queries, check overlap)
3. Define new axes: independent questions that span the same information space
4. Test each new axis: can it be answered by combining existing ones? If yes, it's a query.
5. Redefine contracts.py, registry specs, and injectors
6. Run wiki-compiler build → graph rebuilds from source

No data migration. The codebase and docs are always the ground truth.
