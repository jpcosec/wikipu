# Fix test_delta_compile_workflow

**Explanation:** Test fails because stale node detection doesn't recognize that a live draft node has become stale when its source is modified.

**Reference:** `tests/test_delta_compile.py`

**What to fix:** The `detect_stale_nodes` function in drafts.py should detect when `wiki/drafts/` files are outdated vs their raw sources.

**How to do it:**
1. Check drafts.py detect_stale_nodes function
2. Add logic to compare draft timestamps against source timestamps
3. Fix manifest tracking for drafts

**Depends on:** none
