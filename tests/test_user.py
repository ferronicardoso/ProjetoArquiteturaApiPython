from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_user():
    response = client.post("/users/", json={"id": 1, "name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john@example.com"}


def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john@example.com"}
