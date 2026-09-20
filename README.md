::: {align="center"}
# 📄 Autonomous arXiv Paper Digest & QA Agent

### 🤖 Agentic AI · RAG · LangGraph · arXiv · Grounded QA

```{=html}
<p>
```
`<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">`{=html}
`<img src="https://img.shields.io/badge/LangGraph-Agentic%20Workflow-1C3C3C?style=for-the-badge">`{=html}
`<img src="https://img.shields.io/badge/Gemini-LLM-4285F4?style=for-the-badge&logo=google&logoColor=white">`{=html}
`<img src="https://img.shields.io/badge/ChromaDB-Vector%20Store-FF6F61?style=for-the-badge">`{=html}
`<img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">`{=html}
```{=html}
</p>
```
`<br>`{=html}

### **Retrieve → Parse → Embed → Brief → Ask**

*A stateful agentic AI system for autonomous research-paper analysis and
grounded question answering.*
:::

------------------------------------------------------------------------

::: {align="center"}
```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td align="center" width="33%">
```
### 🔎 Retrieve

Research topic, arXiv ID, or URL

```{=html}
</td>
```
```{=html}
<td align="center" width="33%">
```
### 🧠 Understand

Parse, chunk, embed and index

```{=html}
</td>
```
```{=html}
<td align="center" width="33%">
```
### 💬 Answer

Brief the paper and answer questions

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
:::

## 🌟 Overview

**Autonomous arXiv Paper Digest & QA Agent** retrieves research papers
from **arXiv**, processes their PDF content, generates an **executive
briefing**, and answers questions using the selected paper as the
knowledge source.

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<th>
```
Layer
```{=html}
</th>
```
```{=html}
<th>
```
Technology
```{=html}
</th>
```
```{=html}
<th>
```
Purpose
```{=html}
</th>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🤖 Agent Orchestration
```{=html}
</td>
```
```{=html}
<td>
```
`<b>`{=html}LangGraph`</b>`{=html}
```{=html}
</td>
```
```{=html}
<td>
```
Stateful nodes, edges and conditional routing
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🧠 Generative AI
```{=html}
</td>
```
```{=html}
<td>
```
`<b>`{=html}Google Gemini`</b>`{=html}
```{=html}
</td>
```
```{=html}
<td>
```
Executive briefing and grounded QA
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🔎 Retrieval
```{=html}
</td>
```
```{=html}
<td>
```
`<b>`{=html}Official arXiv API`</b>`{=html}
```{=html}
</td>
```
```{=html}
<td>
```
Paper discovery and metadata
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
📄 PDF Processing
```{=html}
</td>
```
```{=html}
<td>
```
`<b>`{=html}PyMuPDF`</b>`{=html}
```{=html}
</td>
```
```{=html}
<td>
```
Text extraction
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🧬 Embeddings
```{=html}
</td>
```
```{=html}
<td>
```
`<b>`{=html}Sentence Transformers`</b>`{=html}
```{=html}
</td>
```
```{=html}
<td>
```
Semantic representation
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🗄️ Vector Store
```{=html}
</td>
```
```{=html}
<td>
```
`<b>`{=html}ChromaDB`</b>`{=html}
```{=html}
</td>
```
```{=html}
<td>
```
Semantic retrieval
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🖥️ Interface
```{=html}
</td>
```
```{=html}
<td>
```
`<b>`{=html}Streamlit`</b>`{=html}
```{=html}
</td>
```
```{=html}
<td>
```
Interactive application
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
## 🎯 Problem Statement

Research papers contain large amounts of technical information that can
be difficult to process quickly.

The system autonomously: - 🧠 Understands user input - 🔎 Retrieves
relevant papers from arXiv - 🎯 Selects an appropriate paper - 📥
Downloads and parses the PDF - ✂️ Splits the paper into chunks - 🧬
Generates embeddings - 📝 Creates an executive briefing - 💬 Answers
questions using paper content - 🛡️ Handles failures through conditional
routing

------------------------------------------------------------------------

## 🏗️ System Architecture

``` text
👤 USER INPUT
      │
      ▼
🧠 Understand Query
      │
      ▼
🔎 arXiv Search
      │
      ▼
🎯 Select Paper
      │
      ├──────── error ────────► END
      │
      ▼
📥 Fetch + Parse PDF
      │
      ├──────── error ────────► END
      │
      ▼
✂️ Chunk + Embed
      │
      ▼
🗄️ ChromaDB
      │
      ▼
📝 Executive Brief
      │
      ▼
💬 User Question
      │
      ▼
🔍 Retrieve Relevant Chunks
      │
      ▼
🤖 Gemini Grounded QA
      │
      ▼
✅ Paper-Based Answer
```

