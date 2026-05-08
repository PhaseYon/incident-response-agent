from pydantic import BaseModel


class LogSearchRequest(BaseModel):
    query: str
    index: str | None = None
    size: int | None = 10
    start_time: str | None = None
    end_time: str | None = None


class LogSearchResponse(BaseModel):
    query: str
    hits: list[dict] = []
    total: int = 0
    message: str = ""


class ErrorSummaryRequest(BaseModel):
    index: str | None = None
    size: int | None = 20
    start_time: str | None = None
    end_time: str | None = None


class ErrorSummaryResponse(BaseModel):
    summary: str
    error_count: int = 0
    top_errors: list[dict] = []
