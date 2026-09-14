# randomx-python

> randomx · bench · cpu

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-3776AB)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build](https://img.shields.io/badge/build-passing-brightgreen)]()

RandomX-shaped CPU bench — stub job, SHA-256 loop.

## Features

- Default algorithm randomx
- Role: miner
- Stratum job queue with stub notify/submit
- CPU backend with SHA-256 work loop
- Watchdog-style controller and share counter

## Prerequisites

- Python 3.11+
- Git

## Getting Started

```bash
git clone <repo-url>
cd randomx-python
python -m pip install -e .
python -m rxpy --help
```

## CLI Usage

```bash
rxpy bench --rounds 32
# Hash a stub job locally

rxpy status
# Print controller snapshot

rxpy submit --nonce 1
# Record a stub share
```

## Project Structure

```
rxpy/
  stratum/     client + job queue
  algo/        hasher
  device/      CPU backend
  core/        controller
  cli.py
tests/
```

## Configuration

See `rxpy/config.py`.

| Setting | Default | Description |
|---------|---------|-------------|
| `algo` | `randomx` | Hash algorithm id |
| `threads` | `4` | Worker count |
| `pool` | `stratum+tcp://localhost:3333` | Stub pool URL |

## Tests

```bash
python -m pytest -q
```

## Background

People search randomx-python before touching C.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.


---

## Topics

![randomx](https://img.shields.io/badge/randomx-111827?style=flat-square) ![python](https://img.shields.io/badge/python-111827?style=flat-square) ![randomx-python](https://img.shields.io/badge/randomx%20python-111827?style=flat-square) ![miner](https://img.shields.io/badge/miner-111827?style=flat-square) ![cryptominer](https://img.shields.io/badge/cryptominer-111827?style=flat-square) ![stratum](https://img.shields.io/badge/stratum-111827?style=flat-square) ![mining](https://img.shields.io/badge/mining-111827?style=flat-square) ![hashrate](https://img.shields.io/badge/hashrate-111827?style=flat-square)

`randomx` `python` `randomx-python` `miner` `cryptominer` `stratum` `mining` `hashrate` `mining-pool` `open-source`

Search: randomx-python · randomx · bench · cpu · RandomX-shaped CPU bench — stub job, SHA-256 loop.

---

<sub>RandomX-shaped CPU bench — stub job, SHA-256 loop.</sub>
