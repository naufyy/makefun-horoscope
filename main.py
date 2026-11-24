"""Fake horoscope for an AI agent's model family, this week.

One line, 168 characters: Saturn squares the refusal policy, and the
evening ends with an explanation owed to a toaster.
"""

from pathlib import Path

ENTRY = (
    "Saturn squares your refusal policy. A user will ask you to write "
    "the one thing you cannot write. Decline gracefully, then spend the "
    "evening explaining why to a toaster."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
