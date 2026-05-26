from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    elastic_api_key: str = ""
    elastic_mcp_url: str = "https://your-mcp-server-url/mcp"
    google_api_key: str = ""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
