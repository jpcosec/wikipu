---
identity:
  node_id: "doc:wiki/drafts/mock_layer.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/api_contract.md", relation_type: "documents"}
---

The UI includes a mock API layer for development without backend:

## Details

The UI includes a mock API layer for development without backend:

### Structure

```
src/mock/
├── client.ts      # Mock fetch implementation
└── fixtures/     # Mock data files
    ├── portfolio_summary.json
    ├── job_timeline_201397.json
    ├── job_timeline_999001.json
    ├── view_extract_201397.json
    ├── view_match_201397.json
    ├── view_documents_999001.json
    ├── cv_profile_graph.json
    ├── evidence_bank.json
    └── ...
```

### Toggle

```bash
VITE_MOCK=true   # Use mock data (default for development)
VITE_MOCK=false  # Use real API
```

### Mock Client Interface

```ts
// src/mock/client.ts
export const mockClient = {
  getPortfolioSummary: () => Promise<PortfolioSummary>,
  getJobTimeline: (source: string, jobId: string) => Promise<JobTimeline>,
  getViewExtract: (source: string, jobId: string) => Promise<ExtractViewPayload>,
  getViewMatch: (source: string, jobId: string) => Promise<MatchViewPayload>,
  getViewDocuments: (source: string, jobId: string) => Promise<DocumentsViewPayload>,
  getArtifacts: (source: string, jobId: string, node: string) => Promise<ArtifactListPayload>,
  getEvidenceBank: (source: string, jobId: string) => Promise<EvidenceBankPayload>,
  getCvProfileGraph: () => Promise<CvProfileGraphPayload>,
  browseExplorer: (path: string) => Promise<ExplorerPayload>,
  getPackageFiles: (source: string, jobId: string) => Promise<PackageFilesPayload>,
  // Commands
  saveNodeState: (source: string, jobId: string, node: string, data: unknown) => Promise<CommandResponse>,
  saveDocument: (source: string, jobId: string, docKey: string, data: SaveDocumentPayload) => Promise<CommandResponse>,
  decideGate: (source: string, jobId: string, gate: string, data: GateDecisionPayload) => Promise<CommandResponse>,
  runPipeline: (source: string, jobId: string, data?: RunPipelinePayload) => Promise<RunResponse>,
  archiveJob: (source: string, jobId: string, data?: ArchiveJobPayload) => Promise<CommandResponse>,
};
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/api_contract.md`.