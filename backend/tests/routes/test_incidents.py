"""
Tests for the /incidents endpoint.
"""
import pytest

from app.db.database import incidents_store
from app.schemas.incidents import IncidentListResponse, IncidentResponse


@pytest.fixture(autouse=True)
def clear_incidents_store():
    incidents_store.clear()
    yield
    incidents_store.clear()


def test_list_incidents(client, fake_incident):
    incidents_store[fake_incident.id] = fake_incident

    response = client.get("/incidents")

    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]

    body = IncidentListResponse.model_validate(response.json())

    assert body.total == 1
    assert body.incidents == [fake_incident]


def test_get_incident_returns_200(client, fake_incident):
    incidents_store[fake_incident.id] = fake_incident

    response = client.get(f"/incidents/{fake_incident.id}")

    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]

    body = IncidentResponse.model_validate(response.json())

    assert body == fake_incident


def test_get_incident_returns_404_when_missing(client, fake_incident):
    response = client.get(f"/incidents/{fake_incident.id}")

    assert response.status_code == 404
    assert response.json() == {"detail": f"Incident '{fake_incident.id}' not found."}
