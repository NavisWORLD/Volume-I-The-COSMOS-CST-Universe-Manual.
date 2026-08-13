from __future__ import annotations
import os

class AzureCosmosMirror:
    """Optional Azure Cosmos DB mirror for Planetary Memory records.

    Uses Microsoft Entra / DefaultAzureCredential. No account keys are required
    in source code. The caller's managed identity must have data-plane access.
    """
    def __init__(self, endpoint: str | None = None, database: str = "cosmic-memory", container: str = "memories"):
        try:
            from azure.identity import DefaultAzureCredential
            from azure.cosmos import CosmosClient
        except ImportError as exc:
            raise RuntimeError("Install the Azure extra: pip install 'cosmic-synaptic-memory[azure]'") from exc
        endpoint = endpoint or os.getenv("COSMOS_ENDPOINT")
        if not endpoint:
            raise ValueError("COSMOS_ENDPOINT is required")
        self.client = CosmosClient(endpoint, credential=DefaultAzureCredential())
        self.database = self.client.get_database_client(database)
        self.container = self.database.get_container_client(container)

    def upsert_memory(self, record: dict):
        item = dict(record)
        item["id"] = item["id"]
        item["namespace"] = item.get("namespace", "default")
        return self.container.upsert_item(item)

    def query_namespace(self, namespace: str, limit: int = 100):
        q = "SELECT * FROM c WHERE c.namespace = @namespace ORDER BY c.updated_at DESC"
        params = [{"name": "@namespace", "value": namespace}]
        items = list(self.container.query_items(query=q, parameters=params, enable_cross_partition_query=False))
        return items[:max(0, int(limit))]
