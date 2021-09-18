#!/usr/bin/env python3
"""CLI Command to generate password."""

import secrets
import string
from pathlib import Path
from typing import Optional

import click


@click.command()
@click.option(
    "-r",
    "--root",
    default=None,
    type=click.Path(file_okay=True, resolve_path=True),
    help="Root password file. Ignored if --directory option is given.",
)
@click.option(
    "-i",
    "--intermediate",
    default=None,
    type=click.Path(file_okay=True, resolve_path=True),
    help="Intermediate password file. Ignored if --directory option is given.",
)
@click.option(
    "-p",
    "--provisioner",
    default=None,
    type=click.Path(file_okay=True, resolve_path=True),
    help="Provisioner password file. Ignored if --directory option is given.",
)
@click.option(
    "-d",
    "--directory",
    default=None,
    type=click.Path(file_okay=True, resolve_path=True),
    help="Directory to store passwords",
)
@click.option(
    "-f",
    "--force",
    default=False,
    type=bool,
    help="Force to create all needed directories before password generation.",
)
def passwords(
    root: Optional[str],
    intermediate: Optional[str],
    provisioner: Optional[str],
    directory: Optional[str],
) -> None:
    """Generate root, intermediate and provisioner passwords."""
    password_characters = (
        string.ascii_letters + string.digits + string.punctuation
    )

    def gen_pass() -> str:
        """Password generation function.

        Returns:
            str: Password string
        """
        while True:
            password = "".join(
                secrets.choice(password_characters) for _ in range(24)
            )
            have_lower = any(c.islower() for c in password)
            have_upper = any(c.isupper() for c in password)
            have_digits = any(c.isdigit() for c in password)
            if have_lower and have_upper and have_digits:
                break
        return password

    if any(item is None for item in [root, intermediate, provisioner]):
        if directory is None:
            directory_path = Path.home() / ".step/secrets/passwords"
        else:
            directory_path = Path(directory)

        if not directory_path.exists():
            directory_path.mkdir(parents=True)

    if root is None:
        root_path = directory_path / "root_ca.txt"
    else:
        root_path = Path(root)

    if intermediate is None:
        intermediate_path = directory_path / "intermediate_ca.txt"
    else:
        intermediate_path = Path(intermediate)

    if provisioner is None:
        provisioner_path = directory_path / "provisioner.txt"
    else:
        provisioner_path = Path(provisioner)

    root_path.write_text(gen_pass())
    if root_path.exists():
        click.secho("Root password:          ", nl=False, fg="magenta")
        click.secho(str(root_path), fg="green")
    else:
        click.secho("Unable to write to root password file", fg="red")
    intermediate_path.write_text(gen_pass())
    if intermediate_path.exists():
        click.secho("Intermediate password:  ", nl=False, fg="magenta")
        click.secho(str(intermediate_path), fg="green")
    else:
        click.secho("Unable to write to intermediate password file", fg="red")
    provisioner_path.write_text(gen_pass())
    if provisioner_path.exists():
        click.secho("Provisioner password:   ", nl=False, fg="magenta")
        click.secho(str(provisioner_path), fg="green")
    else:
        click.secho("Unable to write to provisioner password file", fg="red")
