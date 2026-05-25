"""
Tests for the /health endpoint.
"""
from app.schemas.health import HealthResponse


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]

    data = HealthResponse.model_validate(response.json())
    assert data.status == "ok"
    assert data.version