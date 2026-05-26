from elasticsearch import Elasticsearch
from app.core.config import settings


client = Elasticsearch(
    cloud_id=settings.elastic_cloud_id,
    api_key=settings.elastic_api_key,
)

print(client.info())