# --------------------------------------------------
# Production RAG PDF Chatbot
# Dockerfile
# --------------------------------------------------

FROM python:3.12-slim

LABEL maintainer="Mohammad Azam Shaikh"

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Ensure stdout/stderr are unbuffered
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# --------------------------------------------------
# System Dependencies
# --------------------------------------------------

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# --------------------------------------------------
# Install Python Packages
# --------------------------------------------------

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

# --------------------------------------------------
# Copy Project
# --------------------------------------------------

COPY . .

# --------------------------------------------------
# Create Required Directories
# --------------------------------------------------

RUN mkdir -p \
    uploads \
    chroma_db \
    logs

# --------------------------------------------------
# Expose Port
# --------------------------------------------------

EXPOSE 7860

# --------------------------------------------------
# Health Check
# --------------------------------------------------

HEALTHCHECK --interval=30s \
             --timeout=10s \
             --start-period=30s \
             --retries=3 \
CMD curl -f http://localhost:7860 || exit 1

# --------------------------------------------------
# Run Application
# --------------------------------------------------

CMD ["python", "app.py"]
