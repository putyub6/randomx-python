"""Glue: subscribe, scan, submit."""

from __future__ import annotations

from rxpy.config import MinerConfig
from rxpy.device.cpu import CpuBackend
from rxpy.stratum.client import StratumClient


class MineController:
    def __init__(self, config: MinerConfig | None = None) -> None:
        self.config = config or MinerConfig()
        self.client = StratumClient(self.config)
        self.cpu = CpuBackend()

    def bench(self, rounds: int = 16) -> dict:
        self.client.subscribe()
        job = self.client.jobs.latest()
        assert job is not None
        hashes = self.cpu.scan(job, rounds)
        return {
            "algo": self.config.algo,
            "rounds": rounds,
            "hashes": len(hashes),
            "job": job.job_id,
        }

    def submit(self, nonce: int) -> bool:
        if self.client.jobs.latest() is None:
            self.client.subscribe()
        return self.client.submit(nonce)
