"""
Text Chunker Module
-------------------
Chunks cleaned transcript text into timestamp-aware segments
optimized for embeddings and retrieval.
"""

from typing import List, Dict


def chunk_transcript(
    transcript: List[Dict],
    max_chunk_duration: float = 60.0,
) -> List[Dict]:
    """
    Chunk transcript into time-based segments.

    Args:
        transcript (List[Dict]):
            [
              {"text": "...", "start": 0.0, "duration": 2.3},
              ...
            ]
        max_chunk_duration (float): max duration (seconds) per chunk

    Returns:
        List[Dict]:
            [
              {
                "text": "combined chunk text",
                "start_time": 12.0,
                "end_time": 68.4
              },
              ...
            ]
    """

    chunks = []

    current_chunk_text = []
    chunk_start_time = None
    chunk_end_time = None

    for entry in transcript:
        text = entry["text"]
        start = entry["start"]
        duration = entry["duration"]
        end = start + duration

        # Initialize chunk
        if chunk_start_time is None:
            chunk_start_time = start

        # Check if adding this entry exceeds max duration
        if end - chunk_start_time <= max_chunk_duration:
            current_chunk_text.append(text)
            chunk_end_time = end
        else:
            # Save current chunk
            chunks.append({
                "text": " ".join(current_chunk_text),
                "start_time": round(chunk_start_time, 2),
                "end_time": round(chunk_end_time, 2),
            })

            # Start new chunk
            current_chunk_text = [text]
            chunk_start_time = start
            chunk_end_time = end

    # Save last chunk
    if current_chunk_text:
        chunks.append({
            "text": " ".join(current_chunk_text),
            "start_time": round(chunk_start_time, 2),
            "end_time": round(chunk_end_time, 2),
        })

    return chunks


# -------------------------------
# Manual test
# -------------------------------
if __name__ == "__main__":
    sample_transcript = [
        {"text": "this is sentence one", "start": 0.0, "duration": 5.0},
        {"text": "this is sentence two", "start": 6.0, "duration": 5.0},
        {"text": "this is sentence three", "start": 12.0, "duration": 50.0},
        {"text": "this starts a new chunk", "start": 65.0, "duration": 10.0},
    ]

    chunks = chunk_transcript(sample_transcript, max_chunk_duration=60)

    for c in chunks:
        print(c)
