---
identity:
  node_id: "doc:wiki/drafts/api_client_usage.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/api_contract.md", relation_type: "documents"}
---

```tsx

## Details

```tsx
// In feature API hooks
import { apiClient } from '@/api/client';

const { data, isLoading } = useQuery({
  queryKey: ['timeline', source, jobId],
  queryFn: () => apiClient.getJobTimeline(source, jobId),
});
```

The `apiClient` automatically switches between real API and mock based on `VITE_MOCK` environment variable.

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/api_contract.md`.