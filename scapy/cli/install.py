#!/usr/bin/env python3
"""Installation commands."""


import click
from click.exceptions import Exit


@click.group()
def install():
    """Installation command module."""


@install.command()
def step() -> None:
    """Install Step CA."""
    Exit(0)
