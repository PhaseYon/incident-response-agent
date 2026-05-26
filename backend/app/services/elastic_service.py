"""
Elasticsearch service stub.

All methods here return dummy/placeholder data.
TODO: Replace stub implementations with real Elastic MCP / Elasticsearch SDK calls.
      - Use the `elasticsearch-py` client or Elastic MCP server to connect.
      - Read connection config from app.core.config.settings.
"""

from app.core.config import settings
from app.utils.logging import get_logger
from elasticsearch import Elasticsearch

logger = get_logger(__name__)


class ElasticService:
    def __init__(self) -> None:
        self.client = Elasticsearch(cloud_id=settings.elastic_cloud_id, api_key=settings.elastic_api_key)
        logger.info(
            "ElasticService initialised. "
            "Connect to: %s, index: %s",
            settings.elastic_cloud_id,
            settings.elastic_index,
        )

    async def search_logs(
        self,
        query: str,
        index: str | None = None,
        size: int = 10,
        start_time: str | None = None,
        end_time: str | None = None,
    ) -> dict:
        """
        Search application logs in Elasticsearch.

        TODO: Replace with a real Elasticsearch query, e.g.:
          response = await self.client.search(
              index=index or settings.elastic_index,
              body={
                  "query": {"match": {"message": query}},
                  "size": size,
              },
          )
          return {"hits": response["hits"]["hits"], "total": response["hits"]["total"]["value"]}
        """
        logger.info("search_logs called (stub) | query=%s", query)
        return {"hits": [], "total": 0}

    async def get_latency_metrics(
        self,
        service: str | None = None,
        start_time: str | None = None,
        end_time: str | None = None,
        percentiles: list[float] | None = None,
    ) -> dict:
        """
        Retrieve latency percentile metrics from Elasticsearch.

        TODO: Replace with a real percentile aggregation query, e.g.:
          response = await self.client.search(
              index=settings.elastic_index,
              body={
                  "aggs": {
                      "latency_percentiles": {
                          "percentiles": {
                              "field": "duration_ms",
                              "percents": percentiles or [50, 95, 99],
                          }
                      }
                  },
                  "size": 0,
              },
          )
        """
        logger.info("get_latency_metrics called (stub) | service=%s", service)
        return {"p50_ms": None, "p95_ms": None, "p99_ms": None}

    async def summarize_errors(
        self,
        index: str | None = None,
        size: int = 20,
        start_time: str | None = None,
        end_time: str | None = None,
    ) -> dict:
        """
        Summarise recent errors from Elasticsearch log indices.

        TODO: Replace with a real terms aggregation + log-level filter, e.g.:
          response = await self.client.search(
              index=index or settings.elastic_index,
              body={
                  "query": {"term": {"log.level": "error"}},
                  "aggs": {"top_errors": {"terms": {"field": "message.keyword", "size": 10}}},
                  "size": 0,
              },
          )
        """
        logger.info("summarize_errors called (stub)")
        return {"summary": "No errors found (stub).", "error_count": 0, "top_errors": []}


# Module-level singleton used by route handlers
elastic_service = ElasticService()
