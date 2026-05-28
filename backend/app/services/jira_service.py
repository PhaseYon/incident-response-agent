from app.api import jira_api
from app.schemas.jira import JiraIssueCreateRequest, JiraIssueCreateResponse
from app.utils.logging import get_logger

logger = get_logger(__name__)


async def create_ticket(payload: JiraIssueCreateRequest) -> JiraIssueCreateResponse:
	ticket = await jira_api.create_ticket(payload)
	logger.info("Jira ticket created | key=%s", ticket.key)
	return ticket


async def create_tickets(
	tickets: list[JiraIssueCreateRequest],
) -> list[JiraIssueCreateResponse]:
	created: list[JiraIssueCreateResponse] = []

	for payload in tickets:
		created.append(await create_ticket(payload))

	return created
