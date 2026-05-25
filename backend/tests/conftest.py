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