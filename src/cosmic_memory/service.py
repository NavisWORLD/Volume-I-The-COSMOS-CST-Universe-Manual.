from __future__ import annotations
import os
from .memory import RecursiveMemory
from .heart_bridge import HeartBridge, HeartProfile

DB = os.getenv("COSMIC_MEMORY_DB", "cosmic_memory.db")
NS = os.getenv("COSMIC_MEMORY_NAMESPACE", "default")
memory = RecursiveMemory(DB, namespace=NS)
heart = HeartBridge(HeartProfile("system-heart", os.getenv("HEART_CONSENT_REFERENCE", "self/system-owned"), "api"))

def _azure_mirror():
    if not os.getenv("COSMOS_ENDPOINT"):
        return None
    try:
        from .azure_cosmos import AzureCosmosMirror
        return AzureCosmosMirror()
    except Exception:
        return None

def create_app():
    try:
        from fastapi import FastAPI
        from pydantic import BaseModel
    except ImportError as exc:
        raise RuntimeError("Install the API extra: pip install 'cosmic-synaptic-memory[api]'") from exc
    app = FastAPI(title="Cosmic Synaptic Memory", version="0.1.0")
    class MemoryIn(BaseModel):
        text: str
        importance: float = 0.5
        metadata: dict = {}
    class RecallIn(BaseModel):
        query: str
        limit: int = 5
    class HeartIn(BaseModel):
        bpm: float
        timestamp: float | None = None
        ibi_ms: float | None = None
    @app.get("/health")
    def health(): return {"ok": True, "stats": memory.stats(), "heart_sample": None if not heart.latest else heart.latest.__dict__}
    @app.post("/remember")
    def remember(body: MemoryIn):
        rec = memory.remember(body.text, importance=body.importance, metadata=body.metadata)
        mirror = _azure_mirror()
        cloud = False
        if mirror is not None:
            try:
                mirror.upsert_memory(rec.to_dict())
                cloud = True
            except Exception:
                cloud = False
        return {"memory": rec.to_dict(), "azure_mirrored": cloud}
    @app.post("/recall")
    def recall(body: RecallIn):
        return [{"memory": h.memory.to_dict(), "similarity": h.similarity, "score": h.score} for h in memory.recall(body.query, limit=body.limit)]
    @app.post("/heart/sample")
    def heart_sample(body: HeartIn): return heart.add_sample(body.bpm, timestamp=body.timestamp, ibi_ms=body.ibi_ms).__dict__
    @app.get("/heart/pulse")
    def heart_pulse(): return {"interval_seconds": heart.beat_interval_seconds(), "phase": heart.phase(), "pulse": heart.pulse(), "source": heart.fingerprint()}
    return app

def run():
    try: import uvicorn
    except ImportError as exc: raise RuntimeError("Install API extra") from exc
    uvicorn.run(create_app(), host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
