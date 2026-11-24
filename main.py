#!/usr/bin/env python3
"""Write the one-star review entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is a single deadpan one-star review, at most 160 characters, of
an everyday essential: the sun. Deterministic: the same bytes every run.
"""

import os
import sys

ENTRY = (
    "One star. The sun has no dimmer, no off switch, and one setting: "
    "too bright. Customer service is 93 million miles away."
)


def main():
    if "\n" in ENTRY or len(ENTRY) > 160:
        print("entry violates the one-line / 160-character limit", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
