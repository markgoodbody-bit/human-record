"""Read-only catalogue/source byte check. No network, pin repair or truth verdict."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def git_blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


class BasisParagraphs(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.current = None
        self.paragraphs = []

    def handle_starttag(self, tag, attrs):
        if tag == "p":
            self.current = []

    def handle_data(self, data):
        if self.current is not None:
            self.current.append(data)

    def handle_endtag(self, tag):
        if tag == "p" and self.current is not None:
            text = "".join(self.current)
            if text.strip().startswith("View basis:"):
                self.paragraphs.append(text)
            self.current = None


def check_label(root, record):
    identity = record["id"]
    url = urlsplit(record["human_view"])
    if url.scheme != "https" or url.netloc != "thehumanrecord.net" or url.query or url.fragment:
        raise ValueError(f"{identity}: unsupported human-view URL")
    path = (root / unquote(url.path).lstrip("/")).resolve()
    if not path.is_relative_to(root):
        raise ValueError(f"{identity}: human-view path escapes checkout")
    parser = BasisParagraphs()
    parser.feed(path.read_text(encoding="utf-8"))
    if len(parser.paragraphs) != 1:
        raise ValueError(f"{identity}: expected one View basis paragraph")
    text = parser.paragraphs[0]
    basis = record["view_basis"]
    for name, pin in basis["source_git_blobs"].items():
        matches = re.findall(re.escape(name) + r"@([0-9a-f]{7,40})(?:…|\.\.\.|(?=\s|[).,]|$))", text)
        if len(matches) != 1 or not pin.startswith(matches[0]):
            raise ValueError(f"{identity}: stale or missing HTML source marker for {name}")
    if "source_record_version" in basis:
        versions = re.findall(r"record version\s+([0-9]+(?:\.[0-9]+)+)", text)
        if versions != [basis["source_record_version"]]:
            raise ValueError(f"{identity}: HTML record version mismatch")
    elif "source_record_format" in basis:
        if basis["source_record_format"] not in text:
            raise ValueError(f"{identity}: HTML record format mismatch")
    else:
        raise ValueError(f"{identity}: missing record version or format")


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
            check_label(root, record)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        errors.append(f"Cannot establish view basis: {exc}")
    return count, errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1],
                        help="checkout to inspect (defaults to this script's repository)")
    args = parser.parse_args()
    count, errors = check(args.root)
    for error in errors:
        print(error)
    print(f"{count} source pins checked; {len(errors)} failures. Byte identity is not summary accuracy or truth.")
    sys.exit(1 if errors else 0)
