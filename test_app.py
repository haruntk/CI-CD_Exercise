import pytest
from app import app

def test_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.data == b"Hello, CI/CD Pipeline!"
        assert response.status_code == 200
