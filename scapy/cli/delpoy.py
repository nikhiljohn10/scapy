#!/usr/bin/env python3
"""CLI Command to deploy cloudflare worker."""

from pathlib import Path

import click

from scapy import Worker

from .utils import Printer

HOME = Path.home()


@click.command()
@click.option(
    "-t",
    "--token",
    envvar="CF_TOKEN",
    default=None,
    type=str,
    help="Cloudflare API Token to access workers",
)
@click.option(
    "-w",
    "--worker",
    envvar="WORKER",
    default="ca",
    type=str,
    help="Name of the worker",
)
@click.option(
    "-j",
    "--js",
    envvar="WORKER_FILE",
    default=Path("./build/index.js"),
    type=click.Path(exists=True),
    help="Worker file location",
)
@click.option(
    "-n",
    "--name",
    envvar="CA_NAME",
    type=str,
    help="CA Server's Name",
)
@click.option(
    "-f",
    "--fingerprint",
    envvar="FINGERPRINT",
    type=str,
    help="Root CA Certificate's fingerprint",
)
@click.option(
    "-u",
    "--ca-url",
    envvar="CA_URL",
    default="https://stepca.local",
    type=str,
    help="CA Server's URL",
)
@click.option(
    "-r",
    "--root",
    envvar="ROOT_CERT",
    default=(HOME / ".step/certs/root_ca.crt"),
    type=click.Path(exists=True),
    help="CA Root Certificate file in PEM or DER format",
)
def deploy(
    token: str,
    worker: str,
    js: Path,
    name: str,
    fingerprint: str,
    ca_url: str,
    root: Path,
):
    """Deploy a cloudflare worker to publish CA Certificate."""
    printer = Printer()
    printer.working("Initialising deployment process", animate=False)
    deployer = Worker(token)
    printer.done("Worker instance is created")
    deployer.store(
        web_title=name,
        fingerprint=fingerprint,
        ca_url=ca_url,
    )
    printer.done("Updated worker with given data")
    printer.working("Uploding Root Certificate")
    deployer.loadCA(root)
    printer.done("Root Certificate is uploaded")
    printer.working("Deploying the worker")
    deployed_url = deployer.deploy(worker, js)
    printer.done("Deployed worker:", deployed_url)
