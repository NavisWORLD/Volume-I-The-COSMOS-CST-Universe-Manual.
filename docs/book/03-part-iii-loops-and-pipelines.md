## PART III — LOOPS AND PIPELINES

### 15. Conversation Loop

```text
1. Receive user message.
2. Remove transport/UI noise; classify intent and route.
3. Acquire chat lock / mark live interaction.
4. Retrieve compact relevant Reconciliation/semantic memory.
5. Read fresh sensory/bio summary if bridge is available.
6. Build entropy packet:
   - system entropy
   - optional audio/vision summaries
   - IBM archive/live entropy status
   - Azure Quantum archive/workspace status
7. Update/attach 12D/54D control state.
8. Run Cosmos-native synthesis or swarm/local model.
9. Return response.
10. Persist turn + optional learned associations + telemetry.
11. Release lock.
```
The modern source explicitly tries to keep 'identity' in the Cosmos-native gate and use a local model for language synthesis rather than letting the helper model redefine the entire system. That is a software composition strategy, not evidence of a metaphysical identity.

### 16. Sensory Loop

```text
browser mic/camera
   ↓ local feature extraction
energy / spectrum / light / motion / face summary
   ↓ freshness gate
12D/bio packet on local API (8765)
   ↓
web runtime samples summary
   ↓
state / tone / routing / paired-state logger
   ↓
raw media discarded unless user explicitly chooses another policy
```
The research version should log only numeric summaries needed for a hypothesis, with timestamps precise enough to join each generated response to the nearest state sample.

### 17. Synaptic Persistence Loop

```text
turn text
  ├─→ durable dialogue record
  ├─→ semantic embedding + index
  ├─→ Hebbian co-occurrence updates
  ├─→ salience updates
  ├─→ optional phantom/teacher lesson ledger
  └─→ timestamp + hashes for research snapshots

next turn
  ↓
semantic query over all retained memories
  ↓
filter by similarity / recency / confidence
  ↓
compact memory context
  ↓
response
  ↺
```
A separate dream/consolidation process can compress or synthesize recurring memories into higher-level insights. Consolidation should never silently overwrite the primary record; it should create derived records that point back to sources.

### 18. Heartbeat and Dream Consolidation Loop

```text
heartbeat scheduler (checks roughly every 5 s)
  ↓
which task is due?
  ├─ memory_consolidation → trigger_dream()
  ├─ self_reflection → save reward/experience/swarm summary
  ├─ system_health → save bridge/CNS/autonomy status
  └─ curiosity_exploration → queue research topic
  ↓
persistent memory / telemetry
  ↺
```
This architecture creates a distinction between reactive cognition and background maintenance. The chat loop answers; the heartbeat keeps state coherent between answers.

### 19. Quantum Entropy Loop

```text
IBM / Azure Quantum source
  ↓
harvest or load archived measurements
  ↓
label provider + backend + hardware/simulator status
  ↓
validate shot counts / manifests
  ↓
entropy buffer / archive
  ├─→ model-birth provenance (specific from-scratch artifacts)
  ├─→ optional random seed / control context
  └─→ live COSMOS entropy packet
  ↓
never claim performance advantage without matched classical control
```
The public release is especially careful about labeling: Azure `rigetti.sim.qvm` records are simulator records and are not counted as verified hardware provenance; explicitly labeled IBM hardware jobs are counted separately.

### 20. Paired-State Research Loop

```text
1 Hz numeric state logger
  +
completed Cosmos turn with timestamp
  ↓ nearest-clock join
paired_state_text.json
  ↓
remove clock/counter fields + duplicate channels
  ↓
chronological train/holdout split
  ↓
compare:
  A. plain attention
  B. aligned measured state
  C. shuffled state/text assignment
  D. time-shifted assignment
  ↓
pre-register NULL unless aligned beats required controls
```
This loop exists to prevent a subtle causal error: a state trajectory and a text corpus are not paired merely because both exist. If state row k is fed to unrelated text window k, the experiment tests a training schedule, not whether the measured state of an experience predicts that experience's text.

### 21. Growth / Training Loop

```text
checkpoint_t + optimizer_t + frozen/defined corpus snapshot
  ↓
train additional burst
  ↓
evaluate held-out loss + task metrics
  ↓
record gate / coupling movement + hashes
  ↓
save checkpoint_(t+1) and optimizer_(t+1)
  ↓
append new corpus only outside a controlled benchmark,
or freeze a new named snapshot before comparison
  ↺
```
Warm-starting is part of the lineage story: the model grows from its prior weights rather than being reinitialized each time. But a living corpus creates experimental drift, so benchmarking must freeze a snapshot before comparing arms.
