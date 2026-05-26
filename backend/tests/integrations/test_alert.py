from app.schemas.alerts import AlertIngestResponse


def test_alert_webhook_integration(client, fake_kibana_alert):
    response = client.post("/alerts/webhook/kibana", json=fake_kibana_alert)

    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]

    body = AlertIngestResponse.model_validate(response.json())
    assert body.status == "received"
    assert body.source == "kibana"
    assert body.message == fake_kibana_alert["message"]