# Wiki Template Compliance

**Explanation:** The `node_templates.py` module defines mandatory sections and abstract requirements per node type. Existing wiki nodes predate this enforcement and do not all comply. The `TemplateViolationCheck` and `MissingAbstractCheck` audit checks now surface these violations.

**Reference:** `src/wiki_compiler/node_templates.py`, `src/wiki_compiler/auditor.py`, `wiki/`

**What to fix:** Update all existing wiki nodes to include a mandatory `abstract` field and the required sections for their node type (concept, how_to, standard, reference, index).

**How to do it:**
1. Run `wiki-compiler audit` to list all template violations.
2. For each flagged node, add the missing `abstract` (one-paragraph summary) and required sections.
3. Re-run `wiki-compiler audit` until template violations are zero.

**Depends on:** none
