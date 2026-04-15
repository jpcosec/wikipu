"""
Read command for wiki-compiler.
Allows direct reading of files from the CLI.
"""
import argparse
import sys
from pathlib import Path

def handle_read(args: argparse.Namespace) -> None:
    """
    Handle the read command by printing the contents of the specified file.
    Exits with code 1 if the file does not exist or cannot be read.
    """
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
