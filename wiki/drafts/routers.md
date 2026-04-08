---
identity:
  node_id: "doc:wiki/drafts/routers.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/api/README.md", relation_type: "documents"}
---

### Health

## Details

### Health

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Service health check |
| GET | `/api/v1/neo4j/health` | Neo4j health check |

### Portfolio

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/portfolio/summary` | Job portfolio overview |

### Jobs

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/jobs/{source}/{job_id}/timeline` | Job status and pipeline stage info |
| GET | `/api/v1/jobs/{source}/{job_id}/review/match` | Match review surface |
| GET | `/api/v1/jobs/{source}/{job_id}/view1` | Match graph view |
| GET | `/api/v1/jobs/{source}/{job_id}/view2` | Extract requirements view |
| GET | `/api/v1/jobs/{source}/{job_id}/view3` | Generated documents view |

### Explorer

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/jobs/{source}/{job_id}/browse` | Browse job artifacts |
| GET | `/api/v1/explorer/browse?path=<path>` | Browse arbitrary paths |

### Documents

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/jobs/{source}/{job_id}/documents/<doc_key>` | Get document content |
| PUT | `/api/v1/jobs/{source}/{job_id}/documents/<doc_key>` | Save document edits |

### Review Decisions

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/jobs/{source}/{job_id}/review/match` | Get match review state |
| PUT | `/api/v1/jobs/{source}/{job_id}/review/match` | Submit match decision |

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/api/README.md`.