#!/usr/bin/env python3
"""CLI App module."""

import click

from .delpoy import deploy


@click.group()
def cli():
    """CLI Application entry point."""


cli.add_command(deploy)
