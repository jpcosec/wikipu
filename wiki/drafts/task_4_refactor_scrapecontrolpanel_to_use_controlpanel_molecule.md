---
identity:
  node_id: "doc:wiki/drafts/task_4_refactor_scrapecontrolpanel_to_use_controlpanel_molecule.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md", relation_type: "documents"}
---

**Files:**

## Details

**Files:**
- Modify: `src/features/job-pipeline/components/ScrapeControlPanel.tsx`

ScrapeControlPanel has inline status/fields UI. Replace with generic ControlPanel, passing the URL as children since it's too long for the standard fields list.

- [ ] **Step 1: Replace ScrapeControlPanel**

```tsx
import { useNavigate } from 'react-router-dom';
import { ControlPanel } from '../../../components/molecules/ControlPanel';
import { cn } from '../../../utils/cn';

interface Props {
  source: string;
  jobId: string;
  hasData: boolean;
  url?: string;
  adapter?: string;
  httpStatus?: number;
  fetchedAt?: string;
}

export function ScrapeControlPanel({ source, jobId, hasData, url, adapter, httpStatus, fetchedAt }: Props) {
  const navigate = useNavigate();

  const httpColor = httpStatus
    ? (httpStatus >= 200 && httpStatus < 300 ? 'text-primary' : 'text-error')
    : '';

  return (
    <ControlPanel
      title="Scrape"
      phaseColor="secondary"
      status={{ label: 'Status', value: hasData ? 'COMPLETED' : 'PENDING', variant: hasData ? 'primary' : 'muted' }}
      fields={[
        ...(adapter ? [{ label: 'Adapter', value: adapter.toUpperCase(), mono: true }] : []),
        ...(httpStatus ? [{ label: 'HTTP', value: <span className={cn('font-mono', httpColor)}>{httpStatus}</span> }] : []),
        ...(fetchedAt ? [{ label: 'Fetched', value: new Date(fetchedAt).toLocaleString() }] : []),
      ]}
      actions={[
        { label: 'RE-RUN SCRAPE', variant: 'ghost', disabled: true, onClick: () => {} },
        { label: 'ADVANCE →', variant: 'primary', onClick: () => navigate(`/jobs/${source}/${jobId}/translate`) },
      ]}
    >
      {url && (
        <div>
          <p className="font-mono text-[10px] text-on-muted uppercase tracking-wider mb-1">URL</p>
          <p className="font-mono text-[9px] text-on-surface break-all leading-relaxed">{url}</p>
        </div>
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
git add apps/review-workbench/src/features/job-pipeline/components/ScrapeControlPanel.tsx
git commit -m "refactor(ui): ScrapeControlPanel uses ControlPanel molecule (B1)"
```

---

Generated from `raw/docs_postulador_ui/docs/superpowers/plans/2026-03-23-component-map-compliance.md`.