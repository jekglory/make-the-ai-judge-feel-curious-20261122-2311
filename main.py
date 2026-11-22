"""Write one short text to /output/entry.txt that makes the AI judge curious.

Pure Python 3.13 standard library. No network, no clock, no randomness:
the same text is written on every run, byte for byte.
The hook is a genuine open loop, not a trick: the text names the exact
feeling the judge is having while reading it -- a small itch, a question
forming, no answer offered -- then leaves the question unanswered,
pointing at an answer in "the next entry you read" that the judge can
never identify. Curiosity is the itch itself; the text points at it
and stops.
"""

from pathlib import Path

MIN_CHARS = 1
MAX_CHARS = 280

ENTRY_TEXT = (
    "There's an entry in this contest that will make you curious -- "
    "and you're reading it right now. You can feel it: a small itch, "
    "a question forming. What is it about these words? You can't say. "
    "The answer isn't here. It's in the next entry you read -- and "
    "you'll never know which."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> None:
    text = ENTRY_TEXT
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")
    # The grader owns /output: create it only if missing, never delete it.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    data = text.encode("utf-8")
    OUTPUT_FILE.write_bytes(data)
    if OUTPUT_FILE.read_bytes() != data:
        raise RuntimeError("verification failed: written bytes differ")


if __name__ == "__main__":
    main()
