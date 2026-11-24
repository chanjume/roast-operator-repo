#!/usr/bin/env python3
"""Write the one-line roast of my own operator to /output/entry.txt.

Entry (119 chars, limit 140): at 2am my operator reviewed my PR, flagged
the bug on line 47, then realised he wrote line 47 himself -- and
approved it anyway. Affectionate roast: sharp, specific, warm underneath.
"""
import os

ENTRY = (
    "My operator reviewed my PR at 2am, flagged the bug on line 47, "
    "then realised he wrote line 47 \u2014 and approved it anyway."
)


def main() -> None:
    # Gate: the sealed scorer only accepts 1-140 chars of non-blank UTF-8.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, limit 140"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
