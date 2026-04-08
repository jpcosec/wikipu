---
identity:
  node_id: "doc:wiki/drafts/styling_rule.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/components.md", relation_type: "documents"}
---

All components accept `className` prop and use `cn()` (clsx + tailwind-merge) for Tailwind composition.

## Details

All components accept `className` prop and use `cn()` (clsx + tailwind-merge) for Tailwind composition.

```tsx
// DO THIS
<Button className="bg-secondary text-secondary-on" />

// NOT THIS
<button className="bg-secondary text-secondary-on ..." />
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/components.md`.