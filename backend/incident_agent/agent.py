from google.adk.agents.llm_agent import Agent

from .description import DESCRIPTION
from .instruction import INSTRUCTION
from .toolset import TOOLSET

root_agent = Agent(
    model="gemini-2.5-pro",
    name="incident_response_agent",
    description=DESCRIPTION,
    instruction=INSTRUCTION,
    tools=[TOOLSET],
)
