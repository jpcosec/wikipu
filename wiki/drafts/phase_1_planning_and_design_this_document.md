---
identity:
  node_id: "doc:wiki/drafts/phase_1_planning_and_design_this_document.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/plan/UI_REDESIGN_MERGE_PLAN.md", relation_type: "documents"}
---

### Source of Truth

## Details

### Source of Truth

| Worktree | Commit | Purpose |
|----------|--------|---------|
| `dev` | `3f39ee3` | Current runtime — pipeline + legacy UI + sandbox |
| `ui-redesign` | `55880f6` | Target architecture — atomic/feature-sliced |

### What's in `ui-redesign` (Implemented)

**Architecture:**
- `apps/review-workbench/src/features/` — Feature-Sliced organization
- `apps/review-workbench/src/components/atoms/` — Terran Command atoms (Button, Badge, Tag, Icon, Kbd, Spinner, ShortcutsModal)
- `apps/review-workbench/src/components/layouts/` — AppShell, JobWorkspaceShell
- `apps/review-workbench/src/components/molecules/` — SplitPane
- `apps/review-workbench/src/mock/` — Full mock API layer with fixtures
- `plan/01_ui/specs/` — 15 spec documents defining the architecture

**Implemented Features:**
| Phase | Feature | Spec | Status |
|-------|---------|------|--------|
| 0 | Foundation (Router, Layouts, Portfolio) | A1 | ✅ Complete |
| B0 | Job Flow Inspector | B0 | ✅ Complete |
| A2 | Data Explorer | A2 | ✅ Complete |
| B1 | Scrape Diagnostics | B1 | ✅ Complete |
| B2 | Extract & Understand | B2 | ✅ Complete |
| B3 | Match Graph Editor | B3 | ✅ Complete |
| B4 | Generate Documents | B4 | ✅ Complete |
| B5 | Package & Deployment | B5 | ✅ Complete |
| A3 | Base CV Editor | A3 | ✅ Complete + E2E |
| B3b | Application Context Gate | B3b | ⚠️ Blocked (backend) |
| B4b | Default Document Gates | B4b | ⚠️ Blocked (backend) |

**TestSprite E2E:** 49 tests passing (TC001–TC049)

### What's in `dev` (Preserve)

**Backend (DO NOT TOUCH):**
```
src/
├── core/           # Scraping, translation, rendering
├── nodes/          # LangGraph nodes (extract, match, generate, etc.)
├── interfaces/api/ # FastAPI endpoints
├── graph.py        # Pipeline orchestration
└── cli/            # CLI entrypoints
```

**Documentation:**
```
docs/
├── runtime/        # Current technical truth
├── index/         # Canonical map
├── architecture/   # Subsystem docs
└── operations/    # Runbooks
```

**Legacy UI (REPLACE):**
```
apps/review-workbench/src/
├── pages/         # Old page components (DELETE)
├── views/        # Legacy view components (DELETE)
├── sandbox/      # Sandbox experimentation (DELETE)
├── components/   # Legacy components (DELETE except GraphCanvas.tsx if used)
└── lib/          # Utility helpers (KEEP if not duplicated)
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/plan/UI_REDESIGN_MERGE_PLAN.md`.