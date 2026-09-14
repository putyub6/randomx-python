"""In-memory job list."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field


@dataclass
class Job:
    job_id: str
    blob: bytes
    target: int


@dataclass
class JobQueue:
    items: list[Job] = field(default_factory=list)

    def push(self, seed: str, index: int) -> Job:
        raw = hashlib.sha256(f"{seed}:{index}".encode()).digest()
        job = Job(job_id=raw[:4].hex(), blob=raw, target=int.from_bytes(raw[4:8], "big"))
        self.items.append(job)
        return job

    def latest(self) -> Job | None:
        return self.items[-1] if self.items else None
