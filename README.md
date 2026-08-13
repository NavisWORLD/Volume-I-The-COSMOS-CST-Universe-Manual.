# Volume I — The COSMOS / CST Universe Manual

**Open-disclosure reference implementation for the COSMOS / Davis Cosmic Synapse Theory research program.**

This repository combines the book/manual with an installable, provider-agnostic memory library derived from the engineering patterns documented in COSMOS:

- durable persistent memory with **no built-in N-turn expiry**;
- semantic retrieval over the retained store;
- Hebbian-style concept association and salience;
- recursive/dream consolidation;
- **Planetary Memory** namespaces and portable JSONL merge/export;
- a fail-soft **Cosmos Heartbeat** maintenance scheduler;
- a consent-gated **Heart Bridge** that can use a recorded or live heartbeat as a software cadence/control signal;
- optional **Azure Cosmos DB** cloud mirroring using Microsoft Entra / managed identity;
- an experimental **vacuum / danger-corridor** state-space test inspired by the earlier Navier–Stokes reduction work;
- teacher manual, study course, experiments, evidence rules, and the full Volume I manual.

## Evidence rule

This project deliberately separates:

- **IMPLEMENTED** — code exists;
- **OBSERVED** — a captured runtime shows the code executed;
- **MEASURED** — a defined experiment produced a metric;
- **NULL** — a tested hypothesis failed its declared success criterion;
- **HYPOTHESIS** — a falsifiable proposition awaiting stronger evidence;
- **METAPHOR / MODEL** — useful language that is not itself literal physics or biology.

The library does **not** claim machine consciousness, infinite storage, medical diagnosis, a Navier–Stokes proof, or quantum ML advantage.

## Install

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .
```

Optional capabilities:

```bash
pip install -e '.[api]'
pip install -e '.[azure]'
pip install -e '.[ble]'
pip install -e '.[all]'
```

## Five-minute memory adapter

```python
from cosmic_memory import RecursiveMemory
from cosmic_memory.adapters import ModelMemoryAdapter

memory = RecursiveMemory("my_agent.db", namespace="my-agent")

# Replace this callable with ANY local or hosted model SDK.
def model(prompt: str) -> str:
    return your_model_call(prompt)

agent = ModelMemoryAdapter(memory, model)
reply = agent("Remember that the deployment codename is Aurora.")
reply = agent("What is the deployment codename?")
```

The adapter retrieves semantically relevant old records, prepends only the compact memory block to the current prompt, stores the new exchange, and keeps doing so across process restarts.

> **“Forever memory” means durable owner-controlled persistence without an automatic chat-window expiry.** It is not a promise that a disk can never fail. Back up the database.

## CLI

```bash
cosmic-memory remember "The launch codename is Aurora" --importance 0.9
cosmic-memory recall "What was the launch codename?"
cosmic-memory stats
cosmic-memory dream
cosmic-memory export memories.jsonl
cosmic-memory vacuum-test --seed 7 --steps 5000
```

## Heart Bridge

A heartbeat can drive a software cadence without pretending the program is biological.

```python
from cosmic_memory import HeartBridge, HeartProfile

heart = HeartBridge(HeartProfile(
    label="someone-I-love",
    consent_reference="written-consent-2026-08-12",
    source_type="recorded"
))
heart.add_sample(72)
print(heart.beat_interval_seconds())
print(heart.pulse())
```

For another person's biometric data, the library requires an explicit `consent_reference`. The sample code is **not a medical device** and does not infer disease or emotion from heart rate.

Import a consented CSV:

```bash
cosmic-memory heart-csv examples/loved_heart.csv \
  --label loved-one \
  --consent 'consent-record-id-or-note'
```

## Planetary Memory

```python
from cosmic_memory import PlanetaryMemory

