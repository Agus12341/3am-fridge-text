#!/usr/bin/env python3
"""Write the 3AM fridge text to entry.txt in the output folder."""

import os

# The gate checks entry.txt as UTF-8 text of 1 to 140 characters: this
# fridge text is 109 code points, one line, sent at 3 AM.
TEXT = "Alert: the yogurt expired on Tuesday. You did not. Put the cake down slowly and nobody tells the fitness app."


def write_entry(out_dir: str) -> None:
    """Write the fridge text, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
