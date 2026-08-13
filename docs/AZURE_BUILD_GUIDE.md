# Microsoft Azure Build Guide — Planetary Memory + Heartbeat

## Architecture

```text
client / model
     |
     v
Azure Container Apps: cosmic-memory API
     |
     +---- local SQLite cache (optional ephemeral/local use)
     |
     +---- DefaultAzureCredential / managed identity
                |
                v
      Azure Cosmos DB for NoSQL
        database: cosmic-memory
        container: memories
        partition key: /namespace
```

Use Azure Key Vault for any external service secrets that cannot use managed identity. Do not put API keys into this repository.

## Current Microsoft-recommended identity pattern
The Python Azure SDK can use `DefaultAzureCredential`. During local development this can resolve the signed-in Azure CLI identity; in Azure-hosted environments it can resolve a managed identity. The Cosmos DB SDK accepts that credential directly.

## Prerequisites

- Azure subscription;
- Azure CLI;
- Docker for local container testing;
- permission to create a resource group, Cosmos DB account, and Container App.

## Automated deployment

```bash
az login
bash infra/azure/deploy.sh
```

Environment overrides:

```bash
export RESOURCE_GROUP=cosmos-cst-rg
export LOCATION=centralus
export COSMOS_ACCOUNT=mygloballyuniqueaccount
export CONTAINER_APP=cosmic-memory-api
bash infra/azure/deploy.sh
```

The script:

1. creates the resource group;
2. creates a Cosmos DB for NoSQL account if needed;
3. creates database `cosmic-memory`;
4. creates container `memories` partitioned by `/namespace`;
5. deploys this repository to Azure Container Apps from the Dockerfile;
6. enables system-assigned managed identity;
7. grants the Container App the Cosmos DB Built-in Data Contributor data-plane role;
8. sets `COSMOS_ENDPOINT` in the Container App environment.

Successful API `/remember` calls locally persist the record and, when `COSMOS_ENDPOINT` is configured and the Azure extra is installed, attempt an Azure Cosmos DB upsert using the managed identity.

## Why `/namespace`
Each memory record includes a namespace. Partitioning on `/namespace` makes a person/agent/project space the unit of locality and makes namespace-scoped queries efficient.

## Key Vault
If you later add a model provider that needs an API key, store it in Azure Key Vault and reference it from Container Apps with managed identity rather than embedding it in an environment file committed to Git.

## Production cautions

- The core `RecursiveMemory` still writes SQLite. For a multi-replica production service, treat Cosmos DB as the shared durable mirror and implement a Cosmos-native backend before relying on cross-replica reads.
- Do not mirror namespaces containing private third-party biometric data unless the data subject explicitly consented to that storage location and retention policy.
- Apply Azure RBAC/data-plane roles at the narrowest usable scope.
- Enable backups/retention according to the sensitivity and deletion obligations of your data.

## Official references

- Azure Cosmos DB Python quickstart: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-python
- Cosmos DB Python + Entra ID: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/how-to-python-get-started
- Cosmos DB data-plane RBAC: https://learn.microsoft.com/en-us/azure/cosmos-db/how-to-connect-role-based-access-control
- Container Apps `az containerapp up`: https://learn.microsoft.com/en-us/azure/container-apps/containerapp-up
- Managed identity for Python apps: https://learn.microsoft.com/en-us/azure/developer/python/sdk/authentication/system-assigned-managed-identity
- Container Apps Key Vault secret references: https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets
