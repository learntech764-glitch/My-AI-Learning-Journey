from fastapi.testclient import TestClient

from app.api import app

client = TestClient(app)


def test_readiness():

    response = client.get(
        "/health/ready"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"