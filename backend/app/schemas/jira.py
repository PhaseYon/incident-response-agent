from pydantic import BaseModel


class JiraProject(BaseModel):
	key: str


class JiraIssueType(BaseModel):
	name: str


class JiraIssueFields(BaseModel):
	project: JiraProject
	summary: str
	description: str
	issuetype: JiraIssueType


class JiraIssueCreateRequest(BaseModel):
	fields: JiraIssueFields


class JiraIssueCreateResponse(BaseModel):
	id: str
	key: str
	self: str
