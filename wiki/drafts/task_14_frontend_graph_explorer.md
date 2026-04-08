---
identity:
  node_id: "doc:wiki/drafts/task_14_frontend_graph_explorer.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Create: `ui/src/features/graph-explorer/hooks/useRouteGraph.ts`
- Create: `ui/src/features/graph-explorer/lib/colors.ts`
- Create: `ui/src/features/graph-explorer/lib/layout.ts`
- Create: `ui/src/features/graph-explorer/components/DocNode.tsx`
- Create: `ui/src/features/graph-explorer/components/CodeNode.tsx`
- Create: `ui/src/features/graph-explorer/components/RouteEdge.tsx`
- Create: `ui/src/features/graph-explorer/components/FilterBar.tsx`
- Create: `ui/src/features/graph-explorer/components/NodeInspector.tsx`
- Create: `ui/src/features/graph-explorer/components/RouteGraphCanvas.tsx`
- Modify: `ui/src/App.tsx`

- [ ] **Step 1: Create data hook**

```typescript
// ui/src/features/graph-explorer/hooks/useRouteGraph.ts
import { useQuery } from "@tanstack/react-query";
import { api } from "../../../api/client";

interface Filters {
  domain?: string;
  stage?: string;
  nature?: string;
}

export function useRouteGraph(filters: Filters = {}) {
  return useQuery({
    queryKey: ["graph", filters],
    queryFn: () => api.getGraph(filters),
    staleTime: 30_000,
  });
}

export function useGraphStats() {
  return useQuery({
    queryKey: ["stats"],
    queryFn: () => api.getStats(),
    staleTime: 30_000,
  });
}
```

- [ ] **Step 2: Create color/layout helpers**

```typescript
// ui/src/features/graph-explorer/lib/colors.ts
const DOMAIN_HUES: Record<string, number> = {
  pipeline: 188,
  ui: 270,
  api: 210,
  core: 168,
  cli: 198,
  data: 36,
  policy: 345,
  practices: 150,
};

export function domainColor(domain: string): string {
  const hue = DOMAIN_HUES[domain] ?? 210;
  return `hsl(${hue} 74% 65%)`;
}

export function domainBg(domain: string): string {
  const hue = DOMAIN_HUES[domain] ?? 210;
  return `hsl(${hue} 40% 15%)`;
}

const NATURE_SHAPES: Record<string, string> = {
  philosophy: "rounded-full",
  implementation: "rounded-md",
  development: "rounded-sm",
  testing: "rounded-none",
};

export function natureShape(nature: string): string {
  return NATURE_SHAPES[nature] ?? "rounded-md";
}
```

```typescript
// ui/src/features/graph-explorer/lib/layout.ts
import Dagre from "@dagrejs/dagre";
import type { RouteNode, RouteEdge } from "../../../types/graph.types";

interface LayoutNode {
  id: string;
  position: { x: number; y: number };
  data: RouteNode;
  type: string;
}

interface LayoutEdge {
  id: string;
  source: string;
  target: string;
  data: RouteEdge;
  type: string;
}

const NODE_WIDTH = 260;
const NODE_HEIGHT = 80;

export function layoutGraph(
  nodes: RouteNode[],
  edges: RouteEdge[],
): { nodes: LayoutNode[]; edges: LayoutEdge[] } {
  const g = new Dagre.graphlib.Graph().setDefaultEdgeLabel(() => ({}));
  g.setGraph({ rankdir: "LR", nodesep: 60, ranksep: 120 });

  nodes.forEach((n) => g.setNode(n.id, { width: NODE_WIDTH, height: NODE_HEIGHT }));
  edges.forEach((e) => g.setEdge(e.source, e.target));

  Dagre.layout(g);

  const layoutNodes: LayoutNode[] = nodes.map((n) => {
    const pos = g.node(n.id);
    return {
      id: n.id,
      position: { x: pos.x - NODE_WIDTH / 2, y: pos.y - NODE_HEIGHT / 2 },
      data: n,
      type: n.type === "doc" ? "docNode" : "codeNode",
    };
  });

  const layoutEdges: LayoutEdge[] = edges.map((e, i) => ({
    id: `e-${i}`,
    source: e.source,
    target: e.target,
    data: e,
    type: "routeEdge",
  }));

  return { nodes: layoutNodes, edges: layoutEdges };
}
```

- [ ] **Step 3: Create custom node components**

```typescript
// ui/src/features/graph-explorer/components/DocNode.tsx
import { Handle, Position } from "@xyflow/react";
import type { RouteNode } from "../../../types/graph.types";
import { domainColor, domainBg } from "../lib/colors";

export function DocNode({ data, selected }: { data: RouteNode; selected: boolean }) {
  const color = domainColor(data.domain);
  const bg = domainBg(data.domain);

  return (
    <div
      className="border px-3 py-2 min-w-[240px]"
      style={{
        borderColor: selected ? "var(--color-primary)" : color,
        backgroundColor: bg,
        borderRadius: "8px",
      }}
    >
      <Handle type="target" position={Position.Left} className="!bg-[var(--color-primary)]" />
      <div className="font-mono text-xs" style={{ color }}>{data.domain}/{data.stage}</div>
      <div className="font-medium text-sm text-[var(--color-on-surface)] truncate">{data.id}</div>
      <div className="text-xs text-[var(--color-on-muted)] truncate">{data.path}</div>
      <Handle type="source" position={Position.Right} className="!bg-[var(--color-primary)]" />
    </div>
  );
}
```

```typescript
// ui/src/features/graph-explorer/components/CodeNode.tsx
import { Handle, Position } from "@xyflow/react";
import type { RouteNode } from "../../../types/graph.types";
import { domainColor, domainBg } from "../lib/colors";

export function CodeNode({ data, selected }: { data: RouteNode; selected: boolean }) {
  const color = domainColor(data.domain);
  const bg = domainBg(data.domain);

  return (
    <div
      className="border-2 border-dashed px-3 py-2 min-w-[240px]"
      style={{
        borderColor: selected ? "var(--color-primary)" : color,
        backgroundColor: bg,
        borderRadius: "4px",
      }}
    >
      <Handle type="target" position={Position.Left} className="!bg-[var(--color-secondary)]" />
      <div className="font-mono text-xs" style={{ color }}>{data.domain}/{data.stage}</div>
      <div className="font-medium text-sm text-[var(--color-on-surface)] truncate">
        {data.symbol ?? data.id}
      </div>
      <div className="text-xs text-[var(--color-on-muted)] truncate">{data.path}</div>
      <Handle type="source" position={Position.Right} className="!bg-[var(--color-secondary)]" />
    </div>
  );
}
```

```typescript
// ui/src/features/graph-explorer/components/RouteEdge.tsx
import { BaseEdge, getBezierPath, type EdgeProps } from "@xyflow/react";
import type { RouteEdge as RouteEdgeType } from "../../../types/graph.types";

const EDGE_COLORS: Record<string, string> = {
  implements: "var(--color-primary)",
  "doc-ref": "var(--color-secondary)",
  depends_on: "var(--color-on-muted)",
  contract: "#a855f7",
};

export function RouteEdge(props: EdgeProps & { data: RouteEdgeType }) {
  const [path, labelX, labelY] = getBezierPath(props);
  const color = EDGE_COLORS[props.data.type] ?? "var(--color-outline)";

  return (
    <>
      <BaseEdge
        path={path}
        style={{
          stroke: color,
          strokeWidth: 1.5,
          strokeDasharray: props.data.type === "depends_on" ? "6 3" : undefined,
        }}
      />
      <text
        x={labelX}
        y={labelY - 8}
        className="fill-[var(--color-on-muted)] text-[10px]"
        textAnchor="middle"
      >
        {props.data.type}
      </text>
    </>
  );
}
```

- [ ] **Step 4: Create FilterBar**

