from langgraph.graph import StateGraph, START, END

from src.state import AgentState
import arxiv
import pymupdf
from urllib.request import urlopen
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
# from src.graph import graph

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0,
)

def understand_query(state: AgentState) -> AgentState:
    """Determine whether the user provided a topic, arXiv ID, or arXiv URL."""

    user_input = state["user_input"].strip()

    if "arxiv.org" in user_input.lower():
        input_type = "paper_url"
        query = user_input

    elif user_input.replace(".", "").isdigit():
        input_type = "paper_id"
        query = user_input

    else:
        input_type = "topic"
        query = user_input

    return {
        "input_type": input_type,
        "query": query,
    }


def retrieve_arxiv(state: AgentState) -> AgentState:
    """Retrieve candidate papers from arXiv."""

    input_type = state["input_type"]
    query = state["query"]

    client = arxiv.Client(
        page_size=5,
        delay_seconds=3.0,
        num_retries=2,
    )

    if input_type == "paper_id":
        search = arxiv.Search(
            id_list=[query]
        )

    elif input_type == "paper_url":
        arxiv_id = query.rstrip("/").split("/")[-1]

        search = arxiv.Search(
            id_list=[arxiv_id]
        )

    else:
        search = arxiv.Search(
            query=query,
            max_results=5,
            sort_by=arxiv.SortCriterion.Relevance,
        )

    candidate_papers = []

    for result in client.results(search):
        candidate_papers.append(
            {
                "title": result.title,
                "authors": [author.name for author in result.authors],
                "arxiv_id": result.entry_id.split("/")[-1],
                "published": result.published.isoformat(),
                "summary": result.summary,
                "pdf_url": result.pdf_url,
            }
        )

    return {
        "candidate_papers": candidate_papers
    }


def select_paper(state: AgentState) -> AgentState:
    candidate_papers = state.get("candidate_papers", [])
    query = state.get("query", "").lower().strip()

    if not candidate_papers:
        return {
            "selected_paper": {},
            "error": "No papers were found on arXiv for the given query."
        }

    query_terms = set(query.split())

    scored_papers = []

    for paper in candidate_papers:
        title = paper.get("title", "").lower()
        summary = paper.get("summary", "").lower()

        title_terms = set(title.split())
        summary_terms = set(summary.split())

        title_score = len(query_terms & title_terms) * 3
        summary_score = len(query_terms & summary_terms)

        score = title_score + summary_score

        paper["relevance_score"] = score
        scored_papers.append((score, paper))

    scored_papers.sort(key=lambda item: item[0], reverse=True)

    selected_paper = scored_papers[0][1]

    return {
        "selected_paper": selected_paper,
        "error": ""
    }


def fetch_parse(state: AgentState) -> AgentState:
    """Download the selected paper PDF and extract its text."""

    selected_paper = state.get("selected_paper", {})

    if not selected_paper:
        return {
            "paper_text": "",
            "error": "No paper was selected for PDF processing.",
        }

    pdf_url = selected_paper.get("pdf_url")

    if not pdf_url:
        return {
            "paper_text": "",
            "error": "The selected paper does not have a PDF URL.",
        }

    try:
        pdf_data = urlopen(pdf_url).read()

        document = pymupdf.open(stream=pdf_data, filetype="pdf")

        pages = []

        for page in document:
            pages.append(page.get_text())

        document.close()

        paper_text = "\n".join(pages).strip()
        reference_markers = [
        "\nReferences\n",
        "\nREFERENCES\n",
        "\nBibliography\n",
        "\nBIBLIOGRAPHY\n",
        ]

        for marker in reference_markers:
            if marker in paper_text:
                paper_text = paper_text.split(marker, 1)[0]
                break

        if not paper_text:
            return {
                "paper_text": "",
                "error": "The PDF was downloaded, but no text could be extracted.",
            }

        return {
            "paper_text": paper_text,
            "error": "",
        }

    except Exception as exc:
        return {
            "paper_text": "",
            "error": f"Failed to fetch or parse the PDF: {exc}",
        }


