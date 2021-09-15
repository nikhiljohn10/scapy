#!/usr/bin/env python3
"""CLI App module."""

import click

from .delpoy import deploy
from .generator import gen
from .install import install
from .paths import path

cli = click.Group()
cli.add_command(deploy)
cli.add_command(gen)
cli.add_command(path)
cli.add_command(install)
