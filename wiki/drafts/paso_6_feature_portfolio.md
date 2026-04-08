---
identity:
  node_id: "doc:wiki/drafts/paso_6_feature_portfolio.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/proposals/phase_0_foundation.md", relation_type: "documents"}
---

### `src/features/portfolio/api/usePortfolioSummary.ts`

## Details

### `src/features/portfolio/api/usePortfolioSummary.ts`

```ts
import { useQuery } from '@tanstack/react-query';
import { getPortfolioSummary } from '../../../api/client';

export function usePortfolioSummary() {
  return useQuery({
    queryKey: ['portfolio', 'summary'],
    queryFn: getPortfolioSummary,
    staleTime: 60_000,
  });
}
```

### `src/features/portfolio/components/PortfolioTable.tsx`

```tsx
import { useNavigate } from 'react-router-dom';
import type { PortfolioSummary } from '../../../types/models';
import { Badge } from '../../../components/atoms/Badge';

const STATUS_VARIANT: Record<string, 'primary' | 'secondary' | 'success' | 'danger' | 'muted'> = {
  completed:    'success',
  pending_hitl: 'secondary',
  running:      'primary',
  failed:       'danger',
  archived:     'muted',
  failed:        'danger',
};

interface Props {
  data?: PortfolioSummary;
  loading: boolean;
  error: boolean;
}

export function PortfolioTable({ data, loading, error }: Props) {
  const navigate = useNavigate();

  if (loading) return <p className="text-on-muted font-mono text-sm">Loading...</p>;
  if (error)   return <p className="text-error font-mono text-sm">Failed to load portfolio.</p>;
  if (!data)   return null;

  return (
    <table className="w-full text-sm border-collapse">
      <thead>
        <tr className="text-[10px] font-mono text-on-muted uppercase tracking-widest border-b border-outline/20">
          <th className="text-left py-2 pr-6">Source / Job ID</th>
          <th className="text-left py-2 pr-6">Current Stage</th>
          <th className="text-left py-2 pr-6">Status</th>
          <th className="text-left py-2">Updated</th>
        </tr>
      </thead>
      <tbody>
        {data.jobs.map((job) => (
          <tr
            key={job.job_id}
            className="border-b border-outline/10 hover:bg-surface-low transition-colors cursor-pointer"
            onClick={() => navigate(`/jobs/${job.source}/${job.job_id}`)}
          >
            <td className="py-3 pr-6 font-mono">
              <span className="text-on-muted">{job.source} / </span>
              <span className="text-primary">{job.job_id}</span>
            </td>
            <td className="py-3 pr-6 font-mono text-on-surface">{job.current_node}</td>
            <td className="py-3 pr-6">
              <Badge variant={STATUS_VARIANT[job.status] ?? 'muted'}>{job.status}</Badge>
            </td>
            <td className="py-3 font-mono text-on-muted text-xs">{job.updated_at}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
```

### `src/pages/global/PortfolioDashboard.tsx`

```tsx
import { usePortfolioSummary } from '../../features/portfolio/api/usePortfolioSummary';
import { PortfolioTable } from '../../features/portfolio/components/PortfolioTable';

export function PortfolioDashboard() {
  const { data, isLoading, isError } = usePortfolioSummary();
  return (
    <div className="p-6">
      <p className="font-mono text-[10px] text-primary uppercase tracking-widest">System / PhD 2.0</p>
      <h1 className="font-headline text-xl font-bold text-on-surface mt-1 mb-6">Application Portfolio</h1>
      <PortfolioTable data={data} loading={isLoading} error={isError} />
    </div>
  );
}
```

---

Generated from `raw/docs_postulador_ui/plan/01_ui/proposals/phase_0_foundation.md`.