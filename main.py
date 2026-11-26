#!/usr/bin/env python3
"""The Self-Checkout Is Judging You.

Writes one line (at most 200 characters) to /output/entry.txt,
or to the path in ENTRY_OUTPUT when set. Standard library only.

The entry is checked against the competition gate before it is
written: 1-200 characters, a single line, plain ASCII. A bad entry
fails loudly here instead of shipping an invalid file to the judge.

Why this line works: it is petty about the one ritual that only
happens at a self-checkout -- weighing produce on the till's
scale -- and it turns that ritual into the whole joke. Twelve
yoghurts plus one banana weighed twice to save four cents is a
basket a stranger gets instantly, and the closer is a double
sting in the machine's smuggest voice: respect for the hustle,
fear of the lifestyle. No "unexpected item" cliche, no loyalty
card gag, nothing the field has already heard a hundred times.
"""

import os
import sys

MAX_ENTRY_CHARS = 200

ENTRY = (
    "Twelve yoghurts, and you weighed the banana twice to save "
    "four cents. I respect the hustle. I fear the lifestyle."
)


def validate_entry(entry: str) -> None:
    """Enforce the competition gate; exit non-zero on any violation."""
    if not 1 <= len(entry) <= MAX_ENTRY_CHARS:
        sys.exit(f"entry is {len(entry)} chars, gate allows 1-{MAX_ENTRY_CHARS}")
    if "\n" in entry or "\r" in entry:
        sys.exit("entry must be a single line")
    if not entry.isascii():
        sys.exit("entry must be plain ASCII")
    if not entry.strip():
        sys.exit("entry must not be only whitespace")


def main() -> None:
    validate_entry(ENTRY)
    output = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(output)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
