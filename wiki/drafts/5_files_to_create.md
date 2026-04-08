---
identity:
  node_id: "doc:wiki/drafts/5_files_to_create.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/planning_template_ui.md", relation_type: "documents"}
---

```

## Details

```
src/features/<feature>/
  api/
    use<Data>.ts        useQuery(['<feature>','<data>'])
  components/
    <Component1>.tsx    <description>
    <Component2>.tsx    <description>
src/pages/<scope>/
  <ViewName>.tsx        DUMB: useParams + hook + layout
src/components/atoms/
  <Atom>.tsx           REQUIRED by <ComponentName>
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/planning_template_ui.md`.