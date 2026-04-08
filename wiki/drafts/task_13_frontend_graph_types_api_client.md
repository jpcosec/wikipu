---
identity:
  node_id: "doc:wiki/drafts/task_13_frontend_graph_types_api_client.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Create: `ui/src/types/graph.types.ts`
- Create: `ui/src/api/client.ts`

- [ ] **Step 1: Create TypeScript types mirroring RouteGraph**

```typescript
// ui/src/types/graph.types.ts
export interface RouteNode {
  id: string;
  type: "doc" | "code";
  path: string;
  domain: string;
  stage: string;
  nature: string;
  version: string | null;
  symbol: string | null;
  tags: Record<string, string | null>;
}

export interface RouteEdge {
  source: string;
  target: string;
  type: "implements" | "doc-ref" | "depends_on" | "contract";
}

export interface RouteGraph {
  nodes: RouteNode[];
  edges: RouteEdge[];
}

export interface GraphStats {
  total_nodes: number;
  doc_nodes: number;
  code_nodes: number;
  total_edges: number;
  issues: number;
  domains: string[];
  stages: string[];
}

export interface NodeDetail {
  node: RouteNode;
  connected_edges: RouteEdge[];
}
```

- [ ] **Step 2: Create API client**

```typescript
// ui/src/api/client.ts
import type { GraphStats, NodeDetail, RouteGraph } from "../types/graph.types";

const BASE = "/api";

async function get<T>(path: string, params?: Record<string, string>): Promise<T> {
  const url = new URL(`${BASE}${path}`, window.location.origin);
  if (params) {
    Object.entries(params).forEach(([k, v]) => {
      if (v) url.searchParams.set(k, v);
    });
  }
  const resp = await fetch(url.toString());
  if (!resp.ok) throw new Error(`${resp.status} ${resp.statusText}`);
  return resp.json();
}

export const api = {
  getGraph: (filters?: { domain?: string; stage?: string; nature?: string }) =>
    get<RouteGraph>("/graph", filters),
  getStats: () => get<GraphStats>("/stats"),
  getNode: (id: string) => get<NodeDetail>(`/nodes/${encodeURIComponent(id)}`),
  rescan: () => fetch(`${BASE}/rescan`, { method: "POST" }).then((r) => r.json()),
};
```

- [ ] **Step 3: Commit**

```bash
git add ui/src/types/ ui/src/api/
git commit -m "feat(doc-router): TypeScript graph types and API client"
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md`.