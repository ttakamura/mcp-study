from mcp_study import hello


def test_hello():
    """Test that the hello function returns the correct greeting."""
    result = hello()
    assert result == "Hello from mcp-study!"