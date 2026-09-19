from src.graph import (
    understand_query,
    select_paper,
    route_after_selection,
    route_after_fetch,
    route_after_chunking,
    fetch_parse,
    chunk_embed,
)


def test_topic_input():
    state = {
        "user_input": "papers about retrieval augmented generation"
    }

    result = understand_query(state)

    assert result["input_type"] == "topic"
    assert result["query"] == "papers about retrieval augmented generation"


def test_arxiv_id():
    state = {
        "user_input": "1706.03762"
    }

    result = understand_query(state)

    assert result["input_type"] == "paper_id"
    assert result["query"] == "1706.03762"


def test_arxiv_url():
    state = {
        "user_input": "https://arxiv.org/abs/1706.03762"
    }

    result = understand_query(state)

    assert result["input_type"] == "paper_url"
    assert result["query"] == "https://arxiv.org/abs/1706.03762"


def test_select_paper_no_results():
    result = select_paper({
        "candidate_papers": [],
        "query": "something"
    })

    assert result["selected_paper"] == {}
    assert result["error"] == "No papers were found on arXiv for the given query."


def test_select_paper_ranking():
    papers = [
        {
            "title": "Introduction to Retrieval",
            "summary": "Basic information about retrieval."
        },
        {
            "title": "Retrieval Augmented Generation",
            "summary": "Retrieval augmented generation methods."
        },
    ]

    result = select_paper({
        "candidate_papers": papers,
        "query": "retrieval augmented generation"
    })

    assert result["selected_paper"]["title"] == (
        "Retrieval Augmented Generation"
    )


def test_select_paper_preserves_existing_error():
    result = select_paper({
        "candidate_papers": [],
        "query": "something",
        "error": "Failed to retrieve papers from arXiv."
    })

    assert result["error"] == "Failed to retrieve papers from arXiv."
    assert result["selected_paper"] == {}


def test_route_after_selection():
    assert route_after_selection({
        "error": ""
    }) == "fetch_parse"

    assert route_after_selection({
        "error": "Something failed"
    }) == "end"


def test_route_after_fetch():
    assert route_after_fetch({
        "error": ""
    }) == "chunk_embed"

    assert route_after_fetch({
        "error": "PDF failed"
    }) == "end"


def test_route_after_chunking():
    assert route_after_chunking({
        "error": ""
    }) == "summarize"

    assert route_after_chunking({
        "error": "Chunking failed"
    }) == "end"
    
def test_fetch_parse_without_selected_paper():
    result = fetch_parse({
        "selected_paper": {}
    })

    assert result["paper_text"] == ""
    assert result["error"] == "No paper was selected for PDF processing."


def test_chunk_embed_without_paper_text():
    result = chunk_embed({
        "paper_text": ""
    })

    assert result["chunks"] == []
    assert result["error"] == "No paper text is available for chunking."