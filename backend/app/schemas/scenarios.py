from pydantic import BaseModel


class ScenarioResponse(BaseModel):
    scenario: str
    status: str
    message: str = ""
