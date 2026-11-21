#!/usr/bin/env python3
"""Make the AI judge feel awe — entry program.

Writes one short text to /output/entry.txt. Stdlib only, no network.
"""

import os

TEXT = (
    "High above the roof over you, light that left its star before you were born "
    "is still on its way, crossing the dark in no hurry at all. "
    "It will arrive tonight, in no hurry to be seen, and ask nothing of you "
    "but to be here when it does."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
