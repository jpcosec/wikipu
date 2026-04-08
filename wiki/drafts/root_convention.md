---
identity:
  node_id: "doc:wiki/drafts/root_convention.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/05_data_architecture.md", relation_type: "documents"}
---

The job folder follows this convention to support local-first flow and feedback loop:

## Details

The job folder follows this convention to support local-first flow and feedback loop:

```
data/jobs/<source>/<job_id>/
├── raw/                      # Original text and screenshots
│   ├── source_text.md
│   └── error_screenshot.png
├── nodes/
│   ├── extract/              # Text Tagger results
│   │   └── state.json
│   ├── match/                # Requirements <-> Evidence (JSON)
│   │   └── state.json
│   ├── strategy/             # Delta and motivations (JSON)
│   │   └── delta.json
│   ├── drafting/             # Final .md documents
│   │   ├── cv.md
│   │   ├── cover_letter.md
│   │   └── email.md
│   └── review/               # User decisions and comments
│       └── decisions.json
├── feedback/                 # Corrections captured for future cycles
│   └── *.md
└── final/                    # PDFs and application packages
    ├── cv.pdf
    ├── cover_letter.pdf
    └── package.zip
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/05_data_architecture.md`.