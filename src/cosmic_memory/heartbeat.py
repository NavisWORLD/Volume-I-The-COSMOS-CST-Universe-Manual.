from __future__ import annotations
from dataclasses import dataclass
import time
from typing import Callable, Any

@dataclass
class Task:
    name: str
    interval: float
    handler: Callable[[], Any]
    next_due: float

class HeartbeatScheduler:
    """Small fail-soft scheduler modeled after COSMOS Heartbeat maintenance tasks."""
    def __init__(self, *, clock=time.time):
        self.clock = clock
        self.tasks: dict[str, Task] = {}
        self.errors: list[dict] = []

    def add(self, name: str, every_seconds: float, handler: Callable[[], Any], *, run_immediately=False):
        if every_seconds <= 0: raise ValueError("interval must be positive")
        now = self.clock()
        self.tasks[name] = Task(name, every_seconds, handler, now if run_immediately else now + every_seconds)

    def tick(self, now: float | None = None) -> list[tuple[str, Any]]:
        now = self.clock() if now is None else now
        results = []
        for task in list(self.tasks.values()):
            if now < task.next_due: continue
            try:
                results.append((task.name, task.handler()))
            except Exception as exc:
                self.errors.append({"task": task.name, "at": now, "error": repr(exc)})
            finally:
                missed = max(1, int((now - task.next_due) // task.interval) + 1)
                task.next_due += missed * task.interval
        return results
