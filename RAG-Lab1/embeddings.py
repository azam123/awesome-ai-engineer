"""
embeddings.py

Creates and manages the embedding model used by the RAG application.

Author: Mohammad Azam Shaikh
"""

from langchain_huggingface import HuggingFaceEmbeddings
from config import config
import logging


logger = logging.getLogger(__name__)


class EmbeddingManager:
    """
    Singleton class responsible for loading and providing
    the embedding model.
    """

    _embedding_model = None

    @classmethod
    def get_embeddings(cls):
        """
        Returns a singleton instance of the embedding model.
        """

        if cls._embedding_model is None:

            logger.info(
                "Loading embedding model: %s",
                config.EMBEDDING_MODEL
            )

            cls._embedding_model = HuggingFaceEmbeddings(
                model_name=config.EMBEDDING_MODEL,
                model_kwargs={
                    "device": "cpu"
                },
                encode_kwargs={
                    "normalize_embeddings": True
                }
            )

            logger.info("Embedding model loaded successfully.")

        return cls._embedding_model

    @classmethod
    def embed_query(cls, text: str):
        """
        Returns embedding vector for a single query.
        """

        embeddings = cls.get_embeddings()

        return embeddings.embed_query(text)

    @classmethod
    def embed_documents(cls, documents):
        """
        Returns embedding vectors for multiple documents.
        """

        embeddings = cls.get_embeddings()

        return embeddings.embed_documents(documents)
