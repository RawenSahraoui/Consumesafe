from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_check_product():
    response = client.post("/api/v1/check-product", json={"product_name": "Coca Cola"})
    assert response.status_code == 200
    assert response.json()["is_boycotted"] == True