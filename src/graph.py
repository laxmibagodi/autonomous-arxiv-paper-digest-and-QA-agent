from langgraph.graph import StateGraph, START, END

from src.state import AgentState


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

    return {
        "candidate_papers": []
    }


def select_paper(state: AgentState) -> AgentState:
    """Select the most relevant paper from the candidates."""

    return {
        "selected_paper": {}
    }


def fetch_parse(state: AgentState) -> AgentState:
    """Fetch and parse the selected paper."""

    return {
        "paper_text": ""
    }


def chunk_embed(state: AgentState) -> AgentState:
    """Split paper text into chunks and prepare them for retrieval."""

    return {
        "chunks": []
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
