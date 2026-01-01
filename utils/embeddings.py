"""
Embeddings Module
-----------------
Generates semantic embeddings for transcript chunks
using Sentence Transformers.
"""

from typing import List
from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingModel:
    """
    Wrapper around SentenceTransformer for clean reuse.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts: List[str]) -> np.ndarray:
        """
        Convert a list of texts into embeddings.

        Args:
            texts (List[str]): list of chunk texts

        Returns:
            np.ndarray: shape (num_texts, embedding_dim)
        """

        if not texts:
            return np.array([])

        embeddings = self.model.encode(
            texts,
            show_progress_bar=False,
            convert_to_numpy=True,
            normalize_embeddings=True,  # important for cosine similarity
        )

        return embeddings


# -------------------------------
# Manual test
# -------------------------------
if __name__ == "__main__":
    sample_texts = [
        "transformers use self attention",
        "convolutional networks process images",
        "retrieval augmented generation improves factual accuracy",
    ]

    embedder = EmbeddingModel()
    vectors = embedder.embed_texts(sample_texts)

    print("Embedding shape:", vectors.shape)
    print("Sample vector (first 5 values):", vectors[0][:5])
