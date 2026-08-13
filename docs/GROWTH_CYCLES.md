# COSMOS Growth Methods and Cycles

## The six-stage cognition loop

1. **Perceive** — acquire text, tool, sensory, memory and environment signals.
2. **Compress** — turn high-volume signals into compact state/features.
3. **Expand** — retrieve memory, associations, tools, or candidate reasoning paths.
4. **Validate** — run mechanism preflight, consistency checks, controls, and task metrics.
5. **Express** — generate the response/action/artifact.
6. **Store** — persist experience, associations, telemetry and provenance.

Heartbeat adds a seventh timescale: **consolidate**, after which the loop begins again.

## Model-growth protocol

- Begin from `checkpoint_t` and its optimizer state.
- Freeze and hash the corpus snapshot used for a comparison.
- Train a bounded burst.
- Evaluate held-out metrics.
- Record internal mechanism health (gate movement, state variance, kernel degeneracy, gradients).
- Save `checkpoint_t+1` only with its metadata and evidence record.
- Add new data only outside the controlled comparison, then freeze a new named snapshot.

## Memory-growth protocol
Memory grows continuously, but derived/consolidated memories must retain provenance. Use `derived_from` IDs when a summary is based on source records.

## Agent-growth protocol
An autonomous code-writing agent should produce proposals in a sandbox. It may test them, but promotion to protected runtime should require policy/approval and preserve rollback.

## Research-growth protocol
Every surprising result gets four companions:

1. an alternative explanation;
2. a destroyed-mechanism control;
3. a dataset/seed replication;
4. a null criterion written before the next run.
