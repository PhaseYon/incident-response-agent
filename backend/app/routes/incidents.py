from fastapi import APIRouter, HTTPException

from app.schemas.incidents import IncidentListResponse, IncidentResponse
from app.services.incident_service import incident_service

router = APIRouter(prefix="/incidents", tags=["incidents"])


@router.get("", response_model=IncidentListResponse)
async def list_incidents() -> IncidentListResponse:
    """Return all incident reports currently stored in memory."""
    incidents = incident_service.list_incidents()
    return IncidentListResponse(incidents=incidents, total=len(incidents))


@router.get("/{incident_id}", response_model=IncidentResponse)
async def get_incident(incident_id: str) -> IncidentResponse:
    """Return the details of a single incident by its ID."""
    incident = incident_service.get_incident(incident_id)
    if incident is None:
        raise HTTPException(status_code=404, detail=f"Incident '{incident_id}' not found.")
    return incident
