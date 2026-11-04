#!/usr/bin/env python3
"""Build the complete portable skill ZIP, without logins or external writes."""

import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


def main():
    repo = Path(__file__).resolve().parents[1]
    source = repo / "doubao-phone-content-review"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=repo / "dist" / f"{source.name}.zip")
    args = parser.parse_args()
    if not (source / "SKILL.md").is_file():
        raise SystemExit("Missing SKILL.md")
    files = []
    for path in sorted(source.rglob("*")):
        relative = path.relative_to(source)
        if "__pycache__" in relative.parts or path.name == ".DS_Store":
            continue
        if path.is_symlink():
            raise SystemExit(f"Refusing symlink: {relative}")
        if not path.is_file():
            continue
        if any(part.startswith(".") for part in relative.parts):
            raise SystemExit(f"Unexpected hidden file: {relative}")
        if path.suffix.lower() not in {".md", ".json", ".yaml", ".yml", ".py"}:
            raise SystemExit(f"Review new resource type before packaging: {relative}")
        files.append(path)
    output = args.output.resolve()
    if output.is_relative_to(source):
        raise SystemExit("Place the ZIP outside the skill source directory")
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for path in files:
            entry = ZipInfo(path.relative_to(repo).as_posix(),
                            date_time=(1980, 1, 1, 0, 0, 0))
            entry.compress_type = ZIP_DEFLATED
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, path.read_bytes())
    with ZipFile(output) as archive:
        assert archive.testzip() is None
        assert len(archive.namelist()) == len(files)
        for path in files:
            assert archive.read(path.relative_to(repo).as_posix()) == path.read_bytes()
    print(json.dumps({"output": str(output), "files": len(files),
                      "bytes": output.stat().st_size,
                      "sha256": hashlib.sha256(output.read_bytes()).hexdigest()},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
