"""Scapy Manager package setup file."""

import pathlib
import re

from setuptools import find_packages, setup


def main():
    """Scapy Manager's main setup method."""
    HERE = pathlib.Path(__file__).parent
    version_file = HERE / "CloudflareAPI/__version__.py"
    version_file = version_file.resolve(strict=True).read_text()
    VERSION = re.compile(r"#v(.+)").search(version_file).group(1)

    setup(
        name="scapy",
        version=VERSION,
        description="Step CA Manager using Python",
        long_description=(HERE / "README.md").read_text(),
        long_description_content_type="text/markdown",
        author="Nikhil John",
        author_email="nikhiljohn1010@gmail.com",
        url="https://github.com/nikhiljohn10/scapy",
        license="MIT",
        packages=find_packages(),
        install_requires=["requests,cloudflare-api"],
        keywords=["stepca", "cloudflare-api", "workers", "certificate"],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
        ],
    )


if __name__ == "__main__":
    main()