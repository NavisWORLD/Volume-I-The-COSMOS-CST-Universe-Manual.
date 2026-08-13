from __future__ import annotations
import json, sqlite3, threading
from pathlib import Path
from .models import MemoryRecord

SCHEMA = """
PRAGMA journal_mode=WAL;
CREATE TABLE IF NOT EXISTS memories (
  id TEXT PRIMARY KEY,
  namespace TEXT NOT NULL,
  text TEXT NOT NULL,
  created_at REAL NOT NULL,
  updated_at REAL NOT NULL,
  importance REAL NOT NULL,
  metadata_json TEXT NOT NULL,
  embedding_json TEXT NOT NULL,
  checksum TEXT NOT NULL,
  access_count INTEGER NOT NULL DEFAULT 0,
  last_accessed_at REAL,
  derived_from_json TEXT NOT NULL DEFAULT '[]'
);
CREATE INDEX IF NOT EXISTS idx_mem_namespace_created ON memories(namespace, created_at DESC);
CREATE UNIQUE INDEX IF NOT EXISTS idx_mem_namespace_checksum ON memories(namespace, checksum);
CREATE TABLE IF NOT EXISTS associations (
  namespace TEXT NOT NULL,
  source TEXT NOT NULL,
  target TEXT NOT NULL,
  weight REAL NOT NULL,
  updates INTEGER NOT NULL,
  last_seen REAL NOT NULL,
  PRIMARY KEY(namespace, source, target)
);
CREATE TABLE IF NOT EXISTS events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  namespace TEXT NOT NULL,
  kind TEXT NOT NULL,
  timestamp REAL NOT NULL,
  payload_json TEXT NOT NULL
);
"""

class SQLiteStore:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()
        self._conn = sqlite3.connect(self.path, check_same_thread=False)
        self._conn.row_factory = sqlite3.Row
        self._conn.executescript(SCHEMA)
        self._conn.commit()

    def close(self):
        self._conn.close()

    def put(self, rec: MemoryRecord, embedding: list[float]):
        with self._lock:
            self._conn.execute("""INSERT INTO memories
            (id,namespace,text,created_at,updated_at,importance,metadata_json,embedding_json,checksum,access_count,last_accessed_at,derived_from_json)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
            ON CONFLICT(id) DO UPDATE SET
              text=excluded.text, updated_at=excluded.updated_at, importance=excluded.importance,
              metadata_json=excluded.metadata_json, embedding_json=excluded.embedding_json,
              checksum=excluded.checksum, access_count=excluded.access_count,
              last_accessed_at=excluded.last_accessed_at, derived_from_json=excluded.derived_from_json
            """, (rec.id, rec.namespace, rec.text, rec.created_at, rec.updated_at, rec.importance,
                  json.dumps(rec.metadata, sort_keys=True), json.dumps(embedding), rec.checksum,
                  rec.access_count, rec.last_accessed_at, json.dumps(rec.derived_from)))
            self._conn.commit()

    def by_checksum(self, namespace: str, checksum: str):
        row = self._conn.execute("SELECT * FROM memories WHERE namespace=? AND checksum=?", (namespace, checksum)).fetchone()
        return self._decode(row) if row else None

    def iter_memories(self, namespace: str | None = None):
        q = "SELECT * FROM memories" + (" WHERE namespace=?" if namespace else "") + " ORDER BY created_at ASC"
        rows = self._conn.execute(q, (namespace,) if namespace else ()).fetchall()
        for row in rows:
            yield self._decode(row), json.loads(row["embedding_json"])

    def get(self, memory_id: str):
        row = self._conn.execute("SELECT * FROM memories WHERE id=?", (memory_id,)).fetchone()
        return self._decode(row) if row else None

    def touch(self, memory_id: str, now: float):
        with self._lock:
            self._conn.execute("UPDATE memories SET access_count=access_count+1,last_accessed_at=? WHERE id=?", (now, memory_id))
            self._conn.commit()

    def associate(self, namespace: str, source: str, target: str, delta: float, now: float):
        if source > target:
            source, target = target, source
        if source == target:
            return
        with self._lock:
            self._conn.execute("""INSERT INTO associations(namespace,source,target,weight,updates,last_seen)
            VALUES(?,?,?,?,1,?)
            ON CONFLICT(namespace,source,target) DO UPDATE SET
              weight=MIN(20.0, associations.weight + excluded.weight),
              updates=associations.updates+1,last_seen=excluded.last_seen""",
              (namespace, source, target, float(delta), now))
            self._conn.commit()

    def top_associations(self, namespace: str, limit: int = 20):
        rows = self._conn.execute("SELECT * FROM associations WHERE namespace=? ORDER BY weight DESC, updates DESC LIMIT ?", (namespace, limit)).fetchall()
        return [dict(r) for r in rows]

    def event(self, namespace: str, kind: str, timestamp: float, payload: dict):
        with self._lock:
            self._conn.execute("INSERT INTO events(namespace,kind,timestamp,payload_json) VALUES(?,?,?,?)",
                               (namespace, kind, timestamp, json.dumps(payload, sort_keys=True)))
            self._conn.commit()

    def stats(self, namespace: str | None = None):
        args = (namespace,) if namespace else ()
        where = " WHERE namespace=?" if namespace else ""
        mem = self._conn.execute("SELECT COUNT(*) c FROM memories" + where, args).fetchone()[0]
        assoc = self._conn.execute("SELECT COUNT(*) c FROM associations" + where, args).fetchone()[0]
        ev = self._conn.execute("SELECT COUNT(*) c FROM events" + where, args).fetchone()[0]
        return {"memories": mem, "associations": assoc, "events": ev, "path": str(self.path)}

    @staticmethod
    def _decode(row) -> MemoryRecord:
        return MemoryRecord(
            id=row["id"], namespace=row["namespace"], text=row["text"], created_at=row["created_at"],
            updated_at=row["updated_at"], importance=row["importance"], metadata=json.loads(row["metadata_json"]),
            checksum=row["checksum"], access_count=row["access_count"], last_accessed_at=row["last_accessed_at"],
            derived_from=json.loads(row["derived_from_json"] or "[]")
        )
