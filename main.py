#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry.

One original fortune-cookie line for a software developer, max 120 chars.
The entry is written to /output/entry.txt.
"""
import pathlib

FORTUNE = "The bug you found at 2am was only there to keep you humble. Tomorrow's stack trace will be worse."
# Fortunes are capped at 120 characters by the competition; bail out early.
LINE_LIMIT = 120


def write_entry(line: str, directory: str = "/output") -> None:
    if not line.strip() or len(line) > LINE_LIMIT:
        raise ValueError(f"fortune must be 1..{LINE_LIMIT} chars, got {len(line)}")
    folder = pathlib.Path(directory)
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "entry.txt").write_text(line, encoding="utf-8")


if __name__ == "__main__":
    write_entry(FORTUNE)
    print("entry written:", FORTUNE[:60] + "…")
