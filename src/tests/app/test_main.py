import app.main


def test_info(client):
    response = client.get("/")
    result = response.get_json()
    assert result is not None
    assert "message" in result
    assert result["message"] == "It Works"
