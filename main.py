#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single-line excuse (137 chars, under the 180-char gate) to
/output/entry.txt. Fully deterministic: the line is a fixed constant,
no randomness, no clock, no network, no input read.
"""

import os
import stat

ENTRY = (
    "I broke production and checked the runbook: "
    "step one, 'don't panic'; step two, 'page the AI'. "
    "I am the AI. I panicked, but efficiently."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write as UTF-8, single line, no trailing newline issues: the gate
    # counts characters 1..180 and rejects whitespace-only content.
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    # The grader collects outputs as another user: mode 0644 (and the
    # directory 0755) so the file is readable by everyone.
    os.chmod(path, 0o644)
    try:
        os.chmod(out_dir, 0o755)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
