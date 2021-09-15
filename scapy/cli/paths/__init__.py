#!/usr/bin/env python3
"""CLI Command to get predefined step paths."""

import click

from ..settings import STEP_PATH
from .certificates import cert, certs
from .configs import config
from .passwords import password, passwords
from .secrets import key, secrets


@click.group()
def path():
    """Scapy path command."""


path.add_command(cert)
path.add_command(certs)
path.add_command(password)
path.add_command(passwords)
path.add_command(key)
path.add_command(secrets)
path.add_command(config)
