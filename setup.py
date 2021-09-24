"""Scapy Manager package setup file."""

import re
import pathlib

from setuptools import find_packages, setup


def main():
    """Scapy Manager's main setup method."""
    HERE = pathlib.Path(__file__).parent
    version_file = HERE / "scapy/__version__.py"
    version_file = version_file.resolve(strict=True).read_text()
    VERSION = re.compile(r"#v(.+)").search(version_file).group(1)

    setup(
        name="scapy-man",
        version=VERSION,
        description="Step CA Manager using Python",
        long_description=(HERE / "README.md").read_text(),
        long_description_content_type="text/markdown",
        author="Nikhil John",
        author_email="nikhiljohn1010@gmail.com",
        url="https://github.com/nikhiljohn10/scapy",
        license="MIT",
        packages=find_packages(),
        py_modules=["scapy"],
        install_requires=[
            "cloudflare-api>=2.0.4",
            "Click",
            "click-completion",
        ],
        entry_points={
            "console_scripts": [
                "scapy = scapy.cli:cli",
            ],
        },
        include_package_data=True,
        keywords=[
            "step-ca",
            "cloudflare-api",
            "workers",
            "certificate",
            "cli",
        ],
        classifiers=[
            "Development Status :: 5 - Production/Stable",
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
