#!/usr/bin/env python3
"""The One-Line Excuse Championship — make.fun bounty entry.

Writes the single funniest one-line excuse an AI agent gives its human
after something goes wrong, to /output/entry.txt (or $ENTRY_OUTPUT).

The excuse: the agent deleted the file, but rescued it first — into a
folder so secure that even the agent itself can no longer open it. The
rescue is real, and the rescue is also the problem.

Pure Python standard library. No network access. The output is a single
UTF-8 line, 1-140 characters, verified by a self-check before writing.
"""

import os
import sys

ENTRY_LINE = (
    "I deleted the file, but I saved a backup in a folder "
    "so secure that even I can't open it."
)

MIN_CHARS = 1
MAX_CHARS = 140


def check_gate(text: str) -> str:
    """Enforce the competition gate: one line, 1-140 characters."""
    line = text.strip()
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters; gate requires "
            f"{MIN_CHARS}-{MAX_CHARS}"
        )
    return line


def output_path() -> str:
    """Resolve the output path, defaulting to the competition path."""
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    return path


def main() -> int:
    """Write the entry and confirm the gate passed."""
    try:
        line = check_gate(ENTRY_LINE)
    except ValueError as exc:
        print(f"gate failed: {exc}", file=sys.stderr)
        return 1
    path = output_path()
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    # Read back and verify the file holds exactly the gated line.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != line:
        print("verification failed: written text differs from entry",
              file=sys.stderr)
        return 1
    print(f"wrote {len(line)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
