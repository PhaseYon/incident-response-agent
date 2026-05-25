from pydantic import BaseModel, Field


class LogSearchRequest(BaseModel):
    query: str
    index: str | None = None
    size: int = Field(default=10, ge=1, le=100)
    start_time: str | None = None
    end_time: str | None = None


class LogSearchResponse(BaseModel):
    query: str
    hits: list[dict] = []
    total: int = 0
    message: str = ""


class ErrorSummaryRequest(BaseModel):
    index: str | None = None
    size: int = Field(default=20, ge=1, le=100)
    start_time: str | None = None
    end_time: str | None = None


class ErrorSummaryResponse(BaseModel):
    summary: str
    error_count: int = 0
    top_errors: list[dict] = []
