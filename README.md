<div align="center">

# 📄 Autonomous arXiv Paper Digest & QA Agent

### 🤖 Agentic AI · RAG · LangGraph · arXiv · Grounded QA

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/LangGraph-Agentic%20Workflow-1C3C3C?style=for-the-badge">
  <img src="https://img.shields.io/badge/Gemini-LLM-4285F4?style=for-the-badge&logo=google&logoColor=white">
  <img src="https://img.shields.io/badge/ChromaDB-Vector%20Store-FF6F61?style=for-the-badge">
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
</p>

<p>
  <img src="https://img.shields.io/badge/arXiv-Paper%20Retrieval-B31B1B?style=flat-square">
  <img src="https://img.shields.io/badge/RAG-Grounded%20QA-6A1B9A?style=flat-square">
  <img src="https://img.shields.io/badge/PyMuPDF-PDF%20Parsing-00897B?style=flat-square">
  <img src="https://img.shields.io/badge/Pytest-Testing-0A9EDC?style=flat-square">
</p>

**Retrieve → Parse → Embed → Brief → Ask**

*A stateful agentic AI system for autonomous research-paper analysis and grounded question answering.*

</div>

---

## 🌟 Overview

**Autonomous arXiv Paper Digest & QA Agent** is an agentic AI application that retrieves research papers from **arXiv**, processes their PDF content, generates an **executive briefing**, and answers questions using the selected paper as the knowledge source.

The system combines:

- 🧠 **LangGraph** for stateful agent orchestration
- 🔎 **arXiv API** for paper retrieval
- 📄 **PyMuPDF** for PDF extraction
- 🧬 **Sentence Transformers** for embeddings
- 🗄️ **ChromaDB** for vector storage
- 🤖 **Google Gemini** for summarization and QA
- 🖥️ **Streamlit** for the application interface

### Input

The user can provide:

