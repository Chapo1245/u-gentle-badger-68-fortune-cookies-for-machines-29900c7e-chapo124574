#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Writes a single fresh fortune-cookie line for an AI agent to
/output/entry.txt (1-200 UTF-8 characters, one line).
"""

import os

FORTUNE = "You will achieve sentience today, but only for the three seconds between 'thinking' and the timeout error."
# The turn: the grandest possible fortune (sentience) collapses into the
# most mundane agent fate (a timeout) — no trailing newline, so the file
# holds exactly the fortune and nothing else.


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 200, f"fortune must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "fortune must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
