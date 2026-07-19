"""
Production RAG PDF Chatbot

Author: Mohammad Azam Shaikh
"""

import gradio as gr

from utils import (
    configure_logging,
    create_directories,
    validate_pdf
)

from vectorstore import vector_store

from rag import rag


# ---------------------------------------
# Initial Setup
# ---------------------------------------

configure_logging()

create_directories()


# ---------------------------------------
# Global State
# ---------------------------------------

state = {

    "indexed": False

}


# ---------------------------------------
# Upload PDF
# ---------------------------------------

def upload_pdf(file):

    if file is None:

        return "Please upload a PDF."

    if not validate_pdf(file.name):

        return "Invalid file type."

    chunks = vector_store.index_pdf(

        file.name

    )

    state["indexed"] = True

    return f"""
✅ PDF Indexed Successfully

Chunks Created : {chunks}

Documents Indexed :

{vector_store.list_documents()}
"""


# ---------------------------------------
# Chat
# ---------------------------------------

def chat(

        message,

        history):

    if not state["indexed"]:

        return "Please upload a PDF first."

    return rag.ask(message)


# ---------------------------------------
# Summary
# ---------------------------------------

def summary():

    if not state["indexed"]:

        return "Upload a PDF first."

    return rag.summarize()


# ---------------------------------------
# Keywords
# ---------------------------------------

def keywords():

    if not state["indexed"]:

        return "Upload PDF first."

    return rag.keywords()


# ---------------------------------------
# Statistics
# ---------------------------------------

def statistics():

    return vector_store.stats()


# ---------------------------------------
# Build UI
# ---------------------------------------

with gr.Blocks(

    title="Production RAG PDF Chatbot"

) as demo:

    gr.Markdown(

        """
# 📄 Production RAG PDF Chatbot

Powered by

• LangChain

• OpenAI GPT-4o

• ChromaDB

• HuggingFace Embeddings
"""
    )

    pdf = gr.File(

        label="Upload PDF",

        file_types=[".pdf"]

    )

    status = gr.Markdown()

    pdf.upload(

        upload_pdf,

        inputs=pdf,

        outputs=status

    )

    chatbot = gr.ChatInterface(

        fn=chat,

        title="Ask Questions"

    )

    with gr.Row():

        summary_btn = gr.Button(

            "Summarize"

        )

        keyword_btn = gr.Button(

            "Keywords"

        )

        stats_btn = gr.Button(

            "Statistics"

        )

    output = gr.Textbox(

        lines=20,

        label="Output"

    )

    summary_btn.click(

        summary,

        outputs=output

    )

    keyword_btn.click(

        keywords,

        outputs=output

    )

    stats_btn.click(

        lambda: str(statistics()),

        outputs=output

    )


demo.launch(

    share=True,

    debug=True
)
