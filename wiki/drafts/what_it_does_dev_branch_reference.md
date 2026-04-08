---
identity:
  node_id: "doc:wiki/drafts/what_it_does_dev_branch_reference.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/new_feature/extract_understand_node.md", relation_type: "documents"}
---

LLM-based structured extraction from raw job posting text. Takes `IngestedData.raw_text` (scraped+translated markdown) and produces `JobUnderstandingExtract`:

## Details

LLM-based structured extraction from raw job posting text. Takes `IngestedData.raw_text` (scraped+translated markdown) and produces `JobUnderstandingExtract`:

### Output contract (from dev `src/nodes/extract_understand/contract.py`)

```python
JobUnderstandingExtract:
  job_title: str
  analysis_notes: str                    # extraction rationale
  requirements: list[JobRequirement]
    - id: str                            # e.g. "REQ_001"
    - text: str                          # human-readable requirement
    - priority: "must" | "nice"
    - text_span: TextSpan                # source location in raw_text
  constraints: list[JobConstraint]
    - constraint_type: str
    - description: str
  risk_areas: list[str]
  contact_info: ContactInfo              # primary detected contact
  contact_infos: list[ContactInfo]       # all detected contacts
  salary_grade: str | None               # e.g. "TV-L E13"
```

### Deterministic post-processing

After LLM extraction, the node runs:
- Email detection via regex
- Name detection via regex (PhD titles, normal names)
- Text span resolution (line/offset locations for requirements)
- Contact merging (dedup LLM contacts with regex-detected ones)
- Salary grade detection via regex (E12, TV-L E15, etc.)

### What the refactored branch needs

When porting, rewrite as a native LangChain `with_structured_output()` call. The dev branch uses a custom LLM wrapper — replace with the same pattern used in `match_skill/graph.py`. Keep the deterministic post-processing as-is.

Generated from `raw/docs_postulador_refactor/future_docs/new_feature/extract_understand_node.md`.