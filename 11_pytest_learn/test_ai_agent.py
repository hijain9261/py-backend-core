from unittest.mock import patch
from ai_agent import ask_ai_agent

@patch("ai_agent.requests.post")
def test_ask_ai_agent_without_internet(mock_post):

    mock_post.return_value.json.return_value = {"text": "Mocked Quantum Physics Explained"}
    result = ask_ai_agent(prompt="explain QM", api_key="fake_key")

    assert result == "Mocked Quantum Physics Explained"
    mock_post.assert_called_once()