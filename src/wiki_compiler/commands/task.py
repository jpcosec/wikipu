"""
Task command handler using SLDB for structured task documents.
"""

from __future__ import annotations
import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path


def handle_task(args: argparse.Namespace) -> None:
    """Execute the task command."""
    subcommand = args.subcommand.replace("-", "_")
    if subcommand == "list":
        list_tasks(args)
    elif subcommand == "validate":
        validate_tasks(args)
    elif subcommand == "complete":
        complete_task(args)
    elif subcommand == "render_board":
        render_board(args)
    else:
        print(f"Unknown subcommand: {args.subcommand}")
        sys.exit(1)


def list_tasks(args: argparse.Namespace) -> None:
    """List all tasks with optional filtering."""
    tasks_dir = Path(args.tasks_dir)
    if not tasks_dir.exists():
        print(f"Tasks directory not found: {tasks_dir}")
        sys.exit(1)

    model = "wiki_compiler.contracts.tasks:TaskDoc"
    pythonpath = str(Path(__file__).parent.parent.parent / "src")

    tasks = []
    for md_file in tasks_dir.glob("*.md"):
        if md_file.name == "Board.md":
            continue

        result = subprocess.run(
            [
                "sldb",
                "extract",
                model,
                str(md_file),
                "-",
                "--format",
                "json",
                "--pythonpath",
                pythonpath,
            ],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            data = json.loads(result.stdout)
            tasks.append(
                {
                    "file": md_file.name,
                    "status": data.get("frontmatter", {}).get("status"),
                    "priority": data.get("frontmatter", {}).get("priority"),
                    "title": data.get("title", ""),
                    "depends_on": data.get("frontmatter", {}).get("depends_on", []),
                }
            )

    status_filter = args.status
    priority_filter = args.priority

    if status_filter:
        tasks = [t for t in tasks if t["status"] == status_filter]
    if priority_filter:
        tasks = [t for t in tasks if t["priority"] == priority_filter]

    if args.json:
        print(json.dumps(tasks, indent=2))
    else:
        print(f"{'Status':<12} {'Priority':<8} {'Title':<40} {'File'}")
        print("-" * 90)
        for t in tasks:
            title = t["title"][:37] + "..." if len(t["title"]) > 40 else t["title"]
            print(f"{t['status']:<12} {t['priority']:<8} {title:<40} {t['file']}")


def validate_tasks(args: argparse.Namespace) -> None:
    """Validate all task files for roundtrip idempotency."""
    tasks_dir = Path(args.tasks_dir)
    if not tasks_dir.exists():
        print(f"Tasks directory not found: {tasks_dir}")
        sys.exit(1)

    model = "wiki_compiler.contracts.tasks:TaskDoc"
    pythonpath = str(Path(__file__).parent.parent.parent / "src")

    results = []
    for md_file in tasks_dir.glob("*.md"):
        if md_file.name == "Board.md":
            continue

        result = subprocess.run(
            [
                "sldb",
                "validate",
                model,
                "--input",
                str(md_file),
                "--pythonpath",
                pythonpath,
            ],
            capture_output=True,
            text=True,
        )

        results.append(
            {
                "file": md_file.name,
                "valid": result.returncode == 0,
                "output": result.stdout.strip()
                if result.returncode == 0
                else result.stderr.strip(),
            }
        )

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        all_valid = all(r["valid"] for r in results)
        for r in results:
            status = "✓" if r["valid"] else "✗"
            print(f"{status} {r['file']}")
            if not r["valid"]:
                print(f"  {r['output']}")
        print(f"\n{len([r for r in results if r['valid']])}/{len(results)} valid")

    sys.exit(0 if all_valid else 1)


def complete_task(args: argparse.Namespace) -> None:
    """Mark a task as completed."""
    tasks_dir = Path(args.tasks_dir)
    task_file = tasks_dir / args.task_id

    if not task_file.exists():
        task_file = tasks_dir / f"{args.task_id}.md"

    if not task_file.exists():
        print(f"Task not found: {args.task_id}")
        sys.exit(1)

    model = "wiki_compiler.contracts.tasks:TaskDoc"
    pythonpath = str(Path(__file__).parent.parent.parent / "src")

    result = subprocess.run(
        [
            "sldb",
            "extract",
            model,
            str(task_file),
            "-",
            "--format",
            "json",
            "--pythonpath",
            pythonpath,
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"Failed to extract task: {result.stderr}")
        sys.exit(1)

    data = json.loads(result.stdout)
    data["frontmatter"]["status"] = "completed"
    data["frontmatter"]["completed"] = str(date.today())

    result = subprocess.run(
        ["sldb", "render", model, "-", "-", "--pythonpath", pythonpath],
        input=json.dumps(data),
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print(f"Failed to render task: {result.stderr}")
        sys.exit(1)

    task_file.write_text(result.stdout)
    print(f"✓ Marked {task_file.name} as completed")


def render_board(args: argparse.Namespace) -> None:
    """Render Board.md from all task frontmatter."""
    tasks_dir = Path(args.tasks_dir)
    board_file = tasks_dir / "Board.md"

    model = "wiki_compiler.contracts.tasks:TaskDoc"
    pythonpath = str(Path(__file__).parent.parent.parent / "src")

    tasks = {"open": [], "in_progress": [], "completed": [], "blocked": []}

    for md_file in tasks_dir.glob("*.md"):
        if md_file.name == "Board.md":
            continue

        result = subprocess.run(
            [
                "sldb",
                "extract",
                model,
                str(md_file),
                "-",
                "--format",
                "json",
                "--pythonpath",
                pythonpath,
            ],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            data = json.loads(result.stdout)
            status = data.get("frontmatter", {}).get("status", "open")
            priority = data.get("frontmatter", {}).get("priority", "p3")
            title = data.get("title", "")
            depends_on = data.get("frontmatter", {}).get("depends_on", [])

            if status in tasks:
                tasks[status].append(
                    {
                        "file": md_file.stem,
                        "title": title,
                        "priority": priority,
                        "depends_on": depends_on,
                    }
                )

    board = """# Tasks Board

> **Single entry point for all active work.** Read this before starting any task.

## Active (status=open|in_progress)

| ID | Domain | Task | Priority | Depends On |
|----|--------|------|----------|------------|

"""

    for status in ["in_progress", "open"]:
        for t in tasks[status]:
            board += f"| {t['file']} | | {t['title']} | {t['priority']} | {', '.join(t['depends_on'])} |\n"

    board += """

## Blocked (status=blocked)

| ID | Domain | Task | Priority | Depends On |
|----|--------|------|----------|------------|

"""

    for t in tasks["blocked"]:
        board += f"| {t['file']} | | {t['title']} | {t['priority']} | {', '.join(t['depends_on'])} |\n"

    board += """---

**Working rules for every task:**

1. Check whether any existing test is no longer valid and delete it if needed.
2. Add new tests where necessary.
3. Run the relevant tests.
4. Update `changelog.md`.
5. Delete the solved task file from `desk/tasks/`.
6. Update this Board.
7. Make a commit that clearly states what was fixed, making sure all required files are staged.
"""

    board_file.write_text(board)
    print(f"✓ Updated {board_file}")
