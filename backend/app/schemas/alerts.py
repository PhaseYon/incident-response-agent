from datetime import datetime, timezone
from typing import Any

from pydantic import BaseModel, Field


class AlertIngestResponse(BaseModel):
    status: str
    source: str
    message: str = ""

class NormalizedAlert(BaseModel):
    source: str

    parsed_service: str = "failed_to_parse"
    parsed_severity: str = "failed_to_parse"
    parsed_message: str = "failed_to_parse"

    received_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    raw_payload: dict[str, Any] = Field(default_factory=dict)