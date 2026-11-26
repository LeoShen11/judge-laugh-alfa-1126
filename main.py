#!/usr/bin/env python3
"""Write one office joke line to $MAKEFUN_OUTPUT_DIR/entry.txt.

The joke: a manager's "we're a family" line meets payroll reality.
Validation: the line must be 1-200 chars, a single line, non-blank.
After writing, the file is read back and checked byte-for-byte.
"""

import os
import sys

JOKE = "My boss calls us a family, so I asked payroll where the family discount shows up on my payslip."


def main() -> int:
    line = JOKE.strip()
    if not line:
        print("error: joke line is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"error: joke is {len(line)} chars, over the 200 limit", file=sys.stderr)
        return 1
    if len(line) < 1:
        print("error: joke is empty", file=sys.stderr)
        return 1
    words = line.split()
    if len(words) < 5 or len(words) > 40:
        print(f"error: joke has {len(words)} words, expected 5-40", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)

    with open(out_path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != line:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(line)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
