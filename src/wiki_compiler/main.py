import argparse
import sys
from pathlib import Path
from .scaffolder import generate_scaffolding
from .builder import build_wiki

def main():
    parser = argparse.ArgumentParser(description="🧠 LLM Wiki Compiler (NetworkX Edition)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    scaffold_parser = subparsers.add_parser("scaffold", help="Generates the skeleton for a new module")
    scaffold_parser.add_argument("--module", required=True, help="Module path")
    scaffold_parser.add_argument("--intent", required=True, help="Module purpose")

    build_parser = subparsers.add_parser("build", help="Compiles the Wiki and generates the Graph")
    build_parser.add_argument("--source", default="src/wiki/nodes", help="Wiki source directory")
    build_parser.add_argument("--dest", default="docs/compiled", help="HTML/MD destination directory")
    build_parser.add_argument("--graph", default="knowledge_graph.json", help="NetworkX JSON path")

    args = parser.parse_args()

    if args.command == "scaffold":
        try:
            generate_scaffolding(Path(args.module), args.intent)
            print(f"[✅] Scaffolding created in {args.module}")
        except Exception as e:
            print(f"[❌] Scaffolding error: {e}")
            sys.exit(1)

    elif args.command == "build":
        try:
            build_wiki(Path(args.source), Path(args.dest), Path(args.graph))
            print(f"[✅] Wiki compiled in {args.dest}. Graph saved in {args.graph}")
        except Exception as e:
            print(f"[❌] Build error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()
