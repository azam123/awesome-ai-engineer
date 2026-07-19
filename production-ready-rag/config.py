from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
EMBEDDING_MODEL='sentence-transformers/all-MiniLM-L6-v2'
LLM_MODEL='gpt-4o-mini'
CHROMA_DIR='./chroma_db'
