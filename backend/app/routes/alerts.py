from typing import Any
from app.services.alert_service import normalize_alert

from fastapi import APIRouter
from app.schemas.alerts import AlertIngestResponse, NormalizedAlert

router = APIRouter(prefix="/alerts", tags=["alerts"])
@router.post("/webhook/{source}", response_model=AlertIngestResponse)
async def receive_alert(source: str, raw_payload: dict[str, Any]):
    normalized = normalize_alert(source=source, raw_payload=raw_payload)

    return AlertIngestResponse(
        status="received",
        source=normalized.source,
        message=normalized.parsed_message,
    )