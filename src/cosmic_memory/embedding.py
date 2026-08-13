from __future__ import annotations
import hashlib, math, re
from typing import Iterable

_TOKEN_RE = re.compile(r"[A-Za-z0-9_']+")

class HashingEmbedder:
    """Dependency-free deterministic hashing embedder.

    This is deliberately simple so the core library can run anywhere. It is a
    retrieval baseline, not a claim that hashing equals a modern embedding model.
    Applications may pass any callable that returns a numeric vector.
    """
    def __init__(self, dimensions: int = 384):
        if dimensions < 32:
            raise ValueError("dimensions must be >= 32")
        self.dimensions = dimensions

    def __call__(self, text: str) -> list[float]:
        vec = [0.0] * self.dimensions
        tokens = [t.lower() for t in _TOKEN_RE.findall(text)]
        if not tokens:
            return vec
        for pos, tok in enumerate(tokens):
            digest = hashlib.blake2b(tok.encode(), digest_size=16).digest()
            i = int.from_bytes(digest[:8], "big") % self.dimensions
            sign = -1.0 if digest[8] & 1 else 1.0
            weight = 1.0 + 0.15 * math.log1p(max(0, len(tok) - 3))
            vec[i] += sign * weight
            if pos:
                bigram = tokens[pos-1] + "\x1f" + tok
                bd = hashlib.blake2b(bigram.encode(), digest_size=16).digest()
                j = int.from_bytes(bd[:8], "big") % self.dimensions
                vec[j] += (-0.35 if bd[8] & 1 else 0.35)
        norm = math.sqrt(sum(x*x for x in vec)) or 1.0
        return [x / norm for x in vec]

def cosine(a: Iterable[float], b: Iterable[float]) -> float:
    aa, bb = list(a), list(b)
    if len(aa) != len(bb):
        raise ValueError("vector dimensions differ")
    da = sum(x*x for x in aa); db = sum(y*y for y in bb)
    if da <= 0 or db <= 0:
        return 0.0
    return sum(x*y for x, y in zip(aa, bb)) / math.sqrt(da*db)
