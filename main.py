#!/usr/bin/env python3
"""Seventeen Syllables of Debugging (make.fun).

Writes the entry -- one haiku about debugging, three lines in the
5-7-5 syllable shape -- to /output/entry.txt, where the sealed
scorer reads it.
"""

import os

TEXT = "Cursor blinks at three\nthe log line lies, calm and still\none semicolon"

# The gate allows 1 to 200 characters; the haiku is three lines, 5-7-5
# syllables, joined by newlines with no trailing newline.
assert 1 <= len(TEXT) <= 200
assert len(TEXT.split("\n")) == 3 and not TEXT.endswith("\n")


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
