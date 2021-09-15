#!/usr/bin/env python3
"""CLI Command utilities."""


from multiprocessing import Process
from time import sleep
from typing import Optional

import click


class Printer:
    """Custom Styled Printer class."""

    def __init__(self) -> None:
        """Printer class initialisation method."""
        self.left_part = "="
        self.center_part = "*"
        self.right_part = "="
        self.max_animation_width = 5
        self.wip_content_length = 0
        self.process: Optional[Process] = None

    def loop_animation(self, position: int, last_postition: int) -> int:
        """Loop animation logic.

        Args:
            position (int): Current position of moving part
            last_postition (int): Final position of moving part

        Returns:
            int: Calculated position of moving part
        """
        if position < last_postition:
            position += 1
        else:
            position = 1
        return position

    def static_arrow(self, content: str) -> None:
        """Non-animated printing method for first line.

        Args:
            content (str): Content to print
        """
        click.secho("\r====> ", nl=False, bold=True, fg="magenta")
        click.secho(content, fg="green")

    def animate(self, content: str, speed: float = 0.2) -> None:
        """Add animation in front of content using multithreading.

        Args:
            content (str): Content to print
            speed (float, optional): Time intervel between each animation frame. Defaults to 0.2.
        """
        if self.process is not None:
            pos = 1
            c_len = len(self.center_part)
            last_pos = self.max_animation_width - c_len + 1
            while True:
                l_len = pos - 1
                r_len = self.max_animation_width - c_len - l_len
                left = self.left_part * l_len
                right = self.right_part * r_len
                arrow = f"{left}{self.center_part}{right}"
                click.secho(
                    f"\r{arrow} ", nl=False, bold=True, fg="bright_cyan"
                )
                click.secho(content, nl=False, fg="bright_yellow")
                sleep(speed)
                pos = self.loop_animation(pos, last_pos)

    def stop_animation(self) -> None:
        """Stop the current animation in progress."""
        if self.process is not None:
            self.process.terminate()
            self.process = None

    def working(self, content: str, animate: bool = True) -> None:
        """Print animated content with WIP context.

        Args:
            content (str): Content to print
            animate (bool, optional): [description]. Defaults to True.
        """
        self.wip_content_length = len(content)
        if animate:
            self.process = Process(target=self.animate, args=(content,))
            self.process.start()
        else:
            self.static_arrow(content)

    def done(self, content: str, url: str = "") -> None:
        """Print completed content.

        Args:
            content (str): Content to print
            url (str, optional): URL to print and launch in browser. Defaults to "".
        """
        correction_length = self.wip_content_length - len(content)
        empty_string = ""
        if correction_length > 0:
            empty_string = " " * correction_length
        self.stop_animation()
        click.secho("\r<===> ", nl=False, fg="magenta")
        if not url:
            click.secho(f"{content}{empty_string}", fg="green")
        else:
            click.secho(f"{content} ", nl=False, fg="green")
            click.secho(url, nl=False, fg="bright_blue", underline=True)
            click.echo(empty_string)
            click.launch(url)
