# Refactor main.py:main function

**Explanation:** main.py:main has 1489 statements - the main CLI entry point needs refactoring.

**Reference:** `src/wiki_compiler/main.py:1489`

**What to fix:** Extract subcommand handlers from main() into separate modules. Main should only dispatch to subcommand modules.

**How to do it:**
1. Create `src/wiki_compiler/commands/` directory
2. Extract each subcommand logic to its own module
3. Main becomes: `from commands import build, query, audit; build.run(args)`

**Depends on:** split-main-py
