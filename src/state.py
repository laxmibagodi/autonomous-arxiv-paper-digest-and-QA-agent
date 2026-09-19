from typing import TypedDict, Any


class AgentState(TypedDict, total=False):
    # User's original input
    user_input: str

    # input interpreted
    input_type: str
    query: str

    # arXiv retrieval
    candidate_papers: list[dict[str, Any]]
    selected_paper: dict[str, Any]

    # Paper processing
    paper_metadata: dict[str, Any]
    paper_text: str
    chunks: list[str]

    # RAG
    vector_store: Any
    retrieved_chunks: list[str]

    # Output
    briefing: str
    question: str
    answer: str

    # Conversation / error handling
    conversation_history: list[dict[str, str]]
    error: str