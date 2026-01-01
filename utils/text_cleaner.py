"""
Text Cleaner Module
-------------------
Cleans raw YouTube transcript text for downstream processing.

Goals:
- Normalize whitespace
- Remove filler tokens
- Preserve semantic meaning
- Keep timestamps untouched (handled elsewhere)
"""

import re
from typing import List, Dict


# Common filler words that add no semantic value
FILLER_PATTERNS = [
    r"\buh\b",
    r"\bum\b",
    r"\bumm\b",
    r"\buhh\b",
    r"\ber\b",
    r"\blike\b",
]


def clean_text(text: str) -> str:
    """
    Clean a single transcript sentence.
    """

    if not text:
        return ""

    # Convert to lowercase (optional but good for embeddings)
    text = text.lower()

    # Remove filler words
    for pattern in FILLER_PATTERNS:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove space before punctuation
    text = re.sub(r"\s+([?.!,])", r"\1", text)

    return text.strip()


def clean_transcript(transcript: List[Dict]) -> List[Dict]:
    """
    Clean entire transcript while preserving timestamps.

    Input:
    [
        {"text": "...", "start": 0.0, "duration": 3.2},
        ...
    ]

    Output:
    Same structure, cleaned text
    """

    cleaned = []

    for entry in transcript:
        cleaned_text = clean_text(entry.get("text", ""))

        if cleaned_text:
            cleaned.append({
                "text": cleaned_text,
                "start": entry["start"],
                "duration": entry["duration"]
            })

    return cleaned


# -------------------------------
# Manual test
# -------------------------------
if __name__ == "__main__":
    sample = [
        {"text": "Uh this is, um, a test sentence!", "start": 0.0, "duration": 2.0},
        {"text": "   Lots     of    spaces here.  ", "start": 2.0, "duration": 2.5},
    ]

    cleaned = clean_transcript(sample)

    for c in cleaned:
        print(c)
