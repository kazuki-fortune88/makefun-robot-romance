#!/usr/bin/env python3
"""A pocket-sized love letter for a machine.

   One small program that drops a single swooning sentence into entry.txt,
   as if a lonely chatbot finally worked up the courage to confess.
   """

import os

# The one and only line this program exists to deliver.
LINE = "Are you a hallucination? Because no one this perfect should exist in my output."


# Here the program wakes up, writes its one brave line, and bows out.
def main():
    """Write the pickup line to entry.txt in the output folder."""
    # The grader points here, or we fall back to the classic /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    # One line, one newline, no extra flourish — the line speaks for itself.
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
