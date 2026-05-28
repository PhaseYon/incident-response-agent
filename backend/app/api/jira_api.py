from app.schemas.jira import JiraIssueCreateRequest, JiraIssueCreateResponse
from app.utils.logging import get_logger

logger = get_logger(__name__)


async def create_ticket(payload: JiraIssueCreateRequest) -> JiraIssueCreateResponse:
	"""
	Create a Jira issue via the v2 REST API.

	TODO: Replace with a real HTTP call.
	"""
	logger.info("create_ticket called (stub) | summary=%s", payload.fields.summary)
	return JiraIssueCreateResponse(
		id="stub-issue-id",
		key="TEST-1",
		self="https://jira.example.com/rest/api/2/issue/stub-issue-id",
	)
