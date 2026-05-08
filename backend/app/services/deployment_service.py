"""
Deployment service stub.

Returns placeholder deployment data.
TODO: Replace with real calls to a CI/CD provider (GitHub Actions, ArgoCD, etc.)
      or query deployment events from Elasticsearch.
"""

from app.utils.logging import get_logger

logger = get_logger(__name__)


class DeploymentService:
    async def get_recent_deployments(
        self, service: str | None = None, limit: int = 5
    ) -> dict:
        """
        Fetch recent deployments for a given service.

        TODO: Query a real deployment store, e.g.:
          - GitHub Actions API for workflow run history
          - ArgoCD REST API for application sync history
          - Elasticsearch deployment event index
        """
        logger.info("get_recent_deployments (stub) | service=%s limit=%d", service, limit)
        return {"deployments": [], "total": 0}


deployment_service = DeploymentService()
