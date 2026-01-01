🎥 YouTubeKnowledge AI — Video RAG Assistant

YouTubeKnowledge AI is a Retrieval-Augmented Generation (RAG) system that transforms YouTube video transcripts into a clean, structured, timestamped knowledge base, enabling accurate and explainable question answering grounded strictly in video content.

⚠️ This project is for educational and portfolio purposes and is not affiliated with YouTube.

📌 Project Status

🚧 In Active Development

✅ Completed

YouTube transcript extraction (version-safe)

Robust URL parsing

Timestamp-preserving transcript structure

Transcript text cleaning & normalization

Clean project structure and Git setup

⏳ Upcoming

Timestamp-aware text chunking

Semantic embeddings

FAISS vector search

RAG pipeline with LLM

Gradio UI

Docker + Hugging Face Spaces deployment

🎯 Project Goal

Build an AI assistant where users can:

Paste a YouTube video link

Automatically extract the video transcript

Convert the transcript into a searchable knowledge base

Ask natural language questions

Receive accurate, timestamped answers

Avoid hallucinations by grounding responses in video content

🧠 Why This Project Matters

Demonstrates real-world RAG architecture

Uses unstructured video data → structured knowledge

Focuses on explainability via timestamps

Portfolio-ready for AI / ML / Full-Stack roles

Designed with production-level modularity

🏗️ System Architecture (Planned)
YouTube URL
   ↓
Transcript Loader ✅
   ↓
Text Cleaner ✅
   ↓
Timestamp-aware Chunking ⏳
   ↓
Sentence Embeddings ⏳
   ↓
FAISS Vector Store ⏳
   ↓
User Question → Retrieval ⏳
   ↓
LLM Answer Generation ⏳

🛠️ Tech Stack
Core

Python

youtube-transcript-api

Sentence Transformers (planned)

FAISS (planned)

Transformers / LLMs (planned)

UI & Deployment (Planned)

Gradio

Docker

Hugging Face Spaces

📁 Project Structure
YouTubeKnowledge-AI-Video-RAG-Assistant/
│
├── app.py                     # (Coming soon) UI entry point
├── requirements.txt
├── Dockerfile                 # (Coming soon)
├── README.md
│
├── utils/
│   ├── __init__.py
│   ├── transcript_loader.py   # ✅ Transcript extraction
│   ├── text_cleaner.py        # ✅ Text cleaning & normalization
│   ├── text_chunker.py        # ⏳ Timestamp-based chunking
│   ├── embeddings.py          # ⏳ Embedding generation
│   ├── vector_store.py        # ⏳ FAISS index
│   └── rag_pipeline.py        # ⏳ Retrieval + generation
│
└── assets/
    └── styles.css             # (Optional, future UI styling)

🔍 Implemented Modules (So Far)
1️⃣ Transcript Loader

Supports multiple YouTube URL formats

Compatible with youtube-transcript-api v1.2.x

Handles:

Disabled transcripts

Missing captions

Private/unavailable videos

Returns structured output:

{
  "text": "...",
  "start": 12.3,
  "duration": 3.8
}

2️⃣ Text Cleaner

Removes filler words (uh, um, etc.)

Normalizes whitespace and punctuation

Preserves semantic meaning

Keeps timestamps untouched

Why this matters:

Clean text → better embeddings → better retrieval

🧪 Local Setup
git clone https://github.com/rohit3576/YouTubeKnowledge-AI-Video-RAG-Assistant.git
cd YouTubeKnowledge-AI-Video-RAG-Assistant

python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt

🧠 Interview Talking Points

Why transcript cleaning should be conservative

Handling breaking API changes safely

Importance of timestamp preservation

Difference between chatbots and RAG systems

Designing modular ML pipelines

🚀 Roadmap

 Timestamp-aware chunking

 Semantic embeddings

 FAISS vector search

 RAG prompt engineering

 Gradio UI

 Dockerized deployment

 Public demo on Hugging Face Spaces

📌 Resume-Ready Description

Built YouTubeKnowledge AI, a Video RAG Assistant that converts YouTube transcripts into a structured, timestamped knowledge base as a foundation for explainable AI question answering.

🤝 Contributions

This project is currently developed as a solo portfolio project.
Feedback and suggestions are welcome.

⭐ Final Note

This project is intentionally built step-by-step to reflect how real AI systems are engineered in production.