```typescript
// ui/src/features/graph-explorer/components/FilterBar.tsx
import { useGraphStats } from "../hooks/useRouteGraph";

interface Props {
  domain: string;
  stage: string;
  nature: string;
  onChange: (filters: { domain: string; stage: string; nature: string }) => void;
}

export function FilterBar({ domain, stage, nature, onChange }: Props) {
  const { data: stats } = useGraphStats();

  return (
    <div className="flex gap-3 items-center px-4 py-2 border-b border-[var(--color-outline)]/30 bg-[var(--color-surface)]">
      <label className="font-mono text-xs text-[var(--color-on-muted)] uppercase">Filters</label>
      <select
        value={domain}
        onChange={(e) => onChange({ domain: e.target.value, stage, nature })}
        className="bg-[var(--color-surface-container)] text-[var(--color-on-surface)] text-xs px-2 py-1 rounded border border-[var(--color-outline)]/30"
      >
        <option value="">All domains</option>
        {stats?.domains.map((d) => <option key={d} value={d}>{d}</option>)}
      </select>
      <select
        value={stage}
        onChange={(e) => onChange({ domain, stage: e.target.value, nature })}
        className="bg-[var(--color-surface-container)] text-[var(--color-on-surface)] text-xs px-2 py-1 rounded border border-[var(--color-outline)]/30"
      >
        <option value="">All stages</option>
        {stats?.stages.map((s) => <option key={s} value={s}>{s}</option>)}
      </select>
      {stats && (
        <span className="ml-auto font-mono text-xs text-[var(--color-on-muted)]">
          {stats.total_nodes} nodes / {stats.total_edges} edges
        </span>
      )}
    </div>
  );
}
```

- [ ] **Step 5: Create NodeInspector**

```typescript
// ui/src/features/graph-explorer/components/NodeInspector.tsx
import { useQuery } from "@tanstack/react-query";
import { api } from "../../../api/client";
import { Badge } from "../../../components/atoms/Badge";

interface Props {
  nodeId: string | null;
  onClose: () => void;
}

export function NodeInspector({ nodeId, onClose }: Props) {
  const { data } = useQuery({
    queryKey: ["node", nodeId],
    queryFn: () => api.getNode(nodeId!),
    enabled: !!nodeId,
  });

  if (!nodeId || !data) return null;
  const { node, connected_edges } = data;

  return (
    <div className="w-80 border-l border-[var(--color-outline)]/30 bg-[var(--color-surface)] p-4 overflow-y-auto">
      <div className="flex justify-between items-center mb-4">
        <h3 className="font-headline text-sm uppercase tracking-wider text-[var(--color-primary)]">
          Inspector
        </h3>
        <button onClick={onClose} className="text-[var(--color-on-muted)] hover:text-[var(--color-on-surface)]">
          &times;
        </button>
      </div>

      <div className="space-y-3">
        <div>
          <div className="font-mono text-xs text-[var(--color-on-muted)]">ID</div>
          <div className="text-sm">{node.id}</div>
        </div>
        <div className="flex gap-2">
          <Badge variant="primary">{node.domain}</Badge>
          <Badge variant="secondary">{node.stage}</Badge>
          <Badge variant="muted">{node.nature}</Badge>
        </div>
        <div>
          <div className="font-mono text-xs text-[var(--color-on-muted)]">Path</div>
          <div className="text-sm font-mono">{node.path}</div>
        </div>
        {node.symbol && (
          <div>
            <div className="font-mono text-xs text-[var(--color-on-muted)]">Symbol</div>
            <div className="text-sm font-mono">{node.symbol}</div>
          </div>
        )}
        {node.version && (
          <div>
            <div className="font-mono text-xs text-[var(--color-on-muted)]">Version</div>
            <div className="text-sm">{node.version}</div>
          </div>
        )}
        {Object.keys(node.tags).length > 0 && (
          <div>
            <div className="font-mono text-xs text-[var(--color-on-muted)] mb-1">Tags</div>
            {Object.entries(node.tags).map(([k, v]) =>
              v ? <div key={k} className="text-xs font-mono">{k}: {v}</div> : null
            )}
          </div>
        )}
        <div>
          <div className="font-mono text-xs text-[var(--color-on-muted)] mb-1">
            Edges ({connected_edges.length})
          </div>
          {connected_edges.map((e, i) => (
            <div key={i} className="text-xs font-mono">
              {e.source === node.id ? `→ ${e.target}` : `← ${e.source}`}
              <span className="text-[var(--color-on-muted)]"> ({e.type})</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
```

