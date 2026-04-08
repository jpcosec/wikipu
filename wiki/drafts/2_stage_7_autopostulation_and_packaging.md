---
identity:
  node_id: "doc:wiki/drafts/2_stage_7_autopostulation_and_packaging.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/09_autopostulation_deployment.md", relation_type: "documents"}
---

This stage depends entirely on the Application Method identified in the initial scrape.

## Details

This stage depends entirely on the Application Method identified in the initial scrape.

### Scenario A: Email Application

| Element | Description |
|---------|-------------|
| **UI Action** | "Prepare Email Draft" button |
| **Result** | Opens email client with body, subject, and PDFs attached |
| **Package** | Folder with `email_body.txt` and final rendered documents |

### Scenario B: Internal Portal / Form (Fast Apply)

| Element | Description |
|---------|-------------|
| **UI Action** | "Download Application Package" button |
| **Result** | `.zip` file named with `job_id` containing everything in correct order |
| **Checklist** | List of common fields (profile URL, LinkedIn, Phone) for quick copy-paste |

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/09_autopostulation_deployment.md`.