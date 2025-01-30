import pytest
import requests

BASE_URL = "http://localhost:5000/api" 
ADMIN_API_KEY = "your_admin_api_key"

 Test booking functionalities (test_booking.py)
def test_book_seat():
    login_resp = requests.post(f"{BASE_URL}/login", json={
        "username": "testuser",
        "password": "password123"
    })
    token = login_resp.json().get("token")
    
    response = requests.post(f"{BASE_URL}/book", headers={"Authorization": f"Bearer {token}"}, json={
        "train_id": 1,
        "seat_count": 1
    })
    assert response.status_code == 200
    assert "booking_id" in response.json()


def test_get_booking_details():
    login_resp = requests.post(f"{BASE_URL}/login", json={
        "username": "testuser",
        "password": "password123"
    })
    token = login_resp.json().get("token")
    
    response = requests.get(f"{BASE_URL}/booking/1", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert "train_id" in response.json()
