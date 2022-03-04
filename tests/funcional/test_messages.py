from fastapi.testclient import TestClient
from chat_api.app import app

client = TestClient(app)


def test_read_main():
    response = client.get("/docs")
    assert response.status_code == 200


def test_get_messages_empty():
    response = client.get("/v1/messages")
    assert response.status_code == 200


def test_get_messages_not_found():
    response = client.get("/v1/messages/123")
    assert response.status_code == 404
