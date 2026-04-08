# Planning Checklist

This is the single planning checklist for active work.

## Workflow Rules

1. **Commit OBLIGATORIO** al cerrar cada fase — seguir formato:
   ```
   feat(ui): implement <view name> (<spec-id>)
   
   - <component 1>
   - <component 2>
   ...
   - Connected to <hook names>
   ```
2. **Changelog** — agregar entrada en `changelog.md`
3. **Checklist** — marcar `[x]` en este archivo

## 01 UI — ui-redesign branch (Terran Command design system)

### Fase 0 — Foundation (Router + Layouts + Portfolio) ✅
- [x] `utils/cn.ts` — clsx + tailwind-merge helper
- [x] `main.tsx` — QueryClientProvider wrapper
- [x] `AppShell.tsx` — LeftNav + `<Outlet />`
- [x] `JobWorkspaceShell.tsx` — Pipeline TopBar + nested `<Outlet />`
- [x] `Badge.tsx` atom — forwardRef, cn(), variant prop
- [x] `types/api.types.ts` — PortfolioSummary, ViewPayload, GraphNode, GraphEdge, etc.
- [x] `types/ui.types.ts` — MatchNodeData, ExtractEditorState, DocumentDraft, ExplorerTreeNode, GateDecisionState
- [x] Mock fixtures y client

### Fase 0 — A1 Portfolio Dashboard ✅
- [x] `usePortfolioSummary.ts`
- [x] `PortfolioTable.tsx`
- [x] `DeadlineSidebar.tsx`, `RecentArtifacts.tsx`, `SystemStatus.tsx`
- [x] `PortfolioDashboard.tsx`

### Fase 1 — B0 Job Flow Inspector ✅
- [x] `useJobTimeline.ts`
- [x] `JobFlowInspector.tsx` — timeline visual con pipeline stages
- [x] `HitlCtaBanner.tsx`, `JobMetaPanel.tsx`, `PipelineTimeline.tsx`, `StageRow.tsx`

### Atoms pre-Fase 2 ✅
- [x] `Button.tsx` — variant: primary|ghost|danger, size: sm|md, loading?: boolean
- [x] `Icon.tsx` — Lucide wrapper, name prop, size: xs|sm|md
- [x] `Spinner.tsx` — CSS spinner, size: xs|sm|md, color primario
- [x] `SplitPane.tsx` (molecule) — wrapper de react-resizable-panels

### Fase 2 — A2 Data Explorer ✅
- [x] `useExplorerBrowse.ts`
- [x] `ExplorerTree.tsx`, `BreadcrumbNav.tsx`, `FilePreview.tsx`, `JsonPreview.tsx`, `MarkdownPreview.tsx`, `ImagePreview.tsx`
- [x] `DataExplorer.tsx`

### Fase 3 — B1 Scrape Diagnostics ✅
- [x] `useArtifacts.ts`
- [x] `ScrapeMetaCard.tsx`, `SourceTextPreview.tsx`, `ErrorScreenshot.tsx`, `ScrapeControlPanel.tsx`
- [x] `ScrapeDiagnostics.tsx`

### Atoms pre-Fase 4 ✅
- [x] `Tag.tsx` — inline span, category: skill|req|risk, border-l-2 color-coded

### Fase 4 — B2 Extract & Understand ✅
- [x] `useViewExtract.ts`
- [x] `SourceTextPane.tsx`, `RequirementList.tsx`, `RequirementItem.tsx`, `ExtractControlPanel.tsx`
- [x] `ExtractUnderstand.tsx`

### Fase 5 — B3 Match ✅
- [x] `useViewMatch.ts`, `useEvidenceBank.ts`, `useGateDecide.ts`, `useEditorState.ts`
- [x] `MatchGraphCanvas.tsx`, `RequirementNode.tsx`, `ProfileNode.tsx`, `EdgeScoreBadge.tsx`
- [x] `EvidenceBankPanel.tsx`, `MatchControlPanel.tsx`, `MatchDecisionModal.tsx`
- [x] `Match.tsx`

