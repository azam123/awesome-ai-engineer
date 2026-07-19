from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from config import *
emb=HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
def build_index(pdf):
 docs=PyPDFLoader(pdf).load();chunks=RecursiveCharacterTextSplitter(chunk_size=800,chunk_overlap=100).split_documents(docs);return Chroma.from_documents(chunks,emb,persist_directory=CHROMA_DIR)
