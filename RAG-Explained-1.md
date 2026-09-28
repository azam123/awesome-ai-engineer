# 🔎 RAG Explained — From Zero to Production
### 🟨 A Visual, Beginner-Friendly Guide with a Real-World Document Intelligence Project

> **Retrieval-Augmented Generation (RAG) = Search the right knowledge + give it to the LLM + generate a grounded answer.**
>
> This guide explains RAG step by step using simple language, visual diagrams, real-world analogies, practical code, and an **Enterprise Document Intelligence** example.

<div align="center">

![RAG](https://img.shields.io/badge/RAG-Retrieval--Augmented%20Generation-2563EB?style=for-the-badge)
![Document Intelligence](https://img.shields.io/badge/Project-Document%20Intelligence-16A34A?style=for-the-badge)
![Beginner Friendly](https://img.shields.io/badge/Level-Beginner%20Friendly-FACC15?style=for-the-badge)
![AI Engineering](https://img.shields.io/badge/AI%20Engineering-Production%20Patterns-7C3AED?style=for-the-badge)

**Learn the concept → visualize the pipeline → build the pieces → understand production RAG.**

</div>

---

## 🧭 Table of Contents

1. [What is RAG?](#1-what-is-rag)
2. [The Document Intelligence Project](#2-the-document-intelligence-project)
3. [Why Do We Need RAG?](#3-why-do-we-need-rag)
4. [RAG in One Picture](#4-rag-in-one-picture)
5. [The Two Pipelines: Ingestion and Query](#5-the-two-pipelines-ingestion-and-query)
6. [Step 1 — Documents and Document Intelligence](#6-step-1--documents-and-document-intelligence)
7. [Step 2 — Document Parsing and OCR](#7-step-2--document-parsing-and-ocr)
8. [Step 3 — Cleaning and Normalization](#8-step-3--cleaning-and-normalization)
9. [Step 4 — Chunking](#9-step-4--chunking)
10. [Step 5 — Embeddings](#10-step-5--embeddings)
11. [Step 6 — Vector Database](#11-step-6--vector-database)
12. [Step 7 — Metadata and Security Filters](#12-step-7--metadata-and-security-filters)
13. [Step 8 — User Query](#13-step-8--user-query)
14. [Step 9 — Query Understanding](#14-step-9--query-understanding)
15. [Step 10 — Retrieval](#15-step-10--retrieval)
16. [Step 11 — Hybrid Search](#16-step-11--hybrid-search)
17. [Step 12 — Re-ranking](#17-step-12--re-ranking)
18. [Step 13 — Prompt Augmentation](#18-step-13--prompt-augmentation)
19. [Step 14 — Generation](#19-step-14--generation)
20. [Step 15 — Citations and Grounding](#20-step-15--citations-and-grounding)
21. [Complete Document Intelligence RAG Flow](#21-complete-document-intelligence-rag-flow)
22. [Hands-On: Tokenization](#22-hands-on-tokenization)
23. [Hands-On: Chunking](#23-hands-on-chunking)
24. [Hands-On: Embeddings](#24-hands-on-embeddings)
25. [Hands-On: Vector Search](#25-hands-on-vector-search)
26. [Minimal End-to-End RAG](#26-minimal-end-to-end-rag)
27. [.NET / Azure Implementation](#27-net--azure-implementation)
28. [RAG Types](#28-rag-types)
29. [Common RAG Failures](#29-common-rag-failures)
30. [RAG Evaluation](#30-rag-evaluation)
31. [Security](#31-security)
32. [Production Architecture](#32-production-architecture)
33. [Agentic RAG](#33-agentic-rag)
34. [RAG Mental Model](#34-the-final-rag-mental-model)

---

# 1. What is RAG?

Imagine you have a **very intelligent employee**.

That employee knows how to read, reason, summarize and explain things.

But now you ask:

> "According to our company's 2026 travel policy, how much can a Principal Engineer claim for a hotel in Singapore?"

The employee may be very intelligent, but intelligence alone is not enough.

The employee needs to **look up the latest company policy**.

That is the basic idea behind RAG.

> 🟨 **RAG gives an LLM the right information at the time it needs to answer.**

### The simple formula

~~~
RAG
│
├── Retrieval     → Find relevant information
├── Augmentation  → Add that information to the prompt
└── Generation    → LLM generates the answer
~~~

### 🟨 Real-world analogy

Think about a doctor.

A doctor has years of knowledge, but for a specific patient the doctor may still:

- open the patient's medical record
- check recent test results
- look at previous prescriptions
- review clinical guidelines

Then the doctor makes a decision.

The LLM is similar:

**LLM = reasoning and language capability**

**RAG = giving the LLM the relevant evidence**

---

# 2. The Document Intelligence Project

Throughout this article, imagine we are building:

## 📚 Enterprise Document Intelligence

A company uploads:

- PDF contracts
- invoices
- HR policies
- product manuals
- insurance documents
- Word documents
- scanned documents
- presentations
- compliance documents

Employees can then ask:

> "What is the termination notice period in the Acme supplier contract?"

or:

> "What is our work-from-home policy?"

or:

> "Which invoice has an amount greater than ₹10 lakh?"

The system should:

1. understand the documents
2. extract their content
3. split them into useful chunks
4. create embeddings
5. store them for search
6. retrieve relevant evidence
7. give that evidence to the LLM
8. generate an answer
9. show citations back to the user

### 🟩 Our project

~~~mermaid
flowchart LR
    A["📄 Enterprise Documents"] --> B["🧠 Document Intelligence"]
    B --> C["✂️ Chunks"]
    C --> D["🔢 Embeddings"]
    D --> E[("🗄️ Search / Vector Store")]
    E --> F["🔍 RAG Retrieval"]
    F --> G["🤖 LLM"]
    G --> H["💬 Grounded Answer"]
    H --> I["📌 Citations"]
    
    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;
    classDef purple fill:#EDE9FE,stroke:#7C3AED,color:#111827,stroke-width:2px;
    
    class A,C yellow;
    class B,D green;
    class E,F blue;
    class G,H,I purple;
~~~

---

# 3. Why Do We Need RAG?

LLMs are powerful, but they are **not enterprise databases**.

An LLM does not automatically know:

- your company's latest policy
- today's internal sales report
- a document uploaded five minutes ago
- confidential customer information
- a newly signed contract

### Without RAG

~~~
User Question
     ↓
    LLM
     ↓
"Based on what I know..."
~~~

### With RAG

~~~
User Question
     ↓
Search enterprise knowledge
     ↓
Retrieve relevant evidence
     ↓
LLM + Evidence
     ↓
Grounded Answer
~~~

> 🔵 **Important:** RAG does not magically eliminate hallucinations. It improves grounding by giving the model relevant evidence, but retrieval quality, prompt design, model behaviour and security still matter.

---

# 4. RAG in One Picture

## 🧩 The simplest possible RAG diagram

~~~mermaid
flowchart LR
    U["👤 User<br/>What is the leave policy?"] --> Q["📝 Query"]
    Q --> R["🔍 Retrieve"]
    R --> C["📄 Relevant Chunks"]
    C --> P["🧩 Build Context"]
    P --> L["🤖 LLM"]
    L --> A["✅ Answer"]

    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;
    classDef purple fill:#EDE9FE,stroke:#7C3AED,color:#111827,stroke-width:2px;

    class U,Q yellow;
    class R,C blue;
    class P green;
    class L,A purple;
~~~

### Remember this sentence

> 🟨 **RAG is basically Search + Context + LLM.**

Everything else is about making those three parts **accurate, secure, fast and scalable**.

---

# 5. The Two Pipelines: Ingestion and Query

A production RAG system is easier to understand when you split it into **two pipelines**.

## Pipeline A — Ingestion

This happens when documents enter the system.

~~~mermaid
flowchart LR
    D["📄 Document"] --> P["🧠 Parse"]
    P --> C["✂️ Chunk"]
    C --> E["🔢 Embed"]
    E --> S[("🗄️ Store")]

    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;

    class D,P yellow;
    class C,E green;
    class S blue;
~~~

## Pipeline B — Query

This happens when a user asks a question.

~~~mermaid
flowchart LR
    Q["👤 Question"] --> E["🔢 Query Embedding"]
    E --> R["🔍 Retrieve"]
    R --> RR["📊 Re-rank"]
    RR --> P["🧩 Prompt"]
    P --> L["🤖 LLM"]
    L --> A["💬 Answer"]

    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;
    classDef purple fill:#EDE9FE,stroke:#7C3AED,color:#111827,stroke-width:2px;

    class Q,E yellow;
    class R,RR blue;
    class P green;
    class L,A purple;
~~~

### 🟩 The most important distinction

**Ingestion prepares knowledge.**

**Query-time RAG finds knowledge.**

---

# 6. Step 1 — Documents and Document Intelligence

Our Document Intelligence application may receive:

~~~
📄 contract.pdf
📄 invoice_10482.pdf
📄 employee_handbook.docx
📄 scanned_policy.pdf
📄 product_manual.pdf
~~~

A simple PDF loader may work for digitally generated PDFs.

But enterprise documents can contain:

- tables
- images
- scanned pages
- handwriting
- headers and footers
- multi-column layouts
- signatures
- forms

This is where **Document Intelligence / OCR / layout analysis** becomes important.

### 🟨 Analogy

A PDF is like a **photograph of a book**.

Before RAG can search the book, the system needs to understand:

> "What text is on this page, where is it located, which text belongs to the table, and which page did it come from?"

---

# 7. Step 2 — Document Parsing and OCR

### Example

Suppose a scanned invoice contains:

~~~
-------------------------------------
ACME INDUSTRIES
Invoice: INV-10082

Customer: Contoso Ltd.
Amount: ₹12,45,000
Due Date: 30-Sep-2026
-------------------------------------
~~~

Document Intelligence extracts structured information.

### 🟩 Extraction flow

~~~mermaid
flowchart TD
    PDF["📄 Scanned PDF"] --> OCR["👁️ OCR"]
    OCR --> TEXT["📝 Extracted Text"]
    OCR --> TABLE["📊 Tables"]
    OCR --> META["🏷️ Layout / Metadata"]
    TEXT --> NORMAL["🧹 Normalized Document"]
    TABLE --> NORMAL
    META --> NORMAL

    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;

    class PDF yellow;
    class OCR green;
    class TEXT,TABLE,META blue;
    class NORMAL green;
~~~

### Why page metadata matters

Do not store only:

~~~
"Termination notice is 90 days."
~~~

Prefer:

~~~json
{
  "text": "Termination notice is 90 days.",
  "documentId": "contract-1042",
  "fileName": "Acme-Supplier-Contract.pdf",
  "pageNumber": 18,
  "section": "Termination",
  "tenantId": "contoso",
  "department": "Legal"
}
~~~

That metadata later enables:

- citations
- filtering
- authorization
- debugging
- document tracing

---

# 8. Step 3 — Cleaning and Normalization

Raw extracted text is often messy.

For example:

~~~
TERMI-
NATION

The agreement may be termi-
nated by either party...
~~~

The ingestion pipeline may normalize it into:

~~~
TERMINATION

The agreement may be terminated by either party...
~~~

Typical processing includes:

- removing repeated headers
- removing page numbers where appropriate
- fixing broken words
- preserving headings
- normalizing whitespace
- preserving table meaning
- attaching metadata

> 🟨 **Do not blindly clean documents.** Some headers, footers, page numbers and table structures are meaningful for retrieval and citations.

---

# 9. Step 4 — Chunking

This is one of the most important RAG steps.

A 200-page contract is too large and too broad to treat as one retrieval unit.

So we split it into **chunks**.

### 🟨 Real-world analogy

Imagine giving a student an entire 500-page textbook and saying:

> "Find the answer."

Now imagine giving the student the relevant **two paragraphs**.

The second approach is much easier.

### Chunking

~~~mermaid
flowchart TD
    DOC["📕 200-page Contract"] --> C1["Chunk 1<br/>Definitions"]
    DOC --> C2["Chunk 2<br/>Payment Terms"]
    DOC --> C3["Chunk 3<br/>Termination"]
    DOC --> C4["Chunk 4<br/>Liability"]
    DOC --> C5["Chunk 5<br/>Confidentiality"]

    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;

    class DOC yellow;
    class C1,C2,C3,C4,C5 green;
~~~

### The goal of chunking

A good chunk should contain enough context to answer a question.

Bad:

~~~
"The notice period is..."
~~~

Better:

~~~
Section 14 — Termination

Either party may terminate this agreement by providing
90 days written notice to the other party.
~~~

### Chunking strategies

| Strategy | Idea | Useful for |
|---|---|---|
| Fixed-size | Split every N tokens | Simple text |
| Recursive | Prefer paragraphs/sentences | General RAG |
| Semantic | Split when meaning changes | High-quality retrieval |
| Structure-aware | Respect headings/tables/pages | Enterprise documents |
| Parent-child | Retrieve small chunk but retain parent context | Complex documents |

### A good enterprise rule

> 🟩 **Chunk by meaning first, token count second.**

---

# 10. Step 5 — Embeddings

Now we convert each chunk into numbers.

For example:

~~~
"Termination notice is 90 days."
                 ↓
        Embedding Model
                 ↓
[0.021, -0.193, 0.774, ...]
~~~

This vector represents the **semantic meaning** of the text.

### 🟨 Analogy: GPS for meaning

Imagine every sentence has a location on a huge **meaning map**.

These two sentences may be close:

~~~
"The contract can be terminated with 90 days notice."

"Either party must provide 90 days written notice to terminate."
~~~

Even though the words differ, their meanings are similar.

### Embedding flow

~~~mermaid
flowchart LR
    T["📝 Chunk Text"] --> M["🧠 Embedding Model"]
    M --> V["🔢 Vector"]
    V --> S[("🗄️ Vector Store")]

    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;

    class T yellow;
    class M green;
    class V,S blue;
~~~

---

# 11. Step 6 — Vector Database

Now we need somewhere to store:

- chunk text
- embedding
- metadata

Example:

~~~
Chunk ID: contract-1042-page-18-chunk-03

Text:
"Either party may terminate the agreement with 90 days notice."

Vector:
[0.12, -0.41, 0.83, ...]

Metadata:
documentId = contract-1042
page = 18
section = Termination
tenant = Contoso
~~~

### 🟦 Vector search

When a user asks:

> "How much notice is required to cancel the contract?"

The query also becomes a vector.

The system searches for vectors that are close to the query vector.

~~~mermaid
flowchart TD
    Q["❓ How much notice to cancel?"] --> QE["🔢 Query Vector"]
    QE --> VS["🔍 Similarity Search"]
    VS --> C1["🥇 Termination — 90 days"]
    VS --> C2["🥈 Renewal — annual"]
    VS --> C3["🥉 Payment — 30 days"]

    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;

    class Q yellow;
    class QE,VS blue;
    class C1,C2,C3 green;
~~~

---

# 12. Step 7 — Metadata and Security Filters

Enterprise RAG cannot be:

> "Search everything."

Suppose the company has:

~~~
Finance documents
HR documents
Legal documents
Engineering documents
Customer documents
~~~

An employee should not retrieve documents they are not authorized to access.

### 🔐 Retrieval should respect authorization

~~~mermaid
flowchart LR
    U["👤 User"] --> A["🔐 Identity / Claims"]
    A --> F["🛡️ Security Filter"]
    F --> R["🔍 Retrieval"]
    R --> C["📄 Authorized Chunks"]

    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;

    class U,A yellow;
    class F green;
    class R,C blue;
~~~

Example filter:

~~~
tenantId = "contoso"
AND userDepartment = "legal"
AND documentClassification IN ("internal", "confidential")
~~~

> 🔴 **Security must be enforced during retrieval, not only after the LLM generates an answer.**

---

# 13. Step 8 — User Query

Now the user asks:

> **"What is the termination notice period in the Acme supplier contract?"**

This is not simply text.

The system can identify:

- intent: retrieve contract information
- entity: Acme supplier contract
- topic: termination
- requested fact: notice period

This query may be rewritten or expanded before retrieval.

---

# 14. Step 9 — Query Understanding

Sometimes the user's wording does not match the document wording.

User:

> "How long before I can cancel it?"

Document:

> "Either party may terminate this agreement by providing 90 days written notice."

A query transformation step can make retrieval stronger:

~~~
Original Query:
"How long before I can cancel it?"

Expanded Query:
"contract termination cancellation notice period
required written notice"
~~~

Possible techniques:

- query rewriting
- query expansion
- multi-query retrieval
- HyDE
- intent classification
- metadata extraction

---

# 15. Step 10 — Retrieval

Retrieval means:

> **Find candidate chunks that may contain the answer.**

Suppose we retrieve 10 candidates.

~~~
1. Termination — 90 days
2. Contract renewal — annual
3. Payment terms — 30 days
4. Liability — $1M
5. Confidentiality — 5 years
...
~~~

The first retrieval stage should focus on **recall**.

In simple words:

> "Don't miss the correct answer."

---

# 16. Step 11 — Hybrid Search

Vector search is powerful, but semantic similarity is not always enough.

Suppose the user asks:

> "Find invoice INV-10082."

A keyword search can be excellent because **INV-10082** is an exact identifier.

For semantic questions:

> "What are the termination conditions?"

Vector search can be useful.

### 🟦 Hybrid search

~~~mermaid
flowchart TD
    Q["❓ User Query"] --> K["🔤 Keyword / BM25"]
    Q --> V["🧠 Vector Search"]
    K --> M["🔀 Merge Results"]
    V --> M
    M --> R["📊 Re-ranker"]
    R --> C["📄 Best Context"]

    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;

    class Q yellow;
    class K,V blue;
    class M,R green;
    class C blue;
~~~

### Think of it this way

**Keyword search asks:**

> "Which documents contain these words?"

**Vector search asks:**

> "Which documents mean something similar?"

**Hybrid search asks both.**

---

# 17. Step 12 — Re-ranking

Initial retrieval may return 20 candidates.

A re-ranker can inspect the query and candidate text more carefully and reorder them.

~~~
Initial retrieval

1. Payment terms
2. Renewal
3. Termination — 90 days
4. Liability
5. Confidentiality

             ↓ Re-ranker

1. Termination — 90 days  ⭐
2. Renewal
3. Payment terms
...
~~~

### 🟩 Why re-ranking helps

Vector search is designed to retrieve candidates efficiently.

A re-ranker can spend more computation deciding:

> "Which of these candidates actually answers this particular question?"

A common production pattern is:

~~~
Retrieve Top 50
      ↓
Re-rank Top 50
      ↓
Keep Top 5
      ↓
Send to LLM
~~~

---

# 18. Step 13 — Prompt Augmentation

Now we have:

**Question**

~~~
What is the termination notice period?
~~~

**Retrieved context**

~~~
Document: Acme-Supplier-Contract.pdf
Page: 18
Section: Termination

Either party may terminate this agreement by providing
90 days written notice to the other party.
~~~

We combine them.

### 🟨 Augmented prompt

~~~
SYSTEM:
Answer using only the supplied context.
If the context does not contain the answer, say that
the information was not found.

CONTEXT:
[Acme Contract — Page 18]
Either party may terminate this agreement by providing
90 days written notice...

QUESTION:
What is the termination notice period?
~~~

This is the **A in RAG — Augmented**.

---

# 19. Step 14 — Generation

The LLM receives:

~~~
Question
   +
Retrieved Context
   +
Instructions
   ↓
LLM
   ↓
Answer
~~~

Possible answer:

> "The Acme supplier contract requires **90 days' written notice** for termination."

The LLM is not expected to remember this private contract.

It is reading the retrieved evidence and producing a useful response.

---

# 20. Step 15 — Citations and Grounding

A production Document Intelligence application should ideally show:

> **The termination notice period is 90 days.**
>
> 📄 *Acme-Supplier-Contract.pdf — Page 18 — Section: Termination*

This is much more useful than:

> "The answer is 90 days."

### Why citations matter

Citations help users:

- verify the answer
- open the source
- trust the system
- detect retrieval errors
- audit decisions

### 🟩 Grounded answer flow

~~~mermaid
flowchart LR
    Q["Question"] --> R["Retrieve"]
    R --> C["Evidence"]
    C --> L["LLM"]
    L --> A["Answer"]
    C --> S["📌 Source"]
    A --> S

    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;

    class Q yellow;
    class R,C blue;
    class L,A green;
    class S yellow;
~~~

---

# 21. Complete Document Intelligence RAG Flow

Now let's connect everything.

~~~mermaid
flowchart TD
    D["📄 Enterprise Documents"] --> DI["🧠 Document Intelligence / OCR"]
    DI --> N["🧹 Normalize + Structure"]
    N --> C["✂️ Structure-aware Chunking"]
    C --> E["🔢 Embeddings"]
    E --> VS[("🗄️ Vector / Search Index")]

    U["👤 User"] --> Q["❓ Query"]
    Q --> QE["🧠 Query Understanding"]
    QE --> F["🔐 ACL + Metadata Filters"]
    F --> RS["🔍 Hybrid Retrieval"]
    RS --> RR["📊 Re-ranking"]
    RR --> PB["🧩 Prompt Builder"]
    Q --> PB
    PB --> LLM["🤖 LLM"]
    LLM --> G["🛡️ Guardrails"]
    G --> A["💬 Answer + 📌 Citations"]

    VS --> RS

    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;
    classDef purple fill:#EDE9FE,stroke:#7C3AED,color:#111827,stroke-width:2px;

    class D,U,Q yellow;
    class DI,N,C,E green;
    class VS,F,RS,RR blue;
    class QE,PB,LLM,G,A purple;
~~~

## 🧠 One-line explanation of every stage

| Stage | Simple explanation |
|---|---|
| Document | The knowledge entering the system |
| Document Intelligence | Understand text, layout, tables and OCR |
| Normalize | Clean and structure extracted content |
| Chunk | Break documents into useful retrieval units |
| Embedding | Convert meaning into vectors |
| Search Index | Store searchable chunks + metadata |
| Query | User's question |
| Query Understanding | Improve/interpret the question |
| ACL Filter | Remove unauthorized knowledge |
| Retrieval | Find candidate evidence |
| Hybrid Search | Combine lexical + semantic retrieval |
| Re-ranking | Put the best evidence first |
| Prompt Builder | Combine question + evidence + instructions |
| LLM | Generate the answer |
| Guardrails | Apply safety and policy controls |
| Citation | Show where the answer came from |

---

# 22. Hands-On: Tokenization

LLMs process tokens rather than simply reading characters as humans do.

### 🟨 Analogy

Think of a sentence as a LEGO structure.

The tokenizer breaks the sentence into smaller pieces that the model can process.

~~~mermaid
flowchart LR
    T["RAG improves document search"] --> TK["Tokenizer"]
    TK --> P["Tokens"]
    P --> ID["Token IDs"]

    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;

    class T yellow;
    class TK blue;
    class P,ID green;
~~~

### Python example

~~~python
import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4o-mini")

text = "RAG improves document search."

token_ids = encoding.encode(text)

print("Token IDs:", token_ids)
print("Token count:", len(token_ids))
~~~

### Why tokens matter in RAG

Token counts influence:

- chunk size
- context window usage
- LLM cost
- latency
- prompt size

> 🟨 **Do not choose chunk sizes blindly. Measure them with the tokenizer used by your model.**

---

# 23. Hands-On: Chunking

### Python example

~~~python
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Termination

Either party may terminate this agreement by providing
90 days written notice to the other party.

Payment

Invoices must be paid within 30 days.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
    separators=["\n\n", "\n", ". ", " ", ""]
)

chunks = splitter.split_text(text)

for index, chunk in enumerate(chunks, start=1):
    print(f"--- Chunk {index} ---")
    print(chunk)
~~~

### Important production improvement

For enterprise documents, consider preserving:

~~~
Document
 ├── Page
 │    ├── Section
 │    │    ├── Paragraph
 │    │    └── Table
 │    └── Metadata
~~~

This is usually more useful than blindly splitting every N characters.

---

# 24. Hands-On: Embeddings

~~~python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [
    "The contract can be terminated with 90 days notice.",
    "Either party must provide 90 days written notice.",
    "The invoice must be paid within 30 days."
]

embeddings = model.encode(texts)

print(embeddings.shape)
~~~

The embedding model transforms text into vectors.

~~~
Text
 ↓
Embedding Model
 ↓
Vector
 ↓
Similarity Search
~~~

> 🟩 **Embeddings are not the answer. They are a representation used to find potentially relevant information.**

---

# 25. Hands-On: Vector Search

FAISS is useful for learning and local experimentation.

~~~python
import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

chunks = [
    "Termination requires 90 days written notice.",
    "Invoices must be paid within 30 days.",
    "The annual renewal period is 12 months.",
]

vectors = model.encode(chunks).astype("float32")

index = faiss.IndexFlatL2(vectors.shape[1])
index.add(vectors)

query = "How much notice is needed to terminate?"
query_vector = model.encode([query]).astype("float32")

distances, indices = index.search(query_vector, k=2)

for rank, index_value in enumerate(indices[0], start=1):
    print(rank, chunks[index_value], distances[0][rank - 1])
~~~

### Remember

~~~
Query
  ↓
Query Embedding
  ↓
Nearest-neighbour search
  ↓
Candidate chunks
~~~

---

# 26. Minimal End-to-End RAG

Here is the smallest useful mental model in code.

~~~python
from sentence_transformers import SentenceTransformer
import faiss

documents = [
    "Employees receive 18 paid leaves per year.",
    "Employees can work from home twice per week.",
    "The standard notice period is 60 days."
]

embedder = SentenceTransformer("all-MiniLM-L6-v2")

document_vectors = embedder.encode(documents).astype("float32")

index = faiss.IndexFlatL2(document_vectors.shape[1])
index.add(document_vectors)

def retrieve(query: str, top_k: int = 2):
    query_vector = embedder.encode([query]).astype("float32")
    distances, indices = index.search(query_vector, top_k)

    return [documents[i] for i in indices[0]]

question = "How many paid leaves do employees get?"

context = retrieve(question)

print("Retrieved context:")
for item in context:
    print("-", item)
~~~

The missing final step is:

~~~
Retrieved Context
       +
User Question
       ↓
      LLM
       ↓
Final Answer
~~~

That is RAG.

---

# 27. .NET / Azure Implementation

For an enterprise .NET implementation, the architecture can look like:

~~~mermaid
flowchart TD
    API["🌐 ASP.NET Core API"] --> AUTH["🔐 Entra ID / OAuth"]
    AUTH --> ORCH["🧭 RAG Orchestrator"]

    DOC["📄 Document Upload"] --> BLOB["☁️ Azure Blob Storage"]
    BLOB --> DI["🧠 Azure AI Document Intelligence"]
    DI --> CH["✂️ Chunking Service"]
    CH --> EMB["🔢 Embedding Service"]
    EMB --> SEARCH["🔎 Azure AI Search"]

    ORCH --> SEARCH
    ORCH --> PROMPT["🧩 Prompt Builder"]
    PROMPT --> LLM["🤖 Azure OpenAI / LLM"]
    LLM --> SAFE["🛡️ Guardrails"]
    SAFE --> API

    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;
    classDef purple fill:#EDE9FE,stroke:#7C3AED,color:#111827,stroke-width:2px;

    class API,DOC yellow;
    class BLOB,DI,CH,EMB green;
    class SEARCH,ORCH blue;
    class AUTH,PROMPT,LLM,SAFE purple;
~~~

### Example C# retrieval model

~~~csharp
/// <summary>
/// Represents a piece of document content returned by the retrieval layer.
/// </summary>
public sealed class RetrievedDocumentChunk
{
    /// <summary>
    /// Gets the unique document identifier.
    /// </summary>
    public required string DocumentId { get; init; }

    /// <summary>
    /// Gets the extracted chunk text.
    /// </summary>
    public required string Content { get; init; }

    /// <summary>
    /// Gets the source page number.
    /// </summary>
    public int PageNumber { get; init; }

    /// <summary>
    /// Gets the relevance score assigned by the search layer.
    /// </summary>
    public double Score { get; init; }
}
~~~

### Example service contract

~~~csharp
/// <summary>
/// Retrieves relevant document chunks for a natural-language query.
/// </summary>
public interface IDocumentRetriever
{
    /// <summary>
    /// Retrieves the most relevant chunks that the current user is authorized to access.
    /// </summary>
    /// <param name="query">The user's natural-language question.</param>
    /// <param name="cancellationToken">Cancellation token for the request.</param>
    /// <returns>A collection of ranked document chunks.</returns>
    Task<IReadOnlyList<RetrievedDocumentChunk>> RetrieveAsync(
        string query,
        CancellationToken cancellationToken = default);
}
~~~

### A production API should expose documentation

For ASP.NET Core:

- OpenAPI / Swagger
- XML documentation
- request/response schemas
- authentication requirements
- error responses
- correlation IDs

The RAG API should be observable like any other production API.

---

# 28. RAG Types

~~~mermaid
flowchart TD
    R["RAG"] --> N["Naive RAG"]
    R --> A["Advanced RAG"]
    R --> M["Modular RAG"]
    R --> AG["Agentic RAG"]
    R --> G["Graph-based RAG"]

    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;
    classDef purple fill:#EDE9FE,stroke:#7C3AED,color:#111827,stroke-width:2px;

    class R yellow;
    class N,A green;
    class M,AG blue;
    class G purple;
~~~

| Type | Description |
|---|---|
| **Naive RAG** | Retrieve → prompt → generate |
| **Advanced RAG** | Adds query transformation, hybrid search, filters and re-ranking |
| **Modular RAG** | Retrieval components can be independently replaced |
| **Agentic RAG** | An agent decides which retrieval/tool action is needed |
| **Graph-based RAG** | Uses relationships and graph structures for retrieval |

---

# 29. Common RAG Failures

A RAG system can fail at many different points.

## Failure 1 — Wrong chunk

The answer exists, but chunking split the important context.

**Fix:** improve structure-aware chunking.

## Failure 2 — Wrong embedding

The query and answer are semantically difficult for the embedding model.

**Fix:** evaluate domain-appropriate embedding models.

## Failure 3 — Search misses the answer

The correct chunk is not in Top-K.

**Fix:** improve retrieval, hybrid search, query rewriting or index configuration.

## Failure 4 — Correct chunk but wrong ranking

The answer is retrieved but appears too low.

**Fix:** re-ranking.

## Failure 5 — Correct context but wrong answer

The LLM misunderstands or ignores the evidence.

**Fix:** improve prompt instructions, context formatting, model selection and evaluation.

## Failure 6 — Unauthorized context

A user receives information they should not access.

**Fix:** enforce ACL/tenant filters before retrieval results reach the model.

### 🟥 The debugging ladder

~~~
Wrong Answer
    ↓
Was the correct document indexed?
    ↓
Was it chunked correctly?
    ↓
Was it retrieved?
    ↓
Was it ranked highly enough?
    ↓
Was it passed to the LLM?
    ↓
Did the LLM use it correctly?
    ↓
Was the response properly cited?
~~~

> 🟨 **Do not immediately change the LLM when the real problem is retrieval.**

---

# 30. RAG Evaluation

A production RAG system needs measurement.

### Retrieval metrics

| Metric | Meaning |
|---|---|
| Recall@K | Did we retrieve the relevant chunk? |
| Precision@K | How much of retrieved content was relevant? |
| MRR | How high was the first relevant result? |
| nDCG | How good was the ranking overall? |

### Generation metrics

| Metric | Meaning |
|---|---|
| Faithfulness | Is the answer supported by the retrieved context? |
| Answer relevance | Does the answer address the question? |
| Citation correctness | Do citations actually support the answer? |
| Completeness | Did the answer cover the important information? |

### The golden dataset

Create questions such as:

~~~
Question:
What is the termination notice period?

Expected source:
Acme-Supplier-Contract.pdf, Page 18

Expected answer:
90 days

Expected citation:
Page 18 / Termination
~~~

Then test every pipeline change against the same dataset.

---

# 31. Security

Enterprise RAG introduces security risks.

### 🔐 Protect against

- prompt injection
- malicious documents
- cross-tenant data leakage
- unauthorized retrieval
- sensitive information exposure
- PII leakage
- unsafe tool calls

### Security architecture

~~~mermaid
flowchart LR
    U["👤 User"] --> AUTH["🔐 Authenticate"]
    AUTH --> ACL["🛡️ Authorize"]
    ACL --> RET["🔍 Secure Retrieval"]
    RET --> SAN["🧹 Sanitize / Validate"]
    SAN --> LLM["🤖 LLM"]
    LLM --> G["🛡️ Output Guardrails"]
    G --> R["✅ Response"]

    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;
    classDef purple fill:#EDE9FE,stroke:#7C3AED,color:#111827,stroke-width:2px;

    class U yellow;
    class AUTH,ACL green;
    class RET,SAN blue;
    class LLM,G,R purple;
~~~

---

# 32. Production Architecture

A larger enterprise Document Intelligence platform may look like this:

~~~mermaid
flowchart TD
    UP["📤 Upload API"] --> BLOB["☁️ Object Storage"]
    BLOB --> BUS["📨 Event Bus"]
    BUS --> ING["⚙️ Ingestion Worker"]
    ING --> DI["🧠 Document Intelligence"]
    DI --> PARSE["📄 Parser"]
    PARSE --> CHUNK["✂️ Chunking"]
    CHUNK --> EMB["🔢 Embeddings"]
    EMB --> IDX[("🔎 Search Index")]

    USER["👤 User"] --> API["🌐 RAG API"]
    API --> ID["🔐 Identity"]
    ID --> QRY["🧭 Query Orchestrator"]
    QRY --> FILTER["🛡️ ACL Filter"]
    FILTER --> SEARCH["🔍 Hybrid Search"]
    SEARCH --> RANK["📊 Re-ranker"]
    RANK --> CONTEXT["📚 Context Builder"]
    CONTEXT --> MODEL["🤖 LLM"]
    MODEL --> GUARD["🛡️ Guardrails"]
    GUARD --> RESP["💬 Answer + Citations"]

    IDX --> SEARCH

    OBS["📊 Observability / Evaluation"] -.-> ING
    OBS -.-> API
    OBS -.-> SEARCH
    OBS -.-> MODEL

    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;
    classDef purple fill:#EDE9FE,stroke:#7C3AED,color:#111827,stroke-width:2px;

    class UP,USER yellow;
    class BLOB,BUS,ING,DI,PARSE,CHUNK,EMB green;
    class IDX,API,QRY,FILTER,SEARCH,RANK,CONTEXT blue;
    class ID,MODEL,GUARD,RESP,OBS purple;
~~~

### Production concerns

A real enterprise implementation also needs:

- retries
- idempotency
- dead-letter queues
- document versioning
- incremental indexing
- tenant isolation
- caching
- rate limiting
- monitoring
- tracing
- evaluation
- cost controls
- disaster recovery

---

# 33. Agentic RAG

Traditional RAG follows a relatively predictable path.

Agentic RAG adds decision-making.

For example:

> "Compare the termination clauses in the Acme and Contoso contracts and tell me which one has the longer notice period."

An agent may decide:

~~~
Question
   ↓
Need two contracts
   ↓
Retrieve Acme
   ↓
Retrieve Contoso
   ↓
Extract termination clauses
   ↓
Compare
   ↓
Generate answer
   ↓
Cite both documents
~~~

### 🟪 Agentic RAG

~~~mermaid
flowchart TD
    Q["👤 Complex Question"] --> AG["🤖 Agent / Orchestrator"]
    AG --> R1["🔍 Document Search"]
    AG --> R2["🗃️ SQL"]
    AG --> R3["🌐 External API"]
    AG --> R4["📚 Knowledge Base"]
    R1 --> AG
    R2 --> AG
    R3 --> AG
    R4 --> AG
    AG --> A["💬 Final Grounded Answer"]

    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;
    classDef purple fill:#EDE9FE,stroke:#7C3AED,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;

    class Q yellow;
    class AG,A purple;
    class R1,R4 blue;
    class R2,R3 green;
~~~

RAG is therefore not disappearing.

It is increasingly becoming a **retrieval capability inside larger AI systems**.

---

# 34. The Final RAG Mental Model

If you remember only one diagram from this article, remember this:

~~~mermaid
flowchart TD
    D["📄 YOUR KNOWLEDGE"] --> P["🧠 PREPARE"]
    P --> C["✂️ CHUNK"]
    C --> E["🔢 EMBED"]
    E --> S[("🗄️ SEARCHABLE STORE")]

    U["👤 USER QUESTION"] --> Q["🧭 UNDERSTAND QUERY"]
    Q --> F["🔐 FILTER"]
    F --> R["🔍 RETRIEVE"]
    R --> RR["📊 RE-RANK"]
    RR --> CTX["📚 CONTEXT"]
    CTX --> L["🤖 LLM"]
    L --> G["🛡️ GROUND + GUARD"]
    G --> A["💬 ANSWER + 📌 CITATIONS"]

    S --> R

    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;
    classDef purple fill:#EDE9FE,stroke:#7C3AED,color:#111827,stroke-width:2px;

    class D,U yellow;
    class P,C,E green;
    class S,Q,F,R,RR,CTX blue;
    class L,G,A purple;
~~~

## 🧠 In one sentence

> **RAG is the engineering pattern of retrieving the right external knowledge at query time, giving that evidence to a language model as context, and generating a grounded response.**

## 🏗️ For our Document Intelligence project

Think:

~~~
Documents
   ↓
Document Intelligence
   ↓
Clean + Structure
   ↓
Chunk
   ↓
Embed
   ↓
Index
   ↓
User Question
   ↓
Secure Retrieval
   ↓
Hybrid Search
   ↓
Re-rank
   ↓
Context
   ↓
LLM
   ↓
Guardrails
   ↓
Answer + Citations
~~~

### ⭐ The most important lesson

> 🟨 **A RAG system is not just an LLM connected to a vector database.**
>
> A production RAG system is an end-to-end information retrieval system involving **document understanding, chunking, embeddings, indexing, retrieval, ranking, security, prompt construction, generation, citations, evaluation and observability.**


---

# 35. Top 10 Frequently Asked RAG / GenAI Interview Questions

> 🎯 **Interview preparation note:** The questions below focus on practical RAG and GenAI engineering topics that recur across public interview-preparation material and reported interview discussions. Company names indicate where similar topics have been publicly reported; they should **not** be interpreted as a guarantee that the exact wording is used in every interview.

These questions are especially useful for **Senior Software Engineer, Staff Engineer, Principal Engineer, AI Engineer and ML Engineer** interviews.

---

## Q1. What is RAG, and why would you use it instead of fine-tuning an LLM?

**Asked in / publicly reported for:** Google, Microsoft, Amazon and other AI-focused companies.

### What the interviewer is testing

Whether you understand the architectural reason for using RAG rather than simply memorizing the definition.

### Strong answer

**RAG (Retrieval-Augmented Generation)** retrieves relevant external information at query time and provides it to an LLM as context before generating the response.

RAG is useful when:

- knowledge changes frequently
- information is private or enterprise-specific
- answers need source citations
- documents need to be updated without retraining the model
- retrieval quality can be independently improved

Fine-tuning is more appropriate when the goal is to change the model's **behavior, style, task performance or domain adaptation**, rather than simply inject frequently changing factual knowledge.

### Simple example

> **RAG:** "What does our latest HR policy say about parental leave?" → retrieve the current policy → answer with citation.

> **Fine-tuning:** "Always respond to customer-support requests in our company's desired style and format."

---

## Q2. Your RAG system retrieves the wrong documents. How would you debug and improve retrieval quality?

**Asked in / publicly reported for:** Google, Microsoft and senior AI-engineering interviews.

### What the interviewer is testing

Whether you can diagnose RAG as an **information-retrieval system**, rather than immediately changing the LLM.

### Strong answer

I would debug retrieval in layers:

1. Verify the correct document was ingested.
2. Verify parsing and OCR quality.
3. Inspect chunk boundaries.
4. Evaluate the embedding model.
5. Measure **Recall@K / Precision@K**.
6. Inspect metadata filters.
7. Test keyword/BM25 retrieval.
8. Compare dense vs hybrid retrieval.
9. Add query rewriting where appropriate.
10. Add a re-ranker.
11. Build a golden evaluation dataset.
12. Compare every change against the same benchmark.

> 🟨 **Key principle:** If the correct chunk never reaches the LLM, changing the LLM will not solve the retrieval problem.

---

## Q3. How would you choose the right chunk size and chunking strategy?

**Asked in / publicly reported for:** Google, Anthropic, Microsoft and other AI engineering interviews.

### What the interviewer is testing

Whether you understand that chunking directly affects retrieval quality.

### Strong answer

There is no universal chunk size.

I would consider:

- document structure
- semantic boundaries
- average section size
- model context window
- query patterns
- retrieval metrics
- overlap requirements
- table and heading relationships

For enterprise documents, I would prefer **structure-aware or semantic chunking** over blindly splitting every N characters.

For example:

~~~
Contract
 ├── Definitions
 ├── Payment Terms
 ├── Termination
 │    ├── Notice Period
 │    └── Early Termination
 └── Liability
~~~

A chunk should ideally contain enough context to answer a question without bringing a large amount of unrelated information.

---

## Q4. What is the difference between vector search, keyword search and hybrid search?

**Asked in / publicly reported for:** Amazon, Microsoft, Google and RAG-focused interviews.

### Strong answer

**Keyword search** is excellent for exact terms such as:

~~~
INV-10082
ERR_CONNECTION_RESET
Contract-2026-001
~~~

**Vector search** is useful when semantic meaning matters:

~~~
"How can I cancel the agreement?"
~~~

may retrieve:

~~~
"Either party may terminate the contract with 90 days written notice."
~~~

**Hybrid search** combines lexical and semantic retrieval.

A typical production flow is:

~~~mermaid
flowchart LR
    Q["👤 Query"] --> BM["🔤 BM25 / Keyword Search"]
    Q --> V["🧠 Vector Search"]
    BM --> M["🔀 Merge / Fusion"]
    V --> M
    M --> RR["📊 Re-ranker"]
    RR --> C["📚 Best Context"]

    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;
    class Q yellow;
    class BM,V blue;
    class M,RR green;
    class C yellow;
~~~

> 🟩 In enterprise RAG, hybrid retrieval is often useful because real queries contain both **semantic questions and exact identifiers**.

---

## Q5. What is re-ranking, and why do we need it if vector search already returns Top-K results?

**Asked in / publicly reported for:** Anthropic, Google, Microsoft and RAG engineering interviews.

### Strong answer

The first-stage retriever is optimized for **speed and recall**.

A re-ranker performs a more expensive relevance assessment on a smaller candidate set.

For example:

~~~
1,000,000 documents
        ↓
Vector / hybrid retrieval
        ↓
Top 50 candidates
        ↓
Re-ranker
        ↓
Top 5 highly relevant chunks
        ↓
LLM
~~~

This can improve precision without running an expensive ranking model over the entire corpus.

---

## Q6. What would you do if the correct document is retrieved but the LLM still gives the wrong answer?

**Asked in / publicly reported for:** senior RAG/GenAI engineering interviews.

### Strong answer

I would separate **retrieval failure** from **generation failure**.

First verify:

- Was the correct evidence retrieved?
- Is the evidence complete?
- Is it ranked highly enough?
- Is it actually included in the final prompt?
- Is context truncated?
- Are there conflicting chunks?
- Does the prompt clearly instruct the model how to use evidence?
- Is the model following the evidence?
- Are citations generated from the retrieved source?

Possible improvements include:

- better context ordering
- removing irrelevant chunks
- contextual compression
- stronger prompt instructions
- structured context
- citation-aware generation
- a different model
- answer verification / groundedness checks

> 🟨 **Important:** "The LLM hallucinated" is not a complete diagnosis. First determine exactly where the pipeline failed.

---

## Q7. How do you evaluate a production RAG system?

**Asked in / publicly reported for:** Google, Microsoft, Anthropic and other AI/ML engineering interviews.

### Strong answer

I would evaluate both **retrieval** and **generation**.

### Retrieval metrics

| Metric | Question |
|---|---|
| Recall@K | Did the relevant document appear in the retrieved set? |
| Precision@K | How much of the retrieved content was relevant? |
| MRR | How high was the first relevant result? |
| nDCG | How good was the overall ranking? |

### Generation metrics

| Metric | Question |
|---|---|
| Faithfulness | Is the answer supported by retrieved evidence? |
| Answer Relevance | Does the answer address the user's question? |
| Citation Correctness | Do citations actually support the answer? |
| Completeness | Did the answer include the important information? |

I would maintain a **golden dataset** containing representative production questions, expected sources and expected answers, then run it whenever retrieval, prompts, embedding models or LLMs change.

---

## Q8. What is the "Lost in the Middle" problem, and how can you reduce it?

**Asked in / publicly reported for:** Anthropic and other senior RAG/LLM interviews.

### Strong answer

Even when an LLM receives a large amount of context, information placed in the middle of a long context can receive less effective attention than information near the beginning or end.

In RAG, simply retrieving more documents is therefore not always better.

Possible mitigations include:

- retrieve fewer but higher-quality chunks
- re-rank aggressively
- remove redundant context
- use contextual compression
- place the most relevant evidence strategically
- summarize or organize long evidence
- test answer quality at different context sizes

> 🟩 **More retrieved context does not automatically mean a better answer.**

---

## Q9. How would you design secure multi-tenant RAG?

**Asked in / publicly reported for:** enterprise AI and senior software engineering interviews.

### Strong answer

Security must be enforced **before unauthorized content reaches the LLM**.

A production design could be:

~~~mermaid
flowchart LR
    U["👤 User"] --> ID["🔐 Identity / Claims"]
    ID --> ACL["🛡️ Authorization Filter"]
    ACL --> RET["🔍 Secure Retrieval"]
    RET --> CTX["📚 Authorized Context"]
    CTX --> LLM["🤖 LLM"]
    LLM --> OUT["💬 Response"]

    classDef yellow fill:#FEF3C7,stroke:#D97706,color:#111827,stroke-width:2px;
    classDef green fill:#DCFCE7,stroke:#16A34A,color:#111827,stroke-width:2px;
    classDef blue fill:#DBEAFE,stroke:#2563EB,color:#111827,stroke-width:2px;
    classDef purple fill:#EDE9FE,stroke:#7C3AED,color:#111827,stroke-width:2px;

    class U yellow;
    class ID,ACL green;
    class RET,CTX blue;
    class LLM,OUT purple;
~~~

I would typically use metadata such as:

~~~
tenantId
documentId
department
classification
allowedUsers
allowedGroups
~~~

The retrieval query should apply authorization constraints so that unauthorized chunks are never supplied to the model.

---

## Q10. What is Agentic RAG, and when would you use it instead of traditional RAG?

**Asked in / publicly reported for:** Microsoft, Google and modern AI-engineering interviews.

### Strong answer

Traditional RAG generally follows:

~~~
Question
   ↓
Retrieve
   ↓
Context
   ↓
LLM
   ↓
Answer
~~~

Agentic RAG allows an agent/orchestrator to decide:

- whether retrieval is needed
- which knowledge source to use
- whether to call SQL
- whether to call an API
- whether another retrieval round is necessary
- whether the evidence is sufficient
- how multiple sources should be combined

Example:

> "Compare revenue from the database with the explanation in the quarterly business report."

The agent may use:

~~~
User Question
      ↓
Agent
 ┌────┼─────────┐
 ↓    ↓         ↓
RAG  SQL      API
 └────┼─────────┘
      ↓
  Reason / Compare
      ↓
Answer + Citations
~~~

Agentic RAG is useful when a question requires **multiple tools, iterative retrieval, planning or multi-step reasoning**. It also introduces additional concerns such as latency, cost, tool authorization, reliability and evaluation.

---

## 🏢 Company / Topic Map

The following map is intended as an **interview-preparation guide**, not as a claim that each company asks these exact questions in every interview.

| Topic | Companies publicly reported in interview-prep sources |
|---|---|
| RAG fundamentals | Google, Microsoft, Amazon and other AI companies |
| Retrieval debugging | Google, Microsoft, Anthropic |
| Chunking | Google, Anthropic, Microsoft |
| Hybrid search | Amazon, Microsoft, Google |
| Re-ranking | Anthropic, Google, Microsoft |
| RAG evaluation | Google, Microsoft, Anthropic |
| Lost in the Middle | Anthropic, Google-related interview reports |
| Secure enterprise RAG | Microsoft and enterprise AI roles |
| Agentic RAG | Microsoft, Google and modern AI roles |

Public interview reports vary in reliability, and exact questions can differ by team, role and interview loop. Treat the company names as **signals for topics to prepare**, not guarantees.

---

## 🎯 Senior/Principal Engineer Interview Tip

For senior-level interviews, do not stop at:

> "RAG retrieves documents and sends them to an LLM."

A stronger answer connects the complete system:

~~~
Documents
   ↓
Parsing / OCR
   ↓
Structure-aware Chunking
   ↓
Embeddings
   ↓
Indexing
   ↓
Metadata + ACL
   ↓
Query Understanding
   ↓
Hybrid Retrieval
   ↓
Re-ranking
   ↓
Context Construction
   ↓
LLM
   ↓
Grounded Answer
   ↓
Citations
   ↓
Evaluation + Observability
~~~

Then discuss the engineering trade-offs:

- accuracy vs latency
- recall vs precision
- context size vs cost
- model quality vs inference cost
- freshness vs indexing cost
- security vs retrieval flexibility
- simple RAG vs Agentic RAG
- managed services vs self-hosted infrastructure

> 🟨 **This is the level of thinking that turns a RAG answer from a definition into a system-design answer.**

---


---

## 📚 Useful Technologies to Explore

### Python

- LangChain
- LlamaIndex
- Haystack
- sentence-transformers
- FAISS
- Qdrant
- Chroma
- Transformers

### .NET / Azure

- ASP.NET Core
- Microsoft.Extensions.AI
- Semantic Kernel
- Azure AI Search
- Azure AI Document Intelligence
- Azure OpenAI
- Azure Blob Storage
- Azure Service Bus

### Search concepts

- Dense retrieval
- BM25
- Hybrid search
- Metadata filtering
- MMR
- Re-ranking
- Query rewriting
- Semantic search
- Vector indexing
- Retrieval evaluation

---

<div align="center">

# 🚀 Build It. Measure It. Improve It.

**RAG becomes much easier once you stop thinking of it as "LLM magic" and start thinking of it as an information retrieval pipeline.**

⭐ If this guide helped you understand RAG, consider starring the repository.

</div>
