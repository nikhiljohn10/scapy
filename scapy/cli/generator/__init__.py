#!/usr/bin/env python3
"""CLI Command to generate files."""

import click

from .password import passwords
from .worker import worker


@click.group()
def gen():
    """Scapy Generator Command."""


gen.add_command(worker)
gen.add_command(passwords)
