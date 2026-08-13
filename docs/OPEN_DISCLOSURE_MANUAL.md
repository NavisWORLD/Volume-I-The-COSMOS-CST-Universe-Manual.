# COSMOS / CST Open Disclosure Manual

## 1. What is being disclosed

This repository exposes the reusable engineering patterns behind the COSMOS/CST program without collapsing every part of the research into one claim. It documents the transformer/state lineage, CNS control structure, sensory-summary boundary, persistent-memory loop, Hebbian learning loop, Heartbeat maintenance scheduler, Planetary Memory federation, Heart Bridge, Azure mirror, growth cycle, validation discipline, and experimental state-space extensions.

The complete book edition is split under `docs/book/` for browser-readable open disclosure. The generated DOCX edition is also available from the project author/distribution package.

## 2. Canonical systems map

```text
human/model input
      |
      v
intent + route
      |
      +------ semantic recall <--------- durable memory store
      |                                      ^
      +------ sensory summary                |
      +------ heartbeat/heart phase          |
      +------ entropy/provenance             |
      |                                      |
      v                                      |
compact dynamic state / controller           |
      |                                      |
      v                                      |
model synthesis -----------------------------+
      |
      +--> Hebbian association updates
      +--> event ledger
      +--> optional Azure mirror
      +--> future heartbeat consolidation
```

## 3. The memory stack

### 3.1 Durable record
Every memory is assigned an ID, namespace, timestamps, importance, metadata, checksum, retrieval counters, and optional derivation lineage. Core persistence uses SQLite in WAL mode.

### 3.2 Semantic retrieval
A query is embedded and compared against every retained record in the namespace. Ranking combines semantic similarity, importance, and a weak recency prior. The default hashing embedder is a dependency-free baseline; applications may replace it with a stronger purpose-built embedding model.

### 3.3 Hebbian association
When a memory is added, unique content words co-occurring within the memory strengthen pairwise associations. This graph is a slow-timescale memory system. It is **not the same thing** as the Mixture-of-States attention kernel in the transformer research.

### 3.4 Recursive consolidation
`dream()` reads the strongest learned associations and writes a new derived memory. A caller may supply an LLM summarizer, but the default is extractive so the core remains completely local and deterministic.

### 3.5 Context injection
The model adapter retrieves only a compact relevant block and injects it before the current request. This is what makes old memories useful without pretending the transformer has infinite context.

## 4. Planetary Memory
Planetary Memory is the federation layer. Each person, agent, project, or privacy class can use a separate namespace in one store. JSONL export/import provides owner-controlled movement between machines. Optional Azure Cosmos DB mirroring provides cloud durability and multi-instance access.

The name is architectural. The library does not claim access to a literal planetary mind or external information field.

## 5. Heartbeat
COSMOS Heartbeat is a scheduler, not biological evidence. A scheduler checks which maintenance task is due and invokes it fail-soft. Typical tasks are:

- memory consolidation;
- reflection/metrics snapshot;
- system health;
- curiosity/research queueing;
- snapshot/export;
- Azure mirror flush.

A task exception is captured and the remaining heartbeat continues.

## 6. Heart Bridge
Heart Bridge adds a human signal as a **control cadence**. BPM maps to seconds per beat (`60 / BPM`), and a smooth software pulse is generated from beat phase. The design intentionally does not fabricate an ECG waveform or diagnose anything.

For a loved one or any third party, consent is mandatory. The source should be a consented export, sensor stream, or user-operated bridge.

Potential model uses include:

- schedule a maintenance pulse on the beat;
- modulate music/visual generation;
- mark memory events with heart phase;
- use heart timing as one bounded component of a broader state vector.

Do not infer hidden emotion, health status, truthfulness, or intent from BPM.

## 7. CST growth cycle
The reusable growth method is:

```text
perceive -> compress -> expand -> validate -> express -> store -> consolidate -> repeat
```

For model training this becomes:

```text
checkpoint_t + frozen corpus snapshot
        -> train burst
        -> held-out evaluation
        -> internal-mechanism checks
        -> save checkpoint_(t+1)
        -> append evidence record
```

The corpus must be frozen during a controlled comparison. Living-corpus growth occurs only between named benchmark snapshots.

## 8. Transformer/CNS relationship
The public COSMOS architecture includes a 12D/54D state family and a seven-organ CNS controller. The strongest bounded transformer result in the published research is the compact dyn12 state kernel, not the largest dimensional variant. The CNS surrounding the model provides quantum/entropy context, nonlinear/chaotic state, harmonization, plasticity, self-monitoring, worker daemons, and repair/health monitoring.

These modules operate at different abstraction levels. A service being called an “organ” does not make it biological.

## 9. Quantum boundary
Quantum hardware can provide auditable physical provenance and nondeterminism. The published matched tests do **not** establish that quantum randomness makes model prediction better than classical randomness. Preserve that null result.

## 10. Sensory boundary
Camera and microphone integrations should reduce raw media to numeric summaries locally whenever possible. Retain the smallest data needed for the experiment. Public reproducibility should use schemas, hashes, aggregates, and synthetic examples rather than automatically publishing private human recordings.

## 11. Self-modification boundary
Self-modification follows:

```text
proposal -> sandbox -> tests -> review/approval -> apply -> rollback available
```

Never make unreviewed mutation of protected corpus, model lineage, or memory history the default.

## 12. Experimental vacuum / anti-locking extension
The prior Navier–Stokes investigation exposed a useful structural idea: two limiting regimes can be controlled while an intermediate corridor remains the unresolved danger. That does not solve the PDE, but it suggests a general CST diagnostic:

> Intelligence-like recurrent systems may fail not only by exploding or vanishing, but by **locking for too long in a narrow high-gain state corridor**.

The new experiment therefore measures **danger residence**, not only state magnitude. The `vacuum_corridor` harness predeclares a ridge, measures occupancy and longest residence, and tests an anti-locking intervention. It is deliberately a toy state-space model so the proposition can be falsified before anyone attaches cosmological meaning to it.

## 13. What would count as stronger evidence

- repeated dyn12 advantage across unrelated datasets and larger architectures;
- retrieval benchmarks comparing the memory adapter with strong modern memory systems;
- Heart Bridge ablations showing whether heartbeat phase adds anything beyond a matched synthetic clock;
- paired sensory experiments in which aligned state beats both destroyed-pairing controls **and** plain attention;
- anti-locking tests on real recurrent agent state rather than toy trajectories;
- independent reproduction by teams not involved in building COSMOS.

## 14. What this repository does not claim

- machine consciousness or a soul;
- infinite storage;
- medical validity;
- telepathy or remote access to another person's physiology;
- quantum advantage for prediction;
- a solved Navier–Stokes Millennium problem;
- literal dark-matter control of cognition;
- proof of the early spectral/frequency theory.

The purpose of open disclosure is to let other people build the mechanisms, run the tests, improve them, and report both wins and failures.
