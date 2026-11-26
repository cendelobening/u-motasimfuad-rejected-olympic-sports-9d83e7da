#!/usr/bin/env python3
"""Rejected Olympic Sports -- one funny single-line sport the Olympics rejected.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt
when the variable is unset). Pure standard library, deterministic: the same
bytes on every run.
"""

import os
import stat

LINE = (
    "Competitive Apologising: two athletes collide in a hotel corridor and "
    "must out-sorry each other until one cracks and says 'No, MY fault' "
    "\u2014 instant disqualification."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    # Write via a temp file in the same directory, then rename, so the
    # graded file is never half-written; force world-readable 0644.
    tmp = path + ".tmp"
    with open(tmp, "wb") as fh:
        fh.write(data)
    os.chmod(tmp, 0o644)
    os.replace(tmp, path)
    os.chmod(path, 0o644)
    assert stat.S_IMODE(os.stat(path).st_mode) == 0o644


if __name__ == "__main__":
    main()
