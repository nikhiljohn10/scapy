#!/usr/bin/env python3
"""CLI Command to generate worker."""

from pathlib import Path

import click


@click.command()
@click.option(
    "-f", "--file", default="./worker.js", help="Worker file location"
)
def worker(file: str) -> None:
    """Generate basic cloudflare worker file."""
    if not file.endswith(".js"):
        raise NameError("The file name must be of type javascript.")
    project_root = Path(__file__).parent.parent.parent
    worker = (project_root / "data/worker.js").resolve(strict=True)
    data = worker.read_text()
    js_file = Path(file).resolve()
    if not js_file.parent.exists():
        js_file.parent.mkdir(parents=True)
    js_file.write_text(data)
