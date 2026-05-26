from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

from .config import settings


TOOLSET = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url=settings.elastic_mcp_url,
        headers={
            "Authorization": f"ApiKey {settings.elastic_api_key}",
            "Accept": "text/event-stream, application/json",
            "Content-Type": "application/json",
        },
    ),
)