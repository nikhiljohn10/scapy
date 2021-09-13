#!/usr/bin/env python3
"""Argument module."""

from argparse import ArgumentParser, Namespace


def worker_arguments() -> Namespace:
    """Parse arguments for worker deployment.

    Returns:
        Namespace: Argument list as object
    """
    parser = ArgumentParser(
        prog="scapy", description="Step CA Worker Deployment"
    )
    parser.add_argument(
        "-t",
        "--token",
        dest="token",
        type=str,
        help="CA Server's Name",
    )
    parser.add_argument(
        "-n",
        "--name",
        dest="name",
        type=str,
        help="CA Server's Name",
        required=True,
    )
    parser.add_argument(
        "-p",
        "--fingerprint",
        dest="fingerprint",
        type=str,
        help="Root CA Certificate's fingerprint",
        required=True,
    )
    parser.add_argument(
        "-u",
        "--ca-url",
        dest="url",
        type=str,
        help="CA Server's URL",
        required=True,
    )
    parser.add_argument(
        "-r",
        "--root",
        dest="ca",
        type=str,
        help="CA Root Certificate file in PEM or DER format",
        default="~/.step/certs/root_ca.crt",
    )
    parser.add_argument(
        "-w",
        "--worker",
        dest="worker",
        type=str,
        help="Name of the worker",
        default="ca",
    )
    parser.add_argument(
        "-f",
        "--file",
        dest="file",
        type=str,
        help="Worker file location",
        default="./build/index.js",
    )
    return parser.parse_args()
