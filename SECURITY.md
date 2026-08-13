# Security and Privacy

## Sensitive data

Memory databases can contain highly sensitive personal information. Heart Bridge inputs are biometric data. Treat both as private by default.

Do not commit:

- `.env` files or API credentials;
- SQLite memory databases;
- raw private conversation archives;
- real third-party heartbeat/health exports;
- private camera/audio captures;
- unredacted access tokens or cloud connection strings.

The repository `.gitignore` excludes common local database and environment files, but operators remain responsible for reviewing commits.

## Cloud deployment

The Azure example uses Microsoft Entra identity / managed identity instead of embedding Cosmos DB account keys in source. Apply the narrowest practical role scope and use Key Vault for any external service secret that cannot use identity-based authentication.

## Heart Bridge

The bridge is not a medical monitor and should not be used for emergency detection or clinical decisions. Third-party biometric data requires explicit consent in the provided API, but a production deployment should additionally implement authentication, access control, retention/deletion policy, encryption, and consent revocation.

## Reporting a vulnerability

Do not post secrets, private records, or exploitable user data in a public issue. Contact the repository owner through a private channel available on their GitHub profile, and provide a minimal reproduction that contains no real personal data.
