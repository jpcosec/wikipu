---
identity:
  node_id: "doc:wiki/drafts/1_api_surface_comparison.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/02_migration/api_migration_and_gap_analysis.md", relation_type: "documents"}
---

### 1.1 Structural Differences

## Details

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

Generated from `raw/docs_postulador_ui/plan/02_migration/api_migration_and_gap_analysis.md`.