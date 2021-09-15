#!/usr/bin/env python3
"""Scapy CLI Settings."""

from pathlib import Path

STEP_PATH = (Path.home() / ".step").resolve()
DEFAULT_ROOT_CA_FILE = (STEP_PATH / "certs/root_ca.crt").resolve()
DEFAULT_WORKER_FILE = Path("./worker.js").resolve()
