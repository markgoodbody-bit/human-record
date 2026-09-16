"""Read-only catalogue/source byte check. No network, pin repair or truth verdict."""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def git_blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def check(root):
    root = Path(root).resolve()
    errors = []
    count = 0
    try:
        catalog = json.loads((root / "records/catalog.json").read_text(encoding="utf-8"))
        records = catalog["records"]
        if not isinstance(records, list) or not records:
            raise ValueError("records must be a non-empty list")
        seen = set()
        for record in records:
            identity = record["id"]
            if not isinstance(identity, str) or not identity or identity in seen:
                raise ValueError("record IDs must be unique non-empty strings")
            seen.add(identity)
            pins = record["view_basis"]["source_git_blobs"]
            expected_paths = set()
            for field in ("full_human_record", "machine_record"):
                url = urlsplit(record[field])
                if url.scheme != "https" or url.netloc != "thehumanrecord.net" or url.query or url.fragment:
                    raise ValueError(f"{identity}: unsupported source URL in {field}")
                expected_paths.add(unquote(url.path).lstrip("/"))
            if not isinstance(pins, dict) or set(pins) != expected_paths or len(pins) != 2:
                raise ValueError(f"{identity}: both source routes must have exactly one pin")
            for name, pin in pins.items():
                path = (root / name).resolve()
                if not path.is_relative_to(root):
                    raise ValueError(f"{identity}: source path escapes checkout")
                if not isinstance(pin, str) or not re.fullmatch(r"[0-9a-f]{40}", pin):
                    raise ValueError(f"{identity}: invalid Git blob ID for {name}")
                actual = git_blob(path.read_bytes())
                count += 1
                if actual != pin:
                    errors.append(f"{identity}: {name}: expected {pin}, found {actual}; view freshness unestablished")
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        errors.append(f"Cannot establish view basis: {exc}")
    return count, errors


if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) == 2 else Path(__file__).resolve().parents[1]
    count, errors = check(root)
    for error in errors:
        print(error)
    print(f"{count} source pins checked; {len(errors)} failures. Byte identity is not summary accuracy or truth.")
    sys.exit(1 if errors else 0)
