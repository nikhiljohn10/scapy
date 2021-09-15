#!/usr/bin/env python3
"""CLI Command to get predefined paths."""

from pathlib import Path

import click


@click.group()
def path():
    """Scapy path command."""


@path.command()
def passwords():
    """Return path of the passwords directory."""
    click.echo(Path.home() / ".step/secrets/passwords")


@path.command()
def certs():
    """Return path of the certificate directory."""
    click.echo(Path.home() / ".step/certs")
