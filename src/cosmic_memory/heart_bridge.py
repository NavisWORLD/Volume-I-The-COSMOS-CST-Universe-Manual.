from __future__ import annotations
from dataclasses import dataclass
import csv, hashlib, math, time
from pathlib import Path

@dataclass(frozen=True)
class HeartProfile:
    label: str
    consent_reference: str
    source_type: str = "recorded"

    def validate(self):
        if not self.consent_reference.strip():
            raise PermissionError("Heart Bridge requires an explicit consent_reference for another person's biometric data.")

@dataclass(frozen=True)
class HeartSample:
    timestamp: float
    bpm: float
    ibi_ms: float | None = None

class HeartBridge:
    """Maps consented heartbeat samples into a software beat clock.

    This is expressive/control data, not medical diagnosis. The bridge never
    infers disease or emotion from heart rate.
    """
    def __init__(self, profile: HeartProfile):
        profile.validate()
        self.profile = profile
        self.samples: list[HeartSample] = []

    def add_sample(self, bpm: float, *, timestamp: float | None = None, ibi_ms: float | None = None):
        if not 20.0 <= float(bpm) <= 260.0:
            raise ValueError("bpm outside supported software-control range 20..260")
        s = HeartSample(time.time() if timestamp is None else float(timestamp), float(bpm), None if ibi_ms is None else float(ibi_ms))
        self.samples.append(s); return s

    @property
    def latest(self) -> HeartSample | None:
        return self.samples[-1] if self.samples else None

    def beat_interval_seconds(self) -> float:
        if not self.latest: return 1.0
        return 60.0 / self.latest.bpm

    def phase(self, at: float | None = None) -> float:
        s = self.latest
        if not s: return 0.0
        t = time.time() if at is None else at
        return ((t - s.timestamp) / self.beat_interval_seconds()) % 1.0

    def pulse(self, at: float | None = None) -> float:
        ph = self.phase(at)
        return math.exp(-((ph - 0.08) / 0.09) ** 2)

    def fingerprint(self) -> str:
        material = f"{self.profile.label}|{self.profile.consent_reference}|{self.profile.source_type}"
        return hashlib.sha256(material.encode()).hexdigest()[:16]

    @classmethod
    def from_csv(cls, path: str | Path, profile: HeartProfile):
        bridge = cls(profile)
        with Path(path).open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                bridge.add_sample(float(row["bpm"]), timestamp=float(row.get("timestamp") or time.time()),
                                  ibi_ms=float(row["ibi_ms"]) if row.get("ibi_ms") else None)
        return bridge
