"""
Report service stub.

Generates incident reports from in-memory data.
TODO: Replace with real report generation (PDF, Jira ticket, PagerDuty alert, etc.).
"""

from app.utils.logging import get_logger

logger = get_logger(__name__)


class ReportService:
    async def generate_report(self, incident_id: str) -> dict:
        """
        Generate a report for the given incident.

        TODO: Integrate with a real reporting backend, e.g.:
          - Create a Jira ticket via the Jira REST API
          - Send a PagerDuty alert
          - Write a PDF report to object storage
        """
        logger.info("generate_report (stub) | incident_id=%s", incident_id)
        return {
            "incident_id": incident_id,
            "report_url": None,
            "message": "Report generation is not yet implemented.",
        }


report_service = ReportService()