- [ ] **Step 6: Create RouteGraphCanvas**

```typescript
// ui/src/features/graph-explorer/components/RouteGraphCanvas.tsx
import {
  ReactFlow,
  Background,
  Controls,
  type OnNodeClick,
} from "@xyflow/react";
import "@xyflow/react/dist/style.css";
import { useMemo, useState } from "react";
import { useRouteGraph } from "../hooks/useRouteGraph";
import { layoutGraph } from "../lib/layout";
import { DocNode } from "./DocNode";
import { CodeNode } from "./CodeNode";
import { RouteEdge } from "./RouteEdge";
import { FilterBar } from "./FilterBar";
import { NodeInspector } from "./NodeInspector";
import { Spinner } from "../../../components/atoms/Spinner";

const nodeTypes = { docNode: DocNode, codeNode: CodeNode };
const edgeTypes = { routeEdge: RouteEdge };

export function RouteGraphCanvas() {
  const [filters, setFilters] = useState({ domain: "", stage: "", nature: "" });
  const [selectedNode, setSelectedNode] = useState<string | null>(null);

  const queryFilters = {
    domain: filters.domain || undefined,
    stage: filters.stage || undefined,
    nature: filters.nature || undefined,
  };
  const { data: graph, isLoading } = useRouteGraph(queryFilters);

  const { nodes, edges } = useMemo(() => {
    if (!graph) return { nodes: [], edges: [] };
    return layoutGraph(graph.nodes, graph.edges);
  }, [graph]);

  const handleNodeClick: OnNodeClick = (_, node) => {
    setSelectedNode(node.id);
  };

  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-full">
        <Spinner size="md" />
      </div>
    );
  }

  return (
    <div className="flex flex-col h-full">
      <FilterBar {...filters} onChange={setFilters} />
      <div className="flex flex-1 min-h-0">
        <div className="flex-1">
          <ReactFlow
            nodes={nodes}
            edges={edges}
            nodeTypes={nodeTypes}
            edgeTypes={edgeTypes}
            onNodeClick={handleNodeClick}
            fitView
            proOptions={{ hideAttribution: true }}
          >
            <Background color="var(--color-outline)" gap={20} size={1} />
            <Controls />
          </ReactFlow>
        </div>
        <NodeInspector nodeId={selectedNode} onClose={() => setSelectedNode(null)} />
      </div>
    </div>
  );
}
```

- [ ] **Step 7: Update App.tsx**

```typescript
// ui/src/App.tsx
import { RouteGraphCanvas } from "./features/graph-explorer/components/RouteGraphCanvas";

export default function App() {
  return (
    <div className="h-screen flex flex-col bg-[var(--color-background)] text-[var(--color-on-surface)]">
      <header className="flex items-center gap-3 px-4 py-2 border-b border-[var(--color-outline)]/30 bg-[var(--color-surface)]">
        <h1 className="font-headline text-sm tracking-widest uppercase text-[var(--color-primary)]">
          Doc-Router
        </h1>
      </header>
      <main className="flex-1 min-h-0">
        <RouteGraphCanvas />
      </main>
    </div>
  );
}
```

- [ ] **Step 8: Verify it works end-to-end**

Terminal 1: `doc-router serve --project . --port 8030`
Terminal 2: `cd ui && npm run dev`

Open http://127.0.0.1:5174 — should show the graph explorer with nodes from the project.

- [ ] **Step 9: Commit**

```bash
git add ui/src/features/ ui/src/App.tsx
git commit -m "feat(doc-router): interactive graph explorer with React Flow"
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-phase1-plan.md`.