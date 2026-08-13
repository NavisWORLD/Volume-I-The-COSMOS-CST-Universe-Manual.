# Teacher's Guide — Persistent Synaptic Memory and COSMOS/CST

## Course purpose
Teach students how to turn a speculative systems idea into testable software while preserving the difference between implementation, measurement, null result, hypothesis and metaphor.

## Eight-module short course

### Module 1 — Memory is not context
Students compare an N-turn buffer with a durable database and explain why persistence alone still fails without retrieval.

**Lab:** store 100 memories, hide one relevant fact, and recover it after closing/reopening the process.

### Module 2 — Semantic retrieval
Study vector similarity, recency, importance and retrieval thresholds.

**Lab:** replace the default hashing embedder with a stronger embedding callable and compare ranking accuracy.

### Module 3 — Hebbian association
Explain 'fire together, wire together' as a software co-occurrence update rather than a biological identity claim.

**Lab:** inspect `top_associations()` before and after repeated concept co-occurrence.

### Module 4 — Recursive consolidation
Distinguish source records from derived summaries.

**Lab:** run `dream()` and verify the original memories are unchanged.

### Module 5 — Heartbeat and Heart Bridge
Build a fail-soft maintenance scheduler, then map a synthetic heartbeat to software cadence.

**Ethics discussion:** why does a loved one's biometric signal require explicit consent even if the intended use is affectionate/artistic?

### Module 6 — Planetary Memory and cloud sync
Partition memory by namespace and discuss which spaces must never be cloud mirrored.

**Lab:** export one namespace, import it into another database, verify checksums/deduplication.

### Module 7 — Vacuum/corridor experiment
Run the anti-locking toy model and identify what it does and does not imply.

**Lab:** change corridor threshold and intervention delay; graph residence fraction and longest run.

### Module 8 — Research defense
Students make one bounded positive claim and one null claim from their own results.

## Examination questions

1. Why is 'forever memory' not the same thing as infinite context?
2. Why is semantic retrieval a model-selection problem of its own?
3. What is the difference between the Hebbian association graph and state-modulated Hebbian attention?
4. Why should derived memory be additive rather than silently rewriting source records?
5. Why is a heartbeat scheduler not evidence of biological life?
6. Why must real-heart modulation be tested against a matched synthetic clock?
7. What did the Navier–Stokes corridor work actually establish, and what remains unresolved?
8. What would falsify the CST anti-locking hypothesis?
9. Why is Azure managed identity preferable to hard-coded cloud credentials?
10. What privacy boundary should exist between public source code and private human memory/biometric data?

## Instructor answer key

1. Persistence keeps records; finite model contexts still require selection/retrieval.
2. Bad embeddings or scoring can store everything and retrieve the wrong thing.
3. The graph is durable symbolic/co-occurrence memory; the attention kernel changes token attention inside a transformer.
4. Auditability and provenance require the original evidence to remain available.
5. It is a timed software loop with a biological metaphor.
6. Otherwise periodic timing alone is an uncontrolled alternative explanation.
7. It localized an unresolved dangerous intermediate regime in a derived framework; it did not prove global regularity. The missing closure is finite danger residence/anti-locking.
8. If triggered control fails to reduce locking, only matches random intervention, or harms task utility enough to erase benefit.
9. It provides passwordless identity-based access and avoids secrets embedded in source/config.
10. Publish mechanisms, schemas, hashes and synthetic examples; keep private conversations, raw media, credentials and real third-party biometric data private by default.
