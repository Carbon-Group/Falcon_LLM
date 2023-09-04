import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Тесты для API сервера

def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the API server"}

def test_process_request_with_valid_token():
    response = client.post(
        "/process_request/",
        json={"prompt": "Translate: I love programming."},
        headers={"Authorization": "Bearer your_secret_token"},
    )
    assert response.status_code == 200
    assert "response" in response.json()

def test_process_request_with_invalid_token():
    response = client.post(
        "/process_request/",
        json={"prompt": "Translate: I love programming."},
        headers={"Authorization": "Bearer invalid_token"},
    )
    assert response.status_code == 403

def test_process_request_missing_token():
    response = client.post(
        "/process_request/",
        json={"prompt": "Translate: I love programming."},
    )
    assert response.status_code == 401