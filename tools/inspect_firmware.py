#!/usr/bin/env python3
"""Read-only fingerprint and selected literal scan of a local firmware file."""

import argparse
import hashlib
import json
from pathlib import Path


def inspect(path):
    data = path.read_bytes()
    markers = {}
    for term in (b"AC791N_STORY", b"JLUFW", b"uboot.", b"*.ufw"):
        positions = []
        start = 0
        while True:
            offset = data.find(term, start)
            if offset < 0:
                break
            positions.append(offset)
            start = offset + 1
        markers[term.decode("ascii")] = positions
    return {
        "filename": path.name,
        "size_bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "marker_offsets_decimal": markers,
        "interpretation": "Update-container offsets only; no disassembly or device access.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    print(json.dumps(inspect(args.file), indent=2))


if __name__ == "__main__":
    main()
