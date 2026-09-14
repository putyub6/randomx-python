"""Stub stratum session."""

from __future__ import annotations

from rxpy.config import MinerConfig
from rxpy.stratum.jobs import JobQueue


class StratumClient:
    """No sockets. Jobs are synthesized from the pool URL."""

    def __init__(self, config: MinerConfig) -> None:
        self.config = config
        self.jobs = JobQueue()
        self.accepted = 0

    def subscribe(self) -> str:
        self.jobs.push(self.config.pool, 0)
        return "sub-001"

    def submit(self, nonce: int) -> bool:
        job = self.jobs.latest()
        if job is None:
            return False
        self.accepted += 1
        return True
