---
identity:
  node_id: "doc:wiki/drafts/2_backend_migration_plan.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/02_migration/api_migration_and_gap_analysis.md", relation_type: "documents"}
---

### Phase M-1: Path Migration (no logic change)

## Details

### Phase M-1: Path Migration (no logic change)
**Effort:** ~2h · **Risk:** Low · **Prerequisite:** none

1. Create new FastAPI router factory at `src/interfaces/api/v2/` with CQRS sub-routers
2. Mount all existing v1 handlers at v2 paths with renames:
   - `portfolio/summary` → stays
   - `portfolio/*-cv-graph` → `profile/*-cv-graph`
   - `jobs/{s}/{j}/view1` → `jobs/{s}/{j}/views/match`
   - `jobs/{s}/{j}/view2` → `jobs/{s}/{j}/views/extract`
   - `jobs/{s}/{j}/views/documents` → `jobs/{s}/{j}/views/documents`
   - `jobs/{s}/{j}/stage/{stage}/outputs` → `jobs/{s}/{j}/artifacts/{nodeName}`
   - All write endpoints → `/commands/` prefix
3. Add `view` discriminator field to all view responses
4. Keep `/api/v1/` alive (or not — UI mock switches between mock/real)

### Phase M-2: Gate Decision Generalisation
**Effort:** ~3h · **Risk:** Low-Medium

The current `PUT /api/v1/jobs/{s}/{j}/review/match` is hardcoded to match review.
The UI expects `POST /api/v2/commands/jobs/{s}/{j}/gates/{gate}/decide` for any gate.

1. Refactor the handler to accept `gate_name` from the URL
2. Route to the appropriate filesystem writer based on gate name
3. Support gates: `review_match`, `review_application_context`, `review_motivation_letter`, `review_cv`, `review_email`

### Phase M-3: Pipeline Execution Commands
**Effort:** ~1 day · **Risk:** Medium (threading, process management)

The UI needs `POST /commands/jobs/{s}/{j}/run` and `POST /commands/jobs/scrape` to trigger background LangGraph execution without blocking the HTTP response.

1. Introduce a `BackgroundRunner` (thread pool or `asyncio.create_task`) in the API
2. `POST .../run` → validate params, enqueue job, return `RunResponse { run_id, status: "accepted" }`
3. `POST .../scrape` → validate URL/source/adapter, enqueue scrape, return `RunResponse`
4. Store `run_id` → thread mapping so orchestration status can be polled
5. Handle concurrent runs (one active run per `thread_id` at a time)

### Phase M-4: System Endpoints
**Effort:** ~4h · **Risk:** Low-Medium

1. `GET /system/orchestration/threads/{s}/{j}` — query LangGraph SQLite checkpoint for thread status
2. `GET /system/orchestration/traces/{s}/{j}` — query LangSmith API (optional; return 404 if not configured)
3. `GET /system/scrapers/roadmap` — list adapters from scraper registry
4. `POST /system/neo4j/sync` — call existing Neo4j bootstrap and job data sync

### Phase M-5: Archive / Delete / Explorer Write
**Effort:** ~3h · **Risk:** Low

1. `POST /commands/jobs/{s}/{j}/archive` — move job data to archive folder or compress to MinIO
2. `DELETE /commands/jobs/{s}/{j}` — delete job directory (with confirmation guard)
3. `PUT /commands/explorer/file` — write file content at arbitrary path (with path traversal protection)

---

Generated from `raw/docs_postulador_ui/plan/02_migration/api_migration_and_gap_analysis.md`.