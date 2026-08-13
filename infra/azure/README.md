# Azure deployment

Run from the repository root:

```bash
az login
bash infra/azure/deploy.sh
```

The script uses identity-based access and does not print or commit Cosmos account keys.
See `docs/AZURE_BUILD_GUIDE.md` for architecture and production cautions.
