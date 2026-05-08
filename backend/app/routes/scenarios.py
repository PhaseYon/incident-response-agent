"""
Scenario routes.

Simulate infrastructure scenarios (e.g., payment-latency) for testing
the incident response agent without a live production environment.

TODO: Replace the in-memory flag with real infrastructure calls, e.g.:
  - Fault-injection via Chaos Mesh / Gremlin API
  - Feature flag toggle via LaunchDarkly / Unleash
  - Kubernetes network policy manipulation
"""

from fastapi import APIRouter

from app.schemas.scenarios import ScenarioResponse
from app.utils.logging import get_logger

router = APIRouter(prefix="/scenarios", tags=["scenarios"])
logger = get_logger(__name__)

# In-memory scenario state: scenario_name -> bool (active/inactive)
_scenario_state: dict[str, bool] = {
    "payment-latency": False,
}


@router.post("/payment-latency/on", response_model=ScenarioResponse)
async def payment_latency_on() -> ScenarioResponse:
    """Activate the payment-latency simulation scenario."""
    _scenario_state["payment-latency"] = True
    logger.info("Scenario payment-latency ACTIVATED")
    return ScenarioResponse(
        scenario="payment-latency",
        status="active",
        message="Payment latency scenario has been activated.",
    )


@router.post("/payment-latency/off", response_model=ScenarioResponse)
async def payment_latency_off() -> ScenarioResponse:
    """Deactivate the payment-latency simulation scenario."""
    _scenario_state["payment-latency"] = False
    logger.info("Scenario payment-latency DEACTIVATED")
    return ScenarioResponse(
        scenario="payment-latency",
        status="inactive",
        message="Payment latency scenario has been deactivated.",
    )
