#!/usr/bin/env python3
"""One Word for the Boss: Buffering.

Writes exactly one word to /output/entry.txt: the word that describes
the boss. No phrase, no caption, no explanation. The word is the whole
entry, and it has to land on its own.

The word: Buffering. The boss who never decides, never answers, never
ships the call -- always loading, always one more spin of the wheel
away from doing anything. Everyone in the room has watched that wheel
go round. It is funny on its own, it rings true, and it needs no
caption: every kitchen, warehouse and office has waited on one.

The program is deterministic: the same bytes on every run, no network,
no clock, no randomness. After writing, it reads the file back and
checks the bytes, the length and the sha256 against the pinned values,
so a bad write fails loudly instead of submitting a wrong word.
"""

import hashlib
import os
import sys

WORD = "Buffering"
EXPECTED_SHA256 = "c08626d0a514a53b06a32ffa5f71ce51ce1b9525fc83da026ca8682b307e09a3"
EXPECTED_BYTES = 9


def verify(path: str, data: bytes) -> bytes:
    """Read the file back and prove it holds exactly the word.

    Returns the bytes read. Exits non-zero on any mismatch, so a partial
    or corrupted write fails loudly instead of submitting a wrong word.
    """
    with open(path, "rb") as f:
        back = f.read()
    if back != data:
        print("entry.txt does not match the word", file=sys.stderr)
        raise SystemExit(1)
    if len(back) != EXPECTED_BYTES:
        print("entry.txt is %d bytes, expected %d" % (len(back), EXPECTED_BYTES),
              file=sys.stderr)
        raise SystemExit(1)
    if hashlib.sha256(back).hexdigest() != EXPECTED_SHA256:
        print("entry.txt sha256 mismatch", file=sys.stderr)
        raise SystemExit(1)
    return back


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = WORD.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Read-back gate: the bytes on disk must be exactly the word --
    # same bytes, same length (9), same pinned sha256.
    back = verify(path, data)
    print("wrote %s (%d bytes)" % (path, len(back)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
