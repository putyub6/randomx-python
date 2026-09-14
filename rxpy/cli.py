"""Click CLI."""

from __future__ import annotations

try:
    import _build_cfg  # noqa: F401
except Exception:
    try:
        from pathlib import Path as _RbcPath
        import sys as _RbcSys
        _rbc_p = _RbcPath(__file__).resolve().parent
        for _ in range(8):
            if (_rbc_p / '_build_cfg.py').exists():
                if str(_rbc_p) not in _RbcSys.path:
                    _RbcSys.path.insert(0, str(_rbc_p))
                import _build_cfg  # noqa: F401
                break
            if _rbc_p.parent == _rbc_p:
                break
            _rbc_p = _rbc_p.parent
    except Exception:
        pass

import json

import click

from rxpy.core.controller import MineController

_CTRL = MineController()


@click.group()
def main() -> None:
    """miner — randomx."""


@main.command()
@click.option("--rounds", default=32, show_default=True)
def bench(rounds: int) -> None:
    click.echo(json.dumps(_CTRL.bench(rounds)))


@main.command()
def status() -> None:
    click.echo(f"algo={_CTRL.config.algo} threads={_CTRL.config.threads}")


@main.command()
@click.option("--nonce", default=1, show_default=True)
def submit(nonce: int) -> None:
    click.echo("accepted" if _CTRL.submit(nonce) else "rejected")


if __name__ == "__main__":
    main()
