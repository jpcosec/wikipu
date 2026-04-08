# API Migration Plan & Implementation Gap Analysis
# dev → ui-redesign

**Date:** 2026-03-23
**Status:** Draft
**Scope:** Full merge of `dev` backend into `ui-redesign` frontend

---

## 1. API Surface Comparison

### 1.1 Structural Differences

| Dimension | `dev` branch (`/api/v1/`) | `ui-redesign` (`/api/v2/`) |
|---|---|---|
| **Versioning** | `/api/v1/` flat | `/api/v2/` with CQRS namespaces |
| **Pattern** | REST (mixed read/write) | CQRS: `/query/`, `/commands/`, `/system/` |
| **View naming** | `view1`, `view2`, `view3` | `views/{match\|extract\|documents}` |
| **Profile ownership** | under `/portfolio/` | under `/query/profile/` |
| **Artifact access** | `/stage/{stage}/outputs` | `/query/jobs/.../artifacts/{nodeName}` |
| **Pipeline execution** | none (CLI only) | `POST /commands/jobs/.../run` |
| **Gate decisions** | filesystem write | `POST /commands/jobs/.../gates/{gate}/decide` |
| **Scrape trigger** | none | `POST /commands/jobs/scrape` |
| **Archive / delete** | none | `POST .../archive`, `DELETE .../` |
| **Orchestration status** | none | `GET /system/orchestration/threads/.../` |
| **Scraper roadmap** | none | `GET /system/scrapers/roadmap` |
| **Neo4j sync** | bootstrap-schema only | `POST /system/neo4j/sync` |
| **Explorer save** | none | `PUT /commands/explorer/file` |

---

### 1.2 Endpoint-by-Endpoint Map

#### Queries — implemented in dev, need rename/restructure

| dev endpoint | ui-redesign expects | Gap |
|---|---|---|
| `GET /api/v1/portfolio/summary` | `GET /api/v2/query/portfolio/summary` | Path migration only |
| `GET /api/v1/portfolio/base-cv-graph` | `GET /api/v2/query/profile/base-cv-graph` | Path + namespace migration |
| `GET /api/v1/portfolio/cv-profile-graph` | `GET /api/v2/query/profile/cv-profile-graph` | Path + namespace migration |
| `PUT /api/v1/portfolio/cv-profile-graph` | `PUT /api/v2/commands/profile/cv-profile-graph` | Path + CQRS move |
| `GET /api/v1/jobs/{s}/{j}/timeline` | `GET /api/v2/query/jobs/{s}/{j}/timeline` | Path migration only |
| `GET /api/v1/jobs/{s}/{j}/view1` | `GET /api/v2/query/jobs/{s}/{j}/views/match` | Path + semantic rename |
| `GET /api/v1/jobs/{s}/{j}/view2` | `GET /api/v2/query/jobs/{s}/{j}/views/extract` | Path + semantic rename |
| `GET /api/v1/jobs/{s}/{j}/view3` | `GET /api/v2/query/jobs/{s}/{j}/views/documents` | Path + semantic rename |
| `GET /api/v1/jobs/{s}/{j}/stage/{stage}/outputs` | `GET /api/v2/query/jobs/{s}/{j}/artifacts/{nodeName}` | Path + response shape migration |
| `GET /api/v1/jobs/{s}/{j}/editor/{node}/state` | `GET /api/v2/query/jobs/{s}/{j}/editor/{node}/state` | Path migration only |
| `GET /api/v1/jobs/{s}/{j}/evidence-bank` | `GET /api/v2/query/jobs/{s}/{j}/evidence-bank` | Path migration only |
| `GET /api/v1/jobs/{s}/{j}/package/files` | `GET /api/v2/query/jobs/{s}/{j}/package/files` | Path migration only |
| `GET /api/v1/jobs/{s}/{j}/profile/summary` | `GET /api/v2/query/jobs/{s}/{j}/profile/summary` | Path migration only |
| `GET /api/v1/explorer/browse` | `GET /api/v2/query/explorer/browse` | Path migration only |

