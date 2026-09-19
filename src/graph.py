from langgraph.graph import StateGraph, START, END

from src.state import AgentState
import arxiv
import pymupdf
from urllib.request import urlopen
from langchain_text_splitters import RecursiveCharacterTextSplitter


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
    """Select the most relevant paper from the candidates."""

    candidate_papers = state.get("candidate_papers", [])

    if not candidate_papers:
        return {
            "selected_paper": {},
            "error": "No papers were found on arXiv for the given query.",
        }

    selected_paper = candidate_papers[0]

    return {
        "selected_paper": selected_paper,
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
    """Split paper text into overlapping chunks for retrieval."""

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

    return {
        "chunks": chunks,
        "error": "",
    }


def summarize(state: AgentState) -> AgentState:
    """Generate an executive briefing for the selected paper."""

    return {
        "briefing": ""
    }


def qa(state: AgentState) -> AgentState:
    """Answer a question using retrieved paper content."""

    return {
        "answer": ""
    }


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
builder.add_edge("select_paper", "fetch_parse")
builder.add_edge("fetch_parse", "chunk_embed")
builder.add_edge("chunk_embed", "summarize")
builder.add_edge("summarize", "qa")
builder.add_edge("qa", END)

# Compile the graph
graph = builder.compile()
