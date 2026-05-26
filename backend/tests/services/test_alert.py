from app.services.alert_service import FAILED_TO_PARSE, normalize_alert


def test_normalize_alert_kibana(fake_kibana_alert):
    normalized = normalize_alert(source="kibana", raw_payload=fake_kibana_alert)

    assert normalized.source == "kibana"
    assert normalized.parsed_service == "checkout-service"
    assert normalized.parsed_severity == "high"
    assert normalized.parsed_message == fake_kibana_alert["message"]
    assert normalized.raw_payload == fake_kibana_alert


def test_normalize_alert_missing_fields(fake_kibana_alert):
    raw_payload = dict(fake_kibana_alert)
    raw_payload.pop("service", None)
    raw_payload.pop("severity", None)
    raw_payload.pop("message", None)

    normalized = normalize_alert(source="kibana", raw_payload=raw_payload)
    
    assert normalized.source == "kibana"
    assert normalized.parsed_service == FAILED_TO_PARSE
    assert normalized.parsed_severity == FAILED_TO_PARSE
    assert normalized.parsed_message == FAILED_TO_PARSE
    assert normalized.raw_payload == raw_payload