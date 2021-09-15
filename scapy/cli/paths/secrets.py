#!/usr/bin/env python3
"""CLI Sub Command to get predefined secrets paths."""

import click

from ..settings import STEP_PATH


@click.command()
def secrets():
    """Path to the secrets directory."""
    click.echo(STEP_PATH / "secrets")


@click.group()
def key():
    """Sub command to get different private key files."""


@key.command()
def root():
    """Path to Root CA private key file."""
    click.echo(STEP_PATH / "secrets/root_ca_key")


@key.command()
def intermediate():
    """Path to Intermediate CA private key file."""
    click.echo(STEP_PATH / "secrets/intermediate_ca_key")
