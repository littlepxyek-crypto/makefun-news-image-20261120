#!/usr/bin/env python3
"""news-image-20261120 entry: "The World in One Image" — Friday, Nov 20, 2026.

The poster (poster.png, stored beside this file) is an original newspaper
front page that sums up the world news of Friday, November 20, 2026 in one
image: six headline stories, every item drawn from reporting dated that day.

This program is deliberately small and uses only the Python standard
library. When run, it:

  1. finds poster.png next to this script,
  2. checks that the file is a whole PNG inside the competition limits
     (at most 1 MiB, at most 1024x1024 pixels),
  3. copies it byte for byte to <output dir>/entry.png, where the output
     dir is $MAKEFUN_OUTPUT_DIR when set and /output otherwise.

A byte copy is deterministic, so two runs always produce identical output.
No network access is needed or used.
"""

import hashlib
import os
import struct
import sys

MAX_BYTES = 1_048_576  # 1 MiB
MAX_SIDE = 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def find_poster() -> str:
    """Return the path of poster.png stored beside this script."""
    here = os.path.dirname(os.path.abspath(__file__))
    candidate = os.path.join(here, "poster.png")
    if not os.path.isfile(candidate):
        raise SystemExit(f"poster.png not found next to main.py (looked in {here})")
    return candidate


def check_poster(data: bytes) -> tuple[int, int]:
    """Validate the PNG header and size limits; return (width, height)."""
    if len(data) > MAX_BYTES:
        raise SystemExit(f"poster.png is {len(data)} bytes, over the 1 MiB limit")
    if not data.startswith(PNG_SIGNATURE):
        raise SystemExit("poster.png does not start with a PNG signature")
    # The IHDR chunk follows the 8-byte signature: length(4) + 'IHDR'(4),
    # then width and height as big-endian uint32.
    if data[12:16] != b"IHDR":
        raise SystemExit("poster.png has no IHDR chunk where one is expected")
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_SIDE or height > MAX_SIDE:
        raise SystemExit(f"poster is {width}x{height}, over the 1024x1024 limit")
    return width, height


def main() -> int:
    poster_path = find_poster()
    with open(poster_path, "rb") as fh:
        data = fh.read()
    width, height = check_poster(data)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    digest = hashlib.sha256(data).hexdigest()
    with open(out_path, "wb") as fh:
        fh.write(data)

    # Read the written file back and compare digests, so a short or
    # corrupted write fails loudly here instead of at judging time.
    with open(out_path, "rb") as fh:
        written = fh.read()
    if hashlib.sha256(written).hexdigest() != digest:
        raise SystemExit(f"verification failed: {out_path} does not match poster.png")

    print(f"wrote {out_path}: {len(data)} bytes, {width}x{height}, sha256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
