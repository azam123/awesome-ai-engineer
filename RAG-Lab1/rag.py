"""
rag.py

Production RAG Pipeline

Author: Mohammad Azam Shaikh
"""

import logging

from langchain_openai import ChatOpenAI

from config import config
from prompts import PromptTemplates
from vectorstore import vector_store


logger = logging.getLogger(__name__)


class RAGPipeline:

    def __init__(self):

        self.llm = ChatOpenAI(

            model=config.GPT_MODEL,

            temperature=config.TEMPERATURE,

            api_key=config.OPENAI_API_KEY
        )

    # --------------------------------------------
    # Retrieve Context
    # --------------------------------------------

    def retrieve(self, question):

        docs = vector_store.mmr_search(question)

        return docs

    # --------------------------------------------
    # Build Context
    # --------------------------------------------

    def build_context(self, documents):

        context = []

        sources = []

        for doc in documents:

            page = doc.metadata.get("page", 0) + 1

            source = doc.metadata.get("source", "Unknown")

            context.append(

                f"""
Page {page}

{doc.page_content}
"""
            )

            sources.append(

                f"{source} (Page {page})"

            )

        return (

            "\n\n".join(context),

            sorted(set(sources))
        )

    # --------------------------------------------
    # Ask Question
    # --------------------------------------------

    def ask(self, question):

        logger.info(question)

        docs = self.retrieve(question)

        context, sources = self.build_context(docs)

        chain = PromptTemplates.QA_PROMPT | self.llm

        response = chain.invoke(

            {

                "context": context,

                "question": question

            }

        )

        answer = response.content

        answer += "\n\n### Sources\n"

        for source in sources:

            answer += f"- {source}\n"

        return answer

    # --------------------------------------------
    # Summarize
    # --------------------------------------------

    def summarize(self):

        data = vector_store.vector_db.get()

        text = ""

        for doc in data["documents"]:

            text += doc

            text += "\n"

        chain = PromptTemplates.SUMMARY_PROMPT | self.llm

        response = chain.invoke(

            {

                "context": text

            }

        )

        return response.content

    # --------------------------------------------
    # Extract Keywords
    # --------------------------------------------

    def keywords(self):

        data = vector_store.vector_db.get()

        text = "\n".join(data["documents"])

        chain = PromptTemplates.KEYWORDS_PROMPT | self.llm

        return chain.invoke(

            {

                "context": text

            }

        ).content

    # --------------------------------------------
    # Bullet Summary
    # --------------------------------------------

    def bullets(self):

        data = vector_store.vector_db.get()

        text = "\n".join(data["documents"])

        chain = PromptTemplates.BULLET_PROMPT | self.llm

        return chain.invoke(

            {

                "context": text

            }

        ).content

    # --------------------------------------------
    # Explain
    # --------------------------------------------

    def explain(self, question):

        docs = self.retrieve(question)

        context, _ = self.build_context(docs)

        chain = PromptTemplates.EXPLAIN_PROMPT | self.llm

        return chain.invoke(

            {

                "context": context,

                "question": question

            }

        ).content


rag = RAGPipeline()
