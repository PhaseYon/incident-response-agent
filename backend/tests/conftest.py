import pytest
from fastapi.testclient import TestClient
from app.schemas.incidents import IncidentResponse
from datetime import datetime, timezone

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def fake_incident():
    return IncidentResponse(
        id="INC-123",
        title="Checkout latency spike",
        description="p95 latency increased",
        severity="high",
        status="open",
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
        metadata={},
    )

@pytest.fixture
def fake_kibana_alert():
    return {
        "rule_name": "Checkout p95 latency threshold",
        "rule_id": "apm-latency-threshold-checkout",
        "message": "p95 latency exceeded 2000ms for 5 minutes",
        "service": "checkout-service",
        "severity": "high",
        "kibana_url": "https://kibana.example.com/app/observability/alerts/...",
    }