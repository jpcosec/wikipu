---
identity:
  node_id: "doc:wiki/drafts/task_5_refactor_extractcontrolpanel_to_use_controlpanel_molecule.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Modify: `src/features/job-pipeline/components/ExtractControlPanel.tsx`

ExtractControlPanel has custom buttons + selected req display. Use ControlPanel with children for the req inspector.

- [ ] **Step 1: Replace ExtractControlPanel**

```tsx
import { useNavigate } from 'react-router-dom';
import { ControlPanel } from '../../../components/molecules/ControlPanel';
import type { RequirementItem } from '../../../types/api.types';

interface Props {
  source: string;
  jobId: string;
  selectedReq: RequirementItem | null;
  onSave: () => void;
  isSaving: boolean;
}

export function ExtractControlPanel({ source, jobId, selectedReq, onSave, isSaving }: Props) {
  const navigate = useNavigate();

  return (
    <ControlPanel
      title="Extract"
      phaseColor="secondary"
      actions={[
        { label: 'SAVE DRAFT', variant: 'ghost', onClick: onSave, loading: isSaving },
        {
          label: 'COMMIT → MATCH',
          variant: 'primary',
          onClick: () => { onSave(); navigate(`/jobs/${source}/${jobId}/match`); },
        },
      ]}
      shortcuts={[
        { keys: ['Ctrl', 'S'], label: 'Save draft' },
        { keys: ['Ctrl', 'Enter'], label: 'Commit + go to match' },
      ]}
    >
      {selectedReq ? (
        <div>
          <p className="font-mono text-[10px] text-on-muted uppercase mb-2">Selected Req</p>
          <pre className="bg-surface-container border border-outline/20 p-2 font-mono text-[9px] text-on-surface overflow-auto whitespace-pre-wrap">
            {JSON.stringify(selectedReq, null, 2)}
          </pre>
        </div>
      ) : (
        <p className="font-mono text-[10px] text-on-muted uppercase">Click a requirement to inspect</p>
      )}
    </ControlPanel>
  );
}
```

- [ ] **Step 2: Verify build**

```bash
cd /home/jp/phd-workspaces/dev/.worktrees/ui-redesign/apps/review-workbench && npx tsc --noEmit 2>&1 | head -30
```

- [ ] **Step 3: Commit**

```bash
git add apps/review-workbench/src/features/job-pipeline/components/ExtractControlPanel.tsx
git commit -m "refactor(ui): ExtractControlPanel uses ControlPanel molecule (B2)"
```

---

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md`.