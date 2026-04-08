---
identity:
  node_id: "doc:wiki/drafts/key_components.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/core/README.md", relation_type: "documents"}
---

### Graph State

## Details

### Graph State

**File:** `src/core/graph/state.py`

```python
@dataclass
class GraphState:
    source: str              # Job source (e.g., "tu_berlin")
    job_id: str              # Unique job ID
    run_id: str              # Run identifier
    source_url: str          # Job posting URL
    current_node: str        # Current pipeline node
    status: str              # Job status
    review_decision: ReviewDecision  # approve/regenerate/reject
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

### Round Manager

**File:** `src/core/round_manager.py`

Manages the review regeneration cycle:
- Creates per-round artifact folders
- Tracks feedback history
- Handles evidence patching

### Scraping Facade

**File:** `src/core/scraping/service.py`

```
src/core/scraping/
├── service.py             # Main scraping service
├── registry.py           # Adapter registry
├── contracts.py          # Scraping contracts
├── adapters/             # Source-specific adapters
│   ├── base.py
│   ├── tu_berlin.py
│   └── stepstone.py
├── strategies/           # Extraction strategies
│   └── stepstone.py
├── policy/               # Fetch policies
├── fetch/                # HTTP fetching
├── extract/               # Content extraction
├── normalize/             # Normalization
└── persistence/          # Artifact storage
```

Key functions:
- `scrape_detail()` — Scrape a single job posting
- `crawl_listing()` — Discover job URLs from listing pages

### Text Processing

**File:** `src/core/text/span_resolver.py`

Deterministic span resolution for text matching:
- `resolve_span()` — Case-insensitive, whitespace-normalized matching
- Returns line numbers, character offsets, preview snippets

### Review Decision Service

**File:** `src/core/tools/review_decision_service.py`

Parses human review decisions:
- Validates checkbox markup
- Computes hash-based locks
- Enforces stale-hash protection

### Translation Service

**File:** `src/core/tools/translation/service.py`

- Chunked translation for long inputs
- Default chunk size: 4500 chars
- Handles `NotValidLength` errors gracefully

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/core/README.md`.