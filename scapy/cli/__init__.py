#!/usr/bin/env python3
"""CLI App module."""

from typing import Any

import click
import click_completion
from click.core import Context

from .delpoy import deploy
from .download import get
from .generator import gen
from .paths import path


def install_callback(ctx: Context, attr: Any, value: Any) -> None:
    """Shell competion function.

    Args:
        ctx (click.core.Context): Context
        attr: Attribute
        value: Value
    """
    if not value or ctx.resilient_parsing:
        return value
    shell, path = click_completion.core.install()
    click.echo("%s completion installed in %s." % (shell, path))
    click.echo("Use ", nl=False)
    click.secho(f". {path}", fg="green", bold=True, nl=False)
    click.echo(" to activate the completion.")
    exit(0)


click_completion.init()


@click.group()
@click.option(
    "-c",
    "--completion",
    is_flag=True,
    callback=install_callback,
    expose_value=False,
    help="Install completion for the current shell.",
)
def cli():
    """Commnadline Interface to manage step ca."""


cli.add_command(deploy)
cli.add_command(gen)
cli.add_command(path)
cli.add_command(get)
