---
identity:
  node_id: "doc:wiki/drafts/phase_2_execution_merge_strategy.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/plan/UI_REDESIGN_MERGE_PLAN.md", relation_type: "documents"}
---

### Step 2.1: Pre-Merge Audit

## Details

### Step 2.1: Pre-Merge Audit

```bash
# Compare current state
git -C /home/jp/phd-workspaces/dev/.worktrees/ui-redesign diff dev..HEAD --name-only
```

**Files to REPLACE (from ui-redesign):**
```
apps/review-workbench/src/
├── App.tsx
├── main.tsx
├── api/client.ts
├── components/atoms/*.tsx
├── components/layouts/*.tsx
├── components/molecules/*.tsx
├── features/**/*.tsx
├── mock/*.ts
├── pages/global/*.tsx
├── pages/job/*.tsx
├── types/api.types.ts
├── types/ui.types.ts
├── utils/cn.ts
└── styles.css
```

**Files to KEEP (from dev):**
```
apps/review-workbench/src/
├── api/endpoints.ts       # If exists, reconcile with client.ts
├── lib/                   # Utilities, keep if not duplicated
└── vite.config.ts        # Update if needed for new deps
```

**Files to DELETE (legacy ui-redesign):**
```
apps/review-workbench/src/
├── pages/DataExplorerPage.tsx     # Replaced by global/DataExplorer.tsx
├── pages/DeploymentPage.tsx        # Replaced by job/PackageDeployment.tsx
├── pages/JobNodeEditorPage.tsx    # Replaced by job/* pages
├── pages/JobStagePage.tsx          # Replaced by job/* pages
├── pages/PortfolioPage.tsx         # Replaced by global/PortfolioDashboard.tsx
├── views/                         # All legacy views
├── sandbox/                       # All sandbox experiments
├── components/JobTree.tsx          # Legacy component
├── components/JobWorkspaceSidebar.tsx  # Legacy
├── components/StageStatusBadge.tsx # Replaced by atoms/Badge.tsx
├── components/GraphCanvas.tsx      # May keep for MatchGraphCanvas
├── components/RichTextPane.tsx     # Replaced by DocumentEditor
└── types/models.ts                 # Replaced by api.types.ts + ui.types.ts
```

### Step 2.2: Backend Compatibility Check

| API Contract | `dev` Status | `ui-redesign` Assumption |
|-------------|--------------|--------------------------|
| `/api/v1/portfolio/summary` | ✅ Implemented | ✅ Matches |
| `/api/v1/jobs/{source}/{job_id}/stage/{stage}/outputs` | ✅ Implemented | ✅ Matches |
| `/api/v1/jobs/{source}/{job_id}/browse` | ✅ Implemented | ✅ Matches |
| `/api/v1/jobs/{source}/{job_id}/documents/{doc_key}` | ✅ Implemented | ✅ Matches |
| `/api/v1/jobs/{source}/{job_id}/review/match` | ✅ Implemented | ✅ Matches |

**Compatible:** API contracts align. No backend changes required for core merge.

### Step 2.3: Merge Execution

```bash
# In ui-redesign worktree, create merge commit
cd /home/jp/phd-workspaces/dev/.worktrees/ui-redesign

# Option A: Merge commit (preserves history)
git merge dev --no-ff -m "Merge dev into ui-redesign"

# Option B: Rebase (cleaner linear history)
git rebase dev
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/plan/UI_REDESIGN_MERGE_PLAN.md`.