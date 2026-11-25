"""Copy the robot vacuum's excuse into the grader's output directory.

The entry text lives in ``entry.txt`` next to this script. This program
reads it, validates it is a single non-empty line within the competition's
140-character limit, and writes it to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
with mode 0644 so the grader can read it.
"""

import os
import shutil
import sys

MAX_CHARS = 140


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    try:
        with open(src, "r", encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        print(f"cannot read {src}: {exc}", file=sys.stderr)
        return 1

    line = text.strip()
    if not line:
        print("entry.txt is empty", file=sys.stderr)
        return 1
    if "\n" in line:
        print("entry.txt must hold a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"entry is {len(line)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    try:
        os.makedirs(out_dir, exist_ok=True)
        dst = os.path.join(out_dir, "entry.txt")
        shutil.copyfile(src, dst)
        os.chmod(dst, 0o644)
    except OSError as exc:
        print(f"cannot write output: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
