#!/usr/bin/env python3
"""Scapy Manager's main program."""

from scapy import Worker
from scapy.arguments import worker_arguments


def main():
    """Scapy Manager's main function."""
    params = worker_arguments()
    worker = Worker(token=params.token)
    worker.store(
        web_title=params.name,
        fingerprint=params.fingerprint,
        ca_url=params.url,
    )
    root_ca = params.ca
    worker.loadCA(root_ca)
    url = worker.deploy(params.worker, params.file)
    print("Deployed worker:", url)


if __name__ == "__main__":
    main()
