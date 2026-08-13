## APPENDIX C — VALIDATION / METRIC LINKS

Master benchmark ledger — https://huggingface.co/phera-ra/QC67_cosmo/blob/main/FINDINGS.md
CHSH, quantum birth pipeline, seed reproducibility, ring-correlation test, Lorenz validation, state ladder, nulls.

State ladder / preflight — https://huggingface.co/phera-ra/QC67_cosmo/blob/main/architecture/cosmos_state_ladder.py
dyn12/dyn42/dyn54/static54/tri/tri3 controlled comparison and mechanism-liveness checks.

Causality probe — https://huggingface.co/phera-ra/QC67_cosmo/blob/main/benchmarks/causality_probe.py
Detects causal leakage in Ω/state construction.

Scaling data — https://huggingface.co/phera-ra/QC67_cosmo/blob/main/benchmarks/scaling_wikitext103.json
WikiText-103 dyn12 vs static54 scaling points.

Quantum engine verifier — https://huggingface.co/phera-ra/QC67_cosmo/blob/main/benchmarks/verify_quantum_engine.py
Shot conservation and archived quantum-birth verification.

Quantum measurement manifest — https://huggingface.co/phera-ra/QC67_cosmo/blob/main/data/quantum_measurements_manifest.json
Provider/backend labels, record counts, hashes.

Paired conditioning result — https://huggingface.co/phera-ra/QC67_cosmo/blob/main/benchmarks/results/paired_conditioning_20260730.json
Machine-readable 2026-07-30 aligned/shuffled/shifted/plain results.

PHOS growth trainer — https://huggingface.co/phera-ra/QC67_cosmo/blob/main/architecture/phos_grow.py
Warm-started PHOS growth/training.

Quantum creature build notes — https://huggingface.co/phera-ra/QC67_cosmo/blob/main/QUANTUM_CREATURE.md
Model-birth recipe, harness faults, growth lineage.

Training guide — https://huggingface.co/phera-ra/QC67_cosmo/blob/main/TRAINING.md
Reproduction and train-your-own instructions.
