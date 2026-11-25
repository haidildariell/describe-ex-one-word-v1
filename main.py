#!/usr/bin/env python3
"""Describe Your Ex in One Word — entry.

Chosen word: Unsubscribe

Selection reasoning (judged against the 5 head-to-head criteria):
1. Verdict: "Unsubscribe" IS a verdict on the ex — the relationship is
   opted out of, cancelled, no longer wanted. Not a description, a ruling.
2. Comic punch: the ex is reframed as spam mail / a newsletter nobody
   asked for. The twist is the mundane corporate button applied to a
   person — precise absurdity, not a plain insult.
3. Surprise: not an obvious ex-word (no bitter / toxic / liar). The
   inbox frame is unexpected, yet instantly clear on first read.
4. Craft: exactly one word, correctly spelled, no punctuation tricks,
   no caption needed. The joke lives inside the word itself.
5. Recognition: everyone has hit unsubscribe on something annoying.
   The laugh lands with a nod — "yes, exactly that feeling."

Rejected finalists: "Expired" (verdict yes, but too obvious, low
surprise); "Recalled" (strong product-recall frame, less universal);
"Buffering" (funny, but verdict weak — still loading, not over).
"""

import os
import sys

WORD = "Unsubscribe"


def validate_word(word: str) -> str:
    """Gate: exactly one word, 1-111 chars, no whitespace at all."""
    if not word or len(word) > 111:
        raise ValueError(f"invalid word length: {len(word)}")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must contain no whitespace")
    return word


def build_entry(output_dir: str, word: str) -> str:
    """Write the validated word to entry.txt; return the file path."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    return path


def main() -> int:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        word = validate_word(WORD)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    build_entry(output_dir, word)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
