#!/usr/bin/env python3
"""CLI Sub Command to get predefined config paths."""

import click

from ..settings import STEP_PATH


@click.group()
def config():
    """Sub command to get config paths."""


@config.command()
def ca():
    """Path to the ca.json."""
    click.echo(STEP_PATH / "config/ca.json")


@config.command()
def default():
    """Path to the default.json."""
    click.echo(STEP_PATH / "config/defaults.json")
