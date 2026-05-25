from pydantic import BaseModel


class LatencyMetricsRequest(BaseModel):
    service: str | None = None
    start_time: str | None = None
    end_time: str | None = None
    percentiles: list[float] | None = [50.0, 95.0, 99.0]


class LatencyMetricsResponse(BaseModel):
    service: str | None
    p50_ms: float | None = None
    p95_ms: float | None = None
    p99_ms: float | None = None
    message: str = ""


class DeploymentRequest(BaseModel):
    service: str | None = None
    limit: int = 5


class DeploymentResponse(BaseModel):
    deployments: list[dict] = []
    total: int = 0


class IncidentTicketRequest(BaseModel):
    title: str
    description: str
    severity: str = "medium"
    service: str | None = None
    metadata: dict | None = None


class IncidentTicketResponse(BaseModel):
    ticket_id: str
    title: str
    status: str
    message: str = ""
