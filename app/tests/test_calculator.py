from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Calculator App!"}

def test_add():
    response = client.get("/add/1/2")
    assert response.status_code == 200
    assert response.json() == {"result": 3.0}

def test_subtract():
    response = client.get("/subtract/5/2")
    assert response.status_code == 200
    assert response.json() == {"result": 3.0}

def test_multiply():
    response = client.get("/multiply/3/4")
    assert response.status_code == 200
    assert response.json() == {"result": 12.0}

def test_divide():
    response = client.get("/divide/10/2")
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}

def test_divide_by_zero():
    response = client.get("/divide/10/0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Division by zero is not allowed"}
