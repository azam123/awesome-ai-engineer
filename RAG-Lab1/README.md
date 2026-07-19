# 🚀 Production RAG PDF Chatbot

A production-ready **Retrieval-Augmented Generation (RAG)** chatbot built with **Python, LangChain, OpenAI, Hugging Face Embeddings, ChromaDB, and Gradio**.

Upload one or more PDF documents and ask natural language questions. The application retrieves the most relevant document chunks using semantic search and generates accurate, context-aware answers powered by an LLM.

---

# Features

* 📄 Upload single or multiple PDF documents
* 🔍 Semantic document search using ChromaDB
* 🧠 Retrieval-Augmented Generation (RAG)
* 🤖 OpenAI GPT integration
* 🧩 Hugging Face Sentence Transformers
* ✂️ Intelligent document chunking
* 📚 Source citations with page numbers
* 📝 Document summarization
* 🔑 Keyword extraction
* 📊 Document statistics
* 💾 Persistent vector database
* 🐳 Docker & Docker Compose support
* ✅ Unit tests
* 📋 Configurable using environment variables

---

# Architecture

```text
                +----------------+
                |   PDF Upload   |
                +--------+-------+
                         |
                         v
               +-------------------+
               |   PyPDF Loader    |
               +-------------------+
                         |
                         v
          +-------------------------------+
          | Recursive Character Splitter  |
          +-------------------------------+
                         |
                         v
           +------------------------------+
           | HuggingFace Embeddings       |
           +------------------------------+
                         |
                         v
               +-------------------+
               |    ChromaDB       |
               +-------------------+
                         |
              Semantic Retrieval (MMR)
                         |
                         v
              +--------------------+
              |   OpenAI GPT Model |
              +--------------------+
                         |
                         v
                 Final Answer + Sources
```

---

# Project Structure

```text
Production_RAG_PDF_Chatbot/
│
├── app.py
├── config.py
├── embeddings.py
├── prompts.py
├── rag.py
├── vectorstore.py
├── utils.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── README.md
│
├── uploads/
├── chroma_db/
├── logs/
│
├── sample_pdfs/
│
└── tests/
    ├── test_rag.py
    └── test_vectorstore.py
```

---

# Technology Stack

| Component        | Technology            |
| ---------------- | --------------------- |
| Language         | Python 3.12           |
| LLM              | OpenAI GPT            |
| Framework        | LangChain             |
| Embeddings       | Sentence Transformers |
| Vector Database  | ChromaDB              |
| PDF Loader       | PyPDF                 |
| UI               | Gradio                |
| API              | FastAPI (optional)    |
| Containerization | Docker                |
| Testing          | PyTest / unittest     |

---

# Installation

## Clone the repository

```bash
git clone https://github.com/yourusername/Production_RAG_PDF_Chatbot.git

cd Production_RAG_PDF_Chatbot
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Copy the example configuration.

```bash
cp .env.example .env
```

Update your OpenAI API key.

```text
OPENAI_API_KEY=your_api_key_here
```

---

# Run the Application

```bash
python app.py
```

The application starts on:

```text
http://localhost:7860
```

---

# Using Docker

Build the image.

```bash
docker build -t production-rag .
```

Run the container.

```bash
docker run -p 7860:7860 --env-file .env production-rag
```

Or use Docker Compose.

```bash
docker compose up --build
```

---

# Workflow

1. Upload one or more PDF documents.
2. Documents are parsed using PyPDF.
3. Text is split into overlapping chunks.
4. Chunks are converted into embeddings.
5. Embeddings are stored in ChromaDB.
6. User submits a question.
7. Most relevant chunks are retrieved.
8. Retrieved context is sent to the LLM.
9. The chatbot returns an answer with source references.

---

# Running Tests

```bash
python -m unittest discover tests
```

or

```bash
pytest
```

---

# Configuration

The application can be configured using environment variables.

| Variable        | Description                |
| --------------- | -------------------------- |
| OPENAI_API_KEY  | OpenAI API Key             |
| GPT_MODEL       | GPT model name             |
| EMBEDDING_MODEL | Embedding model            |
| CHUNK_SIZE      | Document chunk size        |
| CHUNK_OVERLAP   | Chunk overlap              |
| TOP_K_RESULTS   | Number of retrieved chunks |
| FETCH_K         | Candidate chunks for MMR   |
| SEARCH_TYPE     | Retrieval strategy         |
| LOG_LEVEL       | Logging level              |

---

# Future Enhancements

* Hybrid Search (BM25 + Vector Search)
* Cross-Encoder Reranking
* Streaming Responses
* OCR Support for Scanned PDFs
* Multi-user Sessions
* Conversation Memory
* FastAPI REST APIs
* Authentication & Authorization
* Azure OpenAI Support
* Azure AI Search Integration
* Kubernetes Deployment
* CI/CD Pipeline
* Monitoring & Observability

---

# Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your fork.
5. Open a Pull Request.

---

# License

This project is licensed under the MIT License.

---

# Author

**Mohammad Azam Shaikh**

* Principal Software Engineer
* Azure Solution Architect
* AI & Generative AI Engineer
* RAG, Agentic AI, Cloud Architecture, and Distributed Systems Enthusiast

---

# Acknowledgements

Special thanks to the open-source community and the teams behind:

* LangChain
* OpenAI
* Hugging Face
* ChromaDB
* Gradio
* FastAPI
* PyTorch

for building the tools that make modern AI applications possible.
