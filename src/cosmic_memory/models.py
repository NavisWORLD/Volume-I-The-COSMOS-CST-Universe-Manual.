from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Any

@dataclass(slots=True)
class MemoryRecord:
    id: str
    namespace: str
    text: str
    created_at: float
    updated_at: float
    importance: float = 0.5
    metadata: dict[str, Any] = field(default_factory=dict)
    checksum: str = ""
    access_count: int = 0
    last_accessed_at: float | None = None
    derived_from: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

@dataclass(slots=True)
class RecallResult:
    memory: MemoryRecord
    similarity: float
    score: float
    recency: float
