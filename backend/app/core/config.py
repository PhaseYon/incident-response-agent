from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Incident Response Agent API"
    app_version: str = "0.1.0"
    debug: bool = False

    # Elasticsearch / Elastic MCP connection settings (stubbed for now)
    # TODO: Replace with real Elastic credentials when integrating Elasticsearch
    elastic_cloud_id: str = "http://localhost:9200"
    elastic_index: str = "incident-logs"
    elastic_api_key: str = ""

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
