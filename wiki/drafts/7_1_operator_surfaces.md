---
identity:
  node_id: "doc:wiki/drafts/7_1_operator_surfaces.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/review_workbench_product_brief.md", relation_type: "documents"}
---

### A. Portfolio Page

## Details

### A. Portfolio Page

Route:

- `/`

Purpose:

- landing page for the review workbench
- overview of jobs and statuses
- quick access to workstreams and operator commands

What it currently shows:

1. high-level job counters
2. job tree / job list
3. review queue hint
4. links to sandbox workstreams
5. operator quick commands

UX role:

- command center / dashboard

Design need:

- it currently mixes product UI and developer dashboard concerns
- needs a clearer split between operator work and experimental tooling

### B. Job Workspace Page

Route:

- `/jobs/:source/:jobId`

Purpose:

- main per-job workspace
- timeline overview + stage switching + review entry point

What it currently shows:

1. breadcrumbs
2. job identity
3. current node / current stage
4. stage list with statuses
5. tabbed views
   - View 1 Graph Explorer
   - View 2 Document to Graph
   - View 3 Graph to Document
   - Pipeline Outputs
6. link to the local job node editor

UX role:

- central navigation shell for a single job

Design need:

- should become the main operational hub for stage-based review
- needs stronger information architecture and clearer action hierarchy

### C. Pipeline Outputs View

Embedded in job workspace.

Purpose:

- inspect real local artifacts for the currently selected stage
- edit structured JSON or markdown where allowed
- preview scrape screenshots

What it currently supports:

1. stage-based artifact list
2. JSON preview
3. markdown preview/edit
4. screenshot preview for scrape failures
5. save-to-file behavior for:
   - `extract_understand`
   - `match`
   - generated documents

UX role:

- raw artifact inspector / fallback editor / stage debugger

Design need:

- important operational surface
- should feel like a deliberate inspector, not a developer dump

### D. Job Node Editor Page

Route:

- `/jobs/:source/:jobId/node-editor`

Purpose:

- graph-shaped editor over local JSON for the two most important structured stages
  - `extract_understand`
  - `match`

What it currently does:

1. load the JSON state for the selected stage
2. build a lightweight graph projection
3. let the user click a node/object path
4. edit the selected JSON fragment
5. save back to `state.json`

UX role:

- minimal structured editor over local artifacts

Design need:

- this should evolve toward reusing the full `NodeEditor` interaction language rather than staying as a plain JSON+graph helper

### E. View 1 - Graph Explorer

Purpose:

- show graph relationships in the matching space
- especially requirement -> match -> evidence understanding

Current behavior:

1. graph display
2. match table with score and reasoning

UX role:

- read-only semantic overview of matching

### F. View 2 - Document to Graph

Purpose:

- compare extracted requirements against source text
- navigate from text to structured requirements

Current behavior:

1. source text displayed line by line
2. extracted requirements list
3. requirement-linked spans
4. graph view of source -> requirement links

UX role:

- extraction review surface

Important logic:

- this view is central to the deterministic evidence-linking concept
- the product should not rely on invented offsets from the LLM

### G. View 3 - Graph to Document

Purpose:

- inspect generated documents in relation to their source graph context

Current behavior:

1. tabbed documents
   - motivation letter
   - CV
   - email
2. contributing graph nodes view

UX role:

- text generation review surface

Generated from `raw/docs_postulador_langgraph/docs/ui/review_workbench_product_brief.md`.