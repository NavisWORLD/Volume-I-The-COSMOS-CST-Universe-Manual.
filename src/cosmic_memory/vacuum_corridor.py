"""Experimental CST state-space 'vacuum / danger corridor' test harness.

This module is inspired by the prior Navier-Stokes reduction work in which two
asymptotic regimes were comparatively safe and the unresolved dynamics lived in
an intermediate-R corridor. It DOES NOT prove Navier-Stokes regularity.

Engineering transfer: measure how long a recurrent state process remains in a
predeclared high-danger corridor and test whether an anti-locking control reduces
residence time without destroying useful state variation.
"""
from __future__ import annotations
from dataclasses import dataclass
import math, random

@dataclass
class CorridorResult:
    steps: int
    dangerous_steps: int
    longest_run: int
    residence_fraction: float
    mean_r: float
    escaped_runs: int


def danger_score(r: float, eta: float, tau: float, *, ridge_r: float = 3.0) -> float:
    r_term = math.exp(-0.5 * ((r - ridge_r) / 0.65) ** 2)
    alignment = math.exp(-0.5 * (eta / 0.35) ** 2) * math.exp(-0.5 * (tau / 0.35) ** 2)
    return r_term * alignment


def simulate(*, steps: int = 5000, seed: int = 7, anti_locking: bool = False,
             threshold: float = 0.65) -> CorridorResult:
    rng = random.Random(seed)
    r, eta, tau = 2.0, 0.5, 0.5
    dangerous = longest = run = escaped = 0
    total_r = 0.0
    for _ in range(steps):
        r += 0.035 * (2.6 - r) + 0.055 * rng.gauss(0, 1) + 0.012 * eta
        r = max(1.001, min(8.0, r))
        eta += -0.045 * eta + 0.06 * rng.gauss(0, 1)
        tau += -0.040 * tau + 0.06 * rng.gauss(0, 1)
        score = danger_score(r, eta, tau)
        if score >= threshold:
            dangerous += 1; run += 1; longest = max(longest, run)
            if anti_locking and run >= 12:
                eta += 0.75 if eta <= 0 else -0.75
                escaped += 1; run = 0
        else:
            run = 0
        total_r += r
    return CorridorResult(steps, dangerous, longest, dangerous / steps, total_r / steps, escaped)


def compare(seed: int = 7, steps: int = 5000):
    base = simulate(seed=seed, steps=steps, anti_locking=False)
    controlled = simulate(seed=seed, steps=steps, anti_locking=True)
    return {"baseline": base.__dict__, "anti_locking": controlled.__dict__,
            "residence_reduction": base.residence_fraction - controlled.residence_fraction,
            "longest_run_reduction": base.longest_run - controlled.longest_run}
