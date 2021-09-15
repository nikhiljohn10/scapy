#!/usr/bin/env python3
"""CLI Sub Command to get predefined certificate paths."""

import click

from ..settings import STEP_PATH


@click.command()
def certs():
    """Path to the certificate directory."""
    click.echo(STEP_PATH / "certs")


@click.group()
def cert():
    """Sub command to get different certificate files."""


@cert.command()
def root():
    """Path to Root CA certificate file."""
    click.echo(STEP_PATH / "certs/root_ca.crt")


@cert.command()
def intermediate():
    """Path to Intermediate CA certificate file."""
    click.echo(STEP_PATH / "certs/intermediate_ca.crt")
