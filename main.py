"""The Moon Finally Answers Back.

The Moon answers a lifetime of wishes literally and wrong: asked for
taller, richer, loved, it hands over the tide instead - and the tide
keeps a little of the wisher every night. Wry, old, tired of being
wished upon; the dark twist lands in the final clause.
"""

import os

TEXT = (
    "You wished to be taller, richer, loved. "
    "I gave you the tide instead \u2014 "
    "it takes a little more of you every night."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
