import pytest
import requests

BASE_URL = "http://localhost:5000/api" 
ADMIN_API_KEY = "your_admin_api_key"


 Test train functionalities (test_train.py)
def test_add_train():
    response = requests.post(f"{BASE_URL}/trains", headers={"x-api-key": ADMIN_API_KEY}, json={
        "train_name": "Express Train",
        "source": "Station A",
        "destination": "Station B",
        "total_seats": 100
    })
    assert response.status_code == 201


def test_get_train_availability():
    response = requests.get(f"{BASE_URL}/trains?source=Station A&destination=Station B")
    assert response.status_code == 200
    assert isinstance(response.json(), list) 
