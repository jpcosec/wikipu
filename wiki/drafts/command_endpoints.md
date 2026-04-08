---
identity:
  node_id: "doc:wiki/drafts/command_endpoints.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/api_contract.md", relation_type: "documents"}
---

### State Updates

## Details

### State Updates

#### `PUT /commands/jobs/:source/:job_id/state/:node_name`

Save node state (extract, match, etc.).

**Request:**
```ts
// For extract
{ requirements: RequirementItem[] }

// For match
{ nodes: GraphNode[]; edges: GraphEdge[] }
```

**Response:**
```ts
interface CommandResponse {
  success: boolean;
  message?: string;
}
```

---

#### `PUT /commands/jobs/:source/:job_id/documents/:doc_key`

Save document content.

**Request:**
```ts
interface SaveDocumentPayload {
  markdown: string;
}
```

**doc_key:** `cv` | `motivation_letter` | `application_email`

---

### Gate Decisions

#### `POST /commands/jobs/:source/:job_id/gates/:gate/decide`

Make a decision at a HITL gate.

**Request:**
```ts
interface GateDecisionPayload {
  decision: GateDecision;
  feedback?: string[];
}

type GateDecision = "approve" | "request_regeneration" | "reject";
```

**gate:** `review_match`

---

### Pipeline Execution

#### `POST /commands/jobs/:source/:job_id/run`

Resume or start pipeline execution.

**Request:**
```ts
interface RunPipelinePayload {
  target_node?: string;
  resume_from_hitl?: boolean;
}
```

**Response:**
```ts
interface RunResponse {
  run_id: string;
  status: "accepted";
}
```

---

### Archive

#### `POST /commands/jobs/:source/:job_id/archive`

Mark job as deployed and optionally compress.

**Request:**
```ts
interface ArchiveJobPayload {
  compress_to_minio: boolean;
}
```

---

### Scrape (Future)

#### `POST /commands/jobs/scrape`

Initiate a new scrape job.

**Request:**
```ts
interface ScrapeJobPayload {
  url: string;
  source: string;
  adapter?: string;
}
```

**Status:** Not implemented — UI shows setup form but uses mock data.

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/api_contract.md`.