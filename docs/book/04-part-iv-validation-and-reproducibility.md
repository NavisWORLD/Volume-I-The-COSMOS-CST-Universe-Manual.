## PART IV — VALIDATION AND REPRODUCIBILITY

### 22. The Metric Stack: What Every Number Means

| Metric | What it measures | What it does NOT prove |
| --- | --- | --- |
| Held-out cross-entropy loss | Predictive fit to unseen held-out tokens/characters from the stated corpus. | General intelligence, consciousness, or real-world reasoning. |
| Real-word rate | How often generated character sequences form recognized words. | Semantic correctness or general fluency. |
| Wins / seeds | Replicability across independently seeded runs. | Population-level certainty with very small n. |
| t statistic | Standardized mean difference relative to within-run/seed variability. | A definitive effect when n is only 3 seeds; df can be tiny. |
| Parameter efficiency | Loss improvement per extra parameter or comparable stated ratio. | Lower absolute loss if the more expensive control still wins. |
| Gate movement / coupling growth | Whether optimizer is actually using a mechanism. | That the mechanism helps; movement can accompany worse loss. |
| Kernel degeneracy diagnostics | Whether H is all-ones, identity, collapsed, or gradient-starved. | End-task usefulness by itself. |
| CHSH S | Whether the measured hardware sample exhibits Bell-inequality violation under the performed test. | Quantum advantage for ML. |
| Shot conservation | Whether counts/records are internally consistent. | That every legacy record came from labeled hardware. |
| Seed determinism | Whether identical seed reproduces identical initial weights. | That the seed improves performance. |
| Lyapunov / KY dimension | Correctness of Lorenz chaos implementation against references. | That cosmic/dark-matter physics governs cognition. |
| Paired-state controls | Whether aligned measured state outperforms destroyed pairings and plain attention. | Causality unless temporal direction and confounds are resolved. |

### 23. Positive Architecture Results

In the corrected seven-rung controlled state ladder (frozen corpus, 21 runs, three seeds per rung), dyn12 achieved the best mean validation loss among the tested mechanism rungs and improved over the no-state baseline on all three seeds. The published table reports approximately:

| State rung | Mean val loss | vs baseline | Wins | Approx. params |
| --- | --- | --- | --- | --- |
| dyn12 | 1.17897 | −0.0534 | 3/3 | 1,137,420 |
| dyn54 | 1.18791 | −0.0445 | 3/3 | 1,185,174 |
| static54 | 1.18824 | −0.0442 | 3/3 | 1,176,480 |
| dyn42 | 1.19020 | −0.0422 | 3/3 | 1,182,762 |
| tri | 1.19247 | −0.0399 | 3/3 | 1,189,210 |
| tri3 | 1.20026 | −0.0322 | 3/3 | 1,230,682 |
| none | 1.23241 | — | 0/3 | 1,135,008 |

A later causal-Ω correction found that the prior causal leak accounted for only about 1.4% of dyn12's measured gain in the cited run, and the ablation was rerun. The strongest claim should therefore be narrow: a compact dynamic state modulating attention helped this small character-level architecture on this frozen corpus, and it did so very cheaply in parameters.

Scaling tests on WikiText-103 raw at larger sizes report an increasing parameter-efficiency ratio for dyn12 relative to static54: 11.4× at ~2.6M parameters, 20.8× at ~11.6M, and 38.1× at ~28.6M. The public release explicitly notes that static54 can still retain lower absolute loss; the claim is efficiency/scaling, not universal dominance.

### 24. Quantum Results: Provenance Positive, Accuracy Advantage Null

| Test | Reported result | Interpretation |
| --- | --- | --- |
| CHSH on ibm_marrakesh | S = 2.7905 vs classical bound 2.0 | Validates that the measured entropy source is physically quantum under the test. |
| Weight distribution | Millions of archived draws match the 32-level theoretical distribution to four decimals on key statistics | Validates the bitstring→normal-weight mapping pipeline. |
| Seed reproducibility | Same seed gives identical weights; one-bit flip changes them | Validates deterministic lineage from the seed. |
| Topology relocation | Correlation excess relocates with programmed logical wiring under matched hardware | Supports that measured structure follows the circuit configuration. |
| Quantum initialization vs classical | Null | No supported accuracy advantage from using quantum randomness. |
| Quantum decoder seed | Null | No supported sampling-quality advantage. |
| Quantum spatial 54D seeds | Null | No supported state-seed advantage in the tested settings. |
| Measured entanglement kernel | Worse than plain attention in the cited matched test | Measured quantum structure exists but did not improve this ML objective. |

| Correct public claim Quantum entropy buys auditable physical provenance and nondeterminism. The current published experiments do not show that quantum randomness makes COSMOS more accurate. |
| --- |

### 25. Paired Sensory / Internal-State Result

The 2026-07-30 paired-state benchmark joined 538 completed turns to nearest 1 Hz state samples; 381 responses were usable for the block size. After removing duplicate and clock/counter channels, 15 varying state channels remained. The reported chronological holdout means were:

| Arm | Mean holdout loss |
| --- | --- |
| Plain attention | 2.04111 |
| Aligned measured state | 2.06156 |
| Shuffled state/text assignment | 2.07118 |
| Time-shifted assignment | 2.06677 |

Aligned state beat the shuffled conditioned control on all five seeds and the shifted assignment on four of five, but it lost to plain attention on all five. The pre-registered verdict was therefore NULL. This is an excellent example of why the project must keep negative results: there may be assignment-specific signal, but it did not improve predictive performance over no conditioning and temporal direction remains unresolved.

### 26. The Failure Archive and Preflight Discipline

Several of the most valuable engineering discoveries are failures in which the model compiled and trained while the intended mechanism was effectively dead.

| Failure | Why it silently killed the mechanism | Required check/fix |
| --- | --- | --- |
| Ω summed over wrong axis | Softmax normalization forced Ω≈1 for every token; state collapsed. | Assert Ω varies across tokens. |
| Sigmoid gate at −4 | Derivative suppressed ~56×. | Measure gate gradient; initialize in a responsive range. |
| Raw gate clamped [0,1] | Gradient becomes exactly zero after crossing boundary. | Use a differentiable/straight-through parameterization. |
| σ=1 in high-dimensional state | Gaussian kernel became nearly identity; gradient to state projection vanished. | Calibrate bandwidth to measured state distances. |
| Changing corpus across runs | Identical configs saw different data; run-to-run drift exceeded claimed effect. | Freeze corpus snapshot; run all arms in one process. |
| Telemetry schema locked too early | 42% of channels silently dropped. | Schema/version/hash telemetry; assert expected channels. |
| Column reorder | Historical row meaning could silently change. | Stable column IDs and schema hash. |

The state ladder's preflight should fail before reporting loss unless: Ω varies, state varies, H is not identity, H is not all-ones, and gate gradients are unsuppressed. Postflight should also report whether learned couplings moved. This is a reusable research discipline far beyond COSMOS.