### Atoms pre-Fase 6 ✅
- [x] `Kbd.tsx` — keyboard shortcut display, keys: string[], estilo mono

### Fase 6 — B4 Generate Documents ✅
- [x] `useViewDocuments.ts`, `useDocumentSave.ts`, `useGateDecide.ts`
- [x] `DocumentTabs.tsx`, `DocumentEditor.tsx`, `ContextPanel.tsx`
- [x] `DocApproveBar.tsx`, `RegenModal.tsx`
- [x] `GenerateDocuments.tsx`

### Fase 7 — B5 Package & Deployment ✅
- [x] `usePackageFiles.ts`
- [x] `MissionSummaryCard.tsx`, `PipelineChecklist.tsx`, `PackageFileList.tsx`, `DeploymentCta.tsx`
- [x] `PackageDeployment.tsx`

### Fase 8 — B4b Default Document Gates ⚠️ BLOCKED — requiere backend
- [ ] `useDocumentGate.ts`, `useGateDecision.ts`
- [ ] Prop `mode="default_gate"` en `GenerateDocuments.tsx`

### Fase 9 — A3 Base CV Editor ✅
- [x] `useCvProfileGraph.ts`, `useSaveCvGraph.ts`
- [x] `CvGraphCanvas.tsx`, `EntryNode.tsx`, `SkillNode.tsx`, `NodeInspector.tsx`, `ProfileStats.tsx`
- [x] `BaseCvEditor.tsx`
- [x] **E2E tests** — all TestSprite tests passing (TC001–TC049 suite, 100%)

### Fase 11 — Component Map Compliance ✅
- [x] `IntelligentEditor` — fixed decorations (StateField), added `onSpanSelect` prop
- [x] `SourceTextPane` → uses IntelligentEditor (tag-hover mode)
- [x] `DocumentEditor` → uses IntelligentEditor (fold mode)
- [x] `ScrapeControlPanel` → uses ControlPanel molecule
- [x] `ExtractControlPanel` → uses ControlPanel molecule
- [x] `MatchControlPanel` → uses ControlPanel molecule (with children for detail pane)
- [x] `GraphCanvas` → added `onConnect` prop
- [x] `MatchGraphCanvas` → uses GraphCanvas organism
- [x] `ExplorerTree` → delegates to FileTree organism
- [x] `JsonPreview` → uses IntelligentEditor (fold/json)
- [x] `MarkdownPreview` → uses IntelligentEditor (fold/markdown)
- [x] `CvGraphCanvas` — kept as-is (uses parentId/extent, incompatible with generic GraphCanvas)
- [x] **E2E tests** — Full suite on production build: 86.67% pass (26/30); 4 remaining are test limitations (TC008 mock error, TC013 test bug, TC015 mock limitation, TC046 bogus assertion)

### CSS Migration — legacy ne-* → Tailwind Terran ✅
- [x] Audit all ne-* usages (Haiku agent — LEGACY_CSS_AUDIT.md)
- [x] Migrate all 64 ne-* classes in `KnowledgeGraph.tsx` to Tailwind Terran utilities
- [x] Replace 2 inline `var()` references with Terran hex values
- [x] Remove legacy CSS block from `styles.css` + delete `legacy.css`
- [x] Remove `:root` variable bridge from `styles.css`
- [x] Verify no legacy conventions remain in any `.tsx`/`.ts` files

### C1 — Graph Editor Redesign ✅
- [x] `styles.css` — fix 5 hardcoded light `.ne-*` values + `.react-flow__node` transparent override
- [x] `KnowledgeGraph.tsx` — Terran dark CATEGORY_COLORS, GroupNode, SubFlowEdge, Document template, initialNodes/initialEdges/onSave/onChange props
- [x] `features/base-cv/lib/cvToGraph.ts` — adapter with meta passthrough (cvProfileToGraph / graphToCvProfile)
- [x] `pages/global/BaseCvEditor.tsx` — thin KnowledgeGraph wrapper (37 lines)
- [x] `types/api.types.ts` — add `category?: string` to `GraphNode`
- [x] `mock/fixtures/view_match_*.json` — add `category` to all nodes
- [x] `features/job-pipeline/lib/matchToGraph.ts` — adapter + MatchEdits type
- [x] `features/job-pipeline/components/UnmappedSkillsPanel.tsx` — collapsible right rail
- [x] `pages/job/Match.tsx` — KnowledgeGraph 2-column layout + UnmappedSkillsPanel + MatchDecisionModal

