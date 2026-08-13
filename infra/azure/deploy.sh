#!/usr/bin/env bash
set -euo pipefail

RESOURCE_GROUP="${RESOURCE_GROUP:-cosmos-cst-rg}"
LOCATION="${LOCATION:-centralus}"
COSMOS_ACCOUNT="${COSMOS_ACCOUNT:-cosmoscst$RANDOM$RANDOM}"
DATABASE="${DATABASE:-cosmic-memory}"
CONTAINER="${CONTAINER:-memories}"
CONTAINER_APP="${CONTAINER_APP:-cosmic-memory-api}"
ENVIRONMENT="${ENVIRONMENT:-cosmos-cst-env}"
ROLE_ID="00000000-0000-0000-0000-000000000002"

echo "[1/8] resource group"
az group create --name "$RESOURCE_GROUP" --location "$LOCATION" --output none

echo "[2/8] Cosmos DB account"
if ! az cosmosdb show -g "$RESOURCE_GROUP" -n "$COSMOS_ACCOUNT" >/dev/null 2>&1; then
  az cosmosdb create -g "$RESOURCE_GROUP" -n "$COSMOS_ACCOUNT" --locations regionName="$LOCATION" failoverPriority=0 isZoneRedundant=False --output none
fi

echo "[3/8] database"
az cosmosdb sql database create -g "$RESOURCE_GROUP" -a "$COSMOS_ACCOUNT" -n "$DATABASE" --output none

echo "[4/8] container"
az cosmosdb sql container create -g "$RESOURCE_GROUP" -a "$COSMOS_ACCOUNT" -d "$DATABASE" -n "$CONTAINER" -p '/namespace' --output none

COSMOS_ENDPOINT="$(az cosmosdb show -g "$RESOURCE_GROUP" -n "$COSMOS_ACCOUNT" --query documentEndpoint -o tsv)"

echo "[5/8] Container App from local source"
az containerapp up --name "$CONTAINER_APP" --resource-group "$RESOURCE_GROUP" --location "$LOCATION" --environment "$ENVIRONMENT" --source . --ingress external --target-port 8080 --output none

echo "[6/8] managed identity"
PRINCIPAL_ID="$(az containerapp identity assign -g "$RESOURCE_GROUP" -n "$CONTAINER_APP" --system-assigned --query principalId -o tsv)"

echo "[7/8] Cosmos DB data-plane role"
az cosmosdb sql role assignment create -g "$RESOURCE_GROUP" -a "$COSMOS_ACCOUNT" --principal-id "$PRINCIPAL_ID" --role-definition-id "$ROLE_ID" --scope "/" --output none || true

echo "[8/8] app environment"
az containerapp update -g "$RESOURCE_GROUP" -n "$CONTAINER_APP" --set-env-vars "COSMOS_ENDPOINT=$COSMOS_ENDPOINT" "COSMIC_MEMORY_NAMESPACE=default" --output none

FQDN="$(az containerapp show -g "$RESOURCE_GROUP" -n "$CONTAINER_APP" --query properties.configuration.ingress.fqdn -o tsv)"
printf '\nDeployed: https://%s\nCosmos endpoint: %s\n' "$FQDN" "$COSMOS_ENDPOINT"
