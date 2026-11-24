#!/usr/bin/env python3
"""Write one sick-day excuse for the make.fun bounty.

Deterministic, standard library only: it always writes the same
single line to ``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (default /output).
"""

import os

# The excuse: half believable (food poisoning is a classic sick day),
# fresh (self-inflicted by your own cooking, not a fever or a dead
# grandmother), and the laugh lands on the last word — the shame
# hurting more than the stomach.
LINE = (
    "Sorry, can't come in \u2014 I gave myself food poisoning with my "
    "own cooking, and honestly the shame hurts more than the stomach."
)

MAX_CHARS = 200


def main() -> None:
    if not LINE.strip():
        raise ValueError("entry must not be blank")
    if len(LINE) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(LINE)} chars, over the {MAX_CHARS} limit"
        )
    if "\n" in LINE:
        raise ValueError("entry must be exactly one line")
    if LINE != LINE.strip() or not LINE.endswith("."):
        raise ValueError("entry must be one trimmed line ending in a period")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
