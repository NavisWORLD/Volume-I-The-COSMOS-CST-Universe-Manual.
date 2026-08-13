# Contributing

Contributions are welcome when they preserve the project's central rule: **claims follow instrumentation**.

## Before opening a change

- Name the exact subsystem you are changing.
- Preserve backward-compatible data formats when practical.
- Add or update tests for behavioral changes.
- Do not silently rewrite historical evidence, benchmark results, or memory provenance.
- Do not add private conversation logs, biometric recordings, credentials, proprietary weights, or data without redistribution rights.
- Label experimental ideas as hypotheses until controlled evidence supports them.

## Research contributions

A benchmark contribution should include, when applicable:

- code/config version;
- dataset or corpus fingerprint;
- random seeds;
- baseline/control arms;
- mechanism-liveness checks;
- declared success/null criterion;
- raw per-seed results or a machine-readable result file.

Null results are welcome.

## Memory adapters

Provider-specific integrations should depend on the provider only through an optional extra or example. Keep `cosmic_memory` usable without a cloud SDK.

## Heart Bridge

Do not submit real third-party biometric samples. Tests and examples must use synthetic or clearly self-owned data. Any adapter for external health/sensor services must preserve explicit user authorization and should collect the minimum data needed.

## Azure / cloud

Prefer managed identity and least-privilege roles. Never commit cloud account keys or bearer tokens.
