#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — make.fun entry.

Writes exactly one excuse, in the dog's own voice, to /output/entry.txt.
Deterministic: the same line on every run.
"""

import os

ENTRY = "It smelled like the park, so I ate the park. The homework was just in the way."

# Bounty gate: /output/entry.txt must be UTF-8, a single line, 1-200 characters.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY, "entry must be a single line"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