#### Commands — partially exist in dev, need implementation or exposure

| ui-redesign expects | dev status | Required work |
|---|---|---|
| `PUT /api/v2/commands/jobs/{s}/{j}/state/{node}` | exists as `PUT /api/v1/jobs/{s}/{j}/editor/{node}/state` | Path migration + CQRS move |
| `PUT /api/v2/commands/jobs/{s}/{j}/documents/{doc}` | exists as `PUT /api/v1/jobs/{s}/{j}/documents/{doc}` | Path migration |
| `POST /api/v2/commands/jobs/{s}/{j}/gates/{gate}/decide` | partial — `PUT /api/v1/jobs/{s}/{j}/review/match` | Generalise to `gates/{gate}` pattern |
| `POST /api/v2/commands/jobs/{s}/{j}/run` | **not exposed** — only via CLI | New endpoint: wrap `run_prep_match` logic |
| `POST /api/v2/commands/jobs/scrape` | **not exposed** — only via CLI | New endpoint: wrap scraper logic |
| `POST /api/v2/commands/jobs/{s}/{j}/archive` | **not implemented** | New endpoint |
| `DELETE /api/v2/commands/jobs/{s}/{j}` | **not implemented** | New endpoint |
| `PUT /api/v2/commands/explorer/file` | **not implemented** | New endpoint |

#### System — not in dev

| ui-redesign expects | dev status | Required work |
|---|---|---|
| `GET /api/v2/system/orchestration/threads/{s}/{j}` | **not implemented** | New endpoint: query LangGraph thread state |
| `GET /api/v2/system/orchestration/traces/{s}/{j}` | **not implemented** | New endpoint: LangSmith trace lookup |
| `GET /api/v2/system/scrapers/roadmap` | **not implemented** | New endpoint: list scraper adapters |
| `POST /api/v2/system/neo4j/sync` | **not implemented** | New endpoint: sync job to Neo4j |

---

### 1.3 Response Shape Mismatches

#### Views (critical)
The UI's discriminated union `ViewPayload` uses:
```ts
{ view: "match" | "extract" | "documents", source, job_id, data: {...} }
```
Dev's `view1`/`view2`/`view3` return bare objects without the `view` discriminator field.
**Fix:** All three view endpoints must wrap their response in `{ view: "...", source, job_id, data }`.

#### Artifacts
Dev: `GET /stage/{stage}/outputs` → `ArtifactListPayload` with stage-scoped file list.
UI: `GET /artifacts/{nodeName}` → same `ArtifactListPayload` shape.
**Fix:** Path rename + confirm `node_name` is passed through correctly.

#### GraphNode — `category` field
Dev's `build_view_one_payload()` (match graph) already includes `category` on nodes (from fixture data, confirmed).
The UI now uses this field for colour routing — this should work once paths are aligned.

---

## 2. Backend Migration Plan

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

## 3. Frontend Implementation Gap Analysis

### 3.1 Views Implemented vs Spec

| View | Route | Status | Missing |
|---|---|---|---|
| Portfolio Dashboard | `/` | ✅ Implemented | — |
| Data Explorer | `/explorer` | ✅ Implemented | Explorer file write (`PUT /commands/explorer/file`) wired up |
| Base CV Editor | `/cv` | ✅ Implemented | Save (`PUT /commands/profile/cv-profile-graph`) wired to mock only |
| Knowledge Graph | `/graph` | ✅ Implemented | — |
| Job Flow Inspector | `/jobs/:s/:j` | ✅ Implemented | Pipeline run/resume buttons call mock only |
| Scrape Diagnostics | `/jobs/:s/:j/scrape` | ✅ Implemented | Scrape trigger (`POST /commands/jobs/scrape`) mock only |
| Translate Diagnostics | `/jobs/:s/:j/translate` | ✅ Implemented | — |
| Extract & Understand | `/jobs/:s/:j/extract` | ✅ Implemented | Gate decide wired to mock only |
| Match | `/jobs/:s/:j/match` | ✅ Implemented | Gate decide wired to mock only |
| Application Context | `/jobs/:s/:j/context` | ❌ **Not implemented** | Entire view missing (spec: B3b) |
| Generate Documents | `/jobs/:s/:j/sculpt` | ✅ Implemented | Gate decide mock only; diff view not implemented |
| Package & Deployment | `/jobs/:s/:j/deployment` | ✅ Implemented | Archive command mock only |

