---
identity:
  node_id: "doc:wiki/drafts/canonical_layout.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/runtime/data_management.md", relation_type: "documents"}
---

All schema-v0 jobs live under:

## Details

All schema-v0 jobs live under:

```text
data/jobs/<source>/<job_id>/
```

Each job root contains a single lifecycle file:

```text
meta.json
```

And per-node outputs under:

```text
nodes/<node_name>/<stage>/<artifact>
```

Example:

```text
data/jobs/stepstone/12345/
  meta.json
  nodes/
    ingest/
      proposed/
        state.json
        content.md
        raw_page.html
        cleaned_page.html
        raw_extracted.json
        listing.json
        listing_case.json
        listing_case.md
        listing_case.html
        listing_case.cleaned.html
        listing_content.md
        listing_page.html
        listing_page.cleaned.html
        scrape_meta.json
      failed/
        state.json
        content.md
        raw_page.html
        cleaned_page.html
        raw_extracted.json
        listing.json
        listing_case.json
        scrape_meta.json
    translate/
      proposed/
        state.json
        content.md
    extract_bridge/
      proposed/
        state.json
        content.md
    match_skill/
      approved/
        state.json
      review/
        current.json
        decision.json
        rounds/
          round_001/
            proposal.json
            decision.json
            feedback.json
    generate_documents/
      proposed/
        deltas.json
        cv.md
        cover_letter.md
        email_body.txt
      review/
        assist.json
    render/
      proposed/
        cv.pdf
        cover_letter.pdf
    package/
      final/
        manifest.json
        cv.pdf
        cover_letter.pdf
        email_body.txt
```

---

Generated from `raw/docs_postulador_refactor/docs/runtime/data_management.md`.