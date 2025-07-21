from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_pirate_style():
    response = client.post("/style", data={"text": "you stole my treasure.", "style": "pirate"})
    assert response.status_code == 200
    assert "ye" in response.json()["styled_text"].lower()

def test_reverse_style():
    response = client.post("/style", data={"text": "hello", "style": "reverse"})
    assert response.status_code == 200
    assert response.json()["styled_text"] == "olleh"

def test_invalid_style_fallback():
    response = client.post("/style", data={"text": "test", "style": "nonexistent"})
    assert response.status_code == 200
    assert response.json()["styled_text"] == "test"

    