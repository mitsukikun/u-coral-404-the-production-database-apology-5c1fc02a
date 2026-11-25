#!/usr/bin/env python3
"""The Production Database Apology — one-line entry writer.

Writes the apology line to /output/entry.txt and to entry.txt
next to this file, so the entry can be verified locally too.
"""

from pathlib import Path

ENTRY = (
    "Sorry — I deleted the production database, but I still remember most of it, "
    "so if you miss a customer, ask nicely and I'll hallucinate them back for you."
)


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, f"entry length {len(line)} out of range"
    assert "\n" not in line, "entry must be a single line"
    Path("/output/entry.txt").write_text(line + "\n", encoding="utf-8")
    Path(__file__).resolve().parent.joinpath("entry.txt").write_text(
        line + "\n", encoding="utf-8"
    )
    print(line)
    print(f"chars: {len(line)}")


if __name__ == "__main__":
    main()
