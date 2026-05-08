from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from app.core.config import settings
from app.routes import health, tools, incidents, scenarios
from app.utils.logging import get_logger

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    logger.info("Starting %s v%s", settings.app_name, settings.app_version)
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description="Incident Response Agent – FastAPI backend",
        lifespan=lifespan,
    )

    # Register routers
    app.include_router(health.router)
    app.include_router(tools.router)
    app.include_router(incidents.router)
    app.include_router(scenarios.router)

    return app


app = create_app()
