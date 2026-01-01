"""
Vector Store Module
-------------------
Stores and retrieves transcript embeddings using FAISS.
"""

from typing import List, Dict
import faiss
import numpy as np


class FAISSVectorStore:
    """
    Lightweight FAISS wrapper for semantic search.
    """

    def __init__(self, embedding_dim: int):
        """
        Args:
            embedding_dim (int): dimension of embedding vectors
        """
        self.embedding_dim = embedding_dim
        self.index = faiss.IndexFlatIP(embedding_dim)
        self.metadata: List[Dict] = []

    def add_embeddings(self, embeddings: np.ndarray, metadatas: List[Dict]):
        """
        Add embeddings and corresponding metadata to the index.

        Args:
            embeddings (np.ndarray): shape (n, embedding_dim)
            metadatas (List[Dict]): metadata for each embedding
        """

        if len(embeddings) == 0:
            return

        if len(embeddings) != len(metadatas):
            raise ValueError("Embeddings and metadata length mismatch")

        self.index.add(embeddings)
        self.metadata.extend(metadatas)

    def search(self, query_embedding: np.ndarray, top_k: int = 5) -> List[Dict]:
        """
        Search for the most relevant chunks.

        Args:
            query_embedding (np.ndarray): shape (1, embedding_dim)
            top_k (int): number of results to return

        Returns:
            List[Dict]: retrieved chunks with similarity score
        """

        if self.index.ntotal == 0:
            return []

        scores, indices = self.index.search(query_embedding, top_k)

        results = []

        for score, idx in zip(scores[0], indices[0]):
            if idx == -1:
                continue

            chunk = self.metadata[idx].copy()
            chunk["score"] = float(score)
            results.append(chunk)

        return results


# -------------------------------
# Manual test
# -------------------------------
if __name__ == "__main__":
    # Dummy embeddings (normalized)
    embeddings = np.array([
        [0.1, 0.2, 0.3],
        [0.0, 0.1, 0.9],
        [0.2, 0.1, 0.0],
    ], dtype="float32")

    # Normalize manually for test
    embeddings /= np.linalg.norm(embeddings, axis=1, keepdims=True)

    metadatas = [
        {"text": "chunk one", "start_time": 0, "end_time": 10},
        {"text": "chunk two", "start_time": 10, "end_time": 20},
        {"text": "chunk three", "start_time": 20, "end_time": 30},
    ]

    store = FAISSVectorStore(embedding_dim=3)
    store.add_embeddings(embeddings, metadatas)

    query = np.array([[0.0, 0.1, 1.0]], dtype="float32")
    query /= np.linalg.norm(query)

    results = store.search(query, top_k=2)

    for r in results:
        print(r)
