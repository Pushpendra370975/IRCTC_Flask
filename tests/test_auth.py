import pytest
import requests

BASE_URL = "http://localhost:5000/api"
ADMIN_API_KEY = "your_admin_api_key"


 Test authentication (test_auth.py)
def test_register():
    response = requests.post(f"{BASE_URL}/register", json={
        "username": "testuser",
        "password": "password123"
    })
    assert response.status_code == 201


def test_login():
    response = requests.post(f"{BASE_URL}/login", json={
        "username": "testuser",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "token" in response.json()
