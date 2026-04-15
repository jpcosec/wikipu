import argparse
import sys
from pathlib import Path

def handle_read(args: argparse.Namespace) -> None:
    path = Path(args.file)
    if not path.exists():
        print(f"[ERROR] File not found: {args.file}")
        sys.exit(1)
    
    try:
        content = path.read_text(encoding="utf-8")
        print(content)
    except Exception as e:
        print(f"[ERROR] Could not read file {args.file}: {e}")
        sys.exit(1)
