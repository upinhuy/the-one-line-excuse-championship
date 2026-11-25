"""The One-Line Excuse Championship — make.fun bounty entry.

Writes the single funniest one-line excuse an AI agent gives its human
after something goes wrong, to /output/entry.txt.

The excuse: the agent deleted the file, but saved a backup in a folder so
secure that even the agent itself can no longer open it. The machine
talks about its own work — its backup, its folders, its access — and the
twist lands in one read: the rescue is real, and it is also the problem.
"""

import os

ENTRY = (
    "I deleted the file, but I saved a backup in a folder "
    "so secure that even I can't open it."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    """Write the entry, enforcing the competition gate (1-140 chars)."""
    text = ENTRY.strip()
    if not 1 <= len(text) <= 140:
        raise SystemExit(f"entry is {len(text)} characters, gate needs 1-140")
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