planet = PlanetaryMemory("planet.db")
research = planet.space("research")
family = planet.space("family")
research.remember("Experiment 17 used seed 42.")
family.remember("A private family memory.")
```

Namespaces are isolated in recall but can be exported and merged intentionally. "Planetary" is an engineering name for federated, portable, durable memory — **not a claim of an external planetary/Akashic information source**.

## API service

```bash
pip install -e '.[api]'
cosmic-memory-api
```

Endpoints:

- `GET /health`
- `POST /remember`
- `POST /recall`
- `POST /heart/sample`
- `GET /heart/pulse`

## Azure

The optional Azure path mirrors durable records to Azure Cosmos DB for NoSQL and runs the API in Azure Container Apps. It uses `DefaultAzureCredential`, so local development can use Azure CLI identity and production can use managed identity rather than hard-coded secrets.

See **[`docs/AZURE_BUILD_GUIDE.md`](docs/AZURE_BUILD_GUIDE.md)** and **[`infra/azure/deploy.sh`](infra/azure/deploy.sh)**.

## The vacuum / corridor experiment

The prior Navier–Stokes work did **not** produce a Millennium proof. It reduced the remaining danger to an unresolved intermediate state-space corridor, with the missing closure being a finite-danger-residence / anti-locking theorem.

This repository transfers that idea into CST as a software experiment:

1. define a high-danger ridge in state space;
2. measure residence time and longest lock duration;
3. introduce a transparent anti-locking control;
4. test whether it reduces sustained locking without collapsing state variation.

Run:

```bash
cosmic-memory vacuum-test --seed 7 --steps 10000
```

The implementation is in [`src/cosmic_memory/vacuum_corridor.py`](src/cosmic_memory/vacuum_corridor.py). It is a **toy falsifiable state-space experiment**, not fluid-dynamics proof code.

## Repository map

```text
.
├── README.md
├── LICENSE
├── NOTICE
├── CITATION.cff
├── pyproject.toml
├── Dockerfile
├── src/cosmic_memory/
│   ├── memory.py              durable semantic + recursive memory
│   ├── store.py               SQLite persistence and Hebbian graph
│   ├── embedding.py           zero-dependency retrieval baseline
│   ├── adapters.py            generic model integration
│   ├── planetary.py           multi-namespace/federated memory
│   ├── heartbeat.py           proactive fail-soft scheduler
│   ├── heart_bridge.py        consented heartbeat→software cadence
│   ├── azure_cosmos.py        optional Cosmos DB mirror
│   ├── vacuum_corridor.py     experimental anti-locking harness
│   ├── service.py             optional FastAPI service
│   └── cli.py
├── docs/
│   ├── COSMOS_CST_UNIVERSE_MANUAL.md
│   ├── OPEN_DISCLOSURE_MANUAL.md
│   ├── TEACHERS_GUIDE.md
│   ├── MEMORY_ARCHITECTURE.md
│   ├── HEART_BRIDGE_GUIDE.md
│   ├── AZURE_BUILD_GUIDE.md
│   ├── GROWTH_CYCLES.md
│   ├── EXPERIMENTAL_VACUUM_CORRIDOR_ADDENDUM.md
│   └── PUBLIC_RESEARCH_LINKS.md
├── examples/
├── tests/
└── infra/azure/
```

## Reproducibility

```bash
pip install -e '.[dev]'
pytest -q
```

The CI workflow runs the same test suite on every push and pull request.

## Citation and DOI

Foundational CST deposit:

**Cory Shane Davis, _12-Dimensional Cosmic Synapse Theory_, Zenodo.**  
DOI: **10.5281/zenodo.17574447**

See `CITATION.cff` for machine-readable citation metadata. A DOI establishes a persistent scholarly reference; it is not, by itself, a patent or exclusive copyright registration.

## License

Apache License 2.0. See `LICENSE` and `NOTICE`.

Open disclosure means others may inspect, study, modify, and redistribute the software under the license while retaining required notices. Biometric data, private conversation archives, credentials, and third-party model weights are **not** automatically licensed merely because this source code is public.
