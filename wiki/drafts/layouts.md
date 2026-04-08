---
identity:
  node_id: "doc:wiki/drafts/layouts.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/components.md", relation_type: "documents"}
---

### `<AppShell>`

## Details

### `<AppShell>`

**Path:** `components/layouts/AppShell.tsx`

**Structure:**
```
┌─────────────────────────────────────────────────────┐
│  TopBar h-14  [PHD_OS // INTEL_REVIEW]  [nav icons] │
├──────────┬──────────────────────────┬───────────────┤
│ LeftNav  │   <Outlet />              │  (optional)   │
│  w-64    │   (main content)         │               │
│          │                          │               │
│ Portfolio│                          │               │
│ Explorer│                          │               │
│ CV      │                          │               │
└──────────┴──────────────────────────┴───────────────┘
```

**Usage:**
```tsx
// In App.tsx router
<Route element={<AppShell />}>
  <Route path="/" element={<PortfolioDashboard />} />
  <Route path="/explorer" element={<DataExplorer />} />
  <Route path="/cv" element={<BaseCvEditor />} />
</Route>
```

---

### `<JobWorkspaceShell>`

**Path:** `components/layouts/JobWorkspaceShell.tsx`

**Structure:**
```
┌─────────────────────────────────────────────────────┐
│  Pipeline TopBar: SCRAPE → EXTRACT → MATCH → ...    │
├──────────┬──────────────────────────┬───────────────┤
│ LeftNav  │   <Outlet />              │  (optional)   │
│  (mini)  │   (job view content)     │               │
└──────────┴──────────────────────────┴───────────────┘
```

**Usage:**
```tsx
// In App.tsx router (nested)
<Route element={<JobWorkspaceShell />}>
  <Route path="/jobs/:source/:jobId" element={<JobFlowInspector />} />
  <Route path="/jobs/:source/:jobId/scrape" element={<ScrapeDiagnostics />} />
  <Route path="/jobs/:source/:jobId/extract" element={<ExtractUnderstand />} />
  ...
</Route>
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/components.md`.