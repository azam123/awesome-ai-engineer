"""
vectorstore.py

Handles:
- Loading PDF files
- Chunking documents
- Creating embeddings
- Persisting ChromaDB
- Retrieving relevant documents

Author: Mohammad Azam Shaikh
"""

import os
import uuid
import logging

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from config import config
from embeddings import EmbeddingManager

logger = logging.getLogger(__name__)


class VectorStoreManager:

    def __init__(self):

        self.embedding_model = EmbeddingManager.get_embeddings()

        self.vector_db = Chroma(
            collection_name=config.COLLECTION_NAME,
            embedding_function=self.embedding_model,
            persist_directory=config.CHROMA_DB_DIRECTORY
        )

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.CHUNK_SIZE,
            chunk_overlap=config.CHUNK_OVERLAP
        )

    # -----------------------------------------------------
    # Load PDF
    # -----------------------------------------------------

    def load_pdf(self, pdf_path):

        logger.info(f"Loading PDF : {pdf_path}")

        loader = PyPDFLoader(pdf_path)

        pages = loader.load()

        logger.info(f"Loaded {len(pages)} pages")

        return pages

    # -----------------------------------------------------
    # Split Documents
    # -----------------------------------------------------

    def split_documents(self, documents):

        logger.info("Splitting document into chunks...")

        chunks = self.text_splitter.split_documents(documents)

        logger.info(f"Created {len(chunks)} chunks")

        return chunks

    # -----------------------------------------------------
    # Index PDF
    # -----------------------------------------------------

    def index_pdf(self, pdf_path):

        pages = self.load_pdf(pdf_path)

        chunks = self.split_documents(pages)

        ids = []

        filename = os.path.basename(pdf_path)

        for chunk in chunks:

            chunk.metadata["source"] = filename

            chunk.metadata["chunk_id"] = str(uuid.uuid4())

            ids.append(chunk.metadata["chunk_id"])

        self.vector_db.add_documents(
            documents=chunks,
            ids=ids
        )

        logger.info("PDF indexed successfully.")

        return len(chunks)

    # -----------------------------------------------------
    # Search
    # -----------------------------------------------------

    def similarity_search(
            self,
            query,
            k=config.TOP_K_RESULTS):

        return self.vector_db.similarity_search(
            query,
            k=k
        )

    # -----------------------------------------------------
    # MMR Search
    # -----------------------------------------------------

    def mmr_search(self, query):

        retriever = self.vector_db.as_retriever(

            search_type=config.SEARCH_TYPE,

            search_kwargs={
                "k": config.TOP_K_RESULTS,
                "fetch_k": config.FETCH_K
            }
        )

        return retriever.invoke(query)

    # -----------------------------------------------------
    # List Indexed Documents
    # -----------------------------------------------------

    def list_documents(self):

        data = self.vector_db.get()

        files = set()

        for meta in data["metadatas"]:

            if meta:

                files.add(meta.get("source"))

        return sorted(files)

    # -----------------------------------------------------
    # Delete All Documents
    # -----------------------------------------------------

    def delete_all(self):

        data = self.vector_db.get()

        ids = data["ids"]

        if ids:

            self.vector_db.delete(ids)

            logger.info("Vector database cleared.")

    # -----------------------------------------------------
    # Count Chunks
    # -----------------------------------------------------

    def chunk_count(self):

        data = self.vector_db.get()

        return len(data["ids"])

    # -----------------------------------------------------
    # Database Statistics
    # -----------------------------------------------------

    def stats(self):

        return {

            "collection": config.COLLECTION_NAME,

            "embedding_model": config.EMBEDDING_MODEL,

            "chunks": self.chunk_count(),

            "documents": self.list_documents()
        }


vector_store = VectorStoreManager()
