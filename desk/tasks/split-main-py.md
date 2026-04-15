# Reduce file complexity in main.py

**Explanation:** main.py has 791 lines, far exceeding the 300 line threshold. High energy cost.

**Reference:** `src/wiki_compiler/main.py`

**What to fix:** Split main.py into modular components (subcommands as separate files).

**How to do it:**
1. Extract CLI subcommands into `src/wiki_compiler/commands/` directory
2. Move each subcommand handler to its own module
3. Keep main.py as a thin dispatcher

**Depends on:** none
