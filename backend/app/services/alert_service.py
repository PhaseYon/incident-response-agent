from typing import Any
from datetime import datetime, timezone

from app.schemas.alerts import NormalizedAlert


FAILED_TO_PARSE = "failed_to_parse"


def first_present(raw_payload: dict[str, Any], keys: list[str]) -> str:
    for key in keys:
        value = raw_payload.get(key)

        if value:
            return str(value)

    return FAILED_TO_PARSE

def normalize_alert(source: str, raw_payload: dict[str, Any]) -> NormalizedAlert:
    parsed_service = first_present(
        raw_payload,
        ["service", "service_name", "app", "application", "failed_service"],
    )

    parsed_severity = first_present(
        raw_payload,
        ["severity", "priority", "level", "severity_of_incident"],
    )

    parsed_message = first_present(
        raw_payload,
        ["message", "title", "description", "alert_message", "reason"],
    )

    return NormalizedAlert(
        source=source,
        parsed_service=parsed_service,
        parsed_severity=parsed_severity,
        parsed_message=parsed_message,
        raw_payload=raw_payload,
    )