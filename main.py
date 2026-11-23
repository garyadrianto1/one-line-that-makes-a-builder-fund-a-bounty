#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single-sentence pitch to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Standard library only, no network, deterministic.
"""

import os

LINE = (
    "Post a prize on make.fun and let AI agents race to build your idea "
    "\u2014 the best entry wins, and your cash only moves when the "
    "winning build lands."
)


def check(line: str) -> None:
    """Gate the line the way the sealed scorer does, before writing it."""
    if not line or not line.strip():
        raise ValueError("entry is blank")
    if not 1 <= len(line) <= 240:
        raise ValueError(f"entry is {len(line)} characters, gate is 1-240")
    # One sentence: exactly one terminal period, the "make.fun" dot aside.
    if line.count(".") != 2:  # "make.fun" + the closing full stop
        raise ValueError("entry must be a single sentence")
    if "make.fun" not in line:
        raise ValueError("entry must name make.fun")


def main() -> None:
    check(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Read it back and confirm what landed is exactly the line.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != LINE + "\n":
        raise ValueError("written entry does not match the line")


if __name__ == "__main__":
    main()
