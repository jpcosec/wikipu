---
identity:
  node_id: "doc:wiki/drafts/query_endpoints.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/api_contract.md", relation_type: "documents"}
---

### Portfolio

## Details

### Portfolio

#### `GET /query/portfolio/summary`

Returns portfolio overview with job counts and list.

**Response:**
```ts
interface PortfolioSummary {
  totals: {
    jobs: number;
    completed: number;
    pending_hitl: number;
    running: number;
    failed: number;
    archived: number;
  };
  jobs: JobListItem[];
}

interface JobListItem {
  source: string;
  job_id: string;
  thread_id: string;
  current_node: string;
  status: JobStatus;
  updated_at: string;
}

type JobStatus = "running" | "pending_hitl" | "completed" | "failed" | "archived";
```

---

### Job Timeline

#### `GET /query/jobs/:source/:job_id/timeline`

Returns job status and all pipeline stage information.

**Response:**
```ts
interface JobTimeline {
  source: string;
  job_id: string;
  thread_id: string;
  current_node: string;
  status: JobStatus;
  stages: StageItem[];
  artifacts: Record<string, string>;
  updated_at: string;
}

interface StageItem {
  name: string;
  status: StageStatus;
  artifact_ref: string | null;
  updated_at: string;
}

type StageStatus = "pending" | "running" | "needs_review" | "approved" | "error";
```

---

### Views (Discriminated Union)

#### `GET /query/jobs/:source/:job_id/views/:view`

Returns view-specific data for extract, match, or documents.

**Views:**
- `extract` → `ExtractViewPayload`
- `match` → `MatchViewPayload`
- `documents` → `DocumentsViewPayload`

**Extract View:**
```ts
interface ExtractViewPayload {
  view: "extract";
  source: string;
  job_id: string;
  data: {
    source_markdown: string;
    requirements: RequirementItem[];
  };
}

interface RequirementItem {
  id: string;
  text: string;
  priority: string;  // "must" | "nice"
  spans: TextSpanItem[];
  text_span: RequirementTextSpan | null;
  char_start?: number | null;
  char_end?: number | null;
  notes?: string;
}

interface TextSpanItem {
  requirement_id: string;
  start_line: number;
  end_line: number;
  text_preview: string;
}

interface RequirementTextSpan {
  start_line: number | null;
  end_line: number | null;
  start_offset: number | null;
  end_offset: number | null;
  preview_snippet: string | null;
}
```

**Match View:**
```ts
interface MatchViewPayload {
  view: "match";
  source: string;
  job_id: string;
  data: {
    nodes: GraphNode[];
    edges: GraphEdge[];
  };
}

interface GraphNode {
  id: string;
  label: string;
  kind: string;  // "requirement" | "profile"
  score?: number;
  priority?: string;
}

interface GraphEdge {
  source: string;
  target: string;
  label: string;
  score: number | null;
  reasoning: string | null;
  evidence_id: string | null;
}
```

**Documents View:**
```ts
interface DocumentsViewPayload {
  view: "documents";
  source: string;
  job_id: string;
  data: {
    documents: {
      cv: string;
      motivation_letter: string;
      application_email: string;
    };
    nodes: GraphNode[];
    edges: GraphEdge[];
  };
}
```

---

### Artifacts

#### `GET /query/jobs/:source/:job_id/artifacts/:node_name`

Returns artifact files for a specific pipeline node.

**Response:**
```ts
interface ArtifactListPayload {
  source: string;
  job_id: string;
  node_name: string;
  files: ArtifactFile[];
}

interface ArtifactFile {
  path: string;
  content_type: ArtifactContentType;
  content: string;
  editable: boolean;
}

type ArtifactContentType = "json" | "markdown" | "text" | "image" | "binary" | "too_large";
```

---

### Evidence Bank

#### `GET /query/jobs/:source/:job_id/evidence-bank`

Returns evidence items available for matching.

**Response:**
```ts
interface EvidenceBankPayload {
  source: string;
  job_id: string;
  items: EvidenceItem[];
}

interface EvidenceItem {
  id: string;
  title: string;
  category: string;
  tags: string[];
  summary: string;
  source_path: string;
}
```

---

### CV Profile

#### `GET /query/portfolio/cv-profile-graph`

Returns the complete CV profile as a graph structure.

**Response:**
```ts
interface CvProfileGraphPayload {
  profile_id: string;
  snapshot_version: string;
  captured_on: string;
  entries: CvEntry[];
  skills: CvSkill[];
  demonstrates: CvDemonstratesEdge[];
}

interface CvEntry {
  id: string;
  category: string;  // "experience" | "education" | "publication" | "language"
  essential: boolean;
  fields: Record<string, unknown>;
  descriptions: CvDescription[];
}

interface CvDescription {
  key: string;
  text: string;
  weight: "headline" | "primary_detail" | "supporting_detail" | "footnote";
}

interface CvSkill {
  id: string;
  label: string;
  category: string;
  essential: boolean;
  level: string | null;
  meta: Record<string, unknown>;
}

interface CvDemonstratesEdge {
  id: string;
  source: string;  // entry ID
  target: string;  // skill ID
  description_keys: string[];
}
```

---

### Explorer

#### `GET /query/explorer/browse?path=<path>`

Returns directory listing or file content.

**Response:**
```ts
interface ExplorerPayload {
  path: string;
  is_dir: boolean;
  entries?: ExplorerEntry[];      // if directory
  name?: string;
  extension?: string;
  size_bytes?: number;
  content_type?: "text" | "image" | "binary" | "too_large";
  content?: string | null;       // if file
}

interface ExplorerEntry {
  name: string;
  path: string;
  is_dir: boolean;
  size_bytes?: number;
  extension?: string;
  child_count?: number;
}
```

---

### Package

#### `GET /query/jobs/:source/:job_id/package/files`

Returns package files ready for download.

**Response:**
```ts
interface PackageFilesPayload {
  source: string;
  job_id: string;
  files: PackageFile[];
}

interface PackageFile {
  name: string;
  path: string;
  size_kb: number;
}
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/api_contract.md`.