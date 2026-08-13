# Heart Bridge — Human Heartbeat as a Software Cadence

## Purpose
Heart Bridge lets an explicitly consented heartbeat become a clock/control signal for an AI system, music engine, artwork, simulation, memory scheduler, or agent.

The software can **beat with a person** in the engineering sense that its maintenance cadence or modulation envelope can follow the person's recorded/live beat timing.

## What is measured
The minimal input is BPM. Optional inter-beat interval (`ibi_ms`) can also be stored. The core library computes:

- beat interval: `60 / bpm` seconds;
- beat phase: normalized 0..1 time within the current software beat;
- a smooth pulse envelope derived from phase.

It does not reconstruct ECG morphology.

## Consent
For data belonging to another person, `HeartProfile` rejects an empty consent reference. A production system should record what was consented, by whom, for what purpose, and how consent can be revoked.

```python
profile = HeartProfile(
    label='my-loved-one',
    consent_reference='consent-document-1234',
    source_type='apple-health-export'
)
```

## Data sources
Supported immediately:

- CSV (`timestamp,bpm,ibi_ms`);
- programmatic samples from any authorized source;
- HTTP API sample submission.

The `ble` extra is reserved for developers who want to wire a standard Bluetooth Heart Rate Service using `bleak`. The core library intentionally does not auto-connect to nearby devices.

## Integration patterns

### 1. Beat-driven heartbeat scheduler
Set a scheduler task interval to `heart.beat_interval_seconds()` and update it whenever a fresh sample arrives.

### 2. Memory timestamp enrichment
Store `{heart_phase, bpm}` in memory metadata at the moment an event occurs.

### 3. Music/visual modulation
Use `heart.pulse()` as a 0..1 envelope.

### 4. Research control
Always compare real-heart modulation with a matched synthetic clock. Otherwise any improvement could come from ordinary periodic timing rather than human physiology.

## Privacy
Do not commit real loved-one biometric files to a public repository. This repo contains only synthetic demonstration data.

## Medical boundary
This library is not intended for diagnosis, treatment, emergency monitoring, or medical decision-making. It must not infer disease, emotion, deception, compatibility, or relationship state from heart rate.
