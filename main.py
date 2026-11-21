"""Write one relaxing text to /output/entry.txt.

Python 3.13, standard library only, no network. Deterministic: the text
is a fixed literal, so every run writes byte-identical output.

The output path defaults to /output/entry.txt and can be overridden with
the ENTRY_OUTPUT environment variable (used for local testing).
"""

import os

TEXT = (
    "The tide comes in over flat sand at dusk, unhurried, and the last "
    "light turns amber along the water. Far out, a ship\u2019s lamp moves "
    "through the dark, and the whole wide sea keeps room for it \u2014 "
    "and for you, too."
)


def main() -> None:
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
