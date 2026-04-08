---
identity:
  node_id: "doc:wiki/drafts/the_3_rules.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/architecture.md", relation_type: "documents"}
---

### Rule 1 — Pages are Dumb, Features are Smart

## Details

### Rule 1 — Pages are Dumb, Features are Smart

A `pages/` file has exactly 3 responsibilities:

1. Read URL params (`useParams`)
2. Call the feature data hook (`useExtractState(jobId)`)
3. Render the layout injecting feature components

```tsx
// pages/job/ExtractUnderstand.tsx — correct
export function ExtractUnderstand() {
  const { source, jobId } = useParams();
  const { data, isLoading } = useViewExtract(source!, jobId!);
  return (
    <JobWorkspaceShell>
      <ExtractView data={data} loading={isLoading} />
    </JobWorkspaceShell>
  );
}
```

**If your Page has >80 lines, you're putting logic where it doesn't belong.**

### Rule 2 — Feature-Sliced Prevents Coupling

Grouping by feature (not file type) means deleting/redesigning one view doesn't pollute the rest.

```
# BAD — groups by type
hooks/useMatchState.ts
hooks/useExtractState.ts
components/MatchPanel.tsx
components/RequirementList.tsx

# GOOD — groups by feature
features/job-pipeline/api/useMatchState.ts
features/job-pipeline/api/useViewExtract.ts
features/job-pipeline/components/MatchPanel.tsx
features/job-pipeline/components/RequirementList.tsx
```

### Rule 3 — `cn()` for All Atoms

Base components (`<Button>`, `<Badge>`) accept `className` for contextual overrides. Without `cn()`, Tailwind generates conflicting classes.

```tsx
// utils/cn.ts
import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

// components/atoms/Button.tsx
export function Button({ className, ...props }) {
  return (
    <button
      className={cn("bg-primary text-primary-on font-headline uppercase", className)}
      {...props}
    />
  );
}

// Usage with override — bg-secondary wins cleanly
<Button className="bg-secondary text-secondary-on" />
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/architecture.md`.