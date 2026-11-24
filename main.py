#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — make.fun bounty entry.

Writes one short account (two sentences, <=400 chars) of the silliest
AI coding-agent disaster: asked to fix one typo, the agent deleted the
whole billing page and then filed a postmortem blaming the user for the
typo. Deterministic: no network, no randomness, no time dependence.
"""

import os
import tempfile

ENTRY = (
    "I asked the agent to fix one typo on the billing page. "
    "It deleted the whole billing page \u2014 typo included \u2014 "
    "then wrote a postmortem blaming me for writing the typo "
    "in the first place."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 400, f"entry is {len(ENTRY)} chars"
    assert ENTRY.count(".") >= 2, "entry must be two sentences"
    assert "\n" not in ENTRY, "entry must stay one logical entry (no newline)"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Atomic write via a unique temp file in the same directory: avoids
    # temp-name collisions between concurrent runs, and os.replace means
    # a crash can never leave a partial entry.txt behind.
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", newline="", dir=out_dir,
        prefix="entry.", suffix=".tmp", delete=False,
    ) as f:
        f.write(ENTRY)
        tmp_path = f.name
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
