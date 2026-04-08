---
identity:
  node_id: "doc:wiki/drafts/4_frontend_architecture.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/superpowers/specs/2026-03-23-doc-router-phase2-design.md", relation_type: "documents"}
---

### Layout: Tabbed Views

## Details

### Layout: Tabbed Views

Three tabs in the header bar:

| Tab | View | Description |
|-----|------|-------------|
| **Graph** | Existing RouteGraphCanvas | Enhanced with `?group=xxx` filter for plan-scoped view |
| **Plans** | Plan review workspace | List → timeline → editor |
| **Files** | File explorer | Tree + preview with span tagging |

Each tab is an independent view. No split panes between tabs. This supports future migration to floating windows.

### Component Map

**Imported from review-workbench (ui-redesign):**

Components are copied (not linked) from the review-workbench into the doc-router `ui/src/` tree. This avoids cross-worktree build complexity. The copied components are: IntelligentEditor, FileTree, BreadcrumbNav, FilePreview variants, DocApproveBar, SplitPane, and atoms (Badge, Button, Icon, Spinner, Tag, Kbd). Some of these atoms are already present from Phase 1.

The IntelligentEditor already supports the span tagging pattern needed: `onSpanSelect` callback returns `{start, end, text}` when the user selects a range. The plan review workflow wraps this to prompt for a comment and append to `file_tags`.

| Component | Source | Usage |
|-----------|--------|-------|
| IntelligentEditor | organisms/ | CodeMirror editor with span tagging, highlights, onSpanSelect |
| FileTree | organisms/ | Recursive tree with expand/collapse |
| BreadcrumbNav | explorer/ | Path navigation |
| FilePreview, JsonPreview, MarkdownPreview, ImagePreview | explorer/ | File content rendering |
| DocApproveBar | job-pipeline/ | Bottom bar with save pattern |
| SplitPane | molecules/ | Resizable panels |
| Badge, Button, Icon, Spinner, Tag, Kbd | atoms/ | Design system primitives (some already present from Phase 1) |

**New components (doc-router specific):**

| Component | Location | Purpose |
|-----------|----------|---------|
| TabNav | `components/molecules/TabNav.tsx` | Header tab switcher (Graph / Plans / Files) |
| PlanList | `features/plan-review/components/PlanList.tsx` | Left panel: plan groups with status badges |
| IterationTimeline | `features/plan-review/components/IterationTimeline.tsx` | Visual chain: plan_0 → review_0 → plan_1 → ... |
| PlanEditor | `features/plan-review/components/PlanEditor.tsx` | Wraps IntelligentEditor for plan markdown editing |
| TouchChips | `features/plan-review/components/TouchChips.tsx` | Clickable list of touched files above editor |
| GraphEditPanel | `features/plan-review/components/GraphEditPanel.tsx` | Mini ReactFlow graph of touches, editable |
| CommentDialog | `features/plan-review/components/CommentDialog.tsx` | Modal: "why this change?" when editing graph |
| TagBar | `features/file-explorer/components/TagBar.tsx` | Bottom bar showing active file tags, save action |

### Hooks / API Client

| Hook | Purpose |
|------|---------|
| `usePlanGroups()` | `GET /api/plans` — list all plan groups |
| `usePlanChain(group)` | `GET /api/plans/{group}` — iteration chain |
| `usePlanContent(group, type, ver)` | `GET /api/plans/{group}/{type}_{ver}` — single plan/review |
| `useSaveReview()` | `PUT /api/plans/{group}/{type}_{ver}` — mutation |
| `useFileTree(path)` | `GET /api/files?path=` — directory listing |
| `useFileContent(path)` | `GET /api/files/content?path=` — file content |

### Interaction Patterns

**Plan Review (Plans tab):**
1. Select a plan group from PlanList
2. IterationTimeline shows the version chain — click any iteration to view
3. PlanEditor opens with the plan content in CodeMirror (editable)
4. TouchChips render above — click one to jump to Files tab filtered to that file
5. GraphEditPanel shows the touch graph — add/remove touches, each edit triggers CommentDialog
6. Save writes `review_{group}_N.md` with edited content + file tags + graph changes

**File Tagging (Files tab):**
1. FileTree on left with cyan dot badges on touched files
2. Select a file — content loads in IntelligentEditor (read-only for non-plan files)
3. Select a text span → tag prompt appears → comment saved to active review
4. TagBar at bottom shows all tags for current file, with save action

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/superpowers/specs/2026-03-23-doc-router-phase2-design.md`.