from pydantic import BaseModel

from app.schemas.jira import JiraIssueCreateRequest


class AgentResponse(BaseModel):
	success: bool
	tickets: list[JiraIssueCreateRequest]
