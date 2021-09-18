#!/usr/bin/env python3
"""CLI App module."""

import click

from .delpoy import deploy
from .download import get
from .generator import gen
from .paths import path

cli = click.Group()
cli.add_command(deploy)
cli.add_command(gen)
cli.add_command(path)
cli.add_command(get)