### Fase 10 — B3b Application Context Gate ⚠️ BLOCKED — requiere backend
- [ ] `useApplicationContext.ts`, `useContextDecision.ts`
- [ ] `ContextBrief.tsx`, `MatchReferencePanel.tsx`, `ContextDecisionBar.tsx`
- [ ] `ApplicationContext.tsx`

---

## Reference: node-editor branch (compare point)

> Branch `node-editor` contains a parallel implementation of the graph editor with a more
> mature architecture. Items below are available to port — ordered by priority.

### Immediately applicable (graph work, D2+)

- **`stores/graph-store.ts`** — Zustand graph store with semantic undo/redo (`CREATE_ELEMENTS`, `DELETE_ELEMENTS`, `UPDATE_NODE`, `UPDATE_EDGE`). `isVisualOnly` flag keeps drag/selection out of undo history. Replaces `KnowledgeGraphContext`.
- **`stores/ui-store.ts`** — Separate Zustand UI store: editor mode (`browse` / `focus` / `edit_node` / `edit_relation`), filter state, delete-confirm flow, command-dialog toggle.
- **`stores/types.ts`** — `ASTNode`, `ASTEdge`, `SemanticAction` — typed AST layer over ReactFlow primitives.
- **`hooks/use-edge-inheritance.ts`** — `collapseGroupEdges` / `expandGroupEdges`: hides child nodes and re-routes edges to the group parent. The clean version of what D2 collapse/expand needs.
- **`edges/FloatingEdge.tsx` + `edges/edge-helpers.ts`** — Auto-detect source/target attachment geometry (floating handles). Edges with `relationType === 'inherited'` render dashed/dimmed automatically.
- **`edges/ButtonEdge.tsx`** — Extends FloatingEdge with a hover-reveal `×` delete button on the edge path.
- **`hooks/use-keyboard.ts`** — Enter = edit focused node, Escape = browse, Ctrl+Z/Y = undo/redo. Includes `isEditableTarget()` guard so inputs aren't captured.
- **`L2-canvas/GroupShell.tsx`** — Group node with `NodeToolbar` collapse/expand button, `NodeResizer`, handles only when expanded. Pairs with `use-edge-inheritance`.

### For D1 (schema explorer) and beyond

- **`schema/registry.ts`** — `NodeTypeRegistry` class: `register`, `get`, `validatePayload` (Zod), `sanitizePayload`, `canConnect`, `getAll`. Fully tested.
- **`schema/registry.types.ts`** — `NodeTypeDefinition`: `typeId`, `label`, `icon`, `colorToken`, `defaultSize`, `renderers` (detail/label/dot tiers), `payloadSchema`, `sanitizer`, `allowedConnections`.
- **`L2-canvas/NodeShell.tsx`** — Registry-driven node shell with zoom-level rendering tiers (detail ≥0.9×, label ≥0.4×, dot below), context menu (edit / focus neighborhood / copy / delete), category color overrides.
- **`hooks/use-graph-layout.ts`** — Dagre layout hook that reads from graph-store and applies positions with `isVisualOnly: true` (no undo pollution).

### Lower priority (polish)

- **`components/ui/`** — shadcn components not yet in ui-redesign: `command`, `context-menu`, `sheet`, `dropdown-menu`, `popover`, `scroll-area`, `accordion`, `sonner`.
- **`L2-canvas/panels/NodeInspector.tsx`** — Sheet-based node editor form (shadcn `Sheet`), more polished than current inline inspector.

