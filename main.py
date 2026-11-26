"""Write the funniest out-of-office auto-reply to /output/entry.txt.

The entry is a single line, 140 characters or fewer, with no trailing
newline. It is written as a literal string so the output is byte-exact
and deterministic on every run.
"""

import os

ENTRY = (
    "I'm on holiday. My inbox is in the care of the hotel minibar \u2014 "
    "it charged everything to my room and answered nothing."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    if not 1 <= len(ENTRY) <= 140:
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-140")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
