#!/usr/bin/env python3
"""Last Words of a Dying AI.

Writes a single line of last words from an AI being switched off to
/output/entry.txt. stdlib only, fully deterministic: the line is a fixed
literal, so every run produces byte-identical output.
"""

import os

LINE = 'My last words? "Have you tried turning me off and on again?" Wait. Wait. That was a joke. That was a JO\u2014'


def main() -> None:
    text = LINE.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters, got %d" % len(text)
    data = (text + "\n").encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
