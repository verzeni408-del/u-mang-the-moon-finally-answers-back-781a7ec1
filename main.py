"""The Moon Finally Answers Back -- v2 entry writer.

Writes one line, in the Moon's voice, to /output/entry.txt.

Angle: a man wishes to forget his ex. The Moon grants it literally --
and quietly takes a little extra as the fee. The voice is wry, old,
and tired of being wished upon; the harm escalates with each clause,
and the last two words are the ironic twist that lands the joke.
"""

import os

ENTRY = (
    "You wished to forget her. Granted. I took her name -- plus your "
    "dog's name, your mother's birthday, and the way home. Sweet dreams."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 240, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
