from fastapi import APIRouter

from app.schemas.incidents import IncidentCreate
from app.schemas.logs import (
    LogSearchRequest,
    LogSearchResponse,
    ErrorSummaryRequest,
    ErrorSummaryResponse,
)
from app.schemas.tools import (
    LatencyMetricsRequest,
    LatencyMetricsResponse,
    DeploymentRequest,
    DeploymentResponse,
    IncidentTicketRequest,
    IncidentTicketResponse,
)
from app.services.elastic_service import elastic_service
from app.services.deployment_service import deployment_service
from app.services.incident_service import incident_service

router = APIRouter(prefix="/tools", tags=["tools"])


@router.post("/search-logs", response_model=LogSearchResponse)
async def search_logs(body: LogSearchRequest) -> LogSearchResponse:
    """Search application logs stored in Elasticsearch."""
    result = await elastic_service.search_logs(
        query=body.query,
        index=body.index,
        size=body.size,
        start_time=body.start_time,
        end_time=body.end_time,
    )
    return LogSearchResponse(
        query=body.query,
        hits=result["hits"],
        total=result["total"],
        message="Log search completed (stub).",
    )


@router.post("/get-latency-metrics", response_model=LatencyMetricsResponse)
async def get_latency_metrics(body: LatencyMetricsRequest) -> LatencyMetricsResponse:
    """Retrieve latency percentile metrics for a service from Elasticsearch."""
    result = await elastic_service.get_latency_metrics(
        service=body.service,
        start_time=body.start_time,
        end_time=body.end_time,
        percentiles=body.percentiles,
    )
    return LatencyMetricsResponse(
        service=body.service,
        p50_ms=result["p50_ms"],
        p95_ms=result["p95_ms"],
        p99_ms=result["p99_ms"],
        message="Latency metrics retrieved (stub).",
    )


@router.post("/summarize-errors", response_model=ErrorSummaryResponse)
async def summarize_errors(body: ErrorSummaryRequest) -> ErrorSummaryResponse:
    """Return a summary of recent errors from Elasticsearch log indices."""
    result = await elastic_service.summarize_errors(
        index=body.index,
        size=body.size,
        start_time=body.start_time,
        end_time=body.end_time,
    )
    return ErrorSummaryResponse(
        summary=result["summary"],
        error_count=result["error_count"],
        top_errors=result["top_errors"],
    )


@router.post("/get-recent-deployments", response_model=DeploymentResponse)
async def get_recent_deployments(body: DeploymentRequest) -> DeploymentResponse:
    """Return the most recent deployments for a given service."""
    result = await deployment_service.get_recent_deployments(
        service=body.service, limit=body.limit or 5
    )
    return DeploymentResponse(
        deployments=result["deployments"],
        total=result["total"],
    )


@router.post("/create-incident-ticket", response_model=IncidentTicketResponse)
async def create_incident_ticket(body: IncidentTicketRequest) -> IncidentTicketResponse:
    """Create an incident ticket and persist it in the in-memory store."""
    incident = incident_service.create_incident(
        IncidentCreate(
            title=body.title,
            description=body.description,
            severity=body.severity,
            metadata=body.metadata,
        )
    )
    return IncidentTicketResponse(
        ticket_id=incident.id,
        title=incident.title,
        status=incident.status,
        message="Incident ticket created successfully.",
    )
