## PART V — BUILD AND OPERATE

### 27. Rebuild Order for an Independent Engineer

1. Freeze the theory. Start with the minimum operational claim: dynamic state modulates attention.
1. Reproduce the plain transformer baseline on a fixed corpus and seed set.
1. Implement the state kernel and the five preflight assertions before running any comparison.
1. Reproduce dyn12 vs baseline. Do not add quantum, sensory, swarm, or autonomy until the architecture test is stable.
1. Add durable semantic memory as a separate service. Validate retrieval quality with known relevant/irrelevant memories.
1. Add the Hebbian association store. Keep it distinct from transformer attention.
1. Add the sensory bridge with local numeric summaries and a strict retention policy.
1. Add timestamped paired-state logging and only then test state/text alignment.
1. Add quantum archive replay as a provenance/nondeterminism layer. Run matched classical controls.
1. Add Reconciliation Memory + Heartbeat maintenance jobs.
1. Add CNS organs and swarm routing only after every organ exposes health/state telemetry.
1. Add self-modification through proposal/sandbox/approval/rollback lanes.
### 28. Minimal Health Checklist

- Main web API reachable on 8081 (or documented fallback).
- Ollama reachable on 11434.
- Sensory API reachable on 8765 when enabled.
- Memory store loads and can retrieve a known old fact semantically.
- CNS reports all expected organs or clearly marks deferred organs.
- Quantum bridge distinguishes hardware, unlabelled legacy, and simulator records.
- State preflight passes before any benchmark number is accepted.
- Corpus fingerprint is frozen for comparison runs.
- Telemetry schema hash is recorded.
- Every benchmark stores seeds, configuration, code hash, dataset hash, and result status.
- Heartbeat tasks are observable and fail-soft.
- Self-modification cannot overwrite protected weights/corpora without an explicit approved lane.
### 29. Known Operational Failure Modes

| Observed issue | Effect | Mitigation |
| --- | --- | --- |
| scipy/faiss/mediapipe DLL conflicts | Audio analysis/indexing or face tracking can hang/disable. | Fail-soft imports; isolate optional packages; pin compatible runtime. |
| Missing audio_engine | Audio fusion unavailable. | Treat audio as optional capability and expose status. |
| No WebSocket support | Upgrade request fails / `/ws/live` can 404. | Install supported Uvicorn WebSocket stack or use SSE fallback. |
| Ollama unavailable/prewarm failure | Local voice cannot warm at startup. | Health-check 11434 and avoid duplicate/stale process assumptions. |
| SVD did not converge during quantum refill | Quantum symbiotic refill fails. | Retry/fallback to archive; do not block local conversation. |
| Port collisions, especially 8765/11434 | Stale process or wrong service owns port. | Probe process identity before kill/restart; preserve voice verification. |
| f-string backslash syntax error in server.py (historical local build) | Web server import failed. | Run syntax compilation before launch and preserve last-known-good backup. |

### 30. Privacy and Provenance

A reproducible cognitive system must publish mechanisms without automatically publishing private life data. COSMOS already contains the right conceptual boundary: retain public measurement archives and hashed manifests, but do not ship raw camera/audio or private paired conversation datasets by default.

- Publish hashes, schemas, benchmark code, and aggregate statistics.
- Label simulator vs hardware data explicitly.
- Keep private conversation text out of public paired-state releases unless reviewed/redacted.
- Store raw credentials only in local configuration; never place them in model cards or source commits.
- Keep quantum provenance attached to the exact model artifact it initialized.
- Keep third-party model lineage and licenses explicit.