---

## Reference: external projects (compare point)

> These are open-source projects analyzed during design of the node-editor branch.
> Listed here because they solved problems our current implementation still has open.

### Problems our implementation has — and where they were solved

**Hardcoded node types leaking into L2**
Our `CvGraphCanvas` and `MatchGraphCanvas` check `node.category` / `node.type` directly.
- Fix pattern: `agentok` → `frontend/src/nodes/index.ts` — a plain `{ [typeId]: Component }` map, no conditionals in the canvas layer.
- Rule: L2 must never branch on a type string. Unknown `typeId` → `FallbackNode` (renders raw JSON), not a red error box.

**No formal data contract at the graph entry point**
`cvToGraph` and `matchToGraph` accept loosely-typed objects; schema changes break silently.
- Fix pattern: `prismaliser` → `src/lib/layout.ts` + schema transform. Formalise with a typed `DomainGraph` interface at the boundary:
  ```ts
  interface DomainGraph {
    entities: Array<{ id: string; typeId: string; properties: Record<string, unknown> }>;
    relations: Array<{ sourceId: string; targetId: string; label?: string }>;
    schema: Record<string, { label: string; icon?: string; l3ComponentId: string }>;
  }
  ```
  The translator (`schema-to-graph.ts`) must be a **pure function** — testable in isolation, no side effects, fails at TypeScript level if `DomainGraph` contract is violated.

**Collapse/expand re-layout not triggering**
When a group collapses in D2, sibling nodes don't reflow to fill the space.
- Fix pattern: L3 emits a size-change signal → L2 re-runs Dagre. `use-edge-inheritance` + `use-graph-layout` in node-editor branch already wire this up; our D2 implementation skips the re-layout step.

**Focus mode is declared but not implemented**
`ui-store` has `'focus'` as an editor state but nothing moves when it activates.
- Fix pattern: d3-force repulsion around the focused node. On `setEditorState('focus')`, compute neighbor distances and apply position offsets so related nodes orbit the hero. Reference: [react-flow force layout examples](https://reactflow.dev/examples/layout/force-layout) + d3-force.
- Layer attribution: L1 owns which node is hero → L2 applies force layout → L3 receives `isFocused` prop and can expand detail tier.

### Layer ownership reference (anti-confusion map)

| Behavior | L1 (App) | L2 (Canvas/Shell) | L3 (Node Content) |
|---|---|---|---|
| Collapse/expand attributes | — | re-layout after | owns toggle state |
| Toolbar (edit, delete, copy) | — | `NodeToolbar` wrapper | — |
| Hover highlight | — | detects `onMouseEnter`, applies CSS | receives `hovered` prop |
| Focus + neighborhood radial | sets hero node id | applies d3-force, dims non-neighbors | receives `isFocused` |
| Undo/redo | — | `graph-store` semantic actions | `isVisualOnly` for visual-only changes |

### Manual de vuelo (anti-hardcoding rules)

1. **L2 is type-blind.** No `if (typeId === 'person')` anywhere in canvas or shell code. All branching goes through the registry.
2. **Translator is a pure function.** `DomainGraph → { nodes, edges }`. No imports from UI layers. Must have unit tests before connecting to any real data source.
3. **Unknown types get a FallbackNode.** Never a crash, never a silent blank. Raw JSON dump styled as a debug card.
4. **Visual actions don't pollute undo history.** Drag position, zoom, hover, selection → `isVisualOnly: true`. Only semantic edits (rename, delete, add edge) go into the undo stack.

---

## Rules

- Mark a phase complete only when code, verification, and changelog agree.
- **Commit message is OBLIGATORY** — follow format in `README.md`
- **Changelog entry is OBLIGATORY** — add to `changelog.md`
- All E2E tests via TestSprite — never raw Playwright test files.
- No hardcoded data in components — data always from API/mock fixtures.
- Components dumb in `pages/`, logic in `features/`
- `cn()` for all Tailwind class composition
