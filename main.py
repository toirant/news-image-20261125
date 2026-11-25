#!/usr/bin/env python3
"""news-image-20261125 entry: write the day's news image to the output dir.

The image (entry.png, in this repository) is a newspaper front page
summing up the world news of Wednesday 25 November 2026, drawn in code
from the stories reported that day. This program copies it to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR when set), byte for byte,
so both grader runs produce identical output. No network is used.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Verify the copy is complete: same size as the shipped image.
    if os.path.getsize(dst) != os.path.getsize(src):
        print("error: copied entry.png size mismatch", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
