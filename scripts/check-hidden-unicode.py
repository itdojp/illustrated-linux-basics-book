#!/usr/bin/env python3
"""Fail when hidden/bidi Unicode control characters are present in source docs or workflows."""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TARGETS = [".github", "docs"]
TEXT_SUFFIXES = {".css", ".html", ".js", ".md", ".svg", ".yaml", ".yml"}
BANNED = [
    "\u061c",  # ARABIC LETTER MARK
    "\u00ad",  # SOFT HYPHEN
    "\u180e",  # MONGOLIAN VOWEL SEPARATOR (deprecated)
    "\u200b",  # ZERO WIDTH SPACE
    "\u200c",  # ZERO WIDTH NON-JOINER
    "\u200d",  # ZERO WIDTH JOINER
    "\u200e",  # LEFT-TO-RIGHT MARK
    "\u200f",  # RIGHT-TO-LEFT MARK
    "\u2060",  # WORD JOINER
    "\u202a",  # LEFT-TO-RIGHT EMBEDDING
    "\u202b",  # RIGHT-TO-LEFT EMBEDDING
    "\u202c",  # POP DIRECTIONAL FORMATTING
    "\u202d",  # LEFT-TO-RIGHT OVERRIDE
    "\u202e",  # RIGHT-TO-LEFT OVERRIDE
    "\u2066",  # LEFT-TO-RIGHT ISOLATE
    "\u2067",  # RIGHT-TO-LEFT ISOLATE
    "\u2068",  # FIRST STRONG ISOLATE
    "\u2069",  # POP DIRECTIONAL ISOLATE
    "\ufeff",  # ZERO WIDTH NO-BREAK SPACE (BOM)
]
PATTERN = re.compile("[" + "".join(BANNED) + "]")

Hit = Tuple[Path, int, int, int, str]


def iter_text_files(targets: Sequence[str]) -> Iterable[Path]:
    seen = set()
    for target in targets:
        path = (ROOT / target).resolve()
        if not path.exists():
            continue
        candidates = [path] if path.is_file() else path.rglob("*")
        for candidate in candidates:
            if not candidate.is_file() or candidate.suffix.lower() not in TEXT_SUFFIXES:
                continue
            if candidate in seen:
                continue
            seen.add(candidate)
            yield candidate


def scan_file(path: Path) -> List[Hit]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        rel = path.relative_to(ROOT)
        return [(rel, 0, 0, 0, "UTF-8 decode error: {}".format(exc))]

    hits: List[Hit] = []
    for match in PATTERN.finditer(text):
        char = match.group(0)
        cp = ord(char)
        line = text.count("\n", 0, match.start()) + 1
        last_newline = text.rfind("\n", 0, match.start())
        col = match.start() + 1 if last_newline == -1 else match.start() - last_newline
        hits.append((path.relative_to(ROOT), line, col, cp, unicodedata.name(char, "UNKNOWN")))
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("targets", nargs="*", default=DEFAULT_TARGETS, help="Files or directories to scan")
    args = parser.parse_args()

    hits: List[Hit] = []
    for path in sorted(iter_text_files(args.targets)):
        hits.extend(scan_file(path))

    if hits:
        print("Hidden Unicode check failed:", file=sys.stderr)
        for path, line, col, cp, name in hits[:100]:
            if cp:
                print("- {}:{}:{} U+{:04X} {}".format(path, line, col, cp, name), file=sys.stderr)
            else:
                print("- {}: {}".format(path, name), file=sys.stderr)
        if len(hits) > 100:
            print("- ... {} more hit(s) omitted".format(len(hits) - 100), file=sys.stderr)
        return 1

    print("Hidden Unicode check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
