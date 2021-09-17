#!/usr/bin/env python3
"""Download commands."""


import click

from .utils import download


@click.group()
def get():
    """Download command module."""


@get.command()
@click.argument(
    "package",
    nargs=1,
    type=click.Choice(["ca", "cli", "all"], case_sensitive=False),
)
@click.option(
    "-t",
    "--tag",
    default="latest",
    type=str,
    help="Tag verison to download",
)
@click.option(
    "-p",
    "--path-only",
    is_flag=True,
    help="Show only downloaded path",
)
def step(package: str, tag: str, path_only: bool) -> None:
    """Download Step CA packages."""
    ca_url = "https://api.github.com/repos/smallstep/certificates/releases"
    cli_url = "https://api.github.com/repos/smallstep/cli/releases"

    if tag == "latest":
        ca_url += "/latest"
        cli_url += "/latest"
    else:
        if not tag.startswith("v"):
            tag = "v" + tag
        ca_url += "/tags/" + tag
        cli_url += "/tags/" + tag

    download_urls = []
    if package == "ca":
        download_urls.append(ca_url)
    elif package == "cli":
        download_urls.append(cli_url)
    else:
        download_urls.append(ca_url)
        download_urls.append(cli_url)
    paths = []
    for url in download_urls:
        path = download(url, verbose=(not path_only))
        if not path_only:
            click.secho("Downloaded file: ", nl=False, fg="magenta")
            click.secho(path, fg="green", underline=True)
        paths.append(path)
    if path_only:
        click.secho(" ".join(paths), fg="green")
