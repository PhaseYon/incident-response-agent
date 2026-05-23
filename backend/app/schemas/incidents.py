from datetime import datetime

from pydantic import BaseModel


class IncidentCreate(BaseModel):
    title: str
    description: str
    severity: str = "medium"
    metadata: dict | None = None


class IncidentResponse(BaseModel):
    id: str
    title: str
    description: str
    severity: str
    status: str
    created_at: datetime
    updated_at: datetime
    metadata: dict = {}


class IncidentListResponse(BaseModel):
    incidents: list[IncidentResponse]
    total: int
