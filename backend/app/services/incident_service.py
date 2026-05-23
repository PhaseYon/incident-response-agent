"""
Incident service.

Manages CRUD operations on the in-memory incident store.
TODO: Replace in-memory operations with a real database (e.g., SQLAlchemy + PostgreSQL).
"""

import uuid
from datetime import datetime

from app.db.database import incidents_store
from app.db.models import IncidentModel
from app.schemas.incidents import IncidentCreate, IncidentResponse
from app.utils.logging import get_logger

logger = get_logger(__name__)


class IncidentService:
    def create_incident(self, data: IncidentCreate) -> IncidentResponse:
        incident_id = str(uuid.uuid4())
        now = datetime.utcnow()
        incident = IncidentModel(
            id=incident_id,
            title=data.title,
            description=data.description,
            severity=data.severity,
            status="open",
            created_at=now,
            updated_at=now,
            metadata=data.metadata or {},
        )
        incidents_store[incident_id] = incident
        logger.info("Incident created | id=%s title=%s", incident_id, data.title)
        return self._to_response(incident)

    def get_incident(self, incident_id: str) -> IncidentResponse | None:
        incident = incidents_store.get(incident_id)
        if incident is None:
            return None
        return self._to_response(incident)

    def list_incidents(self) -> list[IncidentResponse]:
        return [self._to_response(i) for i in incidents_store.values()]

    @staticmethod
    def _to_response(model: IncidentModel) -> IncidentResponse:
        return IncidentResponse(
            id=model.id,
            title=model.title,
            description=model.description,
            severity=model.severity,
            status=model.status,
            created_at=model.created_at,
            updated_at=model.updated_at,
            metadata=model.metadata,
        )


incident_service = IncidentService()
