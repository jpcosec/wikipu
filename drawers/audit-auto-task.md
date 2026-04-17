# Auto-generate tasks from audit findings

**Explanation:** Audit finds compliance violations but they're not automatically tracked as tasks. This leads to violations being forgotten and accumulating.

**Reference:**
- `src/wiki_compiler/auditor.py`
- `desk/tasks/Board.md`

**What to fix:** The `wiki-compiler audit` command should auto-generate task files in `desk/tasks/` for each finding, or update an existing audit tracking task.

**How to do it:**
1. Add `--auto-task` flag to audit command
2. When violations found, create task files with:
   - Issue ID from audit finding (e.g., audit-fix-{check_name}-{node_id_hash})
   - Domain: compliance
   - Reference to the specific violation (file, line, check_name)
   - Auto-link to the failing code/doc
3. Update Board.md with new audit tasks

**Validation:**
- Run `wiki-compiler audit --auto-task` produces task files
- Board.md shows audit findings as tasks

**Depends on:** none
