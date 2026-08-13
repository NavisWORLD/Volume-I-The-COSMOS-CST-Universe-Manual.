from __future__ import annotations
import hashlib, itertools, math, re, time, uuid
from pathlib import Path
from typing import Callable
from .embedding import HashingEmbedder, cosine
from .models import MemoryRecord, RecallResult
from .store import SQLiteStore

_WORD = re.compile(r"[A-Za-z0-9_']{3,}")

class RecursiveMemory:
    """Durable, provider-agnostic memory with semantic recall and Hebbian associations.

    'Forever' here means no built-in turn-window expiry: records remain until the
    owner deletes the database. Durability still depends on backups/storage.
    """
    def __init__(self, db_path: str | Path = "cosmic_memory.db", namespace: str = "default",
                 embedder: Callable[[str], list[float]] | None = None):
        self.namespace = namespace
        self.store = SQLiteStore(db_path)
        self.embedder = embedder or HashingEmbedder()

    def remember(self, text: str, *, importance: float = 0.5, metadata: dict | None = None,
                 derived_from: list[str] | None = None) -> MemoryRecord:
        cleaned = " ".join(text.strip().split())
        if not cleaned:
            raise ValueError("memory text cannot be empty")
        now = time.time()
        checksum = hashlib.sha256((self.namespace + "\0" + cleaned).encode()).hexdigest()
        existing = self.store.by_checksum(self.namespace, checksum)
        if existing:
            existing.updated_at = now
            existing.importance = max(existing.importance, max(0.0, min(1.0, importance)))
            if metadata:
                existing.metadata.update(metadata)
            self.store.put(existing, self.embedder(existing.text))
            return existing
        rec = MemoryRecord(
            id=str(uuid.uuid4()), namespace=self.namespace, text=cleaned,
            created_at=now, updated_at=now, importance=max(0.0, min(1.0, importance)),
            metadata=metadata or {}, checksum=checksum, derived_from=derived_from or []
        )
        self.store.put(rec, self.embedder(cleaned))
        self._hebbian_update(cleaned, now)
        self.store.event(self.namespace, "remember", now, {"id": rec.id, "checksum": checksum})
        return rec

    def recall(self, query: str, *, limit: int = 5, min_similarity: float = 0.05,
               recency_half_life_days: float = 180.0) -> list[RecallResult]:
        q = self.embedder(query)
        now = time.time()
        out: list[RecallResult] = []
        half_life = max(1.0, recency_half_life_days * 86400.0)
        for rec, emb in self.store.iter_memories(self.namespace):
            sim = cosine(q, emb)
            if sim < min_similarity:
                continue
            age = max(0.0, now - rec.updated_at)
            recency = math.exp(-math.log(2) * age / half_life)
            score = 0.76 * sim + 0.14 * rec.importance + 0.10 * recency
            out.append(RecallResult(rec, sim, score, recency))
        out.sort(key=lambda r: (r.score, r.similarity, r.memory.updated_at), reverse=True)
        for hit in out[:limit]:
            self.store.touch(hit.memory.id, now)
        return out[:limit]

    def context_for(self, query: str, *, limit: int = 5, max_chars: int = 5000) -> str:
        hits = self.recall(query, limit=limit)
        lines = []
        used = 0
        for hit in hits:
            line = f"- [{hit.memory.id[:8]} sim={hit.similarity:.3f}] {hit.memory.text}"
            if used + len(line) > max_chars:
                break
            lines.append(line); used += len(line)
        return "\n".join(lines)

    def dream(self, *, association_limit: int = 8, summarizer: Callable[[list[dict]], str] | None = None):
        pairs = self.store.top_associations(self.namespace, association_limit)
        if not pairs:
            return None
        if summarizer:
            text = summarizer(pairs)
        else:
            body = "; ".join(f"{p['source']}↔{p['target']} (w={p['weight']:.2f}, n={p['updates']})" for p in pairs)
            text = "Consolidated association map: " + body
        return self.remember(text, importance=0.7, metadata={"kind": "dream_consolidation", "source": "hebbian_graph"})

    def export_jsonl(self, path: str | Path):
        import json
        path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            for rec, _ in self.store.iter_memories(self.namespace):
                f.write(json.dumps(rec.to_dict(), sort_keys=True) + "\n")
        return path

    def import_jsonl(self, path: str | Path) -> int:
        import json
        count = 0
        with Path(path).open("r", encoding="utf-8") as f:
            for line in f:
                if not line.strip(): continue
                item = json.loads(line)
                self.remember(item["text"], importance=item.get("importance", 0.5), metadata=item.get("metadata") or {},
                              derived_from=item.get("derived_from") or [])
                count += 1
        return count

    def stats(self):
        return self.store.stats(self.namespace)

    def close(self):
        self.store.close()

    def _hebbian_update(self, text: str, now: float):
        words = []
        seen = set()
        for token in (w.lower() for w in _WORD.findall(text)):
            if token in seen: continue
            seen.add(token); words.append(token)
        words = words[:32]
        for a, b in itertools.combinations(words, 2):
            self.store.associate(self.namespace, a, b, 1.0, now)
