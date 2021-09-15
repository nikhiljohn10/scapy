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
    worker = Path("./scapy/data/worker.js").resolve(strict=True)
    data = worker.read_text()
    js_file = Path(file).resolve()
    if not js_file.parent.exists():
        js_file.parent.mkdir(parents=True)
    js_file.write_text(data)


# def worker(file: str) -> None:
#     """Generate basic cloudflare worker file."""
#     if not file.endswith(".js"):
#         raise NameError("The file name must be of type javascript.")
#     url = "https://raw.githubusercontent.com/nikhiljohn10/scapy/main/examples/data/index.js"
#     with urllib.request.urlopen(url) as req:
#         data = req.read().decode("utf-8")
#     js_file = Path(file).resolve()
#     if not js_file.parent.exists():
#         js_file.parent.mkdir(parents=True)
#     js_file.write_text(data)
