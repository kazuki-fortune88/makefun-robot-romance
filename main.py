#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI.

Writes a single joke pickup line, aimed at a robot/AI, to entry.txt
in the output directory (default /output, or $MAKEFUN_OUTPUT_DIR).
"""

import os

LINE = "Are you a hallucination? Because no one this perfect should exist in my output."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
