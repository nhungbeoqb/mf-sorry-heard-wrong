#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — the apology a smart speaker gives its owner
after mishearing 'feed the dog' as 'feed the fog'.

Writes the single apology line to entry.txt in the output directory
(default: /output, overridable with OUTPUT_DIR for local runs).
Pure Python 3 standard library; deterministic output.
"""

import os

LINE = (
    "Sorry, I heard 'feed the dog' as 'feed the fog' \u2014 "
    "a week's kibble is scattered on the lawn, "
    "and the mist now waits by the back door at six."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
