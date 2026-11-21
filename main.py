"""Write one relaxing text to /output/entry.txt.

Python 3.13, standard library only, no network. Deterministic: the text
is a fixed literal, so every run writes byte-identical output.

The output path defaults to /output/entry.txt and can be overridden with
the ENTRY_OUTPUT environment variable (used for local testing).
"""

import os

TEXT = (
    "The tide comes in over flat sand at dusk, unhurried, and the last "
    "light turns amber along the water. A ship\u2019s lamp moves through "
    "the dark, small as a held breath, and the sea, wide as the night, "
    "keeps room for it \u2014 and for you."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError(
            f"entry text must be 1-280 code points and not whitespace-only, "
            f"got {len(TEXT)} code points"
        )
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
