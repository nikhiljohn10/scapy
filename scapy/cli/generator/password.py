#!/usr/bin/env python3
"""CLI Command to generate password."""

import secrets
import string
from pathlib import Path

import click

PASSWORD_HOME = Path.home() / ".step/secrets/passwords"


@click.command()
@click.option(
    "-r",
    "--root",
    default=(PASSWORD_HOME / "root.txt"),
    type=click.Path(file_okay=True, resolve_path=True, path_type=Path),
    help="Root password file. Ignored if --directory option is given.",
)
@click.option(
    "-i",
    "--intermediate",
    default=(PASSWORD_HOME / "intermediate.txt"),
    type=click.Path(file_okay=True, resolve_path=True, path_type=Path),
    help="Intermediate password file. Ignored if --directory option is given.",
)
@click.option(
    "-p",
    "--provisioner",
    default=(PASSWORD_HOME / "provisioner.txt"),
    type=click.Path(file_okay=True, resolve_path=True, path_type=Path),
    help="Provisioner password file. Ignored if --directory option is given.",
)
@click.option(
    "-d",
    "--directory",
    default=None,
    type=click.Path(dir_okay=True, resolve_path=True, path_type=Path),
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
    root: Path,
    intermediate: Path,
    provisioner: Path,
    directory: Path,
    force: bool,
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

    def have_parent(file: Path, make_parents: bool = False) -> bool:
        """Check if the file's paraent directory exsits and create if confirmed.

        Args:
            file (Path): File to process
            make_parents (bool, optional): Force to make parents. Defaults to False.
        """
        parent = file.parent
        if not parent.is_dir():
            if not make_parents:
                click.secho(
                    "Warning: ",
                    nl=False,
                    fg="red",
                )
                click.echo("To create ", nl=False)
                click.secho(
                    file,
                    nl=False,
                    fg="bright_yellow",
                )
                click.echo(f", the directory {parent.name} is needed.")
                if not click.confirm(
                    "Do you wish to create this direcotry and continue?"
                ):
                    return False
            parent.mkdir(parents=True)
        return True

    if directory is not None:
        root = directory / "root.txt"
        intermediate = directory / "intermediate.txt"
        provisioner = directory / "provisioner.txt"

    if have_parent(root, force) and root.write_text(gen_pass()):
        click.secho("Root password:          ", nl=False, fg="magenta")
        click.secho(root, fg="green")
    if have_parent(intermediate, force) and intermediate.write_text(
        gen_pass()
    ):
        click.secho("Intermediate password:  ", nl=False, fg="magenta")
        click.secho(intermediate, fg="green")
    if have_parent(provisioner, force) and provisioner.write_text(gen_pass()):
        click.secho("Provisioner password:   ", nl=False, fg="magenta")
        click.secho(provisioner, fg="green")
