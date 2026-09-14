"""Local hash helper for randomx."""

from __future__ import annotations

import hashlib
import time


def hash_job(blob: bytes, nonce: int) -> bytes:
    """Return SHA-256(blob || nonce)."""
    return hashlib.sha256(blob + nonce.to_bytes(4, "big")).digest()


def hashrate(rounds: int, blob: bytes) -> float:
    """Run ``rounds`` hashes and return hashes/sec."""
    start = time.perf_counter()
    for nonce in range(rounds):
        hash_job(blob, nonce)
    elapsed = max(time.perf_counter() - start, 1e-9)
    return rounds / elapsed
