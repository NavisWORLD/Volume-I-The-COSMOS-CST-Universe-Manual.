from __future__ import annotations
import json
from pathlib import Path
from .memory import RecursiveMemory

class PlanetaryMemory:
    """Multi-namespace memory federation.

    Planetary Memory is an engineering name for durable memory that can be
    partitioned by person/agent/project and merged by exported records. It does
    not imply a literal planetary or Akashic data source.
    """
    def __init__(self, db_path: str | Path = "planetary_memory.db"):
        self.db_path = Path(db_path)

    def space(self, namespace: str) -> RecursiveMemory:
        return RecursiveMemory(self.db_path, namespace=namespace)

    def export_all(self, path: str | Path):
        from .store import SQLiteStore
        store = SQLiteStore(self.db_path)
        path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            for rec, _ in store.iter_memories(None):
                f.write(json.dumps(rec.to_dict(), sort_keys=True) + "\n")
        store.close(); return path

    def import_all(self, path: str | Path) -> int:
        count = 0
        handles = {}
        try:
            with Path(path).open("r", encoding="utf-8") as f:
                for line in f:
                    if not line.strip(): continue
                    item = json.loads(line); ns = item.get("namespace", "default")
                    mem = handles.setdefault(ns, self.space(ns))
                    mem.remember(item["text"], importance=item.get("importance", 0.5), metadata=item.get("metadata") or {},
                                 derived_from=item.get("derived_from") or [])
                    count += 1
        finally:
            for h in handles.values(): h.close()
        return count
