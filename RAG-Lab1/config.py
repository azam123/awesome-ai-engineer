"""
Configuration file for Production RAG PDF Chatbot

Author: Mohammad Azam Shaikh
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """
    Application Configuration
    """

    # ===============================
    # OpenAI
    # ===============================
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    GPT_MODEL = "gpt-4o-mini"

    TEMPERATURE = 0

    MAX_TOKENS = 2048

    # ===============================
    # Embedding Model
    # ===============================

    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

    # ===============================
    # Vector Database
    # ===============================

    CHROMA_DB_DIRECTORY = "./chroma_db"

    COLLECTION_NAME = "pdf_documents"

    # ===============================
    # PDF Processing
    # ===============================

    CHUNK_SIZE = 800

    CHUNK_OVERLAP = 100

    # ===============================
    # Retrieval
    # ===============================

    TOP_K_RESULTS = 5

    SEARCH_TYPE = "mmr"

    FETCH_K = 20

    # ===============================
    # Uploads
    # ===============================

    UPLOAD_DIRECTORY = "./uploads"

    ALLOWED_FILE_TYPES = [".pdf"]

    MAX_FILE_SIZE_MB = 50

    # ===============================
    # Logging
    # ===============================

    LOG_DIRECTORY = "./logs"

    LOG_FILE = "application.log"

    LOG_LEVEL = "INFO"

    # ===============================
    # Gradio
    # ===============================

    SERVER_PORT = 7860

    SHARE = True

    DEBUG = True

    # ===============================
    # FastAPI
    # ===============================

    API_HOST = "0.0.0.0"

    API_PORT = 8000

    # ===============================
    # Prompt
    # ===============================

    SYSTEM_PROMPT = """
You are an expert AI PDF Assistant.

Rules:

1. Answer ONLY from the retrieved context.

2. Never make up information.

3. If the answer isn't found, reply:

"I couldn't find that information in the uploaded document."

4. Always mention page numbers.

5. Keep answers concise unless asked to explain.

6. Format using Markdown.
"""


config = Config()
