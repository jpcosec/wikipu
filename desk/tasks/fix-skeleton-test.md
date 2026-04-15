# Fix test_run_skeleton_auto_ingest

**Explanation:** Test fails with git subprocess error 128 - likely a git init/clone issue in the test environment.

**Reference:** `tests/test_run_skeleton.py`

**What to fix:** The test invokes skeleton which runs `git status --short`. Need to ensure proper git initialization or mock the git call.

**How to do it:**
1. Check test_setup in test_run_skeleton.py
2. Add git init before skeleton command or mock the git subprocess

**Depends on:** none
