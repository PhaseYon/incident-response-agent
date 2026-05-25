from unittest.mock import AsyncMock, Mock
import app.routes.tools as tools_routes
from app.schemas.logs import (
    ErrorSummaryRequest,
    ErrorSummaryResponse,
    LogSearchRequest,
    LogSearchResponse,
)
from app.schemas.tools import (
    DeploymentRequest,
    DeploymentResponse,
    IncidentTicketRequest,
    IncidentTicketResponse,
    LatencyMetricsRequest,
    LatencyMetricsResponse,
)


TOOLS_PREFIX = tools_routes.router.prefix
SEARCH_LOGS_ROUTE = f"{TOOLS_PREFIX}/search-logs"
LATENCY_METRICS_ROUTE = f"{TOOLS_PREFIX}/get-latency-metrics"
SUMMARIZE_ERRORS_ROUTE = f"{TOOLS_PREFIX}/summarize-errors"
RECENT_DEPLOYMENTS_ROUTE = f"{TOOLS_PREFIX}/get-recent-deployments"
INCIDENT_TICKET_ROUTE = f"{TOOLS_PREFIX}/create-incident-ticket"

SERVICE = "checkout-api"
START_TIME = "2026-05-25T11:00:00Z"
END_TIME = "2026-05-25T12:00:00Z"


def test_search_logs_returns_expected_io(client, monkeypatch):
    request_body = LogSearchRequest(
        query="payment timeout",
        index="app-logs",
        size=3,
        start_time=START_TIME,
        end_time=END_TIME,
    )
    expected_response = LogSearchResponse(
        query=request_body.query,
        hits=[
            {
                "timestamp": END_TIME,
                "service": SERVICE,
                "message": request_body.query,
            }
        ],
        total=1,
        message="Log search completed (stub).",
    )
    search_logs = AsyncMock(return_value={
        "hits": expected_response.hits,
        "total": expected_response.total,
    })
    monkeypatch.setattr(tools_routes.elastic_service, "search_logs", search_logs)

    response = client.post(
        SEARCH_LOGS_ROUTE,
        json=request_body.model_dump(),
    )

    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]

    body = LogSearchResponse.model_validate(response.json())

    assert body == expected_response
    search_logs.assert_awaited_once_with(**request_body.model_dump())

def test_get_latency_metrics_returns_expected_io(client, monkeypatch):
    request_body = LatencyMetricsRequest(
        service=SERVICE,
        start_time=START_TIME,
        end_time=END_TIME,
        percentiles=[50.0, 95.0, 99.0],
    )
    expected_response = LatencyMetricsResponse(
        service=request_body.service,
        p50_ms=42.5,
        p95_ms=125.0,
        p99_ms=260.25,
        message="Latency metrics retrieved (stub).",
    )
    get_latency_metrics = AsyncMock(
        return_value={
            "p50_ms": expected_response.p50_ms,
            "p95_ms": expected_response.p95_ms,
            "p99_ms": expected_response.p99_ms,
        }
    )
    monkeypatch.setattr(
        tools_routes.elastic_service, "get_latency_metrics", get_latency_metrics
    )

    response = client.post(
        LATENCY_METRICS_ROUTE,
        json=request_body.model_dump(),
    )

    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]

    body = LatencyMetricsResponse.model_validate(response.json())

    assert body == expected_response
    get_latency_metrics.assert_awaited_once_with(**request_body.model_dump())

def test_summarize_errors_returns_expected_io(client, monkeypatch):
    request_body = ErrorSummaryRequest(
        index="app-logs",
        size=5,
        start_time=START_TIME,
        end_time=END_TIME,
    )
    expected_response = ErrorSummaryResponse(
        summary="3 timeout errors detected.",
        error_count=3,
        top_errors=[{"message": "payment timeout", "count": 3}],
    )
    summarize_errors = AsyncMock(
        return_value={
            "summary": expected_response.summary,
            "error_count": expected_response.error_count,
            "top_errors": expected_response.top_errors,
        }
    )
    monkeypatch.setattr(
        tools_routes.elastic_service, "summarize_errors", summarize_errors
    )

    response = client.post(
        SUMMARIZE_ERRORS_ROUTE,
        json=request_body.model_dump(),
    )

    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]

    body = ErrorSummaryResponse.model_validate(response.json())

    assert body == expected_response
    summarize_errors.assert_awaited_once_with(**request_body.model_dump())

def test_get_recent_deployments_returns_expected_io(client, monkeypatch):
    request_body = DeploymentRequest(service=SERVICE, limit=2)
    expected_response = DeploymentResponse(
        deployments=[
            {
                "id": "deploy-123",
                "service": SERVICE,
                "version": "2026.05.25",
                "status": "succeeded",
            }
        ],
        total=1,
    )
    get_recent_deployments = AsyncMock(
        return_value={
            "deployments": expected_response.deployments,
            "total": expected_response.total,
        }
    )
    monkeypatch.setattr(
        tools_routes.deployment_service,
        "get_recent_deployments",
        get_recent_deployments,
    )

    response = client.post(
        RECENT_DEPLOYMENTS_ROUTE,
        json=request_body.model_dump(),
    )

    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]

    body = DeploymentResponse.model_validate(response.json())

    assert body == expected_response
    get_recent_deployments.assert_awaited_once_with(**request_body.model_dump())

def test_create_incident_ticket_returns_expected_io(client, fake_incident, monkeypatch):
    request_body = IncidentTicketRequest(
        title=fake_incident.title,
        description=fake_incident.description,
        severity=fake_incident.severity,
        service=SERVICE,
        metadata={"trace_id": "abc-123"},
    )
    expected_response = IncidentTicketResponse(
        ticket_id=fake_incident.id,
        title=fake_incident.title,
        status=fake_incident.status,
        message="Incident ticket created successfully.",
    )
    create_incident = Mock(return_value=fake_incident)
    monkeypatch.setattr(
        tools_routes.incident_service, "create_incident", create_incident
    )

    response = client.post(
        INCIDENT_TICKET_ROUTE,
        json=request_body.model_dump(),
    )

    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]

    body = IncidentTicketResponse.model_validate(response.json())

    assert body == expected_response

    create_incident.assert_called_once()
