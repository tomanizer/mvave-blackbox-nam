#!/usr/bin/env python3
"""Download selected public references locally; never access or write a device."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile
import urllib.error
import urllib.parse
import urllib.request


def fetch(source, output):
    filename = source["download_filename"]
    if Path(filename).name != filename or not filename:
        raise ValueError("Invalid source filename")
    url = source.get("download_url") or source["url"]
    if urllib.parse.urlsplit(url).scheme != "https":
        raise ValueError("Only public HTTPS downloads are supported")
    target = output / (source["id"] + "-" + filename)
    if target.exists():
        digest = hashlib.sha256(target.read_bytes()).hexdigest()
        if source.get("sha256") and digest == source["sha256"]:
            print(source["id"] + ": existing file matches recorded SHA-256")
            return
        raise FileExistsError("Refusing to overwrite " + str(target))
    request = urllib.request.Request(
        url, headers={"User-Agent": "Mozilla/5.0 Blackbox-NAM-source-fetcher/0.1"}
    )
    fd, temporary_name = tempfile.mkstemp(dir=output, prefix="source-")
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        digest = hashlib.sha256()
        size = 0
        with urllib.request.urlopen(request, timeout=30) as response:
            if filename.lower().endswith(".pdf"):
                first = response.read(5)
                if first != b"%PDF-":
                    raise ValueError("Response is not a PDF")
            else:
                first = b""
            with temporary.open("wb") as stream:
                stream.write(first)
                digest.update(first)
                size += len(first)
                while True:
                    chunk = response.read(65536)
                    if not chunk:
                        break
                    size += len(chunk)
                    if size > 32 * 1024 * 1024:
                        raise ValueError("Reference exceeds 32 MiB limit")
                    stream.write(chunk)
                    digest.update(chunk)
        expected = source.get("sha256")
        actual = digest.hexdigest()
        if expected and actual != expected:
            raise ValueError("SHA-256 mismatch; the public source may have changed")
        # Hard-link creation refuses an existing destination, including a symlink.
        os.link(temporary, target)
        print(source["id"] + ": saved " + str(target) + " sha256=" + actual)
    finally:
        temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", action="append", required=True, help="Repeat for several sources")
    parser.add_argument("--output", type=Path, default=Path("research/downloads"))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    sources = json.loads((root / "resources/sources.json").read_text())["sources"]
    by_id = {source["id"]: source for source in sources}
    selected = []
    for source_id in args.id:
        source = by_id.get(source_id)
        if source is None or not source.get("download_filename"):
            parser.error(source_id + " is not a downloadable file in the source catalog")
        selected.append(source)
    args.output.mkdir(parents=True, exist_ok=True)
    errors = 0
    for source in selected:
        try:
            fetch(source, args.output)
        except (OSError, ValueError, urllib.error.URLError) as error:
            errors += 1
            print(source["id"] + ": failed: " + str(error))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
