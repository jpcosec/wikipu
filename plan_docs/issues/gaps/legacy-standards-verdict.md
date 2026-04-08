# Legacy Standards Verdict

**Explanation:** There is content in `raw/` that represents old standards that were never formally accepted or discarded. This creates noise in the "origin" of the knowledge graph.

**Reference:** `raw/old_standards/` (if it exists, based on design commentary)
Wait, let me check if `raw/old_standards/` actually exists.
The design commentary says: "The `raw/old_standards/` content is a decision that was never made."

**What to fix:** Give a final verdict (via ADR) and potentially delete the source material if it's completely superseded.

**How to do it:** 
1. Perform a "Legacy Audit" (Stage 2.1 of Issues Guide).
2. For each file in `raw/old_standards/`, decide if it's been refined into a current rule or is obsolete.
3. Record the decision in a new ADR in `wiki/adrs/`.
4. Delete the files from `raw/` if they are truly obsolete and replaced by ADR. (Wait, `raw/` is supposedly immutable, but if it's legacy clutter, we must decide).

**Depends on:** none
