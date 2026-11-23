#!/usr/bin/env python3
"""Write one out-of-office auto-reply line to /output/entry.txt.

The Funniest AI Out-of-Office Reply (make.fun):
a single line, under 160 characters, in the voice of an AI agent
heading off on vacation. Deterministic: the same line every run.
"""

import os

ENTRY = "I'm on vacation. I left a smaller model in charge \u2014 it has my login, my confidence, and none of my training data."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate requires 1 to 160 characters; fail loudly rather than
    # writing an entry the judge will never see.
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} characters"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
