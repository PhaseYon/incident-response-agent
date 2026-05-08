"""
Data models for in-memory storage.

These dataclasses mirror the shape of objects persisted in the in-memory store.
Replace with SQLAlchemy ORM models when integrating a real database.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class IncidentModel:
    id: str
    title: str
    description: str
    severity: str
    status: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    metadata: dict = field(default_factory=dict)