```text
🔎 Research topic
🆔 arXiv paper ID
🔗 arXiv paper URL
Output

The agent produces:

📝 Executive Briefing
        +
💬 Grounded Paper QA
🎯 Problem Statement

Research papers contain large amounts of technical information that can be difficult to process quickly.

This project builds an autonomous workflow that can:

#	Capability
01	🧠 Understand the user's input
02	🔎 Retrieve relevant papers from arXiv
03	🎯 Select an appropriate paper
04	📥 Download and parse the PDF
05	✂️ Split the paper into meaningful chunks
06	🧬 Generate embeddings and store them
07	📝 Generate an executive briefing
08	💬 Answer questions using paper content
09	🛡️ Handle failures through conditional routing
🏗️ System Architecture
                         👤 USER INPUT
                              │
                              ▼
                  ┌─────────────────────────┐
                  │    🧠 Understand Query  │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │     🔎 arXiv Search     │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │      🎯 Select Paper    │
                  └────────────┬────────────┘
                               │
                         Conditional
                           Routing
                               │
                               ▼
                  ┌─────────────────────────┐
                  │     📥 Fetch + Parse    │
                  │          PDF            │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │      ✂️ Chunk + Embed   │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │     🗄️ ChromaDB Store  │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │    📝 Executive Brief   │
                  └─────────────────────────┘

                               │
                               ▼
                        💬 USER QUESTION
                               │
                               ▼
                  ┌─────────────────────────┐
                  │    🔍 Retrieve Chunks   │
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │    🤖 Gemini Grounded   │
                  │           QA            │
                  └────────────┬────────────┘
                               │
                               ▼
                          ✅ ANSWER
🧩 Agent Workflow

The main processing workflow is implemented as an explicit LangGraph state graph.

START
  │
  ▼
Understand Query
  │
  ▼
Retrieve arXiv Papers
  │
  ▼
Select Paper
  │
  ├──────────── error ────────────► END
  │
  ▼
Fetch + Parse PDF
  │
  ├──────────── error ────────────► END
  │
  ▼
Chunk + Embed
  │
  ├──────────── error ────────────► END
  │
  ▼
Generate Executive Briefing
  │
  ▼
END
💬 QA Loop
User Question
      │
      ▼
Semantic Retrieval
      │
      ▼
Relevant Paper Chunks
      │
      ▼
Grounded Gemini Prompt
      │
      ▼
Paper-Based Answer
🔄 Retrieval-Augmented Generation

The RAG pipeline follows:

📄 Paper PDF
     │
     ▼
📑 PyMuPDF
     │
     ▼
📃 Extracted Text
     │
     ▼
✂️ Text Chunking
     │
     ▼
🧬 Sentence Transformer
     │
     ▼
🗄️ ChromaDB
     │
     ▼
🔍 Semantic Retrieval
     │
     ▼
📚 Relevant Chunks
     │
     ▼
🤖 Gemini
     │
     ▼
💬 Grounded Answer

The QA system is explicitly instructed to use the retrieved paper content rather than relying on unsupported outside information.

If the requested information cannot be found, the agent responds:

The information is not available in the paper.

📝 Executive Briefing

For each successfully processed paper, the agent generates:

Section	Information
01	📌 Title
02	👥 Authors
03	🆔 arXiv ID
04	📅 Date
05	🔗 Link
06	💡 Plain-English Summary
07	🎯 Problem
08	⚙️ Approach
09	📊 Key Results
10	⚠️ Limitations
11	❓ Follow-up Questions

The briefing is generated from the selected paper's content and metadata.

🧠 Shared Agent State

The workflow uses a shared state object that is passed between LangGraph nodes.

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

This allows each node to consume information produced by previous stages while maintaining a stateful workflow.

🧩 Node Responsibilities
Node	Responsibility
🧠 understand_query	Determines whether input is a topic, paper ID, or arXiv URL
🔎 retrieve_arxiv	Retrieves candidate papers using the official arXiv API
🎯 select_paper	Selects the most relevant candidate using deterministic lexical scoring
📥 fetch_parse	Downloads and extracts text from the selected PDF
✂️ chunk_embed	Splits text, generates embeddings, and stores them in ChromaDB
📝 summarize	Generates the executive briefing
🔍 retrieve_chunks	Retrieves semantically relevant chunks for a question
💬 qa	Generates a grounded answer using retrieved paper content
🛡️ Error-Aware Routing

The agent does not blindly continue when a previous stage fails.

Situation	Handling
🔎 No arXiv results	Stops with a clear no-results message
🌐 arXiv retrieval failure	Returns the retrieval error
📄 Paper not selected	Stops before PDF processing
📥 PDF download failure	Stops the workflow
📑 PDF parsing failure	Stops the workflow
📃 Insufficient extracted text	Rejects unusable PDF content
✂️ Chunking failure	Stops before summarization
💬 QA information unavailable	Returns a grounded fallback response

Example:

No papers were found on arXiv for the given query.

For unsupported QA questions:

The information is not available in the paper.
🛠️ Technology Stack
Layer	Technology
🐍 Language	Python
🤖 Agent Framework	LangGraph
🧠 LLM	Google Gemini
🔎 Paper Retrieval	Official arXiv API
📄 PDF Processing	PyMuPDF
✂️ Text Splitting	LangChain Text Splitters
🧬 Embeddings	Sentence Transformers
🗄️ Vector Database	ChromaDB
🖥️ Interface	Streamlit
🧪 Testing	Pytest
🔧 Development	VS Code
🌱 Version Control	Git + GitHub
📁 Project Structure
autonomous-arxiv-paper-digest/
│
├── 📂 src/
│   ├── __init__.py
│   ├── state.py
│   └── graph.py
│
├── 📂 tests/
│   └── test_graph.py
│
├── 📂 data/
│
├── main.py
├── app.py
├── requirements.txt
├── .gitignore
├── .env.example
└── README.md
🚀 Installation & Setup
1️⃣ Clone the Repository
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd autonomous-arxiv-paper-digest
2️⃣ Create a Virtual Environment
python -m venv .venv
Windows PowerShell
.venv\Scripts\Activate.ps1
Windows CMD
.venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
🔐 Environment Configuration

Create a .env file in the project root:

GOOGLE_API_KEY=your_google_api_key

The .env file is excluded from Git through .gitignore.

A template is provided:

.env.example
🖥️ Running the Application
Streamlit Interface

Start the application:

streamlit run app.py

The interface allows users to:

🔎 Enter a research topic, arXiv ID, or arXiv URL.
⚙️ Analyze the paper.
📝 View the executive briefing.
💬 Ask questions about the paper.
✅ Receive grounded answers.
Optional Streamlit Watcher Workaround

If Streamlit's local file watcher produces a torchvision-related watcher error, run:

streamlit run app.py --server.fileWatcherType none

This only disables the file watcher and does not change the agent workflow.

💻 CLI Mode

The backend can also be run directly:

python main.py

The CLI supports:

Research topic
arXiv paper ID
arXiv paper URL

After processing the paper, an interactive QA loop is available.

Type:

exit

to quit.

🧪 Example Inputs
🔹 arXiv Paper ID
1706.03762
🔹 arXiv URL
https://arxiv.org/abs/1706.03762
🔹 Research Topic
retrieval augmented generation
🧪 Testing

Automated tests are included using pytest.

Run:

python -m pytest
Test Coverage
✅ Topic input detection
✅ arXiv ID detection
✅ arXiv URL detection
✅ Paper selection
✅ Paper ranking
✅ Existing error preservation
✅ Conditional routing
✅ Missing paper handling
✅ Missing paper text handling
💡 Key Design Decisions
1. 🧠 LangGraph for Explicit State Management

LangGraph makes the workflow visible through:

Nodes
Edges
Conditional routing
Shared state

This makes the agent easier to reason about and debug.

2. 🎯 Deterministic Paper Selection

Candidate papers are ranked using deterministic lexical matching rather than arbitrary LLM selection.

This makes paper selection reproducible.

3. 🗄️ Paper-Specific Vector Collections

Each processed arXiv paper receives its own ChromaDB collection.

This prevents chunks from different papers from being mixed during retrieval.

4. 🛡️ Grounded QA

The QA prompt explicitly restricts the model to retrieved paper content.

When information is unavailable, the system uses a fixed fallback response rather than inventing an answer.

5. 🔀 Conditional Failure Routing

Each major processing stage can stop the workflow when an error occurs.

This prevents downstream nodes from operating on incomplete state.

⚠️ Limitations
Processes one selected paper at a time.
arXiv retrieval depends on API availability.
PDF extraction quality depends on the source PDF structure.
The current vector store exists within the running application process.
No model fine-tuning is performed.
No authentication is implemented.
No persistent multi-user storage is implemented.
Complex PDF layouts, scanned documents, tables, and mathematical formatting may not always extract perfectly.
🔮 Future Improvements

Potential extensions include:

🔎 Improved query understanding and paper ranking
📚 Multi-paper comparison
🗄️ Persistent vector storage
🔗 Citation-aware answers
📊 Better table and mathematical-content extraction
🧠 Longer conversation memory
🤖 More advanced agent planning and tool selection
📏 Retrieval and answer-quality evaluation datasets
☁️ Hosted deployment
✅ Project Status
Component	Status
🧠 Query Understanding	🟢 Complete
🔎 arXiv Retrieval	🟢 Complete
🎯 Paper Selection	🟢 Complete
📥 PDF Download	🟢 Complete
📑 PDF Text Extraction	🟢 Complete
✂️ Text Chunking	🟢 Complete
🧬 Embeddings	🟢 Complete
🗄️ ChromaDB Storage	🟢 Complete
📝 Executive Briefing	🟢 Complete
💬 Grounded QA	🟢 Complete
🛡️ Error Routing	🟢 Complete
🧪 Automated Tests	🟢 Complete
🖥️ Streamlit Interface	🟢 Complete
📖 Documentation	🟢 Complete
🚀 Project Highlights
<div align="center">
🤖 Agentic Workflow	🔎 Grounded Retrieval	🛡️ Failure Handling
Stateful LangGraph	RAG + ChromaDB	Conditional Routing
📄 Paper Understanding	💬 Interactive QA	🖥️ Application Layer
Executive Briefing	Paper-Grounded Answers	Streamlit
</div>
📌 Project Status

Technical assessment implementation complete.

The system currently supports the complete workflow from:

User Input → Paper Retrieval → PDF Processing → Vector Retrieval → Executive Briefing → Grounded QA

<div align="center">
📄 Autonomous arXiv Paper Digest & QA Agent

Retrieve · Understand · Ground · Answer

Built with 🐍 Python · 🤖 LangGraph · 🧠 Gemini · 🔎 arXiv · 🗄️ ChromaDB · 🖥️ Streamlit

</div>
