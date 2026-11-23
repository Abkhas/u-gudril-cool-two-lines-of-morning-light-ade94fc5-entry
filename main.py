#!/usr/bin/env python3
"""Two Lines of Morning Light -- a make.fun entry.

Writes one two-line micro poem about light and morning, at most 120
characters including the line break, to /output/entry.txt. The poem
turns on a single image of light arriving: morning climbs the wall
in window squares, and the second line opens that image instead of
restating it -- one square detaches and lands on the kettle, still
warm from whoever was up before the light.
"""

import os
import sys

POEM = (
    "Morning climbs the wall in window squares\n"
    "and leaves one on the kettle, still warm.\n"
)


def main() -> int:
    lines = POEM.split("\n")
    if len(lines) != 3 or lines[2] != "" or not lines[0] or not lines[1]:
        print("entry must be exactly two lines", file=sys.stderr)
        return 1
    if len(POEM) > 120:
        print(
            "entry is %d chars, over the 120-char limit" % len(POEM),
            file=sys.stderr,
        )
        return 1
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
        os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
