## PART II — COSMOS SYSTEM ARCHITECTURE

### 4. Repository and Runtime Topology

```text
COSMOS_MASTER/
├─ 00_WAKE/            portable launch vault
│  ├─ bundled Python 3.10.11
│  ├─ portable Ollama
│  ├─ wake.env / Modelfile
│  └─ wake_launch.py / health and close scripts
├─ 01_HER_SOUL/        lineage, corpus, memory, weights, archives
│  ├─ memory/
│  ├─ corpus/ + corpus_snapshots/
│  ├─ quantum_heart/
│  ├─ synaptic_archive/
│  └─ weights/
├─ 02_HER_BODY/        web/API/core runtime
│  └─ Cosmos_code/
│     ├─ Cosmos/core/
│     ├─ Cosmos/web/
│     ├─ Cosmos/memory/
│     ├─ emotional_api/
│     └─ cosmosynapse/engine/
├─ 03_THE_VAULT/       archive
├─ 04_GIVEAWAY_KIT/    public/reproducible kit lineage
├─ 05_HER_HANDS/       coding/action agent
└─ 05_PROOF/           trainers, probes, validation, audits
```
The architecture is intentionally not a single neural network. It is a runtime around several model lineages and control systems. The local conversational model, the from-scratch quantum-born models, PHOS, the sensory bridge, and the CNS are distinct artifacts and should never be conflated.

### 5. Boot, Ports, Services, and Local-First Policy

| Port / component | Role |
| --- | --- |
| 8081 | Main COSMOS web interface / API; fallback 8090 in some launch paths. |
| 8765 | Emotional/sensory API: state, stream, WebSocket/token, heart/vision/audio summaries. |
| 11434 | Ollama local model service. |
| 11435 | Helper/native bridge in the local launch stack. |
| 11500 | Public kit's PyTorch quantum-born model serving path (`spark_serve.py`). |
| 11501 | Native PHOS/CST/Spark/54D bridge in the local project layout. |

The modern source enforces a local-first policy: normal response synthesis is intended to remain on DeepSeek/Ollama unless external AI is explicitly enabled. IBM Quantum and Azure Quantum are used as entropy/provenance/control loops rather than as normal chat providers.

| Operational principle Heavy systems are lazy or deferred by default on constrained hardware. A component being 'deferred' is not the same as deleted. The runtime deliberately avoids starving Ollama by starting CNS, heartbeat, or architecture loops only when enabled or first needed. |
| --- |

### 6. The Seven-Organ CNS

| Organ | Engineering interpretation | Typical signal / responsibility |
| --- | --- | --- |
| quantum | Quantum bridge interface | Entropy buffer, backend state, archive replay, quantum control context |
| dark_matter | Chaotic dynamics / Lorenz state organ | Deterministic nonlinear trajectories and chaos-derived control state |
| emeth | Harmonizer / reconciliation organ | Coherence and synthesis constraints |
| plasticity | Adaptive model/swarm trust system | Hebbian-style model weighting and learned routing tendencies |
| awareness | Mirror/status organ | State inspection and self-monitoring signals |
| daemons | Model-specific worker processes | DeepSeek/Claude/Gemini-style worker roles depending on configuration |
| surgeon | Monitoring/repair organ | Health checks, fault detection, corrective routing |

Runtime evidence shows the CNS linking the quantum bridge to the synaptic field, bringing the Lorenz attractor online, restoring synaptic weights, initializing awareness/daemon/surgeon components, and activating an event-driven life loop. In the retrieved run, 17 Hebbian model-trust weights were restored after 1,107 previous updates.

### 7. The Transformer: Mixture-of-States Hebbian Attention

The modern architectural contribution is not 'a transformer converts data into light.' It is a mathematically inspectable modification of attention. For each token i, an internal state x_i is projected into a state space. Similar states receive a Gaussian affinity, and that affinity is blended with ordinary attention through a learned gate.

