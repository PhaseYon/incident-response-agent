import json

from app.schemas.agent import AgentResponse
from app.schemas.alerts import NormalizedAlert
from app.utils.logging import get_logger
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from incident_agent.agent import root_agent

logger = get_logger(__name__)

session_service = InMemorySessionService()

runner = Runner(
    agent=root_agent,
    app_name="incident_response_agent",
    session_service=session_service,
)

async def process_alert(normalized: NormalizedAlert) -> AgentResponse:
    prompt = json.dumps(normalized.model_dump(), indent=2)

    session_id = "some-session-id"
    user_id = "system"

    await session_service.create_session(
        app_name="incident_response_agent",
        user_id=user_id,
        session_id=session_id,
    )

    message = types.Content(
        role="user",
        parts=[types.Part(text=prompt)],
    )

    final_text = None

    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=message,
    ):
        if event.is_final_response() and event.content and event.content.parts:
            final_text = event.content.parts[0].text

    if final_text is None:
        raise RuntimeError("Agent did not return a final response.")

    response_dict = json.loads(final_text)
    return AgentResponse.model_validate(response_dict)
