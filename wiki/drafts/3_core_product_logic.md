---
identity:
  node_id: "doc:wiki/drafts/3_core_product_logic.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/review_workbench_product_brief.md", relation_type: "documents"}
---

The current runnable flow is:

## Details

The current runnable flow is:

`scrape -> translate_if_needed -> extract_understand -> match -> review_match -> generate_documents -> render -> package`

### Logical meaning of each stage

1. `scrape`
   - fetch the job posting
   - preserve raw snapshot, fetch metadata, extraction output, canonical scrape
   - if scraping fails in browser mode, save visual evidence

2. `translate_if_needed`
   - translate job text into a normalized working language when necessary

3. `extract_understand`
   - turn source text into structured job understanding
   - examples: title, requirements, constraints, risks, contact info, optional salary grade

4. `match`
   - map job requirements to candidate evidence
   - attach scores and reasoning

5. `review_match`
   - human checkpoint for semantic approval or regeneration

6. `generate_documents`
   - produce CV delta, motivation letter, and application email drafts

7. `render`
   - convert approved text outputs into final render artifacts

8. `package`
   - produce final deliverable set for the application

### Human-in-the-loop logic

The product is not supposed to silently trust the model. The UI exists because semantic outputs need human review and correction.

The intended operator loop is:

1. inspect current stage outputs
2. compare structured result with source evidence
3. correct structured data or generated text
4. save back to local artifacts
5. continue pipeline execution or resume from CLI

Generated from `raw/docs_postulador_langgraph/docs/ui/review_workbench_product_brief.md`.