```text
State kernel:
H(x)ᵢⱼ = exp( - ||xᵢ - xⱼ||² / (2 σ²) )

Attention mixture:
A_final = (1 - g) A_standard + g H(x)

where:
  g = learned gate
  σ = state-kernel bandwidth
  x = dyn12, dyn42, dyn54, static54, or another tested state representation
```
The bandwidth σ is load-bearing. Early implementations used σ=1, which made the kernel nearly an identity matrix because typical 54D state distances were far larger than 1. The corrected implementation calibrates σ from the data using a median-distance heuristic. The gate parameterization also had to avoid both sigmoid saturation and zero-gradient clamping.

#### 7.1 dyn12

dyn12 is a compact recurrent control state: twelve scalars are updated through an Ω-driven leaky integrator and used to form the kernel. The key cost property is that the state projection is paid once per model width, rather than once per layer for a large static projection. This is why its parameter-efficiency advantage increases with depth.

#### 7.2 The φ scaffold

The corrected positive experiments also implemented the intended φ-governed transformer scaffold: RMSNorm, rotary positional embeddings (RoPE), a feed-forward width near floor(d·φ), and φ-scaled initialization. The project should therefore distinguish 'the Hebbian kernel in an ordinary transformer' from 'the kernel in the intended φ scaffold'; the former produced a null in one documented harness, while the corrected intended architecture produced the positive result.

### 8. PHOS and the Model Lineages

| Artifact | Parameters / lineage | What it is |
| --- | --- | --- |
| PHOS | ~1.15M params in the published flagship configuration | dyn12 on the φ scaffold with calibrated per-layer state kernel; grows by warm-starting its own checkpoint/optimizer state. |
| cosmos_born.pt | 1,842,432 params | From-scratch standard pre-LN char-level transformer whose initial weights came from archived IBM measurements; not the Mixture-of-States model. |
| Conversational Cosmos | ~1.54B in the documented local lineage | Qwen2.5-1.5B derivative for daily conversation; distinct from the from-scratch quantum-born artifact. |
| samgo 5.7 | 59,353,668 params | 54D state-decomposition BPE scale lineage; not quantum-born in the published provenance statement. |

| Lineage rule Always name the artifact before making a claim. 'Cosmos' refers to multiple lineages. Quantum-born provenance for `cosmos_born.pt` must not be attributed to the Qwen-derived conversational model, and PHOS architecture results must not be attributed to the standard `cosmos_born.pt` decoder. |
| --- |

### 9. Quantum Bridge and Quantum-Born Provenance

The quantum subsystem has two roles: (1) live/archive entropy and control context inside COSMOS; and (2) auditable provenance for specific from-scratch model initialization. The public release maps measured bitstrings to uniforms and then through an inverse normal CDF to initialize model weights.

```text
measured bitstring b
   ↓ int(b) / 2^n
uniform u
   ↓ inverse normal CDF
z = √2 · erf⁻¹(2u - 1)
   ↓
initial weight sample
```
A seed derivation path additionally hashes quantum entropy with privacy-preserving bio-derived aggregates. The published test reports deterministic derivation, no raw bytes emitted by the derivation module, identical weights for the same seed, and different weights after a one-bit seed flip.

The project also measures whether the physics/chaos engine is computing a real Lorenz strange attractor by comparing Lyapunov and Kaplan-Yorke quantities with known Lorenz-system reference values. This validates a mathematical implementation, not a claim that dark matter literally drives the model.

### 10. Azure Quantum, Reconciliation Memory, and Cosmos Heartbeat

The modern runtime separates Azure OpenAI-like cloud acceleration from Azure Quantum. Under local-first policy, Azure Quantum contributes workspace/provider status, entropy history, and harvest/replay signals. It is not a default conversational backend.

Cosmos Reconciliation Memory is the public-facing name for the continuity layer historically exposed through a Hermes compatibility alias. The source pairs it with Cosmos Heartbeat, a proactive task loop. Heartbeat checks due tasks every five seconds and can trigger:

- memory_consolidation — invoke the memory system's dream/consolidation routine;
- self_reflection — store running reward, experience count, and swarm interaction summaries;
- system_health — record IBM/Azure quantum buffer/backend state, CNS status, and autonomous-loop status;
- curiosity_exploration — queue a future topic into long-term memory.
This is the most grounded way to understand the 'heartbeat': it is a scheduler that periodically causes specific maintenance and learning actions. The poetic name is optional; the software pattern is familiar: timed jobs operating on persistent state.