## 🤖 Agentic AI + GenAI + RAG

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td align="center" width="33%">
```
### 🤖 Agentic AI

`<b>`{=html}LangGraph`</b>`{=html}

Stateful nodes, shared state, edges and conditional routing.

```{=html}
</td>
```
```{=html}
<td align="center" width="33%">
```
### 🧠 GenAI

`<b>`{=html}Google Gemini`</b>`{=html}

Generates the executive briefing and paper-grounded answers.

```{=html}
</td>
```
```{=html}
<td align="center" width="33%">
```
### 🔎 RAG

`<b>`{=html}ChromaDB`</b>`{=html}

Retrieves relevant paper chunks before QA generation.

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
## 🔄 Retrieval-Augmented Generation

``` text
📄 PDF
 ↓
📑 PyMuPDF
 ↓
📃 Extracted Text
 ↓
✂️ Chunking
 ↓
🧬 Sentence Transformer
 ↓
🗄️ ChromaDB
 ↓
🔍 Semantic Retrieval
 ↓
📚 Relevant Chunks
 ↓
🤖 Gemini
 ↓
💬 Grounded Answer
```

> 🛡️ **Grounding rule:** When the requested information cannot be found
> in the paper, the system responds: **"The information is not available
> in the paper."**

------------------------------------------------------------------------

## 🖥️ Application Demo

```{=html}
<p align="center">
```
`<em>`{=html}Interactive Streamlit interface for paper analysis,
executive briefing and grounded QA.`</em>`{=html}
```{=html}
</p>
```
```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td width="50%" valign="top">
```
### 📄 Paper Analysis

```{=html}
<p align="center">
```
`<img src="docs/screenshots/01-paper-analysis.png" width="100%">`{=html}
```{=html}
</p>
```
```{=html}
</td>
```
```{=html}
<td width="50%" valign="top">
```
### 📝 Executive Briefing

```{=html}
<p align="center">
```
`<img src="docs/screenshots/02-executive-briefing.png" width="100%">`{=html}
```{=html}
</p>
```
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td width="50%" valign="top">
```
### 💬 Grounded QA

```{=html}
<p align="center">
```
`<img src="docs/screenshots/03-grounded-qa.png" width="100%">`{=html}
```{=html}
</p>
```
```{=html}
</td>
```
```{=html}
<td width="50%" valign="top">
```
### 🛡️ Grounding / Fallback