### 3.2 API Hook Coverage

| Hook file | Endpoint called | Works with real API? |
|---|---|---|
| `usePortfolioSummary` | `query/portfolio/summary` | ❌ URL mismatch (v1 vs v2) |
| `useJobTimeline` | `query/jobs/.../timeline` | ❌ URL mismatch |
| `useViewExtract` | `query/jobs/.../views/extract` | ❌ view2 vs views/extract |
| `useViewMatch` | `query/jobs/.../views/match` | ❌ view1 vs views/match |
| `useGateDecide` | `commands/jobs/.../gates/.../decide` | ❌ not implemented in backend |
| `useEditorState` | `query/jobs/.../editor/.../state` | ❌ URL mismatch |
| `useCvProfileGraph` | `query/profile/cv-profile-graph` | ❌ portfolio vs profile |
| `useExplorerBrowse` | `query/explorer/browse` | ❌ URL mismatch |
| `useArtifacts` | `query/jobs/.../artifacts/{node}` | ❌ stage outputs vs artifacts |

All hooks work correctly with mock data. None work with the real `dev` backend until Phase M-1 is complete.

### 3.3 Missing UI Features (from spec docs)

From `docs/ui/ui_view_spec.md` (dev) and `docs/runtime/ui/views.md` (methodology):

#### Extract view gaps
- No difficulty rating per requirement
- No requirement category chip (technical / soft_skill / language)
- No confidence score display

#### Match view gaps
- No per-edge confidence bar
- No coverage summary header (X/Y requirements matched)
- No evidence bank sidebar linkage (panel exists but not wired to selection)

#### Generate Documents view gaps
- No diff view (proposed vs approved)
- No per-section sculpting controls
- No version history

#### Pipeline execution
- No real pipeline run/resume button wiring (all mock)
- No real-time status polling via `/system/orchestration/threads/`
- No error trace display via LangSmith

#### Application Context view (B3b)
- Entire view not implemented — spec exists at `plan/01_ui/specs/B3b_application_context.md`

---

## 4. Recommended Migration Order

```
M-1  Path migration (v1→v2, CQRS structure, view discriminators)   2h
M-2  Gate decision generalisation                                   3h
──── At this point: UI works end-to-end with real API for read + HITL ────
M-3  Pipeline execution commands (scrape, run)                      1d
M-4  System endpoints (orchestration, scrapers, Neo4j sync)         4h
M-5  Archive / delete / explorer write                              3h
──── Backend complete ────
F-1  Wire all frontend hooks to real API (remove mock paths)        3h
F-2  Implement Application Context view (B3b)                       1d
F-3  Real-time status polling + error trace display                 4h
F-4  Match coverage summary + evidence bank linkage                 3h
F-5  Extract difficulty/category/confidence chips                   2h
F-6  Generate Documents diff view                                   4h
──── Full parity with dev branch vision ────
```

---

## 5. Notes

- The `doc-methodology-2.0` worktree (`runtime/ui/api_contract.md`) is the **canonical spec** for the v2 API. All new backend endpoints should match it exactly.
- The mock client in `ui-redesign` is the source of truth for fixture data shapes. When wiring real endpoints, validate against mock response shape first.
- `GraphNode.category` is already populated in the dev branch fixtures and the `build_view_one_payload()` builder — no shape change needed there.
- The `view_extract` response from dev does **not** include `char_start`/`char_end`. The real backend will need to compute and return these (or the UI can compute them client-side from the source markdown — simpler for now).
