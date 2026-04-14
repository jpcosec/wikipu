---
identity:
  node_id: "doc:wiki/standards/facet_validator.md"
  node_type: "doc_standard"
edges:
  - target_id: "file:src/wiki_compiler/facet_validator.py"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/facet_validator.py:validate_facet_proposal"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/facet_validator.py:_tokenise"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/facet_validator.py:_jaccard"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/facet_validator.py:_find_question_collisions"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/facet_validator.py:_find_field_collisions"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/facet_validator.py:_check_attempted_query"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/facet_validator.py:_update_attempts"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/facet_validator.py:_build_suggestion"
    relation_type: documents
---

Provides logic for validating the orthogonality and uniqueness of proposed Knowledge Graph facets. This module ensures that new facets do not overlap with existing ones and that the information they provide is truly new.

## Rule Schema

```python
def validate_facet_proposal(
    proposal: FacetProposal,
    registry: FacetRegistry,
    graph: nx.DiGraph,
    state_path: Path,
) -> FacetOrthogonalityReport: ...
```

## Fields

- `FacetProposal.question`: The core question the facet answers.
- `FacetProposal.proposed_fields`: List of fields in the new facet.
- `FacetOrthogonalityReport.is_orthogonal`: Boolean indicating if the proposal is accepted.

## Usage Examples

```python
from wiki_compiler.facet_validator import validate_facet_proposal
from wiki_compiler.contracts import FacetProposal

proposal = FacetProposal(
    proposed_facet_name="performance",
    question="What are the performance characteristics of this node?",
    applies_to=["file", "code_construct"],
    proposed_fields=[{"name": "latency_ms", "type": "float"}]
)
# registry and graph are already loaded
report = validate_facet_proposal(proposal, registry, graph, Path(".facet_state.json"))
if report.is_orthogonal:
    print("Proposal accepted!")
else:
    print(f"Collision: {report.resolution_suggestion}")
```
