"""
Transcript Loader
-----------------
Compatible with youtube-transcript-api v1.2.x
"""

import re
from typing import List, Dict
from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
)


def extract_video_id(url: str) -> str:
    patterns = [
        r"v=([^&]+)",
        r"youtu\.be/([^?]+)",
        r"embed/([^?]+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    raise ValueError("Invalid YouTube URL")


def load_transcript(
    youtube_url: str,
    languages: List[str] = ["en"],
) -> List[Dict]:

    video_id = extract_video_id(youtube_url)

    try:
        # ✅ INSTANCE method usage as per your version
        transcript_list = YouTubeTranscriptApi().list(video_id)

        try:
            transcript = transcript_list.find_manually_created_transcript(languages)
        except NoTranscriptFound:
            transcript = transcript_list.find_generated_transcript(languages)

        entries = transcript.fetch()

        # FIX: Access attributes directly (dot notation) instead of dictionary syntax
        return [
            {
                "text": entry.text.strip(),
                "start": float(entry.start),
                "duration": float(entry.duration),
            }
            for entry in entries
            # Use getattr because the object has no .get() method
            if getattr(entry, "text", None)
        ]

    except TranscriptsDisabled:
        raise RuntimeError("Transcripts are disabled for this video.")

    except NoTranscriptFound:
        raise RuntimeError("No transcript found for this video.")

    except VideoUnavailable:
        raise RuntimeError("Video is unavailable or private.")

    except Exception as e:
        raise RuntimeError(f"Failed to fetch transcript: {e}")


if __name__ == "__main__":
    url = input("Enter YouTube URL: ").strip()

    try:
        data = load_transcript(url)
        print(f"Loaded {len(data)} transcript segments")
        if data:
            print("Sample:", data[0])
    except Exception as err:
        print("Error:", err)