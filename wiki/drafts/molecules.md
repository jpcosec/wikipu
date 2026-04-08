---
identity:
  node_id: "doc:wiki/drafts/molecules.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/components.md", relation_type: "documents"}
---

### `<SplitPane>`

## Details

### `<SplitPane>`

**Path:** `components/molecules/SplitPane.tsx`

**Props:**
```ts
interface SplitPaneProps {
  children: [React.ReactNode, React.ReactNode];
  defaultSplit?: number;  // percentage for first panel
  minSize?: number;       // minimum panel size in pixels
}
```

**Usage:**
```tsx
<SplitPane defaultSplit={30} minSize={200}>
  <ExplorerTree />
  <FilePreview />
</SplitPane>
```

---

### `<ControlPanel>`

**Path:** `components/molecules/ControlPanel.tsx`

**Props:**
```ts
interface ControlPanelProps {
  title: string;
  children: React.ReactNode;
}
```

**Usage:**
```tsx
<ControlPanel title="PHASE: MATCH">
  <DecisionButtons />
  <JsonReadout />
</ControlPanel>
```

---

### `<DiagnosticCard>`

**Path:** `components/molecules/DiagnosticCard.tsx`

**Props:**
```ts
interface DiagnosticCardProps {
  title: string;
  children: React.ReactNode;
  status?: 'success' | 'error' | 'warning';
}
```

**Usage:**
```tsx
<DiagnosticCard title="Fetch Metadata" status="success">
  <MetaField label="URL" value="https://..." />
</DiagnosticCard>
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/components.md`.