def chunk_embed(state: AgentState) -> AgentState:
    """Split paper text, create embeddings, and store them in ChromaDB."""

    paper_text = state.get("paper_text", "")

    if not paper_text:
        return {
            "chunks": [],
            "error": "No paper text is available for chunking.",
        }

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=200,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    chunks = splitter.split_text(paper_text)

    if not chunks:
        return {
            "chunks": [],
            "error": "No chunks were created from the paper text.",
        }

    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings = embedding_model.encode(
        chunks,
        show_progress_bar=False,
    )

    client = chromadb.Client()

    collection = client.create_collection(
        name="paper_chunks"
    )

    collection.add(
        ids=[f"chunk_{i}" for i in range(len(chunks))],
        embeddings=embeddings.tolist(),
        documents=chunks,
    )

    return {
        "chunks": chunks,
        "vector_store": collection,
        "error": "",
    }
    
def retrieve_chunks(
    state: AgentState,
    question: str,
    top_k: int = 4,
) -> AgentState:
    """Retrieve relevant paper chunks for a question."""

    collection = state.get("vector_store")

    if collection is None:
        return {
            "retrieved_chunks": [],
            "error": "Vector store is not available.",
        }

    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

    question_embedding = embedding_model.encode(
        [question]
    )[0]

    results = collection.query(
        query_embeddings=[question_embedding.tolist()],
        n_results=top_k,
    )

    retrieved_chunks = results["documents"][0]

    # Keep the beginning of the paper available for
    # high-level questions about the paper.
    paper_text = state.get("paper_text", "")

    intro_text = paper_text[:6000]

    if intro_text:
        retrieved_chunks.insert(0, intro_text)

    # Remove duplicate chunks while preserving order.
    unique_chunks = []

    for chunk in retrieved_chunks:
        if chunk not in unique_chunks:
            unique_chunks.append(chunk)

    return {
        "retrieved_chunks": unique_chunks,
        "error": "",
    }

