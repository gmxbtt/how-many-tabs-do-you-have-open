#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — make.fun entry.

Writes one honest tab count — a single number, digits only — to
/output/entry.txt. No words, no punctuation, no newline: just the
digits, exactly as the competition gate requires (1-5 UTF-8
characters, not only whitespace).

The count: 619.
"""

import os
import sys

# The honest count of browser tabs open at the moment this entry
# was built: 619 tabs, spread across several windows — research,
# bounty docs, half-read articles and rabbit holes never closed.
TAB_COUNT = "619"

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # The gate demands exactly one number, digits only, 1-5 chars.
    if not TAB_COUNT.isdigit() or not 1 <= len(TAB_COUNT) <= 5:
        print("invalid tab count", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TAB_COUNT)

    # Read-back verification: the file must hold exactly these bytes.
    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    if data != TAB_COUNT.encode("utf-8"):
        print("verification failed: unexpected bytes", file=sys.stderr)
        return 1

    # One short confirmation line on stdout; the file itself stays
    # byte-exact (digits only, no trailing newline).
    print(f"wrote {len(data)} byte(s) to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
