#!/usr/bin/env python3
"""CLI Sub Command to get predefined password paths."""

import click

from ..settings import STEP_PATH


@click.command()
def passwords():
    """Path to the passwords directory."""
    click.echo(STEP_PATH / "secrets/passwords")


@click.group()
def password():
    """Sub command to get different password files."""


@password.command()
def root():
    """Path to Root CA password file."""
    click.echo(STEP_PATH / "secrets/passwords/root_ca.txt")


@password.command()
def intermediate():
    """Path to Intermediate CA password file."""
    click.echo(STEP_PATH / "secrets/passwords/intermediate_ca.txt")


@password.command()
def provisioner():
    """Path to Provisioner password file."""
    click.echo(STEP_PATH / "secrets/passwords/provisioner.txt")
