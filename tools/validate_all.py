"""Run the offline THR validators against one identified checkout."""
import argparse
from pathlib import Path
import sys
import validate_entity_admission
import validate_integrity
import validate_operational


def run(root):
    root = Path(root).resolve()
    if not root.is_dir():
        print(f"ERROR: checkout directory does not exist: {root}")
        return 1
    print(f"Checking checkout: {root}")
    previous = (validate_integrity.ROOT, validate_integrity.errors[:], validate_integrity.warnings[:])
    validate_integrity.ROOT = root
    validate_integrity.errors.clear()
    validate_integrity.warnings.clear()
    failures = 0
    stages = (
        ("record integrity", validate_integrity.main),
        ("operational integrity", lambda: validate_operational.main(root)),
        ("entity admission", lambda: validate_entity_admission.main(root)),
    )
    try:
        for name, check in stages:
            try:
                if check() != 0:
                    failures += 1
            except Exception as exc:
                # Checker failure must not hide later stages or become PASS.
                print(f"ERROR: {name} could not complete: {type(exc).__name__}: {exc}")
                failures += 1
    finally:
        validate_integrity.ROOT = previous[0]
        validate_integrity.errors[:] = previous[1]
        validate_integrity.warnings[:] = previous[2]
    if failures:
        print(f"FAIL: {failures} of {len(stages)} validator stages failed or could not complete.")
        return 1
    print("PASS: all validator stages completed. Warnings remain actionable; this is not a truth verdict.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    sys.exit(run(parser.parse_args().root))
