# Cosmic Neural Connective Persistent Memory Architecture

## Design goal
Give any model or agent durable, semantically retrievable memory without requiring modification of the model's weights.

## Core invariants

1. **Owner-controlled persistence.** The canonical record lives in a database the operator controls.
2. **No automatic turn-window expiry.** Records remain until deleted under policy.
3. **Semantic recall, not full replay.** Only relevant records enter the model context.
4. **Provenance.** Every record has an ID, checksum, timestamps, namespace and metadata.
5. **Derived memory is additive.** Consolidation creates new records and does not silently rewrite history.
6. **Multiple timescales.** Immediate context, durable records, Hebbian associations, and periodic consolidation remain distinct.
7. **Portable.** JSONL export/import makes a memory space movable across models.

## Recall score

The default ranking is intentionally simple:

```text
score = 0.76 * semantic_similarity
      + 0.14 * importance
      + 0.10 * recency
```

Recency decays exponentially with a configurable half-life. Applications should benchmark this against their own workload rather than treating these constants as universal.

## Custom embedding model

Pass any callable `str -> list[float]`:

```python
memory = RecursiveMemory('m.db', embedder=my_embedding_function)
```

A purpose-built embedding model is recommended for production semantic recall. The included hashing embedder exists so the package has a zero-dependency baseline and deterministic tests.

## Adapter pattern

```text
current request
  -> retrieve old records by meaning
  -> format compact memory block
  -> prepend/inject to model request
  -> model generates answer
  -> persist current request + answer
```

Because the adapter is provider-agnostic, it can wrap a local model, an OpenAI-compatible HTTP endpoint, a cloud SDK, a game agent, a robot controller, or a custom inference engine.

## Recursive memory cycle

```text
experience
  -> durable record
  -> concept co-occurrence graph update
  -> future retrievals
  -> access counters / importance
  -> heartbeat dream consolidation
  -> derived higher-level memory
  -> future retrievals
```

## Planetary Memory
Planetary Memory adds named spaces and deliberate federation. A useful deployment might have:

- `identity` — stable user-provided preferences;
- `project:<name>` — project-specific decisions;
- `research` — experiment logs and findings;
- `private:<person>` — high-sensitivity memories that never mirror to shared cloud storage;
- `agent:<id>` — each agent's local experience.

Do not merge namespaces merely because the library can. Privacy boundaries are part of memory correctness.

## Backup
SQLite is durable, not immortal. Copy the DB while the application is stopped or use SQLite's backup API, and keep versioned encrypted backups if the contents are sensitive.