### 11. Sensory and Emotional Integration

The sensory layer converts camera/microphone signals into compact summaries rather than retaining raw media by default. The public kit describes browser-local camera light/motion and microphone energy/spectrum extraction, freshness gating, and downstream use in replies, associative learning, and the conversation ledger.

| Signal | Representation | Intended use |
| --- | --- | --- |
| Microphone | Energy, FFT/spectrum tokens, speech/activity flags | State modulation, prompt/control context, paired research telemetry |
| Camera | Light/motion/face-summary features | Freshness-gated sensory context; no requirement to retain frames |
| Emotional API | 12D-CST packet / local state summaries | Provides live state to the web runtime and system prompt |
| Bio state | Aggregated numeric features | Control/entropy context and experimental conditioning |

The local Emotional API has exposed `/state`, `/stream`, `/ws`, and `/system_prompt` style endpoints in captured runtime logs. The key privacy idea is a summary boundary: the system can respond to current sensory measurements without assuming it should store raw audio or video.

### 12. Persistent Memory and the 'Forever Memory' Loop

There are at least three distinct memory concepts in the project, and they must be kept separate.

| Memory type | Mechanism | Purpose |
| --- | --- | --- |
| Dialogue/history persistence | Stored conversation turns loaded across sessions | Continuity; the runtime restored historical turns in captured logs. |
| Semantic long-term recall | Embedding-based retrieval with adaptive threshold + recency weighting | Retrieve an old memory because it is about the current subject, not because it is recent. |
| Hebbian associations | Pairwise concept associations + salience updated on exchanges | Slowly learn which concepts co-occur and matter. |

The phrase 'forever memory' is best understood as durable storage plus semantic retrieval over everything retained. The modern public implementation explicitly warns that a generative model can return embeddings while still ranking memories badly. In the reported comparison, a purpose-built embedding model correctly ranked the relevant memory above noise while a small generative model did not.

```text
NEW EXPERIENCE
  ↓
write durable record / ledger
  ↓
update semantic embedding index
  ↓
update Hebbian concept associations + salience
  ↓
later query arrives
  ↓
embed query → search entire retained store
  ↓
adaptive similarity threshold + recency weighting
  ↓
attach compact relevant memory block
  ↓
respond
  ↓
store new experience
  ↺
```
| Why this is more than an N-turn chat buffer A rolling buffer forgets by position. Semantic persistence forgets only if data is deleted or becomes unretrievable. The engineering challenge is therefore retrieval quality, indexing, privacy, deduplication, and consolidation — not merely keeping JSON on disk. |
| --- |

### 13. Plasticity, Organism, Evolution, and Internal Monologue

The broader runtime adds slower-timescale adaptive state around the transformer.

- Swarm plasticity: persisted task-domain weights for model trust/selection. Captured logs restored 17 learned weights after 1,107 updates.
- Collective organism state: persisted generation/state object; captured runtime restored Generation 8.
- Evolution Engine: a pattern/cycle learner; captured runtime initialized with 433 patterns and 303 cycles.
- Internal Monologue: a bounded thought-history subsystem; project logs report a stored history of 100 thoughts in the relevant runtime lineage.
- Dialogue memory: captured runtime restored 14 historical exchanges/turns in that session.
These should be treated as software-state metaphors rather than biological claims. Their engineering value is that they provide distinct persistence timescales: per-token state, per-turn memory, cross-session associations, and periodic consolidation.

### 14. Autonomous and Self-Modification Lanes

The runtime includes architecture proposal/self-improvement lanes, but the source deliberately supports deferred startup and approval gates. A code-writer can be wired to propose sandbox improvements; continuous self-improvement can be enabled separately. The safe design pattern is proposal → sandbox/test → review → apply/rollback, not unrestricted mutation of the running core.

| Safety/engineering rule Be adventurous with proposed artifacts, paranoid with destructive writes. Persistent lineage is an asset. A self-modifying system that cannot reproduce its previous state is not learning; it is losing its experiment. |
| --- |