```{=html}
<p align="center">
```
`<img src="docs/screenshots/04-grounded-fallback.png" width="100%">`{=html}
```{=html}
</p>
```
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```

------------------------------------------------------------------------

## 📝 Executive Briefing

For each successfully processed paper, the agent generates:

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<th>
```
\#
```{=html}
</th>
```
```{=html}
<th>
```
Section
```{=html}
</th>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
01
```{=html}
</td>
```
```{=html}
<td>
```
📌 Title
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
02
```{=html}
</td>
```
```{=html}
<td>
```
👥 Authors
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
03
```{=html}
</td>
```
```{=html}
<td>
```
🆔 arXiv ID
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
04
```{=html}
</td>
```
```{=html}
<td>
```
📅 Date
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
05
```{=html}
</td>
```
```{=html}
<td>
```
🔗 Link
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
06
```{=html}
</td>
```
```{=html}
<td>
```
💡 Plain-English Summary
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
07
```{=html}
</td>
```
```{=html}
<td>
```
🎯 Problem
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
08
```{=html}
</td>
```
```{=html}
<td>
```
⚙️ Approach
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
09
```{=html}
</td>
```
```{=html}
<td>
```
📊 Key Results
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
10
```{=html}
</td>
```
```{=html}
<td>
```
⚠️ Limitations
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
11
```{=html}
</td>
```
```{=html}
<td>
```
❓ Follow-up Questions
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
## 🧠 Shared Agent State

``` text
user_input
input_type
query
candidate_papers
selected_paper
paper_metadata
paper_text
chunks
vector_store
retrieved_chunks
briefing
question
answer
conversation_history
error
```

Each node consumes information produced by previous stages while
maintaining a stateful workflow.

## 🧩 Node Responsibilities

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<th>
```
Node
```{=html}
</th>
```
```{=html}
<th>
```
Responsibility
```{=html}
</th>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
`<code>`{=html}understand_query`</code>`{=html}
```{=html}
</td>
```
```{=html}
<td>
```
Determines whether input is a topic, paper ID, or arXiv URL
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
`<code>`{=html}retrieve_arxiv`</code>`{=html}
```{=html}
</td>
```
```{=html}
<td>
```
Retrieves candidate papers using the official arXiv API
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
`<code>`{=html}select_paper`</code>`{=html}
```{=html}
</td>
```
```{=html}
<td>
```
Selects the most relevant candidate using deterministic lexical scoring
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
`<code>`{=html}fetch_parse`</code>`{=html}
```{=html}
</td>
```
```{=html}
<td>
```
Downloads and extracts text from the selected PDF
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
`<code>`{=html}chunk_embed`</code>`{=html}
```{=html}
</td>
```
```{=html}
<td>
```
Splits text, generates embeddings, and stores them in ChromaDB
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
`<code>`{=html}summarize`</code>`{=html}
```{=html}
</td>
```
```{=html}
<td>
```
Generates the executive briefing
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
`<code>`{=html}retrieve_chunks`</code>`{=html}
```{=html}
</td>
```
```{=html}
<td>
```
Retrieves semantically relevant chunks for a question
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
`<code>`{=html}qa`</code>`{=html}
```{=html}
</td>
```
```{=html}
<td>
```
Generates a grounded answer using retrieved paper content
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
## 🛡️ Error-Aware Routing

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<th>
```
Situation
```{=html}
</th>
```
```{=html}
<th>
```
Handling
```{=html}
</th>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🔎 No arXiv results
```{=html}
</td>
```
```{=html}
<td>
```
Stops with a clear no-results message
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🌐 arXiv retrieval failure
```{=html}
</td>
```
```{=html}
<td>
```
Returns the retrieval error
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
📄 Paper not selected
```{=html}
</td>
```
```{=html}
<td>
```
Stops before PDF processing
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
📥 PDF download failure
```{=html}
</td>
```
```{=html}
<td>
```
Stops the workflow
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
📑 PDF parsing failure
```{=html}
</td>
```
```{=html}
<td>
```
Stops the workflow
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
📃 Insufficient extracted text
```{=html}
</td>
```
```{=html}
<td>
```
Rejects unusable PDF content
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
✂️ Chunking failure
```{=html}
</td>
```
```{=html}
<td>
```
Stops before summarization
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
💬 QA information unavailable
```{=html}
</td>
```
```{=html}
<td>
```
Returns a grounded fallback response
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
## 🛠️ Technology Stack

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<th>
```
Layer
```{=html}
</th>
```
```{=html}
<th>
```
Technology
```{=html}
</th>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🐍 Language
```{=html}
</td>
```
```{=html}
<td>
```
Python
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🤖 Agent Framework
```{=html}
</td>
```
```{=html}
<td>
```
LangGraph
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🧠 LLM
```{=html}
</td>
```
```{=html}
<td>
```
Google Gemini
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🔎 Paper Retrieval
```{=html}
</td>
```
```{=html}
<td>
```
Official arXiv API
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
📄 PDF Processing
```{=html}
</td>
```
```{=html}
<td>
```
PyMuPDF
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
✂️ Text Splitting
```{=html}
</td>
```
```{=html}
<td>
```
LangChain Text Splitters
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🧬 Embeddings
```{=html}
</td>
```
```{=html}
<td>
```
Sentence Transformers
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🗄️ Vector Database
```{=html}
</td>
```
```{=html}
<td>
```
ChromaDB
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🖥️ Interface
```{=html}
</td>
```
```{=html}
<td>
```
Streamlit
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🧪 Testing
```{=html}
</td>
```
```{=html}
<td>
```
Pytest
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🔧 Development
```{=html}
</td>
```
```{=html}
<td>
```
VS Code
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🌱 Version Control
```{=html}
</td>
```
```{=html}
<td>
```
Git + GitHub
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
## 📁 Project Structure

``` text
autonomous-arxiv-paper-digest/
├── 📂 src/
│   ├── __init__.py
│   ├── state.py
│   └── graph.py
├── 📂 tests/
│   └── test_graph.py
├── 📂 data/
├── 📂 docs/
│   └── screenshots/
│       ├── 01-paper-analysis.png
│       ├── 02-executive-briefing.png
│       ├── 03-grounded-qa.png
│       └── 04-grounded-fallback.png
├── main.py
├── app.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
```

## 🚀 Installation & Setup

### 1️⃣ Clone

``` bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd autonomous-arxiv-paper-digest
```

### 2️⃣ Virtual Environment

``` powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3️⃣ Dependencies

``` bash
pip install -r requirements.txt
```

### 🔐 Environment

Create `.env`:

``` env
GOOGLE_API_KEY=your_google_api_key
```

The `.env` file is excluded from Git through `.gitignore`.

## 🖥️ Running the Application

``` bash
streamlit run app.py
```

If the Streamlit local watcher produces the previously encountered
`torchvision` watcher error:

``` bash
streamlit run app.py --server.fileWatcherType none
```

CLI mode:

``` bash
python main.py
```

## 🧪 Testing

``` bash
python -m pytest
```

Current tests cover:

-   ✅ Topic input detection
-   ✅ arXiv ID detection
-   ✅ arXiv URL detection
-   ✅ Paper selection and ranking
-   ✅ Existing error preservation
-   ✅ Conditional routing
-   ✅ Missing paper handling
-   ✅ Missing paper text handling

## 💡 Key Design Decisions

```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}1. 🧠 LangGraph for Explicit State
Management`</strong>`{=html}
```{=html}
</summary>
```
`<br>`{=html} Nodes, edges, conditional routing and shared state make
the workflow visible, stateful and easier to debug.
```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}2. 🎯 Deterministic Paper Selection`</strong>`{=html}
```{=html}
</summary>
```
`<br>`{=html} Candidate papers are ranked using deterministic lexical
matching rather than arbitrary LLM selection, making selection
reproducible.
```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}3. 🗄️ Paper-Specific Vector
Collections`</strong>`{=html}
```{=html}
</summary>
```
`<br>`{=html} Each processed arXiv paper receives its own ChromaDB
collection so chunks from different papers are not mixed during
retrieval.
```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}4. 🛡️ Grounded QA`</strong>`{=html}
```{=html}
</summary>
```
`<br>`{=html} The QA prompt restricts the model to retrieved paper
content. If the information is unavailable, a fixed fallback response is
returned rather than an invented answer.
```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}5. 🔀 Conditional Failure Routing`</strong>`{=html}
```{=html}
</summary>
```
`<br>`{=html} Each major processing stage can stop the workflow when an
error occurs, preventing downstream nodes from operating on incomplete
state.
```{=html}
</details>
```
## ⚠️ Limitations

-   Processes one selected paper at a time.
-   arXiv retrieval depends on API availability.
-   PDF extraction quality depends on the source PDF structure.
-   The current vector store exists within the running application
    process.
-   No model fine-tuning is performed.
-   No authentication is implemented.
-   No persistent multi-user storage is implemented.
-   Complex PDF layouts, scanned documents, tables, and mathematical
    formatting may not always extract perfectly.

## 🔮 Future Improvements

-   🔎 Improved query understanding and paper ranking
-   📚 Multi-paper comparison
-   🗄️ Persistent vector storage
-   🔗 Citation-aware answers
-   📊 Better table and mathematical-content extraction
-   🧠 Longer conversation memory
-   🤖 More advanced agent planning and tool selection
-   📏 Retrieval and answer-quality evaluation datasets
-   ☁️ Hosted deployment

## 📊 Project Status

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<th>
```
Component
```{=html}
</th>
```
```{=html}
<th>
```
Status
```{=html}
</th>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🧠 Query Understanding
```{=html}
</td>
```
```{=html}
<td>
```
🟢 Complete
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🔎 arXiv Retrieval
```{=html}
</td>
```
```{=html}
<td>
```
🟢 Complete
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🎯 Paper Selection
```{=html}
</td>
```
```{=html}
<td>
```
🟢 Complete
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
📥 PDF Download
```{=html}
</td>
```
```{=html}
<td>
```
🟢 Complete
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
📑 PDF Text Extraction
```{=html}
</td>
```
```{=html}
<td>
```
🟢 Complete
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
✂️ Text Chunking
```{=html}
</td>
```
```{=html}
<td>
```
🟢 Complete
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🧬 Embeddings
```{=html}
</td>
```
```{=html}
<td>
```
🟢 Complete
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🗄️ ChromaDB Storage
```{=html}
</td>
```
```{=html}
<td>
```
🟢 Complete
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
📝 Executive Briefing
```{=html}
</td>
```
```{=html}
<td>
```
🟢 Complete
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
💬 Grounded QA
```{=html}
</td>
```
```{=html}
<td>
```
🟢 Complete
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🛡️ Error Routing
```{=html}
</td>
```
```{=html}
<td>
```
🟢 Complete
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🧪 Automated Tests
```{=html}
</td>
```
```{=html}
<td>
```
🟢 Complete
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td>
```
🖥️ Streamlit Interface
```{=html}
</td>
```
```{=html}
<td>
```
🟢 Complete
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```

------------------------------------------------------------------------

::: {align="center"}
### 🚀 Technical Assessment Implementation Complete

**Retrieve · Understand · Ground · Answer**

`<br>`{=html}

🐍 **Python** · 🤖 **LangGraph** · 🧠 **Gemini** · 🔎 **arXiv** · 🗄️
**ChromaDB** · 🖥️ **Streamlit**
:::