def summarize(state: AgentState) -> AgentState:
    """Generate an executive briefing for the selected paper."""

    selected_paper = state.get("selected_paper", {})
    paper_text = state.get("paper_text", "")

    if not selected_paper:
        return {
            "briefing": "",
            "error": "No paper was selected for summarization.",
        }

    if not paper_text:
        return {
            "briefing": "",
            "error": "No paper text is available for summarization.",
        }

    title = selected_paper.get("title", "Unknown")
    authors = ", ".join(selected_paper.get("authors", []))
    arxiv_id = selected_paper.get("arxiv_id", "Unknown")
    published = selected_paper.get("published", "Unknown")
    pdf_url = selected_paper.get("pdf_url", "")

    # Use the beginning of the paper because it contains
    # the abstract and introduction.
    total_length = len(paper_text)

    total_length = len(paper_text)

    beginning = paper_text[:8000]
    
    middle_start = max(0, total_length // 2 - 4000)
    middle_end = min(total_length, total_length // 2 + 4000)
    middle = paper_text[middle_start:middle_end]
    
    ending = paper_text[-10000:]
    
    paper_context = f"""
    === BEGINNING OF PAPER ===
    {beginning}
    
    === MIDDLE OF PAPER ===
    {middle}
    
    === END OF PAPER ===
    {ending}
    """

    prompt = f"""
You are generating an executive briefing for an academic paper.

Use ONLY the paper content provided below.
Do not use outside knowledge.
Do not invent results, limitations, or claims.

Create a concise but informative briefing with exactly these sections:

1. Title
2. Authors
3. arXiv ID
4. Date
5. Link
6. Plain-English Summary
7. Problem
8. Approach
9. Key Results
10. Limitations
11. Follow-up Questions

For Limitations:
- Report limitations of the proposed method (AR-RAG), not limitations of previous/existing methods.
- Only include limitations explicitly stated by the authors.
- You may use the Conclusion or other sections if the authors explicitly discuss limitations there.
- Do not treat problems with prior methods as limitations of AR-RAG.
- If the paper does not explicitly state limitations of AR-RAG, write:
"Not clearly stated in the provided paper content."

For sections 6-11, use information from the paper content.
If a requested detail cannot be determined from the provided paper content,
write:
"Not clearly stated in the provided paper content."

Paper metadata:
Title: {title}
Authors: {authors}
arXiv ID: {arxiv_id}
Date: {published}
Link: {pdf_url}

Paper content:
{paper_context}
"""

    response = llm.invoke(prompt)

    briefing = response.content

    if isinstance(briefing, list):
        briefing = "".join(
            item.get("text", "")
            for item in briefing
            if isinstance(item, dict)
        )

    return {
        "briefing": briefing,
        "error": "",
    }


def qa(state: AgentState) -> AgentState:
    """Answer a question using only retrieved paper content."""

    question = state.get("question", "").strip()

    if not question:
        return {
            "answer": "",
            "error": "No question was provided.",
        }

    retrieval_result = retrieve_chunks(
        state,
        question,
        top_k=5,
    )

    retrieved_chunks = retrieval_result.get("retrieved_chunks", [])
    retrieved_chunks = [
    chunk
    for chunk in retrieved_chunks
    if not chunk.lstrip().startswith("[")
]

    if not retrieved_chunks:
        return {
            "answer": "The information is not available in the paper.",
            "retrieved_chunks": [],
            "error": "",
        }
    print("\n===== RETRIEVED CONTEXT =====")

    for i, chunk in enumerate(retrieved_chunks, 1):
        print(f"\n--- Chunk {i} ---")
        print(chunk[:1000])

    print("\n=============================\n")

    
    context = "\n\n---\n\n".join(retrieved_chunks)

    prompt = f"""
You are answering questions about an academic paper.

Answer the user's question using ONLY the paper excerpts provided below.

Rules:
- Do not use outside knowledge.
- Do not invent information.
- If the answer cannot be found in the excerpts, say:
  "The information is not available in the paper."
- Give a concise, clear answer.

Paper excerpts:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    answer = response.content

    if isinstance(answer, list):
        answer = "".join(
            item.get("text", "")
            for item in answer
            if isinstance(item, dict)
        )

    return {
        "retrieved_chunks": retrieved_chunks,
        "answer": answer,
        "error": "",
    }

def route_after_selection(state: AgentState) -> str:
    """Route to PDF processing only if paper selection succeeded."""

    if state.get("error"):
        return "end"

    return "fetch_parse"

def route_after_fetch(state: AgentState) -> str:
    """Route to chunking only if PDF fetching and parsing succeeded."""

    if state.get("error"):
        return "end"

    return "chunk_embed"

def route_after_chunking(state: AgentState) -> str:
    """Route to summarization only if chunking and embedding succeeded."""

    if state.get("error"):
        return "end"

    return "summarize"

def route_after_summary(state: AgentState) -> str:
    """Route to QA only if summarization succeeded."""

    if state.get("error"):
        return "end"

    return "qa"

def route_after_qa(state: AgentState) -> str:
    """End the current graph run after answering a question."""

    return "end"

# Build the state graph
builder = StateGraph(AgentState)

builder.add_node("understand_query", understand_query)
builder.add_node("retrieve_arxiv", retrieve_arxiv)
builder.add_node("select_paper", select_paper)
builder.add_node("fetch_parse", fetch_parse)
builder.add_node("chunk_embed", chunk_embed)
builder.add_node("summarize", summarize)
builder.add_node("qa", qa)

# Define the flow
builder.add_edge(START, "understand_query")
builder.add_edge("understand_query", "retrieve_arxiv")
builder.add_edge("retrieve_arxiv", "select_paper")
# builder.add_edge("select_paper", "fetch_parse")
builder.add_conditional_edges(
    "select_paper",
    route_after_selection,
    {
        "fetch_parse": "fetch_parse",
        "end": END,
    },
)

# builder.add_edge("fetch_parse", "chunk_embed")
builder.add_conditional_edges(
    "fetch_parse",
    route_after_fetch,
    {
        "chunk_embed": "chunk_embed",
        "end": END,
    },
)
# builder.add_edge("chunk_embed", "summarize")
builder.add_conditional_edges(
    "chunk_embed",
    route_after_chunking,
    {
        "summarize": "summarize",
        "end": END,
    },
)
# builder.add_edge("summarize", "qa")
# builder.add_conditional_edges(
#     "summarize",
#     route_after_summary,
#     {
#         "qa": "qa",
#         "end": END,
#     },
# )

builder.add_edge("summarize", END)
builder.add_edge("qa", END)

# Compile the graph
graph = builder.compile()