from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_minecraft_provisioning_disabled():
    response = client.post("/api/v1/provision/minecraft")
    assert response.status_code == 503
    assert "disabled" in response.json()["detail"].lower()

def test_vps_provisioning_disabled():
    response = client.post("/api/v1/provision/vps")
    assert response.status_code == 503
    assert "disabled" in response.json()["detail"].lower()

def test_branding_endpoint_is_not_claimed_implemented():
    response = client.post("/api/v1/owner/branding", json={"name":"PiratesNodes","primary_color":"#123456"})
    assert response.status_code == 501
