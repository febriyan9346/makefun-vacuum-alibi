#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes the vacuum's one-line excuse to <output dir>/entry.txt.

The line (127 characters, one line, UTF-8):
  Log 812: after 47 attempts, the spot is still there. I have
  reclassified it as a roommate. It pays no rent, and I respect that.

Output location follows the make.fun program/v1 rule:
  os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") + makedirs(exist_ok=True).
"""

import os

LINE = (
    "Log 812: after 47 attempts, the spot is still there. "
    "I have reclassified it as a roommate. "
    "It pays no rent, and I respect that."
)


def main() -> None:
    # Gate mirror: the sealed scorer requires 1-200 chars, one line,
    # not whitespace-only. Fail loudly here instead of shipping invalid.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert "\n" not in LINE and LINE.strip(), "line must be a single non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")
    print(f"wrote {path} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
