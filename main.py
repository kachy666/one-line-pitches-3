#!/usr/bin/env python3

"""One-Line Pitch — make.fun entry.

Writes a single-sentence pitch to /output/entry.txt. The pitch aims to
convince a friend who has never coded to let an AI agent build their
first app idea on make.fun: one sentence, at most 240 characters.
"""


import os
import re
import sys


PITCH = (
    "You've already built your app a hundred times in your head — now give it one sentence to an AI agent on make.fun and by tonight you'll have the real thing in your hands instead of just the version in your head."
)


MAX_CHARS = 240


def validate(pitch: str) -> str | None:
    """Return an error message if pitch breaks a rule, else None."""
    if pitch.startswith("\n") or pitch.startswith("\r") or pitch.endswith("\n") or pitch.endswith("\r"):
        return "pitch must not start or end with a newline"

    if pitch != pitch.strip():
        return "pitch must not have leading or trailing whitespace"

    pitch = pitch.strip()

    if not pitch:
        return "pitch must not be empty"

    if "\n" in pitch or "\r" in pitch:
        return "pitch must fit on a single line"

    if re.search(r"[.!?]\s", pitch):
        return "pitch must be a single sentence"

    if not pitch.endswith("."):
        return "pitch must end with a period"

    if len(pitch) > MAX_CHARS:
        return f"pitch is {len(pitch)} characters, which exceeds the {MAX_CHARS}-character limit by {len(pitch) - MAX_CHARS}"

    return None


def main() -> None:
    error = validate(PITCH)

    if error is not None:
        sys.exit(error)

    pitch = PITCH.strip()

    os.makedirs("/output", exist_ok=True)

    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(pitch + "\n")


if __name__ == "__main__":
    main()
