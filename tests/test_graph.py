from src.graph import understand_query


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


def test_arxiv_url():
    state = {
        "user_input": "https://arxiv.org/abs/1706.03762"
    }

    result = understand_query(state)

    assert result["input_type"] == "paper_url"