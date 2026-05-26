from unittest.mock import Mock

import app.routes.alerts as alerts_routes
from app.schemas.alerts import AlertIngestResponse, NormalizedAlert


ALERTS_PREFIX = alerts_routes.router.prefix
ALERT_WEBHOOK_ROUTE = f"{ALERTS_PREFIX}/webhook/kibana"


def test_receive_alert_returns_expected_io(client, fake_kibana_alert, monkeypatch):
    normalized = NormalizedAlert(
        source="kibana",
        parsed_service="checkout-service",
        parsed_severity="high",
        parsed_message=fake_kibana_alert["message"],
        raw_payload=fake_kibana_alert,
    )
    normalize_alert = Mock(return_value=normalized)
    monkeypatch.setattr(alerts_routes, "normalize_alert", normalize_alert)

    response = client.post(ALERT_WEBHOOK_ROUTE, json=fake_kibana_alert)

    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]

    body = AlertIngestResponse.model_validate(response.json())
    assert body.status == "received"
    assert body.source == "kibana"
    assert body.message == fake_kibana_alert["message"]

    normalize_alert.assert_called_once_with(
        source="kibana",
        raw_payload=fake_kibana_alert,
    )