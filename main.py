#!/usr/bin/env python3
"""Copy the front-page image for 24 November 2026 to the output folder.

The entry image (entry.png, drawn for this competition) sits next to this
program in the repository. Running this program copies it to
/output/entry.png, creating that folder when it does not exist yet, and
then prints the size and SHA-256 of the file it wrote so the copy can be
checked at a glance.

Usage:
    python3 main.py            copy entry.png to /output/entry.png
    python3 main.py --help     show this help and exit
"""

import argparse
import hashlib
import shutil
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path("/output")
OUTPUT = OUTPUT_DIR / "entry.png"


def png_dimensions(path):
    """Read width and height from a PNG header, or return None."""
    with open(path, "rb") as handle:
        header = handle.read(33)
    if len(header) < 33 or header[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    if header[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Copy entry.png (The World Today, 24 November 2026) "
                    "to /output/entry.png."
    )
    parser.parse_args(argv)

    if not SOURCE.is_file():
        print(f"error: source image not found: {SOURCE}", file=sys.stderr)
        return 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)

    size = OUTPUT.stat().st_size
    digest = sha256_of(OUTPUT)
    source_digest = sha256_of(SOURCE)
    match = "OK" if digest == source_digest else "MISMATCH"
    print(f"wrote {OUTPUT} ({size} bytes)")
    print(f"sha256: {digest}")
    print(f"output matches source: {match}")
    dims = png_dimensions(OUTPUT)
    if dims is None:
        print("error: output is not a readable PNG", file=sys.stderr)
        return 1
    print(f"dimensions: {dims[0]}x{dims[1]}")
    if dims != (1024, 1024):
        print(f"error: expected 1024x1024, got {dims[0]}x{dims[1]}",
              file=sys.stderr)
        return 1
    if digest != source_digest:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
