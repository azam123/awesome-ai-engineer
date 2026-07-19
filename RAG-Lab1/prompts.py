"""
prompts.py

Centralized prompt templates for the Production RAG PDF Chatbot.
"""

from langchain_core.prompts import ChatPromptTemplate


class PromptTemplates:

    QA_PROMPT = ChatPromptTemplate.from_template(
        """
You are an expert AI assistant.

Answer ONLY using the provided context.

Rules:

1. Never hallucinate.
2. If the answer is unavailable, reply:

"I couldn't find that information in the uploaded document."

3. Mention page numbers whenever possible.

4. Use markdown.

Context:
--------------------
{context}
--------------------

Question:
{question}

Answer:
"""
    )

    SUMMARY_PROMPT = ChatPromptTemplate.from_template(
        """
Summarize the following document.

Context:
{context}

Summary:
"""
    )

    BULLET_PROMPT = ChatPromptTemplate.from_template(
        """
Create concise bullet points.

Context:
{context}

Bullet Points:
"""
    )

    COMPARE_PROMPT = ChatPromptTemplate.from_template(
        """
Compare the following information.

Context:
{context}

Question:
{question}

Comparison:
"""
    )

    KEYWORDS_PROMPT = ChatPromptTemplate.from_template(
        """
Extract important keywords.

Context:
{context}

Keywords:
"""
    )

    TABLE_PROMPT = ChatPromptTemplate.from_template(
        """
Convert the following information into a markdown table.

Context:
{context}

Table:
"""
    )

    EXPLAIN_PROMPT = ChatPromptTemplate.from_template(
        """
Explain this in simple language.

Context:
{context}

Question:
{question}

Explanation:
"""
    )

    CITATION_FORMAT = """

Sources

{sources}

"""
