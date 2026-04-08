---
identity:
  node_id: "doc:wiki/drafts/graph_state.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/pipeline/README.md", relation_type: "documents"}
---

State is defined in `src/core/graph/state.py`:

## Details

State is defined in `src/core/graph/state.py`:

```python
@dataclass
class GraphState:
    source: str
    job_id: str
    run_id: str
    source_url: str
    current_node: str
    status: str
    review_decision: ReviewDecision
    pending_gate: Optional[str]
    error_state: Optional[str]
    artifact_refs: Dict[str, Any]
    # Transient payloads
    ingested_data: Optional[Dict]
    extracted_data: Optional[Dict]
    matched_data: Optional[Dict]
    my_profile_evidence: Optional[Dict]
    last_decision: Optional[Dict]
    active_feedback: Optional[Dict]
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/pipeline/README.md`.